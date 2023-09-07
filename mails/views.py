import threading

from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    mail_sent = False

    if request.method == 'POST':
        email = request.POST.get('email')
        
        thread = threading.Thread(target=send_welcome_mail, args=(email, ))
        thread.start()

        mail_sent = True


    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })


def send_welcome_mail(to):
    send_mail(
        "Titulo del correo",
        "Hola mundo",
        "eduardo78d@gmail.com",
        [to],
        fail_silently=False,
    )