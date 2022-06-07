from django.contrib import admin
from .models import User, Customer, Owner

# Register your models here.
# admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Owner)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','phone_number', 'email', 'is_owner', 'is_customer', 'is_superuser']
    list_filter = ['is_owner', 'is_customer','is_superuser']