# IT120_SMS(assignment)

Django SMS Feedback System

*Overview
The Django SMS Feedback System is a web-based application designed to collect feedback from event attendees through a user-friendly feedback form. Feedback is sent directly via SMS to a designated recipient using Twilio's messaging service. This system helps event organizers receive immediate feedback, assess attendee satisfaction, and improve future events.

Installation Guide / Running the Application
Follow the steps below to set up and run the application on your local machine:

Clone the Repository:
git clone https://github.com/jennymaedelatorre/IT120_SMS.git

After cloning:
Create virtual environment
- python -m venv .venv

Install dependencies
- pip install -r requirements.txt

Create .env file containing your twilio credentials
- TWILIO_ACCOUNT_SID=your_twilio_sid
- TWILIO_AUTH_TOKEN=your_twilio_token
- TWILIO_PHONE_NUMBER=your_twilio_number

Run the program
- python manage.py runserver


*Key Features
Feedback Form:

1. Collects attendee details (Name, Event Date and Time, Rating, Feedback Message).
	Structured in two sections: personal information/event details and feedback.

2. SMS Notification:
	Automatically sends an SMS with feedback details (Name, Event details, Rating, Feedback) upon submission.

3. Twilio Integration:
	Utilizes Twilio API for real-time SMS communication.
	Manages credentials securely via environment variables.

4. Dynamic Feedback Submission:
	Enables users to submit feedback anytime.
	Dynamically processes and sends feedback data to designated phone numbers.

5. User-Friendly Interface:
	Built with a responsive design using Django and Bootstrap.
	Ensures accessibility across devices.

6. Thank You Page:
	Redirects users to a confirmation page post-feedback submission.

7. Use Case:
	Targets event organizers seeking to gather actionable feedback efficiently via SMS.


*Tech Stack
1. Backend:
	Django: Handles server-side operations and user interactions.

2. Frontend:
	Bootstrap: Provides a responsive and styled interface.

3. SMS Integration:
	Twilio API: Facilitates SMS messaging.

4. Environment Management:
	Python-dotenv: Secures sensitive credentials (Account SID, Auth Token, Phone Numbers).


*Twilio SetUp
1. Environment Variables:
	Store the Twilio credentials in a .env file:

2. Backend Configuration:
	Load environment variables using python-dotenv

3. Sending SMS:
	Use Twilio's Python library to send an SMS:

4. Integration with Form Submission:
	Trigger the send_sms function upon form submission and validation.

5. Security Considerations:
	Ensure the .env file is excluded from version control using .gitignore.

*This system provides a simple yet effective way for organizers to collect feedback, without requiring attendees to use complex systems or online platforms. It ensures that valuable feedback is easily communicated in real-time through SMS.*
