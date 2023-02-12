from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from webapp.models import contact, apply
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            'this is automatically generated mail from Manollasa College webpage',
            f' a person named {name} is trying to contact you\nRegarding subject:{subject}\n\n{message} \n\n return mail to: {email}',
            'manollasacollage@gmail.com',
            ['adarshsavaligi@gmail.com'],
            fail_silently=False,
        )

        Contact = contact(Name=name, Email=email,
                          Message=message, date=datetime.today(), Subject=subject)
        Contact.save()
        messages.success(request, 'Form submission successful')
        return render(request, 'index.html')

    return render(request, 'index.html')


def register(request):
    print('register page has been requested')
    if request.method == 'POST':
        print('register page has been requested data has been filled')
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        branch = request.POST.get('branch')
        Register = apply(Name=name, Email=email,  Place=place,
                            Phone=phone, Branch=branch, date=datetime.today())
        Register.save()
        send_mail(
            'this is automatically generated mail from Manollasa College webpage',
            f' Name: {name}\nEmail: {email}\n place: {place}\nPhone: {phone}\n Branch: {branch} \n',
            'manollasacollage@gmail.com',
            ['adarshsavaligi@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Form submission successful')
        return render(request, 'Apply.html')
    return render(request, 'Apply.html')


def bba(request):
    return render(request, 'bba.html')
    # return HttpResponse('hello this is bom')


def bcom(request):
    return render(request, 'bcom.html')


def ba(request):
    return render(request, 'barts.html')


def bsw(request):
    return render(request, 'bsw.html')


def bsc(request):
    return render(request, 'bsc.html')


def blis(request):
    return render(request, 'blis.html')


def mlis(request):
    return render(request, 'Mliss.html')


def mba(request):
    return render(request, 'mba.html')


def ma(request):
    return render(request, 'ma.html')


def JSS(request):
    return render(request, 'JSS.html')


def Medical(request):
    return render(request, 'medical.html')


def BOSSE(request):
    return render(request, 'BOSSE.html')
