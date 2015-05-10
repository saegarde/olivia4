from django.contrib import admin

from .models import Art

# Register your models here.

class AddArt(admin.ModelAdmin):
	list_display = ['title', 'artist', 'url', 'size', 'medium', 'price']
	class Meta:
		model = Art

admin.site.register(Art, AddArt)
