from django.urls import path
from . import views
from .views import handler404

urlpatterns = [
    path('', views.index, name='home'),

]

handler404 = 'boutique_ado.views.handler404'