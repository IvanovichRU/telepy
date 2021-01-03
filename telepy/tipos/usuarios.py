class Usuario:
    """Un usuario de Telegram padre de todos los demás tipos de usuario."""
    def __init__(self, objeto: dict):
        self.id = 0 # El identificador único para este usuario o bot.
        self.es_bot = False # Es True si el usuario es un bot.
        self.primer_nombre = '' # El primer nombre del usuario.
        self.apellido = '' # Apellido de 
        self.usuario = '' # El nombre de usuario del usuario.
        self.idioma = '' # Código de lenguaje IETF asignado.

class Bot(Usuario):
    """Un usuario bot, hijo de Usuario."""
    def __init__(self, objeto: dict):
        self.unible_a_grupos = False # Es True si el bot puede ser invitado a grupos.
        self.lee_todo = False # Es True si el modo privacidad está desactivado para el bot.
        self.consultas_dentro = False # Es True si el bot soporta consultas enlínea.