class MiembroChat:
    def __init__(self):
        self.usuario = None # El Usuario del miembro.
        self.estado = 'Sin registrar' # El estado del miembro en el chat.
        self.título_personalizado = 'Sin registrar' # Dueños y administradores solamente. El título personalizado del usuario.
        self.es_anónimo = False # Dueños y administradores solamente. Es True si la presencia del usuario está oculta en el chat.
        self.puede_editarse = False # Administradores solamente. True si es permitido que el bot editar privilegios de administrador para ese usuario.
        self.puede_publicar = False # Administradores solamente. Canales solamente. True si el administrador puede publicar en el canal.
        self.puede_editar =  False # Administradores solamente. Canales solamente. True si el administrador puede editar mensajes de otros usuarios.
        self.puede_eliminar = False # Administradores solamente. True si el administrador puede eliminar mensajes de otros usuarios.
        self.puede_restringir = False # Administradores solamente. True si el administrador puede restringir, prohibir o permitir a miembros del chat.
        self.puede_promover = False # Administradores solamente. True si el administrador puede agregar nuevos administradores.
        self.puede_cambiar_info = False # Administradores y restringidos solamente. True si se le es permitido al usuario cambiar títulos, fotos, etc. del chat.
        self.puede_invitar = False # Administradores y restringidos solamente. True si le es permitido al usuario invitar nuevos usuarios al chat.
        self.puede_anclar = False # Administradores y restringidos solamente. True si le es permitido al usuario anclar mensajes en grupos y supergrupos.
        self.es_miembro = False # Restringidos solamente. True si el usuario es un miembro del chat al momento de la petición.
        self.puede_enviar = False # Restringidos solamente. True si el usuario puede enviar mensajes de texto, contactos, ubicaciones y establecimientos.
        self.puede_enviar_media = False # Restringidos solamente. True si el usuario puede enviar audios, documentos, fotos, vídeos, vídeo notas y notas de voz.
        self.puede_encuestar = False # Restringidos solamente. True si el usuario puede enviar encuestas.
        self.puede_enviar_otros = False # Restringidos solamente. True si el usuario puede enviar animaciones, juegos, stickers y usar bots enlínea.
        self.puede_agregar_páginas = False # True si el usuario puede agregar previsualizaciones de páginas web a sus mensajes.
        self.hasta_fecha = False # Restringidos y suspendidos solamente. La fecha en la que las restricciones serán levantados para este usuario en tiempo Unix.

class PermisosChat:
    def __init__(self):
        self.puede_enviar = False # True si el usuario puede enviar mensajes de texto, contactos, ubicaciones y establecimientos.
        self.puede_enviar_media = False # Restringidos solamente. True si el usuario puede enviar audios, documentos, fotos, vídeos, vídeo notas y notas de voz.
        self.puede_encuestar = False # True si el usuario puede enviar encuestas, implica puede_enviar.
        self.puede_enviar_otros = False # Restringidos solamente. True si el usuario puede enviar animaciones, juegos, stickers y usar bots enlínea, implica puede_enviar_media.
        self.puede_agregar_páginas = False # True si el usuario puede agregar previsualizaciones de páginas web a sus mensajes, implica puede_enviar_media.
        self.puede_cambiar_info = False # True si se le es permitido al usuario cambiar títulos, fotos, etc. del chat, es ignorado en supergrupos públicos.
        self.puede_invitar = False # True si le es permitido al usuario invitar nuevos usuarios al chat.
        self.puede_anclar = False # True si le es permitido al usuario anclar mensajes en grupos y supergrupos, ignorado en supergrupos públicos.

class UbicaciónChat:
    def __init__(self):
        self.ubicación = None # La Ubicación a la cual el supergrupo está enlazado. No puede ser una Ubicación en vivo.
        self.dirección = 'Sin registrar' # La dirección o domicilio de la Ubicación. de 1 a 64 caractéres.