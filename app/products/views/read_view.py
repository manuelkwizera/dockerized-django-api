from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils.constants import ALL_PRODUCTS


class ReadAPIView(APIView):
    def get(self, request):
        if not request.GET['filter']:
            return Response({
                'message': "No filter parameter found",
                'status': 500
            })
        
        filter = request.GET['filter']
        
        response = {
            'products': ALL_PRODUCTS[filter],
            'status': 500,
        }
        
        return Response(response)
        