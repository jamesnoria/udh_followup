import io
from django.http import FileResponse

from datetime import datetime

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from django.shortcuts import render

def busqueda_productos(request):

    return render(request, 'index.html')


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    p = SimpleDocTemplate(buffer, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
    Story = []

    nombreCompleto = f'{request.GET["prd"]}'
    partesDeDireccion = ["Jr. Huánuco s/n", "Huánuco, Código Postal 064"]

    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    dt = datetime.now()

    texto = dt.strftime("%A %d de %B del %Y")

    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))

    for part in partesDeDireccion:
      texto = '%s' % part.strip()
      Story.append(Paragraph(texto, estilos["Normal"]))

    Story.append(Spacer(1, 12))
    texto = f'Estimado(a) {nombreCompleto.title()}:'
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))

    texto = 'Te escribo desde el futuro y ha sido un camino muy largo y difícil el que nos ha tocado pasar, no nos imaginamos nada de esto cuando nos dijeron que estudiar sistemas era algo fácil o llevadero, pero lo mejor de todo es que valió la pena. Hoy me encuentro trabajando en una buena compañía, con un buen sueldo y acabo de dar la inicial para comprar ese departamento que siempre quisimos tener y eso incluye también el carro de nuestros sueños. Todo esto no sería posible si un día no nos hubiéramos puesto la meta de ser diferentes, de dejar a un lado por un momento la flojera, los juegos, los amigos y todo aquello que parecía distraernos de nuestro objetivo y tomar la iniciativa de cambiar. Conocí un método para hacer seguimiento a nuestras metas que podrías usar, se trata de escribir en una hoja en blanco cinco objetivos que quieras cumplir y cada siete días ir colocando 3, si te sientes satisfecho con haberla realizado; 2, si crees que faltó poner algo de empeño y 1, si no pudiste hacerlo. Esto te servirá para que sepas como va tu progreso y para que al cabo de 21 días o tres semanas con la misma meta en calificación tres, te des cuenta, según la ciencia, que ese objetivo ahora es un hábito que te va a acompañar por el resto de tu vida. Espero puedas seguir adelante y recuerda nunca rendirte ante las dificultades. Te espero en la cima.'
    Story.append(Paragraph(texto, estilos["Justify"]))
    Story.append(Spacer(1, 12))

    texto = 'Sinceramente,'
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))
    texto = 'Tu YO del futuro.'
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))
    p.build(Story)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='mi_compromiso.pdf')