class Chat:
    """Un chat de Telegram. Padre de todos los tipos de chat."""
    def __init__(self):
        self.id = 0 # Identificador único para este chat.
        self.tipo = '' # El tipo de chat.
        self.foto = None # La foto del chat, solo se recibe en el método obtener_chat.
        self.mensaje_anclado = None # El mensaje anclado más reciente.
        self.cambia_stickers = False # Es True si el bot puede cambiar el set de stickers.

class ChatPrivado(Chat):
    """Un chat privado de Telegram, en él solo participan dos usuarios de Telegram."""
    def __init__(self):
        super().__init__()
        self.usuario = 'Sin registrar' # El nombre de usuario en chats privados o supergrupos.
        self.primer_nombre = 'Sin registrar' # El primer nombre de la otra persona en un chat privado.
        self.apellido = 'Sin registrar' # El apellido de la otra persona en un chat privado.
        self.bio = 'Sin registrar' # El bio de la otra persona en un chat privado.

class Grupo(Chat):
    """Un grupo de Telegram en el cual puede haber hasta 200 miembros."""
    def __init__(self):
        super().__init__()
        self.título = 'Sin registrar' # El título para supergrupos, canales y grupos.
        self.descripción = 'Sin registrar' # La descripción para grupos, supergrupos y canales.
        self.invitación = 'Sin registrar' # El link de invitación para grupos, supergrupos y canales.
        self.permisos = None # Los permisos por default de miembros del grupo o supergrupo.

class SuperGrupo(Chat):
    """Un supergrupo de Telegram en el cual puede haber hasta 5,000 suscriptores/miembros."""
    def __init__(self):
        super().__init__()
        self.título = 'Sin registrar' # El título para supergrupos, canales y grupos.
        self.descripción = 'Sin registrar' # La descripción para grupos, supergrupos y canales.
        self.invitación = 'Sin registrar' # El link de invitación para grupos, supergrupos y canales.
        self.permisos = None # Los permisos por default de miembros del grupo o supergrupo.
        self.retraso = 0 # El retraso mínimo permitido entre mensajes consecutivos para supergrupos.
        self.nombre_set_stickers = 'Sin registrar' # El nombre del set de stickers del supergrupo.

class Canal(Chat):
    """Un canal de Telegram el cual puede tener un número ilimitado de suscriptores."""
    def __init__(self):
        super().__init__()
        self.título = 'Sin registrar' # El título para supergrupos, canales y grupos.
        self.descripción = 'Sin registrar' # La descripción para grupos, supergrupos y canales.
        self.invitación = 'Sin registrar' # El link de invitación para grupos, supergrupos y canales.