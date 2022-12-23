from django.contrib import admin
from .models import Noticia, Categoria, User
# Register your models here.

@admin.register(Noticia)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id', 'activo', 'fecha', 'Categoria')


admin.site.register(Categoria)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nombre')
#admin.site.register(Noticia)

admin.site.unregister(User)
admin.site.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name','last_name','is_superuser','get_groups')
    def get_groups(self, obj):
        l=obj.groups.values_list('name',flat=True)
        l_as_list=list(l)
        return l_as_list
    get_groups.short_description="Grupo"