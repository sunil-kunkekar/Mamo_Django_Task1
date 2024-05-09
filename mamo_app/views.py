
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class BusinessContactsRetrieve(generics.ListCreateAPIView):
    queryset         = Business_Contacts.objects.all()
    serializer_class = BusinessContactsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class OLGAMatchesRetrieve(generics.ListCreateAPIView):
    queryset         = OLGA_matches.objects.all()
    serializer_class = OLGAMatchesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PremiumNetworkContactsRetrieve(generics.ListCreateAPIView):
    queryset         = Premium_network_contacts.objects.all()
    serializer_class = PremiumNetworkContactsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
