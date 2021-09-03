from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
import re


def index(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        html_content = request.POST.get("body")
        text_content = "This is an important message."
        recipient_list = request.FILES["recipient_list"].read().decode("ascii")

        email_list = []

        for i in recipient_list.split("\n"):
            email_list.append(i[:-1])

        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        for e in email_list:
            if re.fullmatch(regex, e):
                print("Valid Email")
                msg = EmailMultiAlternatives(
                    subject,
                    text_content,
                    "infosec@ieeeiiucsb.org",
                    [e],
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            else:
                print("Invalid Email")

        return HttpResponseRedirect("/")
    else:
        print("Email send error")
        return render(request, "base.html")
