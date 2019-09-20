from django.shortcuts import render

from django.views.generic import TemplateView


class HomePageView(TemplateView):

	template_name = 'home.html'


from django.contrib import admin

from django.urls import path, include #new


urlpatterns = [

	path('admin/', admin.site.urls),

	path('', include('pages.urls')), # new

]

# Create your views here.
