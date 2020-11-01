from django.urls import path
from . import views
from rest_framework import routers

djsktras_pathfinder = views.PathfinderViewSet.as_view({'post': 'djsktras'})
dfs_pathfinder = views.PathfinderViewSet.as_view({'post': 'dfs'})

urlpatterns = [
    
    path('djsktras/<int:row>/<int:col>/<int:start>/<int:end>/', djsktras_pathfinder),
    path('dfs/<int:row>/<int:col>/<int:start>/<int:end>/', dfs_pathfinder)
]
