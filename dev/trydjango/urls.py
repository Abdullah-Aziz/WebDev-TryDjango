"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from dev.pages.views import home_views, contact_views, about_views


urlpatterns = [
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('', home_views, name='home'),
    path('contact/', contact_views),
    path('about/', about_views),
    path('admin/', admin.site.urls),
]
