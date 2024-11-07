from django.contrib                             import admin
from django.utils.html 			                import format_html
from apps.reportes.models.estudiante            import Estudiante

class EstudianteAdmin(admin.ModelAdmin):

    # Accesos directos del lado derecho
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/reportes/estudiante/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/reportes/estudiante/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    def mostrar_nivel(self, obj):
        return f'{obj.nivel.descripcion} ({obj.nivel.area_id})'  # Acceder a los campos del modelo Nivel
    mostrar_nivel.short_description = 'Nivel'  # Nombre de la columna en el admin

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

    list_display        =   ('mostrar_nivel', 'cantidad_femenino', 'cantidad_masculino', 'total', 'editar', 'eliminar',)
    list_filter         =   ('cantidad_femenino', 'cantidad_masculino')
    search_fields       =   ()
    list_display_links  = None
    actions             = None
    exclude             =   ('total','dia', 'mes', 'anio')

admin.site.register(Estudiante, EstudianteAdmin)