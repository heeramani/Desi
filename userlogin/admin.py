from django.contrib import admin
from .models import *
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
	list_display=["Utype","name","phone_number","location"]
	class Meta:
		model = Restaurant


admin.site.register(MyUser)
admin.site.register(SystemAdmin)
admin.site.register(Customer)
admin.site.register(Cuisine)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItems)


