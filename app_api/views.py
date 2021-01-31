from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_api import serializers

class HelloApiView(APIView):
    """test api view class based on the APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns the list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'gives control over logic',
            'You can do anything',
        ]

        return Response({'message':'Welcome to apiview! ', 'an_apiview': an_apiview})


    def post(self, request):
        """creating a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
