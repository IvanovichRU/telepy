class Usuario:
    """Un usuario de Telegram padre de todos los demás tipos de usuario."""
    def __init__(self):
        self.id = 0 # El identificador único para este usuario o bot.
        self.es_bot = False # Es  True si el usuario es un bot.
        self.primer_nombre = '' # El primer nombre del usuario.
        self.usuario = '' # El nombre de usuario del usuario.
        self.idioma = '' # Código de lenguaje IETF asignado.

class Persona(Usuario):
    """Un usuario el cual no es un bot, hijo de Usuario"""
    def __init__(self):
        super().__init__()
        self.apellido = ''

class Bot(Usuario):
    """Un usuario bot, hijo de Usuario."""
    def __init__(self):
        self.unible_a_grupos = False
        self.lee_todo = False
        self.consultas_dentro = False