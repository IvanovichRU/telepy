class Archivo:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.tamaño_archivo = 0
        self.directorio_archivo = ''

class Contacto:
    def __init__(self):
        self.número = ''
        self.primer_nombre = ''
        self.apellido = ''
        self.id_usuario = 0
        self.tarjeta_v = ''

class Dado:
    def __init__(self):
        self.emoji = ''
        self.valor = 0

class DisparadorProximidad:
    def __init__(self):
        self.viajero = None
        self.espectador = None
        self.distancia = 0

class Encuesta:
    def __init__(self):
        self.id = ''
        self.pregunta = ''
        self.opciones = []
        self.cuenta_voto_total = 0
        self.cerrada = False
        self.anónima = False
        self.tipo = ''
        self.múltiples_respuestas = False
        self.id_opción_correcta = 0
        self.explicación = ''
        self.entidades_explicación = []
        self.periodo_abierto = 0
        self.fecha_cerrada = 0

class Establecimiento:
    def __init__(self):
        self.ubicación = None
        self.título = ''
        self.dirección = ''
        self.id_foursquare = ''
        self.tipo_foursquare = ''
        self.id_google_place = ''
        self.tipo_google_place = ''

class FotosPerfilUsuario:
    def __init__(self):
        self.cuenta_total = 0
        self.fotos = []

class OpciónEncuesta:
    def __init__(self):
        self.texto = ''
        self.cuenta_de_voto = 0

class RespuestaEncuesta:
    def __init__(self):
        self.id_encuesta = ''
        self.usuario = None
        self.id_opciones = []

class Ubicación:
    def __init__(self):
        self.longitud = 0.0
        self.latitud = 0.0
        self.precisión_horizontal = 0.0
        self.periodo_en_vivo = 0
        self.dirección = 0
        self.radio_alerta_proximidad = 0