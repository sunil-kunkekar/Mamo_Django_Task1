from django.urls import path
from .views import (
    BusinessContactsRetrieve,
    OLGAMatchesRetrieve,
    PremiumNetworkContactsRetrieve,
)

urlpatterns = [
    #  for Business_Contacts
    path('business_contacts/', BusinessContactsRetrieve.as_view(), name='business_contacts_list_create'),
    path('business_contacts/all/', BusinessContactsRetrieve.as_view(), name='business_contacts_retrieve'),

    # for OLGA_matches
    path('olga_matches/', OLGAMatchesRetrieve.as_view(), name='olga_matches_list_create'),
    path('olga_matches/all/', OLGAMatchesRetrieve.as_view(), name='olga_matches_retrieve'),

    #  for Premium_network_contacts
    path('premium_network_contacts/', PremiumNetworkContactsRetrieve.as_view(), name='premium_network_contacts_list_create'),
    path('premium_network_contacts/all/', PremiumNetworkContactsRetrieve.as_view(), name='premium_network_contacts_retrieve'),
]
