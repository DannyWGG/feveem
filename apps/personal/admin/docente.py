from django.contrib                             import admin
from django.utils.html 			                import format_html
from apps.personal.models.docente               import Docente
class DocenteAdmin(admin.ModelAdmin):

    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/personal/docente/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/personal/docente/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)
    
    def has_add_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    # Sobrescribir el método get_queryset para filtrar por el director
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusuario puede ver todos los registros
        else:
            # Filtrar por el director asociado al usuario
            return qs.filter(director=request.user)

    # Método para guardar automáticamente el director (usuario que ha iniciado sesión)
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Solo si el objeto es nuevo
            obj.director = request.user
        super().save_model(request, obj, form, change)

    # Hacer que el campo 'director' sea de solo lectura
    readonly_fields = ['director']

    list_display        =   ('origen','cedula','nombres_apellidos','tipo_cargo','codigo_plantel','editar')
    list_filter         =   ('codigo_plantel',)
    exclude             = ('numero_cuenta',)
    search_fields       =   ()
    list_display_links  = None
    actions             = None

    
admin.site.register(Docente, DocenteAdmin)