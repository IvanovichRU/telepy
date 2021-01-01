class Mensaje:
    """Un mensaje leído por el bot dentro de algún chat en el que participa. Padre de todos los tipos de mensaje."""

    def __init__(self, objeto: dict):
        self.id = 0
        self.fecha = 0
        self.chat = None
        self.fecha_editado = None
        
        # self.id = objeto['message_id'] # El identificador único para este mensaje dentro de este chat.
        # if 'from' in objeto:
        #     self.remitente = objeto['from']
        # else:
        #     self.remitente = None
        # if 'date' in objeto:
        #     self.fecha = objeto['date']
        # else:
        #     self.fecha = None
        # if 'chat' in objeto:
        #     self.chat = objeto['chat']
        # if 'forward_from' in objeto:
        #     self.reenviado_remitente = objeto['forward_from']
        # if 'forward_from_chat' in objeto:
        #     self.reenviado_de_chat = objeto['forward_from_chat']
        # if 'forward_from_message_id' in objeto:
        #     self.reenviado_id = objeto['forward_from_message_id']
        # if 'forward_signature' in objeto:
        #     self.reenviado_firma = objeto['forward_signature']
        # if 'forward_sender_name' in objeto:
        #     self.reenviado_nombre = objeto['forward_sender_name']
        # if 'forward_date' in objeto:
        #     self.reenviado_fecha = objeto['forward_date']
        # if 'reply_to_message' in objeto:
        #     self.respuesta_a = objeto['reply_to_message']
        # if 'via_bot' in objeto:
        #     self.via_bot = objeto['via_bot']
        # if 'edit_date' in objeto:
        #     self.fecha_editado = objeto['edit_date']
        # if 'text' in objeto:
        #     self.texto = objeto['text']
        # if 'entities' in objeto:
        #     self.entidades = objeto['entities']
        # if 'animation' in objeto:
        #     self.animación = objeto['animation']
        # if 'audio' in objeto:
        #     self.audio = objeto['audio']
        # if 'document' in objeto:
        #     self.documento = objeto['document']
        # if 'photo' in objeto:
        #     self.foto = objeto['photo']
        # if 'sticker' in objeto:
        #     self.sticker = objeto['sticker']
        # if 'video' in objeto:
        #     self.vídeo = objeto['video']
        # if 'video_note' in objeto:
        #     self.vídeo_nota = objeto['video_note']
        # if 'voice' in objeto:
        #     self.nota_voz = objeto['voice']
        # if 'caption' in objeto:
        #     self.leyenda = objeto['caption']
        # if 'caption_entities' in objeto:
        #     self.entidades_leyenda = objeto['caption_entities']
        # if 'contact' in objeto:
        #     self.contacto = objeto['contact']
        # if 'dice' in objeto:
        #     self.dado = objeto['dice']
        # if 'game' in objeto:
        #     self.juego = objeto['game']
        # if 'poll' in objeto:
        #     self.encuesta = objeto['poll']
        # if 'venue' in objeto:
        #     self.establecimiento = objeto['venue']
        # if 'location' in objeto:
        #     self.ubicación = objeto['location']
        # if 'new_chat_members' in objeto:
        #     self.nuevos_miembros = objeto['new_chat_members']
        # if 'left_chat_member' in objeto:
        #     self.miembro_eliminado = objeto['left_chat_member']
        # if 'new_chat_title' in objeto:
        #     self.nuevo_título = objeto['new_chat_title']
        # if 'new_chat_photo' in objeto:
        #     self.nueva_foto = objeto['new_chat_photo']
        # if 'migrate_to_chat_id' in objeto:
        #     self.id_chat_supergrupo = objeto['migrate_to_chat_id']
        # if 'migrate_from_chat_id' in objeto:
        #     self.id_supergrupo_chat = objeto['migrate_from_chat_id']
        # if 'pinned_message' in objeto:
        #     self.mensaje_anclado = objeto['pinned_message']
        # if 'invoice' in objeto:
        #     self.factura = objeto['invoice']
        # if 'successful_payment' in objeto:
        #     self.pago_exitoso = objeto['successful_payment']

