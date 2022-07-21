from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerizalizer

    def get(self,request,format=None):
        """Returns a list of API View Features (return an object in API view)"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'is similar to a traditional django view',
            'Gives you the most control of your application logic',
            'Is maped manually to URLs',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})


    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of object"""
        return Response({'method' : 'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method' : 'Delete'})
