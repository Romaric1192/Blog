
from django.forms import ModelForm
from .models import Articles

class FormArticles(ModelForm):
    class Meta:
        model= Articles
        fields = ['titre','contenu','image','slug']
