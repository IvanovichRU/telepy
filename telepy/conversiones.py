import tipos

def desempacar_actualización(actualización: dict):
    nueva_actualización = tipos.Actualización()
    nueva_actualización.id = actualización['update_id']
    if 'message' in actualización:
        nueva_actualización.mensaje = desempacar_mensaje(actualización['message'])
    if 'edited_message' in actualización:
        nueva_actualización.mensaje_editado = desempacar_mensaje(actualización['edited_message'])
    if 'channel_post' in actualización:
        nueva_actualización.publicación_canal = desempacar_mensaje(actualización['channel_post'])
    if 'edited_channel_post' in actualización:
        nueva_actualización.publicación_editada = desempacar_mensaje(actualización['edited_channel_post'])
    if 'inline_query' in actualización:
        nueva_actualización.consulta_en_línea = desempacar_consultaenlínea(actualización['inline_query'])
    if 'chosen_inline_result' in actualización:
        nueva_actualización.resultado_enlínea = 0
def desempacar_mensaje(mensaje: dict) -> tipos.Mensaje:
    nuevo_mensaje = None
    if 'forward_from' in mensaje:
        nuevo_mensaje = desempacar_mensajereenviado(mensaje)
    elif 'via_bot' in mensaje:
        desempacar_mensajebot(mensaje)
        nuevo_mensaje = desempacar_mensajereenviado(mensaje)
    elif ('animation'  in mensaje or
          'audio'      in mensaje or
          'document'   in mensaje or
          'photo'      in mensaje or
          'sticker'    in mensaje or
          'video'      in mensaje or
          'video_note' in mensaje or
          'voice'      in mensaje or
          'caption'    in mensaje):
        desempacar_mensajemultimedia(mensaje)
        nuevo_mensaje = desempacar_mensajereenviado(mensaje)
    elif ('new_chat_members' in mensaje or
          'left_chat_member' in mensaje or
          'new_chat_title' in mensaje or
          'new_chat_photo' in mensaje or
          'migrate_to_chat_id' in mensaje or
          'migrate_from_chat_id' in mensaje or
          'pinned_message' in mensaje):
        desempacar_mensajecambios(mensaje)
        nuevo_mensaje = desempacar_mensajereenviado(mensaje)
    elif ('contact' in mensaje or
          'dice' in mensaje or
          'game' in mensaje or
          'poll' in mensaje or
          'venue' in mensaje or
          'location' in mensaje or
          'invoice' in mensaje or
          'successful_payment' in mensaje):
        desempacar_mensajevariado(mensaje)
        nuevo_mensaje = desempacar_mensajereenviado(mensaje)
    return nuevo_mensaje
    
def desempacar_mensajereenviado(mensaje: dict) -> tipos.MensajeReenviado:
    nuevo_mensaje = tipos.MensajeReenviado()
    nuevo_mensaje.id = mensaje['message_id']
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

def desempacar_mensajebot(mensaje: dict) -> tipos.MensajeBot:
    nuevo_mensaje = tipos.MensajeBot()
    nuevo_mensaje.via_bot = mensaje['via_bot']
    if 'text' in mensaje:
        nuevo_mensaje.texto = mensaje['text']
    else:
        nuevo_mensaje.texto = ''
    if 'entities' in mensaje:
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(desempacar_entidad(entidad))
    return nuevo_mensaje
        
def desempacar_mensajemultimedia(mensaje: dict) -> tipos.MensajeMultimedia:
    nuevo_mensaje = tipos.MensajeMultimedia()
    if 'animation' in mensaje:
        nuevo_mensaje.animación = desempacar_animación(mensaje['animation'])
    if 'audio' in mensaje:
        nuevo_mensaje.audio = desempacar_audio(mensaje['audio'])
    if 'document' in mensaje:
        nuevo_mensaje.documento = desempacar_documento(mensaje['document'])
    if 'photo' in mensaje:
        nuevo_mensaje.foto = desempacar_foto(mensaje['photo'])
    if 'sticker' in mensaje:
        nuevo_mensaje.sticker = desempacar_sticker(mensaje['sticker'])
    if 'video' in mensaje:
        nuevo_mensaje.vídeo = desempacar_vídeo(mensaje['video'])
    if 'video_note' in mensaje:
        nuevo_mensaje.vídeo_nota = desempacar_vídeo_nota(mensaje['video_note'])
    if 'voice' in mensaje:
        nuevo_mensaje.nota_voz = desempacar_nota_voz(mensaje['voice'])
    if 'caption' in mensaje:
        nuevo_mensaje.leyenda = mensaje['caption']
    if 'entities' in mensaje:
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(desempacar_entidad(entidad))
    return nuevo_mensaje

def desempacar_mensajecambios(mensaje: dict) -> tipos.MensajeCambios:
    nuevo_mensaje = tipos.MensajeCambios()
    if 'new_chat_members' in mensaje:
        for usuario in mensaje['new_chat_members']:
            nuevo_mensaje.nuevos_miembros.append(desempacar_usuario(usuario))
    if 'left_chat_member' in mensaje:
        nuevo_mensaje.miembro_eliminado = desempacar_usuario(mensaje['left_chat_member'])
    if 'new_chat_title' in mensaje:
        nuevo_mensaje.nuevo_título = mensaje['new_chat_title']
    if 'new_chat_photo' in mensaje:
        for tamaño_foto in mensaje['new_chat_photo']:
            nuevo_mensaje.nueva_foto.append(desempacar_tamaño_foto(tamaño_foto))
    if 'migrate_to_chat_id' in mensaje:
        nuevo_mensaje.id_chat_supergrupo = mensaje['migrate_to_chat_id']
    if 'migrate_from_chat_id' in mensaje:
        nuevo_mensaje.id_supergrupo_chat = mensaje['migrate_from_chat_id']
    if 'pinned_message' in mensaje:
        nuevo_mensaje.mensaje_anclado = desempacar_mensaje(mensaje['pinned_message'])
    return nuevo_mensaje

def desempacar_mensajevariado(mensaje: dict) -> tipos.MensajeVariado:
    nuevo_mensaje = tipos.MensajeVariado()
    if 'contact' in mensaje:
        nuevo_mensaje.contacto = desempacar_contacto(mensaje['contact'])
    if 'dice' in mensaje:
        nuevo_mensaje.dado = desempacar_dado(mensaje['dice'])
    if 'game' in mensaje:
        nuevo_mensaje.juego = desempacar_juego(mensaje['game'])
    if 'poll' in mensaje:
        nuevo_mensaje.encuesta = desempacar_encuesta(mensaje['poll'])
    if 'venue' in mensaje:
        nuevo_mensaje.establecimineto = desempacar_establecimineto(mensaje['venue'])
    if 'location' in mensaje:
        nuevo_mensaje.ubicación = desempacar_ubicación(mensaje['location'])
    if 'invoice' in mensaje:
        nuevo_mensaje.factura = desempacar_factura(mensaje['invoice'])
    if 'successful_payment' in mensaje:
        nuevo_mensaje.pago_exitoso = desempacar_pago_exitoso(mensaje['successful_payment'])

def desempacar_usuario(usuario: dict) -> tipos.Usuario:
    if 'via_bot' in usuario:
        