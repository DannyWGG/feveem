from django.contrib                             import admin
from django.utils.html 			                import format_html
from apps.auxiliares.models.Voceria             import Voceria

class VoceriaAdmin(admin.ModelAdmin):

    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/auxiliares/voceria/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/auxiliares/voceria/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    
    list_display        =   ('descripcion', 'editar', 'eliminar')
    #list_filter         =  ('descripcion',)
    search_fields       =   ()
    list_display_links  = None
    actions             = None

admin.site.register(Voceria, VoceriaAdmin)