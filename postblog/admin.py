from django.contrib import admin
from .models import Myblog,Contact

# Register your models here.
@admin.register(Myblog)
class Adminmyblog(admin.ModelAdmin):
    list_display=['title','con']

@admin.register(Contact)
class Adminmyblog(admin.ModelAdmin):
    list_display=['name','email','message']    