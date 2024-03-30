from django.urls import path
from mobile.views import *
app_name='anything'
urlpatterns=[
    path('samsung/',samsung,name='samsung'),
    path('oppo/',oppo,name='oppo'),

]