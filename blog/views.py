
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import send_mail


def accueil(request):
    # return HttpResponse("hello world")
    return render(request,'accueil.html')

def contact(request):
    # return HttpResponse("contactez nous ..")
    form = ContactForm()
    #on veut récupérer le message de l'utilisateur
    if request.method == "POST":
        form = ContactForm(request.POST)
        #pour envoyer un email
        if form.is_valid():
            # form.is_valid() permet de verifier si le formulaire est valide
            nom= form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # print(nom,prenom,email)
            # print(message)
            titre = f'blog|{nom} {prenom} {email}'
            send_mail(titre,message,'blog@gmail.com', ['blog@gmail.com','blog@yahoo.com'] )
        return HttpResponseRedirect(reverse('remerciement'))
    return render(request,'contact.html',{'form':form})

def remerciement(request):
    return HttpResponse("merci de nous avoir contacté")

