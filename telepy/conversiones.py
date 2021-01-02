from tipos import chats, mensajes, usuarios

def clasificar_actualización(objeto: dict):
    if 'message' in objeto:
        desempacar_mensaje(objeto['message'])
    else:
        print('Error al convertir JSON.\nSe recibió:\n', objeto, '\nCerrando el programa.')

def desempacar_mensaje(mensaje: dict) -> mensajes.Mensaje:
    if 'forward_from' in mensaje:
        desempacar_mensajereenviado(mensaje)
    elif 'via_bot' in mensaje:
        desempacar_mensajebot(mensaje)

def desempacar_mensajereenviado(mensaje: dict) -> mensajes.MensajeReenviado:
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
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(desempacar_entidad(entidad))
    else:
        nuevo_mensaje.entidades = []
    nuevo_mensaje.reenviado_remitente = mensaje['forward_from']
    nuevo_mensaje.reenviado_de_chat = desempacar_chat(mensaje['forward_from_chat'])
    nuevo_mensaje.reenviado_id = mensaje['forward_from_message_id']
    nuevo_mensaje.reenviado_firma = mensaje['forward_signature']
    nuevo_mensaje.reenviado_nombre = mensaje['forward_sender_name']
    nuevo_mensaje.reenviado_fecha = mensaje['forward_date']
    return nuevo_mensaje

def desempacar_mensajebot(mensaje: dict) -> mensajes.MensajeBot:
    nuevo_mensaje = mensajes.MensajeBot()
    nuevo_mensaje.via_bot = mensaje['via_bot']
    if 'text' in mensaje:
        nuevo_mensaje.texto = mensaje['text']
    else:
        nuevo_mensaje.texto = ''
    if 'entities' in mensaje:
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(desempacar_entidad(mensaje['entities']))