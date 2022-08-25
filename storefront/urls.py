"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from portfolio.views import main
from portfolio.views import about
from portfolio.views import project
from portfolio.views import skill
from portfolio.views import contact
from portfolio.views import login
from portfolio.views import registration
from portfolio.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__', include('debug_toolbar.urls')),
    path("", main),
    path("about/", about),
    path("projects/", project),
    path("skills/", skill),
    path("contact/", contact),
    path("login/", login),
    path("register/", registration),
    path("logout/", logout)
]
