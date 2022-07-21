from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """Returns a list of API View Features (return an object in API view)"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)'
            'is similar to a traditional django view'
            'Gives you the most control of your application logic'
            'Is maped manually to URLs'
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
            
