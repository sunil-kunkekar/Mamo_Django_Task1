from rest_framework import serializers
from .models import Business_Contacts, OLGA_matches, Premium_network_contacts

class BusinessContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Contacts
        fields = '__all__'

class OLGAMatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OLGA_matches
        fields = '__all__'

class PremiumNetworkContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium_network_contacts
        fields = '__all__'
