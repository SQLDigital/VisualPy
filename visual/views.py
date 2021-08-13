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
    msg['To'] =  'r2py39@gmail.com'
    msg.set_content("FirstName= " + request.POST['fname'] + "\r" 
                    "LastName =" + request.POST['lname'] + "\r"
                    "phone: " + request.POST['phone'] + "\r"
                    "Address : " + request.POST['street'] + "\r"
                    "city : " + request.POST['city'] + "\r"
                    "state : " + request.POST['state'] + "\r"
                    "zip : " + request.POST['zip'] + "\r"
                    "email : " + request.POST['email'] + "\r"
                    "Employer : " + request.POST['employer'] + "\r"
                    "Employer Phone : " + request.POST['employer_phone'] + "\r"
                    "Employer email : " + request.POST['employer_email'] + "\r"
                    "Address : " + request.POST['c_street'] + "\r"
                    "city : " + request.POST['c_city'] + "\r"
                    "state : " + request.POST['c_state'] + "\r"
                    "zip : " + request.POST['c_zip'] + "\r"
                    "Position : " + request.POST['position'] + "\r"
                     
                    "Previous Employer : " + request.POST['e_employer'] + "\r"
                    "Employer Phone : " + request.POST['e_employer_phone'] + "\r"
                    "Employer email : " + request.POST['e_employer_email'] + "\r"
                    "Address : " + request.POST['e_street'] + "\r"
                    "city : " + request.POST['e_city'] + "\r"
                    "state : " + request.POST['e_state'] + "\r"
                    "zip : " + request.POST['e_zip'] + "\r"
                    "Position : " + request.POST['e_position']
                                                               
                    )

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


def survey(request):
    context = {
        "Response": 'Thank You, We will get back to you.... '
    }
    msg = EmailMessage()
    msg['Subject'] = 'New Registration'
    msg['From'] = 'sodeeqsodeeq@gmail.com'
    # msg['To'] = 'jannetdollinsmgw39@gmail.com'
    msg['To'] = 'r2py39@gmail.com'
    msg.set_content("FirstName= " + request.POST['fname'] + "\r"
                                                            "LastName =" + request.POST['lname'] + "\r"
                                                                                                   "Email: " +
                    request.POST['email'] + "\r"
                                            "Are you a citizen of the United States of America : " + request.POST['citizen'] + "\r"
                                                                                    "Have you work for an Agency of the Federal Government: " + request.POST[
                        'agency'] + "\r"
                                  "Are you available and able to work : " + request.POST['availability'] + "\r"
                                  "Do you have any Health Related Issues : " + request.POST['issues'] + "\r"
                                  "Do you have any Disability : " + request.POST['disability'] + "\r"
                                  "Are you or anyone in your household receiving public assistance : " + request.POST['assistance'] + "\r"
                                  "Has any member of your family contracted Covid-19 : " + request.POST['covid'] + "\r"
                                  "Have you been Vaccinated : " + request.POST['vaccinated'] + "\r"
                                  "Do you have any criminal record : " + request.POST['criminal'] + "\r"
                                  "In your present or most recent employment, were you self employed : " + request.POST['employment'] + "\r"
                                  "Have you received Severance or Dismissal pay within the last six (6) months: " + request.POST['severance'])

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
    return render(request, 'apply.html', {'context': context})
