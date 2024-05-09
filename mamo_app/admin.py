from django.contrib import admin

# Register your models here.

from .models import Business_Contacts, OLGA_matches, Premium_network_contacts

admin.site.register(Business_Contacts)
admin.site.register(OLGA_matches)
admin.site.register(Premium_network_contacts)
