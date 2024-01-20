from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import cadastro



urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('flashcard/', include('flashcard.urls')),
    path('apostilas/', include('apostilas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
