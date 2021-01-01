class IdMensaje:
    """Un identificador único de algún mensaje, este tipo solo es utilizado en el método 'copiar_mensaje."""
    def __init__(self):
        super().__init__()
        self.id_mensaje = 0

class EntidadMensaje:
    """Una entidad especial dentro de un mensaje de texto, tales como hashtags, nombres de usuario, URLs, etc."""
    def __init__(self):
        super().__init__()
        self.tipo = ''
        self.desplazo = 0
        self.longitud = 0
        self.url = ''
        self.usuario = None
        self.lenguaje = ''