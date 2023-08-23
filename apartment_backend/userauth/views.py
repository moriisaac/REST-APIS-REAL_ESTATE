from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Username(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


