from django.urls import path
from . import views
from rest_framework import routers

djsktras_pathfinder = views.PathfinderViewSet.as_view({'post': 'djsktras'})
dfs_pathfinder = views.PathfinderViewSet.as_view({'post': 'dfs'})
astar_pathfinder = views.PathfinderViewSet.as_view({'post': 'astar'})

urlpatterns = [
    
    path('djsktras/<int:row>/<int:col>/<int:start>/<int:end>/', djsktras_pathfinder),
    path('astar/<int:row>/<int:col>/<int:start>/<int:end>/', astar_pathfinder),
    path('dfs/<int:row>/<int:col>/<int:start>/<int:end>/', dfs_pathfinder)
]
