from django.contrib import admin
from .models import banner,events,news,about

# Register your models here.
admin.site.register(banner)
admin.site.register(events)
admin.site.register(news)
admin.site.register(about)
