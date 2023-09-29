#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#required library 
# 1 pip install googletranslator
# 2 pip install rasa
# 3 pip install mysql-connector-python


# import library
import random
import string
from googletrans import Translator
import mysql.connector
from mysql.connector import Error
import  requests


# Define database configurations for each ministry
api_key="269A4059AC112293C19A2E58210F8987D147E69AD1A896365FFD24A125A51B1F44FBE3F042EEAC61143E4F05E7B7B574"
ministry_db_configs = {
    "Ministry of Water": {"database": "water_ministry_db"},
    "Ministry of Electricity": {"database": "electricity_ministry_db"},
    "Ministry of Roads": {"database": "roads_ministry_db"},
    # Add more ministries and their respective databases
}

def get_ministry_connection(ministry):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='6554',
            database=ministry_db_configs[ministry]["database"]
        )
        return connection
    except Error as e:
        print(f"Error connecting to the {ministry} database: {e}")
        return None

# Function to insert data into the ministry_complaints table for a specific ministry
def insert_complaint_into_ministry(complaint_description, ministry, token_id, language, pincode, aadhar_number):
    try:
        connection = get_ministry_connection(ministry)
        if connection:
            cursor = connection.cursor()

            # Insert the complaint into the ministry's table
            insert_query = "INSERT INTO ministry_complaints (complaint_description, token_id, language, pincode, aadhar_number) VALUES (%s, %s, %s, %s, %s)"
            data = (complaint_description, token_id, language, pincode, aadhar_number)
            cursor.execute(insert_query, data)
            connection.commit()
            print(f"Complaint data stored in {ministry} database successfully.")
    except Error as e:
        print(f"Error inserting data into {ministry} database: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to insert data into the common database (all_ministries_db)
def store_complaint_in_databases(complaint_description, ministry, token_id, language, pincode, aadhar_number):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='6554',
            database='all_ministries_db'  # Common database
        )
        if connection:
            cursor = connection.cursor()

            # Insert the complaint into the 'all_complaints' table
            insert_query = "INSERT INTO all_complaints (complaint_description, ministry, token_id, language, pincode, aadhar_number) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (complaint_description, ministry, token_id, language, pincode, aadhar_number)
            cursor.execute(insert_query, data)
            connection.commit()
            print("Complaint data stored in the 'all_ministries_db' database successfully.")
    except Error as e:
        print(f"Error inserting data into 'all_ministries_db' database: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to determine the appropriate ministry for a complaint
def send_email(api_key, subject, message, to):
    url = 'https://api.elasticemail.com/v2/email/send'

    data = {
        'apikey': api_key,
        'subject': subject,
        'from': 'webmovie03@gmail.com',  # Your sender email address
        'to': to,
        'bodyHtml': message,
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Email sent successfully to', to)
    else:
        print('Email could not be sent to', to, 'Error:', response.text)
def determine_ministry(complaint):
    for ministry in ministry_db_configs:
        keywords = ministry_db_configs[ministry].get("keywords", [])
        for keyword in keywords:
            if keyword in complaint.lower():
                return ministry
    return None
fake_ministries = {
    "Ministry of Water": {"keywords": ["water", "drinking water", "sanitation", "water supply", "water quality", "water treatment",
                                       "water conservation", "water resources", "water management", "water infrastructure"],
                          "contact": "ams202214@gujaratuniversity.ac.in"},
    "Ministry of Electricity": {
        "keywords": ["electricity", "power", "energy", "electrical supply", "power generation", "electric grid",
                     "power outage", "renewable energy", "electricity rates", "energy efficiency"],
        "contact": "ams202214@gujaratuniversity.ac.in"},
      "Ministry of Roads": {"keywords": ["roads", "infrastructure", "transportation", "road maintenance", "road construction", "traffic management", "road safety", "highways",
                                         "street lighting", "public transportation"],
                            "contact": "ams202214@gujaratuniversity.ac.in"},
    # Add more ministries with keywords and contact information
}

# Function to determine the appropriate ministry for a complaint

def determine_ministry(complaint, ministries):
    for ministry, data in ministries.items():
        keywords = data["keywords"]
        for keyword in keywords:
            if keyword in complaint.lower():
                return ministry,data["contact"]
    return None,None
# Function to generate a unique token ID
def generate_unique_token():
    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    return token

# Function to detect language and translate input
def detect_and_translate(input_text, input_language, target_language='en'):
    try:
        # Translate input to English (or a common language)
        translator = Translator()
        translated_input = translator.translate(input_text, src=input_language, dest='en').text

        # Determine the ministry based on keywords
        ministry,contact_email = determine_ministry(translated_input,fake_ministries)

        if ministry:
            problem_statement=translated_input
            # Confirm the ministry with the user
            while True:
                response = f"Do you want to send your complaint to {ministry}? (yes=1/no=0): "
                translated_response = translator.translate(response, src='en', dest=input_language).text
                confirmation = input(translated_response.strip().lower())

                if confirmation.lower() == '1':
                    # Simulate complaint submission
                    send_email(api_key,f'complaint for {ministry}',problem_statement  ,contact_email)
                    token_id = generate_unique_token()

                    # Call insert_complaint_into_ministry and pass pincode and aadhar_number
                    insert_complaint_into_ministry(input_text, ministry, token_id, input_language, pincode, aadhar_number)

                    # Call store_complaint_in_databases and pass pincode and aadhar_number
                    store_complaint_in_databases(input_text, ministry, token_id, input_language, pincode, aadhar_number)

                    token = f"Your complaint's token number is: {token_id}"
                    translated_token = translator.translate(token, src='en', dest=input_language).text
                    print(translated_token)
                    print(translator.translate("Thank you for using the chatbot.", src='en', dest=input_language).text)
                    return
                elif confirmation.lower() == '0':
                    # Ask the user to describe the complaint again
                    new_description = input(
                        translator.translate("Please describe your complaint again: ", src='en', dest=input_language).text)
                    translated_input = translator.translate(new_description, src=input_language, dest='en').text
                    ministry = determine_ministry(translated_input)
                    if ministry:
                        continue
                    else:
                        response = "Sorry, we couldn't determine the appropriate ministry for your complaint."
                        translated_response = translator.translate(response, src='en', dest=input_language).text
                        print(translated_response)
                else:
                    response = "Invalid input. Please enter '1' or '0'."
                    translated_response = translator.translate(response, src='en', dest=input_language).text
                    print(translated_response)

        else:
            response = "Sorry, we couldn't determine the appropriate ministry for your complaint."
            translated_response = translator.translate(response, src='en', dest=input_language).text
            print(translated_response)

    except Exception as e:
        response = "An error occurred: "
        translated_response = translator.translate(response, src='en', dest=input_language).text
        print(translated_response + str(e))

# Function to choose language
def choose_language():
    print("Choose your preferred language:")
    print("1 - English")
    print("2 - हिंदी")
    print("3 - ગુજરાતી")
    print('4- ਪੰਜਾਬੀ')
    print('5-मराठी')
    print('6-বাঙ্গালি')
    print('7-ಕನ್ನಡ')
    print('8-తెలుగు')
    print('9-اردو')
    print('0-தமிழ்')

    l = ['en', 'hi', 'gu', 'pa', 'mr', 'bn', 'kn', 'te', 'ur', 'ta']
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    while True:
        language_choice = input('Enter the number of your preferred language:')

        # Convert the user input to an integer
        language_choice = int(language_choice)

        if language_choice in c:
            index = c.index(language_choice)
            return l[index]
        else:
            print("Invalid choice. Please enter a valid number.")


def get_valid_pincode(input_language):
    while True:
        pincode = input(translator.translate("Please enter your pincode:", src='en', dest=input_language).text)
        if len(pincode) == 6 and pincode.isdigit():
            return pincode
        else:
            print(translator.translate("Invalid PIN code. Please enter a 6-digit PIN code.", src='en', dest=input_language).text)

# Function to get valid Aadhar number
def get_valid_aadhar_number(input_language):
    while True:
        aadhar_number = input(translator.translate("Please enter your Aadhar number:", src='en', dest=input_language).text)
        if len(aadhar_number) == 12 and aadhar_number.isdigit():
            return aadhar_number
        else:
            print(translator.translate("Invalid Aadhar number. Please enter a 16-digit Aadhar number.", src='en', dest=input_language).text)

# Function to choose action (register complaint or check status)
def choose_action(input_language):
    print(translator.translate("Choose an action:", src='en', dest=input_language).text)
    print(translator.translate("1 - Register a Complaint", src='en', dest=input_language).text)
    print(translator.translate("2 - Check Complaint Status", src='en', dest=input_language).text)
    while True:
        action_choice = input(translator.translate("Enter the number of your preferred action: ", src='en', dest=input_language).text)
        if action_choice == '1':
            return 'register'
        elif action_choice == '2':
            return 'check_status'
        else:
            print(translator.translate("Invalid choice. Please enter 1 or 2.", src='en', dest=input_language).text)


def check_complaint_status(token_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='6554',
            database='all_ministries_db'
        )
        if connection:
            cursor = connection.cursor()

            # Query the database to check if the token ID exists
            query = "SELECT * FROM all_complaints WHERE token_id = %s"
            cursor.execute(query, (token_id,))
            complaint = cursor.fetchone()

            if complaint:
                # Display complaint status
                ministry = complaint[2]
                complaint_description = complaint[1]
                print(f"Complaint Status:\nMinistry: {ministry}\nDescription: {complaint_description}")
            else:
                print("Invalid Token ID. Please check the token ID and try again.")

    except Error as e:
        print(f"Error checking complaint status: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
# Choose user's preferred language
input_language = choose_language()
translator = Translator()
while True:
    # Ask the user to choose an action
    user_action = choose_action(input_language)

    if user_action == 'register':
        # Ask for pincode and Aadhar number
        pincode = get_valid_pincode(input_language)
        aadhar_number = get_valid_aadhar_number(input_language)

        # Ask the user to describe their complaint
        complaint_description = input(
            translator.translate("Please describe your complaint:", src='en', dest=input_language).text)

        # Provide token number
        detect_and_translate(complaint_description, input_language)
    elif user_action == 'check_status':
        token_id_to_check = input(translator.translate("Enter your token ID to check the complaint status: ", src='en',
                                                       dest=input_language).text)
        check_complaint_status(token_id_to_check)
        # Add code to check the status of a complaint here (e.g., using a complaint ID)
        print(translator.translate("Checking complaint status...", src='en', dest=input_language).text)
    else:
        print(translator.translate("Invalid action. Please try again.", src='en', dest=input_language).text)

#To execute the code in anaconda prompt
#We need to open anaconda terminal and write below code 
#streamlit run HF6.py
