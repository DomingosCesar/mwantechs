from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.noticias, name='noticias'),
    path('', views.artigos, name='artigos'),
    path('', views.contribs, name='contribs'),
    path('', views.sobre, name='sobre'),
]

'''
    I AM A HIGHLY MOTIVATED AND RESULTS-DRIVEN SALES PROFESSIONAL SEEKING A CHALLENGING OPPORTUNITY TO LEVERAGE MY SKILLS AND EXPERIENCE IN A DYNAMIC SALES ENVIRONMENT. MBA / SCHOOL, LOCATION 
MAY 20XX 

'''