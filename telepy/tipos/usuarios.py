class Usuario:
    id: int # El identificador único para este usuario o bot.
    es_bot: bool # Es  True si el usuario es un bot.
    primer_nombre: str # El primer nombre del usuario.
    usuario: str # El nombre de usuario del usuario.
    idioma: str # Código de lenguaje IETF asignado.

class Persona(Usuario):
    """Un usuario el cual no es un bot, hijo de Usuario"""
    apellido: str

class Bot(Usuario):
    """Un usuario bot, hijo de Usuario."""
    unible_a_grupos: bool
    lee_todo: bool
    consultas_dentro: bool