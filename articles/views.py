
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Articles
from django.http import HttpResponseRedirect
from django.urls import reverse #retourner les fonctions par les noms des url

from .forms import FormArticles



def article(request):
    articles=Articles.objects.all().order_by('-date_publication')
    return render(request,'articles/list.html',context={'articles':articles})


def contenus(request, slug):

        article = get_object_or_404(Articles, slug=slug)
        return render(request,'articles/detail.html', context={'article':article})
    # try:
    #     article = Articles.objects.get(slug=slug)
    #     return render(request,'articles/detail.html', context={'article':article})
    # except Articles.DoesNotExist:
    #     raise Http404("l'article n'existe pas..")

def créer(request):
    form = FormArticles() 
    # ceci est l'objet de la class FormArticles
    # nous allons récupérer nos données ds la bd
    if request.method == 'POST':
        form = FormArticles(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            contenu = form.cleaned_data['contenu']
            image = form.cleaned_data['image']
            slug = form.cleaned_data['slug']
            form.save() #pour sauvegarder les données ds la bd
            # return HttpResponseRedirect('/articles/')
        return HttpResponseRedirect(reverse('articles:articles'))
    return render(request,'articles/créer.html', context={'form':form})