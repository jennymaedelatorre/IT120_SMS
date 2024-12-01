"""
URL configuration for IT120_SMSproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views  # Ensure this is correct


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_view, name='welcome'),  # Welcome page
    path('feedback/', views.feedback_view, name='feedback'),  # Feedback form
    path('thank-you/', views.thank_you_view, name='thank_you'),  # Thank you page
]
