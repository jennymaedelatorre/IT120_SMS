import os
from django.db import models
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(
        max_length=50,
        choices=[
            ('1st', '1st'),
            ('2nd', '2nd'),
            ('3rd', '3rd'),
            ('4th', '4th'),
            ('5th', '5th'),
            ('Unranked', 'Unranked'),
        ],
        default='Unranked'
    )  

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Fetch Twilio account SID and Auth Token from environment variables
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        from_number = os.getenv('TWILIO_PHONE_NUMBER')
        to_number = os.getenv('TO_PHONE_NUMBER')

        # Ensure environment variables are set
        if not all([account_sid, auth_token, from_number, to_number]):
            raise ValueError("Twilio credentials or phone numbers are not set in environment variables.")
        
        client = Client(account_sid, auth_token)

        # Determine the SMS message based on rank
        if self.rank == '1st':
            body = f"Congratulations {self.name}! You're ranked 1st! Keep it up!"
        elif self.rank in ['2nd', '3rd']:
            body = f"Great job {self.name}! You're ranked {self.rank}. Keep pushing for the top!"
        elif self.rank in ['4th']:
            body = f"Hi {self.name}, you're ranked {self.rank}. Keep striving to improve!"
        elif self.rank in ['5th']:
            body = f"Hi {self.name}, you're ranked {self.rank}. There's always another chance—keep pushing forward!"
        else:  
            body = f"Hi {self.name}, you are currently Unranked. Work hard to make it to the leaderboard!"

        # Send the SMS
        message = client.messages.create(
            body=body,
            from_=from_number,  
            to=to_number        
        )

        print(message.sid)  
        return super().save(*args, **kwargs)
