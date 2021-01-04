class Sticker:
    def __init__(self):
        self.id_archivo = '' # Identificador para este archivo, usado para descargar o reutilizarlo.
        self.id_única_archivo = 'Sin registrar' # Identificador único para este archivo, para largo plazo.
        self.ancho = 0 # El ancho del sticker.
        self.alto = 0 # El alto del sticker.
        self.es_animado = False # Es True si el sticker es animado.
        self.miniatura = None # La miniatura del sticker en formato .WEBP o .JPG
        self.emoji = 'Sin registrar' # El emoji asociado con el sticker.
        self.nombre_set = 'Sin registrar' # El nombre del set al que este sticker pertenece.
        self.posición_máscara = None # Para stickers de máscara, la posición donde debe posicionarse el sticker.
        self.tamaño_archivo = 0 # El tamaño del archivo.

class SetStickers:
    def __init__(self):
        self.nombre = 'Sin registrar' # El nombre del set de stickers.
        self.título = 'Sin registrar' # El título del set de stickers.
        self.es_animado = False # Es True si el set de stickers contiene stickers animados.
        self.contiene_máscaras = False # Es True si el set de stickers contiene máscaras.
        self.stickers = [] # La lista de todos los stickers dentro del set.
        self.miniatura = None # La miniatura del set en formato .WEBP o .TGS.

class PosiciónMáscara:
    def __init__(self):
        self.punto = 'Sin registrar' # La parte de la cara donde debería colocarse la máscara.
        self.desplazo_x = 0.0 # El desplazo en el eje x medido en anchos de la máscara escalada a la cara de izquierda a derecha.
        self.desplazo_y = 0.0 # El desplazo en el eje y medido en anchos de la máscara escalada a la cara de arriba a abajo.
        self.escala = 0.0 # El coeficiente de escalado de la máscara.