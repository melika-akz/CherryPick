from django.contrib import admin
from .models import Place, Geolocation, ImageHome, Home, Address

admin.site.register(Geolocation)
admin.site.register(Place)
admin.site.register(ImageHome)
admin.site.register(Home)
admin.site.register(Address)


