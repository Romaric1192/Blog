
from django.contrib import admin
from django.urls import path, include
from . import views
# pour acceder à la configuration de l'application
from django.conf import settings
# pour créer une url static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.accueil, name ="home"),
    path('contact/',views.contact, name="contact"),
    path('remerciement', views.remerciement, name="remerciement"),
    # path('article/', views.article, name="article"),
    path('articles/', include('articles.urls'), name="articles")
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
