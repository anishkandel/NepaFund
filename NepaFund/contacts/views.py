from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
  if request.method == 'POST':
      platform_id= request.POST['platform_id']
      platform=request.POST['platform']
      name=request.POST['name']
      email=request.POST['email']
      phone=request.POST['phone']
      message=request.POST['message']
      user_id=request.POST['user_id']
      data_email=request.POST['data_email']

    
      if request.user.is_authenticated:
        user_id=request.user.id
        has_contacted=Contact.objects.all().filter(platform_id=platform_id, user_id=user_id)
        if has_contacted:
          messages.error(request, 'you have already made an inquiry for this public sale')
          return redirect('/platforms/'+platform_id)

      contact=Contact(platform=platform, platform_id=platform_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

      contact.save()

         #send email
      send_mail(
        'Investment Platform Inquiry',
        'There has been an inquiry for ' + platform + '. Sign into the admin panel for more info',
        'aayaansharma100@gmail.com',
        [data_email, 'aayaansharma100@gmail.com'],
        fail_silently=False
      )
      messages.success(request, 'Your Whitelisted form has requested, Please wait for response')
      return redirect('/platforms/'+platform_id)
    