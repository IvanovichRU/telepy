class IdMensaje:
    """Un identificador único de algún mensaje, este tipo solo es utilizado en el método 'copiar_mensaje."""
    def __init__(self):
        self.id_mensaje = 0 # El identificador único del mensaje.

class EntidadMensaje:
    """Una entidad especial dentro de un mensaje de texto, tales como hashtags, nombres de usuario, URLs, etc."""
    def __init__(self):
        super().__init__()
        self.tipo = 'Sin registrar' # El tipo de entidad.
        self.desplazo = 0 # El desplazo dentro del mensaje en unidades UTF-16.
        self.longitud = 0 # La longitud de la entidad en unidades UTF-16.
        self.url = 'Sin registrar' # El url al que lleva el "text_link".
        self.usuario = None # El usuario mencionado en el "text_mention".
        self.lenguaje = 'Sin registrar' # El lenguaje de programación en el "pre".