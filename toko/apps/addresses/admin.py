from django.contrib import admin
from .models import AddressBook, City, Province, SubDistrict, Village


admin.site.register(AddressBook)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(SubDistrict)
admin.site.register(Village)
