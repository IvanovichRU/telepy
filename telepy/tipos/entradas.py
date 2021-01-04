class MediaEntrada:
    def __init__(self):
        self.tipo = 'Sin registrar' # El tipo de media.
        self.media = 'Sin registrar' # El archivo a ser enviado.
        self.leyenda = 'Sin registrar' # La leyenda de la media a ser enviada.
        self.modo_analizar = '' # El modo de analizar las entidades en la leyenda.
        self.entidades_leyenda = [] # La lista de entidades especiales en la leyenda, estas pueden ser especificadas en lugar de usar modo_analizar.

class FotoEntrada(MediaEntrada):
    def __init__(self):
        super().__init__()
        self.tipo = 'photo'

class VídeoEntrada(MediaEntrada):
    def __init__(self):
        super().__init__()
        self.tipo = 'video'
        self.miniatura = None # La miniatura del vídeo a ser enviado. Puede ser una cadena str o un ArchivoEntrada.
        self.ancho = 0 # La altura del vídeo en píxeles.
        self.alto = 0 # La anchura del vídeo en píxeles.
        self.duración = 0 # La duración del vídeo en segundos.

class AnimaciónEntrada(MediaEntrada):
    def __init__(self):
        super().__init__()
        self.tipo = 'animation'
        self.miniatura = None # La miniatura de la animación a ser enviada. Puede ser una cadena str o un ArchivoEntrada.
        self.ancho = 0 # La altura de la animación en píxeles.
        self.alto = 0 # La anchura de la animación en píxeles.
        self.duración = 0 # La duración de la animación en segundos.

class AudioEntrada(MediaEntrada):
    def __init__(self):
        super().__init__()
        self.tipo = 'audio'
        self.duración = 0 # La duración del audio en segundos.
        self.actor = 'Sin registrar' # El actor que realizó el audio a ser enviado.
        self.título = 'Sin registrar' # El título del audio el audio a ser enviado.

class DocumentoEntrada(MediaEntrada):
    def __init__(self):
        super().__init__()
        self.tipo = 'document'
        self.miniatura = None # La miniatura del documento a ser enviado. Puede ser una cadena str o un ArchivoEntrada.
        self.desactivar_detección_de_tipo = False # Desactiva la detección automática de lado del servidor para el tipo de archivo. Debe ser True si se envía el archivo mediante multipart/form-data.
                                                  # Siempre True si el documento se envía como parte de un álbum.

class ArchivoEntrada(MediaEntrada):
    pass