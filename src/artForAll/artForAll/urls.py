"""artForAll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Pages.views import about_view, home_view, contact_view
from Gallery.views import gallery_detail_view, gallery_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('home/', home_view, name = 'home'),
    path('gallerydetail/', gallery_detail_view, name = 'gallery detail view'),
    path('admin/', admin.site.urls),
    path('gallery/', gallery_view, name = 'gallery'),
    path('contact/', contact_view, name = "contact"),
    path('about/', about_view, name = 'about'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
