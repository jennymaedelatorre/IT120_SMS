from django.shortcuts import render, redirect
from twilio.rest import Client
import os
from dotenv import load_dotenv
from .forms import FeedbackForm

load_dotenv()

# Welcome Page View
def welcome_view(request):
    return render(request, "welcome.html")

# Feedback Form View
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
             # Get the form data
            name = form.cleaned_data['name']
            event_date = form.cleaned_data['event_date']
            event_time = form.cleaned_data['event_time']
            feedback = form.cleaned_data['feedback']
            ratings = form.cleaned_data['ratings']
            phone_number = form.cleaned_data['phone_number']

            # Construct the SMS message
            message = f"Feedback from {name} on {event_date} at {event_time}: {feedback}. Rating: {ratings} stars."

            # Send the SMS using Twilio
            TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
            TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
            TWILIO_PHONE_FROM = os.getenv('TWILIO_PHONE_NUMBER')
            TWILIO_PHONE_TO = os.getenv('TO_PHONE_NUMBER')

            
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            client.messages.create(
                body=message,
                from_=TWILIO_PHONE_FROM, 
                to=TWILIO_PHONE_TO 
            )

            # Redirect to the thank you page after submission
            return redirect('thank_you')

    else:
        form = FeedbackForm()

    return render(request, "feedback_form.html", {"form": form})

# Thank You Page View
def thank_you_view(request):
    return render(request, "thank_you.html")
