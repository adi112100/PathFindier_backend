from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .algorithms.djsktras import djsktras_algorithm
from .algorithms.dfs import dfs_algorithm
import json

from .serializers import WallsSerializer

from django.shortcuts import render

# Create your views here.
class PathfinderViewSet(viewsets.GenericViewSet):

    default_serializer_class = WallsSerializer

    serializer_classes = {
		'djsktras' : WallsSerializer,
        'dfs' : WallsSerializer
	}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
    
    def djsktras(self, request, row, col, start, end):
       
        serializer = WallsSerializer(data = request.data)
        if serializer.is_valid():
            

            walls = json.loads(serializer.data['walls'])
            streamnodes, shortest_path_val, shortest_path = djsktras_algorithm(row, col, start, end, walls)
            
            streamnodes = json.dumps(streamnodes)
            shortest_path_val = json.dumps(shortest_path_val)
            shortest_path = json.dumps(shortest_path[end])
            return Response(
                {
                    'streamnodes' : streamnodes,
                    'shortest_path_val' : shortest_path_val,
                    'shortest_path' : shortest_path
                }
            )
    
    def dfs(self, request, row, col, start, end):
       
        serializer = WallsSerializer(data = request.data)
        if serializer.is_valid():
            
            
            walls = json.loads(serializer.data['walls'])
            streamnodes, shortest_path = dfs_algorithm(row, col, start, end, walls)
            
            streamnodes = json.dumps(streamnodes)
            shortest_path = json.dumps(shortest_path)
            print(shortest_path)
            return Response(
                {
                    'streamnodes' : shortest_path,
                    'shortest_path' : shortest_path
                }
            )
        
