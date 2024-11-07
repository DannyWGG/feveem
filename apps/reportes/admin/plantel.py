from django.contrib                             import admin
from django.utils.html 			                import format_html
from apps.reportes.models.plantel               import Plantel

class PlantelAdmin(admin.ModelAdmin):

    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/reportes/plantel/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/reportes/plantel/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    list_display        =   ('nombre', 'codigo', 'direccion', 'telefono', 'editar', 'eliminar',)
    list_filter         =   ('nombre', 'codigo')
    search_fields       =   ()
    list_display_links  = None
    actions             = None

admin.site.register(Plantel, PlantelAdmin)