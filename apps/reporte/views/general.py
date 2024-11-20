from ninja import Router
from datetime import datetime
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.chart import BarChart, Reference
from io import BytesIO
from django.http import HttpResponse
from django.db.models import Count

from apps.feveem.models.asistente import Asistente

router = Router()

@router.get("/general", response=None)
def reporte_general(request):

 # Crear un nuevo archivo Excel
    wb = Workbook()
    hoja = wb.active
    hoja.title = "Reporte General"

    # Configurar encabezado con imagen
    try:
        logo = Image("static/img/barra.png")  # Ajusta la ruta según tu proyecto
        logo.width, logo.height = 2220, 90
        hoja.add_image(logo, "A1")
    except FileNotFoundError:
        pass  # Si la imagen no existe, continuar sin ella

    # Encabezados
    encabezados = [
        "Estado", "Vocería", "Actividad Extra Curricular", "Total"]
    
    fila_inicial = 6
    for col_index, encabezado in enumerate(encabezados, start=1):  # Comienza en columna A (1)
        hoja.cell(row=fila_inicial, column=col_index, value=encabezado)

    # Agregar los datos al Excel (a partir de la fila siguiente)
    fila_inicial += 1  # Los datos comienzan en la fila 7
    datos = (
        Asistente.objects
        .values('estado', 'voceria__descripcion', 'extra_curricular__descripcion')  # Agrupar por estado, vocería y actividad
        .annotate(total_solicitantes=Count('id'))  # Contar solicitantes
        .order_by('estado', 'voceria__descripcion')
    )
    # Agregar los datos al Excel
    for dato in datos:
        total_solicitudes = Asistente.objects.filter(estado=dato['estado']).count()
        hoja.cell(row=fila_inicial, column=1, value=dato['estado'])
        hoja.cell(row=fila_inicial, column=2, value=dato['voceria__descripcion'])
        hoja.cell(row=fila_inicial, column=3, value=dato['extra_curricular__descripcion'])
        hoja.cell(row=fila_inicial, column=4, value=total_solicitudes)
        fila_inicial += 1  # Avanzar a la siguiente fila

    # Ajustar el ancho de columnas para que el contenido sea visible
    for col in hoja.columns:
        max_length = 0
        col_letter = col[0].column_letter  # Letra de la columna
        for cell in col:
            try:
                max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        hoja.column_dimensions[col_letter].width = max_length + 2

    # Crear gráficos
    grafico_fila_inicio = 6  # Donde se ubicarán los gráficos
    ultima_fila_datos = fila_inicial - 1

    # Gráfico 1: Voceros Contralor por Estado
    contralor_chart = BarChart()
    contralor_chart.title = "Voceros Contralor por Estado"
    contralor_chart.x_axis.title = "Estado"
    contralor_chart.y_axis.title = "Cantidad"
    datos_contralor = Reference(hoja, min_col=5, min_row=7, max_row=ultima_fila_datos)  # Columna Voceros Contralor
    estados = Reference(hoja, min_col=1, min_row=7, max_row=ultima_fila_datos)  # Columna Estados
    contralor_chart.add_data(datos_contralor, titles_from_data=False)
    contralor_chart.set_categories(estados)
    hoja.add_chart(contralor_chart, f"F{grafico_fila_inicio}")

    # Gráfico 2: Voceros Integrador por Estado
    integrador_chart = BarChart()
    integrador_chart.title = "Voceros Integrador por Estado"
    integrador_chart.x_axis.title = "Estado"
    integrador_chart.y_axis.title = "Cantidad"
    datos_integrador = Reference(hoja, min_col=6, min_row=7, max_row=ultima_fila_datos)  # Columna Voceros Integrador
    integrador_chart.add_data(datos_integrador, titles_from_data=False)
    integrador_chart.set_categories(estados)
    hoja.add_chart(integrador_chart, f"F{grafico_fila_inicio + 15}")  # Ajusta la posición vertical del gráfico

    # Gráfico 3: Voceros Activista por Estado
    activista_chart = BarChart()
    activista_chart.title = "Voceros Activista por Estado"
    activista_chart.x_axis.title = "Estado"
    activista_chart.y_axis.title = "Cantidad"
    datos_activista = Reference(hoja, min_col=7, min_row=7, max_row=ultima_fila_datos)  # Columna Voceros Activista
    activista_chart.add_data(datos_activista, titles_from_data=False)
    activista_chart.set_categories(estados)
    hoja.add_chart(activista_chart, f"F{grafico_fila_inicio + 30}") 




    
    # Guardar el archivo en memoria
    """ buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0) """
    
    # Instancias para la generacion del reporte por el metodo HTTP
    ctime       = datetime.now().strftime('%d-%m-%Y')
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Reporte-General - % s.xlsx' % ctime
    wb.save(response)

    return response
