class Archivo:
    def __init__(self):
        self.id_archivo = '' # El identificador de este archivo, usado para descargar o reutilizar el archivo.
        self.id_única_archivo = '' # El identificador único de este archivo, para largo plazo.
        self.tamaño_archivo = 0 # Tamaño de archivo, si es conocido.
        self.directorio_archivo = '' # El directorio del archivo.

class Contacto:
    def __init__(self):
        self.número = '' # El número telefónico del contacto.
        self.primer_nombre = '' # El primer nombre del contacto.
        self.apellido = '' # El apellido del contacto.
        self.id_usuario = 0 # Identificador del usuario de Telegram enlazado con el contacto.
        self.tarjeta_v = '' # Información adicional acerca del contacto en forma de una vCard.

class Dado:
    def __init__(self):
        self.emoji = '' # El emoji en el cual el lanzamiento está basado.
        self.valor = 0 # El valor en que reuslta el dado.

class DisparadorProximidad:
    def __init__(self):
        self.viajero = None # El usuario que disparó la alerta.
        self.espectador = None # El usuario que puso la alerta.
        self.distancia = 0 # La distancia entre usuarios.

class Encuesta:
    def __init__(self):
        self.id = '' # Identificador único de la encuesta.
        self.pregunta = '' # La pregunta que hace la encuesta.
        self.opciones = [] # Una lista de OpcionEncuesta.
        self.conteo_voto_total = 0 # Número total de usuarios que han votado.
        self.cerrada = False # Es True si la encuesta está cerrada.
        self.anónima = False # Es True si la encuesta es anónima.
        self.tipo = '' # El tipo de encuesta, puede ser 'regular' o 'examen'.
        self.múltiples_respuestas = False # Es True si la encuesta permite múltiples respuestas.
        self.id_opción_correcta = 0 # Identificador de la respuesta correcta mediante una OpciónEncuesta.
        self.explicación = '' # El texto mostrado cuando un usuario selecciona un respuesta incorrecta.
        self.entidades_explicación = [] # Entidades especiales en la explicación como usuarios, URLs, etc.
        self.periodo_abierto = 0 # La cantidad de tiempo en segundos que la encuesta estará abierta.
        self.fecha_cerrada = 0 # El punto en el tiempo en que se cerrará automáticamente la encuesta en tiempo Unix.

class Establecimiento:
    def __init__(self):
        self.ubicación = None # La Ubicación del establecimiento.
        self.título = '' # El nombre del establecimiento.
        self.dirección = '' # La dirección o dimicilio del establecimiento.
        self.id_foursquare = '' # Identificador para foursquare del establecimiento.
        self.tipo_foursquare = '' # El tipo de establecimiento para foursquare.
        self.id_google_place = '' # Identificador para google place del establecimiento.
        self.tipo_google_place = '' # El tipo de establecimiento para google place.

class FotosPerfilUsuario:
    def __init__(self):
        self.cuenta_total = 0 # El número total de fotos que el usuario tiene.
        self.fotos = [] # Fotos de perfil solicitadas.

class OpciónEncuesta:
    def __init__(self):
        self.texto = '' # El texto con la opción de la encuesta.
        self.cuenta_de_voto = 0 # El número de usuarios que han votado por esta opción.

class RespuestaEncuesta:
    def __init__(self):
        self.id_encuesta = '' # El identificador único de la encuesta.
        self.usuario = None # El usuario que haya cambiado la respuesta de la encuesta.
        self.id_opciones = [] # Identificadores de opciones de respuesta.

class Ubicación:
    def __init__(self):
        self.longitud = 0.0 # El valor de la longitud en coordenadas geográficas.
        self.latitud = 0.0 # El valor de la latitud en coordenadas geográficas.
        self.precisión_horizontal = 0.0 # El radio de incertidumbre para la ubicación, varía de 0 a 1500 m.
        self.periodo_en_vivo = 0 # El tiempo en segundos que durarán las actualizaciones desde el envío del mensaje.
        self.dirección = 0 # El ángulo de dirección en el que se está moviendo el usario.
        self.radio_alerta_proximidad = 0 # Distancia máxima para alertas de proximidad.