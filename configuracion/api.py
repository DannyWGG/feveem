from ninja_extra                            import NinjaExtraAPI
from django_rest_passwordreset.controller   import ResetPasswordController
from apps.cuenta.views.token                import MyTokenObtainPairController, CreateUserController
from ninja.errors                           import ValidationError as NinjaValidationError
from datetime                               import datetime

from apps.cuenta.views.token                import router as token_router

from apps.feveem.views.asistente            import router as asistente
from apps.auxiliares.views.Voceria          import router as Voceria
from apps.auxiliares.views.ExtraCurricular  import router as ExtraCurricular
from apps.auxiliares.views.plantel          import router as Plantel
from apps.reporte.views.general             import router as general_reporte


api = NinjaExtraAPI(
                        title           = "Plantilla",
                        description     = "API para Plantillas",
                        urls_namespace  = "demostrador",
                    )



api.add_router("/auth/", token_router)
api.add_router("/asistente/", asistente)
api.add_router("/voceria/", Voceria)
api.add_router("/extracurricular/", ExtraCurricular)
api.add_router("/directores/", Plantel)
api.add_router("/reportes/", general_reporte)

api.register_controllers(ResetPasswordController)
api.register_controllers(MyTokenObtainPairController)
api.register_controllers(CreateUserController)


# Manejador de excepciones global para ValidationError
@api.exception_handler(NinjaValidationError)
def validation_error_handler(request, exc):
    
    print('AQUIIIIIIIIIIIIII', exc)
    
    # Extraer el último elemento de cada ubicación (loc), que debería ser el campo problemático
    property = [error["loc"][-1] for error in exc.errors]  # Extrae el último elemento de 'loc'

    # Devolver los campos en la respuesta
    return api.create_response(
        request,
        {
            "statusCode": 400,
            "message": "Error en las propiedades de entrada",
            "property": f"{', '.join(property)}", # Solo devuelve el nombre de los campos problemáticos
            "url": request.path,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Añadir fecha y hora actual
        },
        status=400,
    )
    
