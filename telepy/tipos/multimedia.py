class Audio:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo =''
        self.duración = 0
        self.actor = ''
        self.título = ''
        self.nombre_archivo = ''
        self.tipo_mime = ''
        self.tamaño_archivo = 0
        self.miniatura = None

class Animación:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.ancho = 0
        self.alto = 0
        self.duración = 0
        self.miniatura = None
        self.nombre_archivo = ''
        self.tipo_mime = ''
        self.tamaño_archivo = 0

class Documento:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.miniatura = None
        self.archivo_nombre = ''
        self.tipo_mime = ''
        self.tamaño_archivo = 0

class FotoChat:
    def __init__(self):
        self.id_foto_pequeña = ''
        self.id_único_foto_pequeña = ''
        self.id_foto_grande = ''
        self.id_único_foto_grande = ''

class NotaVoz:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.duración = 0
        self.tipo_mime = ''
        self.tamaño_archivo = 0

class TamañoFoto:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.ancho = 0
        self.alto = 0
        self.tamaño_archivo = 0

class VideoNota:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.longitud = 0
        self.duración = 0
        self.miniatura = None
        self.tamaño_archivo = 0

class Vídeo:
    def __init__(self):
        self.id_archivo = ''
        self.id_única_archivo = ''
        self.ancho = 0
        self.alto = 0
        self.duración = 0
        self.miniatura = None
        self.nombre_archivo = ''
        self.tipo_mime = ''
        self.tamaño_archivo = 0