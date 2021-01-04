class Audio:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.duración = 0 # La duración del audio en segundos.
        self.actor = 'Sin registrar' # El actor que grabó el audio.
        self.título = 'Sin registrar' # El título del audio.
        self.nombre_archivo = 'Sin registrar' # El nombre original del archivo.
        self.tipo_mime = 'Sin registrar' # El tipo de media MIME del archivo.
        self.tamaño_archivo = 0 # Tamaño del archivo.
        self.miniatura = None # La portada del álbum al cual la música pertenece.

class Animación:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.ancho = 0 # La anchura del vídeo en píxeles.
        self.alto = 0 # La altura del vídeo en píxeles.
        self.duración = 0 # La duración de la animación en segundos.
        self.miniatura = None # La miniatura de la animación.
        self.nombre_archivo = 'Sin registrar' # El nombre original del archivo.
        self.tipo_mime = 'Sin registrar' # El tipo de media MIME del archivo.
        self.tamaño_archivo = 0 # Tamaño del archivo.

class Documento:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.miniatura = None # La miniatura del documento.
        self.nombre_archivo = 'Sin registrar' # El nombre original del archivo.
        self.tipo_mime = 'Sin registrar' # El tipo de media MIME del archivo.
        self.tamaño_archivo = 0 # Tamaño del archivo.

class FotoChat:
    def __init__(self):
        self.id_foto_pequeña = 'Sin registrar' # Identificador de la foto pequeña del chat.
        self.id_único_foto_pequeña = 'Sin registrar' # Identificador único del archivo de la foto pequeña del chat.
        self.id_foto_grande = 'Sin registrar' # Identificador de la foto grande del chat.
        self.id_único_foto_grande = 'Sin registrar' # Identificador único del archivo de la foto grande del chat.

class NotaVoz:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.duración = 0 # La duración del audio en segundos.
        self.tipo_mime = 'Sin registrar' # El tipo de media MIME del archivo.
        self.tamaño_archivo = 0 # Tamaño del archivo.

class TamañoFoto:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.ancho = 0 # Ancho de la foto.
        self.alto = 0 # Alto de la foto.
        self.tamaño_archivo = 0 # Tamaño del archivo.

class VideoNota:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.longitud = 0 # El ancho y alto del vídeo.
        self.duración = 0 # La duración del vídeo en segundos.
        self.miniatura = None # La miniatura del vídeo.
        self.tamaño_archivo = 0 # Tamaño del archivo.

class Vídeo:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.ancho = 0 # La anchura del vídeo.
        self.alto = 0 # La altura del vídeo.
        self.duración = 0 # Duración del vídeo en segundos.
        self.miniatura = None # La miniatura del vídeo.
        self.nombre_archivo = 'Sin registrar' # La miniatura del documento.
        self.tipo_mime = 'Sin registrar' # El tipo de media MIME del archivo.
        self.tamaño_archivo = 0 # Tamaño del archivo.