class MensajeReenviado(Mensaje):
    """Un mensaje reenviado de algún lugar."""

    def __init__(self, objeto: dict):
        super().__init__()
        self.remitente = None # El usuario que envió el mensaje reenviado, del chat local.
        self.texto = '' # El texto del mensaje en UTF-8 como aparece en Telegram.
        self.entidades = [] # Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.
        self.reenviado_remitente = None # El usuario que envió el mensaje original.
        self.reenviado_de_chat = None # La información de mensaje si es reenviado de un canal.
        self.reenviado_id = 0 # El identificador único del mensaje original si es reenviado de un canal.
        self.reenviado_firma = '' # La firma del autor de la publicación si es reenviado de un canal.
        self.reenviado_nombre = '' # El nombre del remitente en caso de que no comparta su perfil completo.
        self.reenviado_fecha = 0 # La fecha en la que se envió el mensaje original en tiempo UNIX.

class MensajeBot(Mensaje):
    """Un mensaje proveniente de un bot."""

    def __init__(self, objeto: dict):
        super().__init__()
        self.via_bot = None # El bot mediante el cual se envió el mensaje.
        self.texto = '' # El texto del mensaje en UTF-8 como aparece en Telegram.
        self.entidades = [] # Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.

class MensajeMultimedia(Mensaje):
    """Un mensaje con contenido multimedia."""

    def __init__(self, objeto: dict):
        super().__init__()
        self.animación = None # El mensaje contiene una Animación que se almacena en esta propiedad.
        self.audio = None # El mensaje contiene un Audio que se almacena en esta propiedad.
        self.documento = None # El mensaje contiene un Documento que se almacena en esta propiedad.
        self.foto = None # El mensaje contiene una lista de Fotos que se almacena en esta propiedad.
        self.sticker = None # El mensaje contiene un Sticker que se almacena en esta propiedad.
        self.vídeo = None # El mensaje contiene un Vídeo que se almacena en esta propiedad.
        self.vídeo_nota = None # El mensaje contiene una VídeoNota que se almacena en esta propiedad.
        self.nota_voz = None # El mensaje contiene una NotaVoz que se almacena en esta propiedad.
        self.leyenda = '' # La leyenda o nota al pie de la animación, audio, documento, foto, vídeo o voz.
        self.entidades = [] # La lista de entidades en la leyenda, tales como usuarios, URLs, comandos, etc.

class MensajeCambios(Mensaje):
    """Un mensaje que registra un cambio en el Chat donde se recibió este mensaje."""

    def __init__(self, objeto: dict):
        super().__init__()
        self.neuvos_miembros = [] # La lista de miembros nuevos que fueron agregados al Chat o SuperGrupo
        self.miembro_eliminado = None # El miembro que fue removido en este mensaje.
        self.nuevo_título = '' # El nuevo título del Chat que se cambió en este mensaje.
        self.nueva_foto = [] # La nueva foto del Chat que se cambió en este mensaje.
        self.id_chat_supergrupo = 0 # El identificador único del SuperGrupo en el cual este Grupo se convirtió.
        self.id_supergrupo_chat = 0 # El identificador único del Grupo en el cual este SuperGrupo se convirtió.
        self.mensaje_anclado = None # El Mensaje que fue anclado a este Chat en este mensaje.
        
class MensajeVariado(Mensaje):
    """Un mensaje que no envía ni una de las especificaciones de los anteriores tipos."""

    def __init__(self, objeto: dict):
        super().__init__()
        self.contacto = None # El mensaje contiene un Contacto compartido que se almacena en esta propiedad.
        self.dado = None # El mensaje contiene un Dado con un valor aleatorio que se almacena en esta propiedad.
        self.juego = None # El mensaje contiene un Juego que se almacena en esta propiedad.
        self.encuesta = None # El mensaje contiene una Encuesta que se almacena en esta propiedad.
        self.establecimineto = None # El mensaje contiene un Establecimineto que se almacena en esta propiedad.
        self.ubicación = None # El mensaje contiene una Ubicación compartida que se almacena en esta propiedad.
        self.factura = None # El mensaje contiene una Factura que se almacena en esta propiedad.
        self.pago_exitoso = None # El mensaje contiene un PagoExitoso que se almacena en esta propiedad.