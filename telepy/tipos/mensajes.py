class Mensaje:
    id: int
    fecha: int
    chat: Chat
    fecha_editado: int

class MensajeReenviado(Mensaje):
    remitente: Usuario
    texto: str
    entidades: list[EntidadMensaje]
    reenviado_remitente: Usuario
    reenviado_de_chat: Chat
    reenviado_id: int
    reenviado_firma: str
    reenviado_nombre: str
    reenviado_fecha: int