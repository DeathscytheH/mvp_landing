from django.contrib import admin

# Register your models here.
from .models import signUp

class signUpAdmin(admin.ModelAdmin):
	class Meta:
		model = signUp

admin.site.register(signUp, signUpAdmin)