from pyexpat.errors import messages
from django.shortcuts import render,get_object_or_404
from .models import *

from django.contrib import messages
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

# Create your views here.
def home(request):
	return render(request,'projects/home.html',{
        'homes':Home.objects,
        'projects':Project.objects,
        'socials':Social.objects,
        'tags':Tag.objects,
        })


def portfolioview(request,project_id):
	project_detail = get_object_or_404(Project,pk=project_id)
	return render(request,'projects/portfolioview.html',{'project':project_detail,'socials':Social.objects,})

def newsletter(request):
	return render(request,'projects/newsletter.html',{'socials':Social.objects,'newsletter':Newsletter.objects})


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

# Subscription Logic
def subscribe(email):

    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


# This is for the subscription form
def subscription(request):
	if request.method == "POST":
		email = request.POST['email']
		subscribe(email)
		messages.success(request, "Subscription successful!")
	return render(request,'projects/newsletter.html',{'socials':Social.objects,})