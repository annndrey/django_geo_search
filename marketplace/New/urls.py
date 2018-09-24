"""Newrecreativo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from . import views



urlpatterns = [
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^activities/',include('core.urls',namespace='activities')),
    url(r'^accounts/',include('Accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    #url(r'^tags/', include("tags.urls", namespace='tags')),
    url(r'^login_success/$',views.LoginSuccessPage.as_view(),name='login_success'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^supplier/', include('suppliers.urls', namespace='supplier')),
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

