from .models import Profile

# Register your models here.
from django.contrib import admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["firstname"]

    # "my_name" needs to be assigned

    @admin.display(description='First name')
    def firstname(self, obj):  # ↑ Displayed
        return obj.firstName



admin.site.register(Profile, ProfileAdmin)