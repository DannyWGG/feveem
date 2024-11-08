from django.contrib                             import admin
from django.utils.html 			                import format_html
from apps.feveem.models.asistente               import Asistente

class AsistenteAdmin(admin.ModelAdmin):

    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/feveem/asistente/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/feveem/asistente/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    
    list_display        =   ('primer_nombre','segundo_nombre','primer_apellido','segundo_apellido', 'editar', 'eliminar')
    #list_filter         =  ('descripcion',)
    search_fields       =   ()
    list_display_links  = None
    actions             = None

admin.site.register(Asistente, AsistenteAdmin)