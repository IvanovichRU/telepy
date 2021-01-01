class Chat:
    """Un chat de Telegram. Padre de todos los tipos de chat."""
    def __init__(self, objeto: dict):
        self.id = 0
        self.tipo = ''
        self.foto = []
        self.mensaje_anclado = None
        self.cambia_stickers = False

        # self.id = objeto['id']
        # if 'type' in objeto:
        #     self.tipo = objeto['type']
        # if 'title' in objeto:
        #     self.título = objeto['title']
        # if 'username' in objeto:
        #     self.usuario = objeto['username']
        # if 'first_name' in objeto:
        #     self.primer_nombre = objeto['first_name']
        # if 'last_name' in objeto:
        #     self.apellido = objeto['last_name']
        # if 'photo' in objeto:
        #     self.foto = objeto['photo']
        # if 'bio' in objeto:
        #     self.bio = objeto['bio']
        # if 'description' in objeto:
        #     self.descripción = objeto['description']
        # if 'invite_link' in objeto:
        #     self.invitación = objeto['invite_link']
        # if 'pinned_message' in objeto:
        #     self.mensaje_anclado = objeto['pinned_message']
        # if 'permissions' in objeto:
        #     self.permisos = objeto['permissions']
        # if 'slow_mode_delay' in objeto:
        #     self.nombre_set_stickers = objeto['slow_mode_delay']
        # if 'sticker_set_name' in objeto:
        #     self.nombre_set_stickers = objeto['sticker_set_name']
        # if 'can_set_sticker_set' in objeto:
        #     self.cambia_stickers = objeto['can_set_sticker_set']
        # if 'linked_chat_id' in objeto:
        #     self.retraso = objeto['linked_chat_id']
        # if 'location' in objeto:
            # self.ubicación = objeto['location']

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
