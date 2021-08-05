import imghdr
import json
import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import smtplib
from email.message import EmailMessage


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def apply(request):
    return render(request, 'apply.html', {})


def sendmail(request):
    context = {
        "Response": 'Thank You, We will get back to you.... '
    }
    msg = EmailMessage()
    msg['Subject'] = 'New Registration'
    msg['From'] = 'sodeeqsodeeq@gmail.com'
    # msg['To'] = 'jannetdollinsmgw39@gmail.com'
    msg['To'] = 'r2py39@gmail.com'
    msg.set_content("FirstName= " + request.POST['fname'] + "\r" 
                    "LastName =" + request.POST['Lname'] + "\r"
                    "phone: " + request.POST['phone'] + "\r"
                    "Address : " + request.POST['street'] + "\r"
                    "city : " + request.POST['city'] + "\r"
                    "state : " + request.POST['state'] + "\r"
                    "zip : " + request.POST['zipcode'] + "\r"
                    "email : " + request.POST['email'])

    file1 = request.FILES['attachment1']
    fs = FileSystemStorage()
    filename = fs.save(file1.name, file1)
    uploaded_file_url = fs.url(filename)
    with open(uploaded_file_url, 'rb') as f:
        file_data = f.read()
        file_type = str(imghdr.what(f.name))
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    file1 = request.FILES['attachment2']
    fs = FileSystemStorage()
    filename = fs.save(file1.name, file1)
    uploaded_file_url = fs.url(filename)
    with open(uploaded_file_url, 'rb') as f:
        file_data = f.read()
        file_type = str(imghdr.what(f.name))
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('sodeeqsodeeq@gmail.com', 'avtltqidkrtbgvmz')
        smtp.send_message(msg)
    return render(request, 'index.html', {'context': context})
