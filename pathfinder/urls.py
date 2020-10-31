from django.urls import path
from . import views
from rest_framework import routers

djsktras_pathfinder = views.PathfinderViewSet.as_view({'post': 'djsktras'})

urlpatterns = [
    
    path('djsktras/<int:row>/<int:col>/<int:start>/<int:end>/', djsktras_pathfinder)
]
