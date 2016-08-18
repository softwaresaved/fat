"""fat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from . import views
from . import settings 

urlpatterns = [
    url(r'^sign-in/', auth_views.login,
        {'template_name': 'fat/sign_in.html'},
        name="sign_in"),
    url(r'^sign-out/', auth_views.logout,
        {'next_page': '/'},
        name="sign_out"),
    url(r'^claimed/(?P<claimed_id>[0-9]+)/', views.claimed_detail, name="claimed_detail"),
    url(r'^claimed/', views.claimed, name="claimed"),
    url(r'^fellow/(?P<claimed_id>[0-9]+)/', views.claimed_detail, name="fellow_detail"),
    url(r'^fellow/', views.claimed, name="fellow"),
    url(r'^fund/(?P<fund_id>[0-9]+)/expense/(?P<expense_relative_number>[0-9\-]+)/review', views.expense_review_relative, name="expense_review_relative"),
    url(r'^fund/(?P<fund_id>[0-9]+)/expense/(?P<expense_relative_number>[0-9\-]+)/', views.expense_detail_relative, name="expense_detail_relative"),
    url(r'^fund/(?P<fund_id>[0-9]+)/review', views.fund_review, name="fund_review"),
    url(r'^fund/(?P<fund_id>[0-9]+)/', views.fund_detail, name="fund_detail"),
    url(r'^fund/previous/', views.fund_past, name="fund_past"),
    url(r'^fund/', views.fund, name="fund"),
    url(r'^expense/(?P<expense_id>[0-9\-]+)/review', views.expense_review, name="expense_review"),
    url(r'^expense/(?P<expense_id>[0-9\-]+)/', views.expense_detail, name="expense_detail"),
    url(r'^expense/', views.expense, name="expense"),
    url(r'^blog/(?P<blog_id>[0-9]+)/review', views.blog_review, name="blog_review"),
    url(r'^blog/(?P<blog_id>[0-9]+)/', views.blog_detail, name="blog_detail"),
    url(r'^blog/', views.blog, name="blog"),
    url(r'^dashboard/', views.dashboard, name="dashboard"),
    url(r'^my-profile/', views.my_profile, name="my_profile"),
    url(r'^geojson/', views.geojson, name="geojson"),
    url(r'^report/', views.report, name="report"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
