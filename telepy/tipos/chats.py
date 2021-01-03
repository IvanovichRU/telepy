class Chat:
    """Un chat de Telegram. Padre de todos los tipos de chat."""
    def __init__(self, objeto: dict):
        self.id = 0
        self.tipo = ''
        self.foto = None
        self.mensaje_anclado = None
        self.cambia_stickers = False

class ChatPrivado(Chat):
    """Un chat privado de Telegram, en él solo participan dos usuarios de Telegram."""
    def __init__(self, objeto: dict):
        super().__init__()
        self.usuario = ''
        self.primer_nombre = ''
        self.apellido = ''
        self.bio = ''

class Grupo(Chat):
    """Un grupo de Telegram en el cual puede haber hasta 200 miembros."""
    def __init__(self, objeto: dict):
        super().__init__()
        self.título = ''
        self.descripción = ''
        self.invitación = ''
        self.permisos = None

class SuperGrupo(Chat):
    """Un supergrupo de Telegram en el cual puede haber hasta 5,000 suscriptores/miembros."""
    def __init__(self, objeto: dict):
        super().__init__()
        self.título = ''
        self.descripción = ''
        self.invitación = ''
        self.permisos = None
        self.retraso = 0
        self.nombre_set_stickers = ''

class Canal(Chat):
    """Un canal de Telegram el cual puede tener un número ilimitado de suscriptores."""
    def __init__(self, objeto: dict):
        super().__init__()
        self.título = ''
        self.descripción = ''
        self.invitación = ''