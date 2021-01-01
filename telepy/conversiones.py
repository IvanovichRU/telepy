from tipos import chats, mensajes, usuarios

def clasificar_actualización(objeto: dict):
    if 'message' in objeto:
        desempacar_mensaje(objeto['message'])
    else:
        print('Error al convertir JSON.\nSe recibió:\n', objeto, '\nCerrando el programa.')

def desempacar_mensaje(mensaje: dict):
    if 'forward_from' in mensaje:
        desempacar_mensajereenviado(mensaje)

def desempacar_mensajereenviado(mensaje: dict):
    nuevo_mensaje = mensajes.MensajeReenviado()
    nuevo_mensaje.id = mensaje_id
    nuevo_mensaje.fecha = mensaje['date']
    nuevo_mensaje.remitente = desempacar_usuario(mensaje['from'])
    nuevo_mensaje.chat = desempacar_chat(mensaje['chat'])
    if 'edit_date' in mensaje:
        nuevo_mensaje.fecha_editado = mensaje['edit_date']
    else:
        nuevo_mensaje.fecha_editado = None
    nuevo_mensaje.texto = mensaje['text']
    if 'entities' in mensaje:
        entidades = []
        for entidad in mensaje['entities']:
            entidades.append(desempacar_entidad(entidad))
        nuevo_mensaje.entidades = entidades
    else:
        nuevo_mensaje.entidades = []
    nuevo_mensaje.reenviado_remitente = mensaje['forward_from']
    nuevo_mensaje.reenviado_de_chat = desempacar_chat(mensaje['forward_from_chat'])
    nuevo_mensaje.reenviado_id = mensaje['forward_from_message_id']
    nuevo_mensaje.reenviado_firma = mensaje['forward_signature']
    nuevo_mensaje.reenviado_nombre = mensaje['']