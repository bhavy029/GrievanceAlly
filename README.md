# GrievanceAlly
# Project Name: [Suggest an Al-based solution to enable ease of grievance lodging and tracking for citizens across multiple departments]
# PS Code : [SIH1516] 

## Team Name: Algorithm Architects
- Team Members: Aangi Gandhi
- Contact Email: aangigandhi2811@gmail.com
- Team Members:Akshat Merchant
- Contact Email: akshatmerchant68@gmail.com
- Team Members: Ayush Singh
- Contact Email:indianpassioner@gmail.com
- Team Members: Vaibhav kumar 
- Contact Email: Vaibhavkumar1097@gmail.com
- Team Members: Smit Kumbhani
- Contact Email: sbkumbhani751@gmail.com
- Team Members: Bhavyakumar patel
- Contact Email: bkpatel6554@gamil.com


## Project Overview 
The introduction of an AI-powered chatbot. This chatbot would serve as a user-friendly interface for citizens to articulate their grievances in their preferred local languages. Beyond language translation, it would possess the ability to comprehensively understand and process complaints. Its responsibilities would extend to categorizing complaints correctly and forwarding them to the respective departments. Furthermore, the chatbot would furnish citizens with unique complaint numbers and provide real-time updates on the status of their grievances.
The overarching objective of this solution is to empower citizens with a straightforward and efficient means of lodging and tracking complaints. Such an approach would not only save citizens valuable time that might otherwise be spent navigating bureaucratic hurdles but also offer the administration a streamlined method for receiving targeted grievances and ultimately improving overall service delivery.  



## Tech Stack 
**AI /ML Libraries  :** 
  rasa
  googletrans
  mysql-connector-python
  streamlit
**Web Scraping :**
  Streamlit 
**Web Technology :**
  Frontend – Python
  Backend- Anaconda Promt
**Database :**
  Database- MySQL 

## Project Features and Functionality 
User Registration: Users create accounts with their details, including a valid Aadhar number.
Complaint Lodging: Users describe their complaints in their preferred language, and the chatbot translates and categorizes them.
Ministry Assignment: The chatbot assigns the complaint to the relevant ministry based on keywords and content analysis.
Real-time Updates: Users receive real-time notifications and can check the status of their complaints.

## How It Works 
<img src="https://github.com/bhavy029/GrievanceAlly/blob/machine-learning/WhatsApp%20Image%202023-09-27%20at%201.37.12%20PM.jpeg" alt="basic idea">


## Challenges and Solutions 
**Challenge 1:** The code connects to multiple databases for different ministries and a common database. Managing these connections and configurations can become complex.
Solution: Consider using a database connection pool to manage database connections efficiently. Additionally, you can centralize database configurations to make maintenance easier.
Email Sending:

**Challenge 2:** The code sends emails to ministry contacts. Handling email delivery failures and ensuring reliable email communication is crucial.
Solution: Implement email delivery status tracking and error handling. Consider using a dedicated email service like SendGrid or AWS SES for more robust email handling.
Keyword-Based Ministry Determination:

**Challenge 3:** The code determines the appropriate ministry for a complaint based on keywords. This approach may not be accurate if keywords are ambiguous or overlapping.
Solution: Implement a more sophisticated natural language processing (NLP) or machine learning model to classify complaints into ministries. This can improve accuracy.
User Interaction and Language Translation:

**Challenge 4:** The code interacts with users in multiple languages and relies on external translation services. This can introduce latency and translation inaccuracies.
Solution: Consider caching translated responses to reduce latency and improve user experience. Use a well-maintained translation service to minimize inaccuracies.
Security:

**Challenge 5:** The code contains sensitive information such as database credentials and API keys. Hardcoding these values can be a security risk.
Solution: Store sensitive information securely, such as using environment variables or a configuration management system. Ensure proper access controls for these resources.
Token Generation:

**Challenge 6:** The code generates unique tokens for each complaint, but there is no guarantee of uniqueness.
Solution: Use a more robust method for generating unique tokens, such as UUIDs, to avoid collision and ensure uniqueness.
User Input Validation:

**Challenge 7:** The code does limited validation of user inputs, such as PIN codes and Aadhar numbers.
Solution: Implement comprehensive input validation to ensure that user-provided data meets the required criteria. This can help prevent invalid data from entering the system.

## Future Enhancements 
Integration with Government Databases: Connect the chatbot to government databases for faster issue resolution.
Voice Input: Enable users to lodge complaints via voice commands.
Predictive Analytics: Use historical data to predict potential grievance areas and proactively address issues.
Mobile App: Develop a mobile app for easier access.
Automatic language detector using AI tools
## Screenshots and Demos 
<img src="https://github.com/Suvagiyadhruv/LearnLinker/blob/main/image2002.png" alt="Screenshot1">
<img src="https://github.com/Suvagiyadhruv/LearnLinker/blob/main/image2003.png" alt="Screenshot2">
<img src="https://github.com/Suvagiyadhruv/LearnLinker/blob/main/image2004.png" alt="Screenshot3">

## Acknowledgments 
We would like to acknowledge the support and contributions of Team Members . Special thanks to Dr Ravi Gor sir  for their guidance throughout the project.

## Get In Touch! 


| Team Member| linkdin |
| Bhavyakumar Patel | https://www.linkedin.com/in/bhavy-patel-1744b319b/ |
| Aanghi Gandhi  | https://www.linkedin.com/in/aangi-gandhi-947006276|
| Akshat Merchant| https://www.linkedin.com/in/akshat-merchant-140513276 |
| Aayush Singh| https://www.linkedin.com/in/ayush-singh-75a00926a |
| Vaibhavkumar|https://www.linkedin.com/in/vaibhav-kumar-1a5b1b269 |


