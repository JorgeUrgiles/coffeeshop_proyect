from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contactForm=ContactForm()
    if request.method == "POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            subject=request.POST.get('subject','')
            message=request.POST.get('message','')
            emailContact=EmailMessage(
               "KOPPE: Nuevo mensaje de contacto",
                "De {} <{}>\n\nAsunto:\n\n{}\n\nMensaje:\n\n{}".format(name,email,subject,message),
                "jorge.urgilesc@gmail.edu.ec",#origen
                ["correo-prueba@inbox.mailtrap.io"],#destino aqui espera una lista o tupla
                reply_to=[email]
            )
            #envolver el send en un try catch porque suel dar error y se cae el programa
            
            #queremos enviar un  mensaje avisando que si se mando
            try:
                emailContact.send()
                return redirect(reverse('contact')+"?ok")  #('contact') hace referencia al routname
            except:
                return redirect(reverse('contact')+"?fail") 
    return render(request, "contact/contact.html",{'contactForm':contactForm})