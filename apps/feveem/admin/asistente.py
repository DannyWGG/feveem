from django.contrib                             import admin
from django.utils.html 			                import format_html
from apps.feveem.models.asistente               import Asistente

class AsistenteAdmin(admin.ModelAdmin):

    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/feveem/asistente/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/feveem/asistente/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)
    
    # Sobrescribir el método get_queryset para filtrar por el director
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusuario puede ver todos los registros
        else:
            # Filtrar por el director asociado al usuario
            return qs.filter(usuario=request.user)

    
    list_display        =   ('primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','origen','cedula','institucion_educativa', 'editar', 'eliminar')
    #list_filter         =  ('cedula','cod_plantel')
    search_fields       =  ('cod_plantel','cedula','institucion_educativa',)
    list_display_links  = None
    actions             = None

admin.site.register(Asistente, AsistenteAdmin)