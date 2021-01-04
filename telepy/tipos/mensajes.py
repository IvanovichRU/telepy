class Mensaje:
    """Un mensaje leído por el bot dentro de algún chat en el que participa. Padre de todos los tipos de mensaje."""

    def __init__(self):
        self.id = 0 # Identificador único para el mensaje dentro del chat correspondiente.
        self.fecha = 0 # La fecha en que se envió el mensaje en tiempo Unix.
        self.remitente = None # El usuario que envió el mensaje reenviado, del chat local.
        self.chat = None # El chat al que el mensaje pertenece.
        self.fecha_editado = None # La fecha en la que el mensaje fue editado por última vez en tiempo Unix.


class MensajeTexto(Mensaje):
    """El mensaje más común que contiene solo texto y quizá algunas Entidades."""
    def __init__(self):
        super().__init__()
        self.texto = 'Sin registrar' # El texto UTF-8 del mensaje de 0 hasta 4096 caractéres.
        self.entidades = [] # Entidades especiales en el texto como usuarios, URLs, comandos, etc.

class MensajeReenviado(Mensaje):
    """Un mensaje reenviado de algún lugar."""

    def __init__(self):
        super().__init__()
        self.texto = 'Sin registrar' # El texto del mensaje en UTF-8 como aparece en Telegram.
        self.entidades = [] # Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.
        self.reenviado_remitente = None # El usuario que envió el mensaje original.
        self.reenviado_de_chat = None # La información de mensaje si es reenviado de un canal.
        self.reenviado_id = 0 # El identificador único del mensaje original si es reenviado de un canal.
        self.reenviado_firma = 'Sin registrar' # La firma del autor de la publicación si es reenviado de un canal.
        self.reenviado_nombre = 'Sin registrar' # El nombre del remitente en caso de que no comparta su perfil completo.
        self.reenviado_fecha = 0 # La fecha en la que se envió el mensaje original en tiempo UNIX.

class MensajeBot(Mensaje):
    """Un mensaje proveniente de un bot."""

    def __init__(self):
        super().__init__()
        self.via_bot = None # El bot mediante el cual se envió el mensaje.
        self.texto = 'Sin registrar' # El texto del mensaje en UTF-8 como aparece en Telegram.
        self.entidades = [] # Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.

class MensajeMultimedia(Mensaje):
    """Un mensaje con contenido multimedia."""

    def __init__(self):
        super().__init__()
        self.animación = None # El mensaje contiene una Animación que se almacena en esta propiedad.
        self.audio = None # El mensaje contiene un Audio que se almacena en esta propiedad.
        self.documento = None # El mensaje contiene un Documento que se almacena en esta propiedad.
        self.foto = [] # El mensaje contiene una lista de Fotos que se almacena en esta propiedad.
        self.sticker = None # El mensaje contiene un Sticker que se almacena en esta propiedad.
        self.vídeo = None # El mensaje contiene un Vídeo que se almacena en esta propiedad.
        self.vídeo_nota = None # El mensaje contiene una VídeoNota que se almacena en esta propiedad.
        self.nota_voz = None # El mensaje contiene una NotaVoz que se almacena en esta propiedad.
        self.leyenda = 'Sin registrar' # La leyenda o nota al pie de la animación, audio, documento, foto, vídeo o voz.
        self.entidades = [] # La lista de entidades en la leyenda, tales como usuarios, URLs, comandos, etc.
        self.entidades_leyenda = []

class MensajeCambios(Mensaje):
    """Un mensaje que registra un cambio en el Chat donde se recibió este mensaje."""

    def __init__(self):
        super().__init__()
        self.nuevos_miembros = [] # La lista de miembros nuevos que fueron agregados al Chat o SuperGrupo
        self.miembro_eliminado = None # El miembro que fue removido en este mensaje.
        self.nuevo_título = 'Sin registrar' # El nuevo título del Chat que se cambió en este mensaje.
        self.nueva_foto = [] # La nueva foto del Chat que se cambió en este mensaje.
        self.id_chat_supergrupo = 0 # El identificador único del SuperGrupo en el cual este Grupo se convirtió.
        self.id_supergrupo_chat = 0 # El identificador único del Grupo en el cual este SuperGrupo se convirtió.
        self.mensaje_anclado = None # El Mensaje que fue anclado a este Chat en este mensaje.
        
class MensajeVariado(Mensaje):
    """Un mensaje que no envía ni una de las especificaciones de los anteriores tipos."""

    def __init__(self):
        super().__init__()
        self.contacto = None # El mensaje contiene un Contacto compartido que se almacena en esta propiedad.
        self.dado = None # El mensaje contiene un Dado con un valor aleatorio que se almacena en esta propiedad.
        self.juego = None # El mensaje contiene un Juego que se almacena en esta propiedad.
        self.encuesta = None # El mensaje contiene una Encuesta que se almacena en esta propiedad.
        self.establecimineto = None # El mensaje contiene un Establecimineto que se almacena en esta propiedad.
        self.ubicación = None # El mensaje contiene una Ubicación compartida que se almacena en esta propiedad.
        self.factura = None # El mensaje contiene una Factura que se almacena en esta propiedad.
        self.pago_exitoso = None # El mensaje contiene un PagoExitoso que se almacena en esta propiedad.