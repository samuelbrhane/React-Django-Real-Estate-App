from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response
import dotenv
import os
dotenv.load_dotenv()


class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self,request,format=None):
        data = self.request.data
        try:
            send_mail(subject = data["subject"], 
                    message = "Name: " + data["name"] 
                    + "\nEmail: " + data["email"]
                    + "\n\nMessage:\n" + data["message"],
                    from_email = os.getenv('EMAIL_HOST'),
                    recipient_list =  [os.getenv('EMAIL_HOST')],
                    fail_silently = False)
            contact = Contact(name=data["name"], email=data["email"], subject=data["subject"], message=data["message"])
            contact.save()
            return Response({"success":"Message Send Successfully."})
        
        except:
            return Response({"error":"Message Fail to Send."})
