
class Chat:
    def __init__(self):
        self.id = 0
        self.tipo = ''
        self.foto = []
        self.mensaje_anclado = None
        self.cambia_stickers = False

class ChatPrivado(Chat):
    usuario: str
    primer_nombre: str
    apellido: str
    bio: str

class Grupo(Chat):
    título: str
    descripción: str
    invitación: str
    permisos: PermisosChat

class SuperGrupo(Chat):
    título: str
    descripción: str
    invitación: str
    permisos: PermisosChat
    retraso: int
    nombre_set_stickers: str

class Canal(Chat):
    título: str
    descripción: str
    invitación: str
