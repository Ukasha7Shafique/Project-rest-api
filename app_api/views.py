from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view class based on the APIView"""

    def get(self, request, format=None):
        """Returns the list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'gives control over logic',
            'You can do anything',
        ]

        return Response({'message':'Welcome to apiview! ', 'an_apiview': an_apiview})
