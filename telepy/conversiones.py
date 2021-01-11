from tipos.mensajes import *
from tipos.actualización import *
from tipos.chats import *
from tipos.entradas import *
from tipos.infowebhook import *
from tipos.juegos import *
from tipos.mensajes import *
from tipos.multimedia import *
from tipos.pagos import *
from tipos.stickers import *
from tipos.teclados import *
from tipos.tipos_variedad import *
from tipos.usuarios import *
from tipos.utilería_chats import *
from tipos.utilería_mensajes import *

def desempacar_actualización(actualización: dict) -> Actualización:
    nueva_actualización = Actualización()
    nueva_actualización.id = actualización['update_id']
    if 'message' in actualización:
        nueva_actualización.mensaje = desempacar_mensaje(actualización['message'])
    if 'edited_message' in actualización:
        nueva_actualización.mensaje_editado = desempacar_mensaje(actualización['edited_message'])
    if 'channel_post' in actualización:
        nueva_actualización.publicación_canal = desempacar_mensaje(actualización['channel_post'])
    if 'edited_channel_post' in actualización:
        nueva_actualización.publicación_editada = desempacar_mensaje(actualización['edited_channel_post'])
    # if 'inline_query' in actualización:
        # nueva_actualización.consulta_en_línea = desempacar_consultaenlínea(actualización['inline_query'])
    if 'chosen_inline_result' in actualización:
        nueva_actualización.resultado_enlínea = 0
    return nueva_actualización

def desempacar_mensaje(mensaje: dict) -> Mensaje:
    if 'forward_from' in mensaje:
        return desempacar_mensajereenviado(mensaje)
    elif 'via_bot' in mensaje:
        return desempacar_mensajebot(mensaje)
    elif ('animation'  in mensaje or
          'audio'      in mensaje or
          'document'   in mensaje or
          'photo'      in mensaje or
          'sticker'    in mensaje or
          'video'      in mensaje or
          'video_note' in mensaje or
          'voice'      in mensaje or
          'caption'    in mensaje):
        return desempacar_mensajemultimedia(mensaje)
    elif ('new_chat_members' in mensaje or
          'left_chat_member' in mensaje or
          'new_chat_title' in mensaje or
          'new_chat_photo' in mensaje or
          'migrate_to_chat_id' in mensaje or
          'migrate_from_chat_id' in mensaje or
          'pinned_message' in mensaje):
        return desempacar_mensajecambios(mensaje)
    elif ('contact' in mensaje or
          'dice' in mensaje or
          'game' in mensaje or
          'poll' in mensaje or
          'venue' in mensaje or
          'location' in mensaje or
          'invoice' in mensaje or
          'successful_payment' in mensaje):
        return desempacar_mensajevariado(mensaje)
    else:
        return desempacar_mensajetexto(mensaje)

def desempacar_mensajetexto(mensaje: dict) -> MensajeTexto:
    nuevo_mensaje = MensajeTexto()
    nuevo_mensaje.id = mensaje['message_id']
    nuevo_mensaje.fecha = mensaje['date']
    if 'from' in mensaje:
        nuevo_mensaje.remitente = desempacar_usuario(mensaje['from'])
    nuevo_mensaje.chat = desempacar_chat(mensaje['chat'])
    if 'edit_date' in mensaje:
        nuevo_mensaje.fecha_editado = mensaje['edit_date']
    nuevo_mensaje.texto = mensaje['text']
    if 'entitites' in mensaje:
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(entidad)
    return nuevo_mensaje

def desempacar_mensajereenviado(mensaje: dict) -> MensajeReenviado:
    nuevo_mensaje = MensajeReenviado()
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

def desempacar_mensajebot(mensaje: dict) -> MensajeBot:
    nuevo_mensaje = MensajeBot()
    nuevo_mensaje.id = mensaje['message_id']
    nuevo_mensaje.fecha = mensaje['date']
    if 'from' in mensaje:
        nuevo_mensaje.remitente = desempacar_usuario(mensaje['from'])
    nuevo_mensaje.chat = desempacar_chat(mensaje['chat'])
    if 'edit_date' in mensaje:
        nuevo_mensaje.fecha_editado = mensaje['edit_date']
    nuevo_mensaje.via_bot = desempacar_usuario(mensaje['via_bot'])
    if 'text' in mensaje:
        nuevo_mensaje.texto = mensaje['text']
    else:
        nuevo_mensaje.texto = ''
    if 'entities' in mensaje:
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(desempacar_entidad(entidad))
    return nuevo_mensaje

def desempacar_mensajemultimedia(mensaje: dict) -> MensajeMultimedia:
    nuevo_mensaje = MensajeMultimedia()
    nuevo_mensaje.id = mensaje['message_id']
    nuevo_mensaje.fecha = mensaje['date']
    if 'from' in mensaje:
        nuevo_mensaje.remitente = desempacar_usuario(mensaje['from'])
    nuevo_mensaje.chat = desempacar_chat(mensaje['chat'])
    if 'edit_date' in mensaje:
        nuevo_mensaje.fecha_editado = mensaje['edit_date']
    if 'animation' in mensaje:
        nuevo_mensaje.animación = desempacar_animación(mensaje['animation'])
    if 'audio' in mensaje:
        nuevo_mensaje.audio = desempacar_audio(mensaje['audio'])
    if 'document' in mensaje:
        nuevo_mensaje.documento = desempacar_documento(mensaje['document'])
    if 'photo' in mensaje:
        for foto in mensaje['photo']:
            nuevo_mensaje.foto.append(desempacar_tamañofoto(foto))
    if 'sticker' in mensaje:
        nuevo_mensaje.sticker = desempacar_sticker(mensaje['sticker'])
    if 'video' in mensaje:
        nuevo_mensaje.vídeo = desempacar_vídeo(mensaje['video'])
    if 'video_note' in mensaje:
        nuevo_mensaje.vídeo_nota = desempacar_vídeonota(mensaje['video_note'])
    if 'voice' in mensaje:
        nuevo_mensaje.nota_voz = desempacar_notavoz(mensaje['voice'])
    if 'caption' in mensaje:
        nuevo_mensaje.leyenda = mensaje['caption']
    if 'entities' in mensaje:
        for entidad in mensaje['entities']:
            nuevo_mensaje.entidades.append(desempacar_entidad(entidad))
    if 'caption_entities' in mensaje:
        for entidad in mensaje['caption_entities']:
            nuevo_mensaje.entidades_leyenda.append(desempacar_entidad(entidad))
    return nuevo_mensaje

def desempacar_mensajecambios(mensaje: dict) -> MensajeCambios:
    nuevo_mensaje = MensajeCambios()
    nuevo_mensaje.id = mensaje['message_id']
    nuevo_mensaje.fecha = mensaje['date']
    if 'from' in mensaje:
        nuevo_mensaje.remitente = desempacar_usuario(mensaje['from'])
    nuevo_mensaje.chat = desempacar_chat(mensaje['chat'])
    if 'edit_date' in mensaje:
        nuevo_mensaje.fecha_editado = mensaje['edit_date']
    if 'new_chat_members' in mensaje:
        for usuario in mensaje['new_chat_members']:
            nuevo_mensaje.nuevos_miembros.append(desempacar_usuario(usuario))
    if 'left_chat_member' in mensaje:
        nuevo_mensaje.miembro_eliminado = desempacar_usuario(mensaje['left_chat_member'])
    if 'new_chat_title' in mensaje:
        nuevo_mensaje.nuevo_título = mensaje['new_chat_title']
    if 'new_chat_photo' in mensaje:
        for tamaño_foto in mensaje['new_chat_photo']:
            nuevo_mensaje.nueva_foto.append(desempacar_tamañofoto(tamaño_foto))
    if 'migrate_to_chat_id' in mensaje:
        nuevo_mensaje.id_chat_supergrupo = mensaje['migrate_to_chat_id']
    if 'migrate_from_chat_id' in mensaje:
        nuevo_mensaje.id_supergrupo_chat = mensaje['migrate_from_chat_id']
    if 'pinned_message' in mensaje:
        nuevo_mensaje.mensaje_anclado = desempacar_mensaje(mensaje['pinned_message'])
    return nuevo_mensaje

def desempacar_mensajevariado(mensaje: dict) -> MensajeVariado:
    nuevo_mensaje = MensajeVariado()
    nuevo_mensaje.id = mensaje['message_id']
    nuevo_mensaje.fecha = mensaje['date']
    if 'from' in mensaje:
        nuevo_mensaje.remitente = desempacar_usuario(mensaje['from'])
    nuevo_mensaje.chat = desempacar_chat(mensaje['chat'])
    if 'edit_date' in mensaje:
        nuevo_mensaje.fecha_editado = mensaje['edit_date']
    if 'contact' in mensaje:
        nuevo_mensaje.contacto = desempacar_contacto(mensaje['contact'])
    if 'dice' in mensaje:
        nuevo_mensaje.dado = desempacar_dado(mensaje['dice'])
    if 'game' in mensaje:
        nuevo_mensaje.juego = desempacar_juego(mensaje['game'])
    if 'poll' in mensaje:
        nuevo_mensaje.encuesta = desempacar_encuesta(mensaje['poll'])
    if 'venue' in mensaje:
        nuevo_mensaje.establecimiento = desempacar_establecimiento(mensaje['venue'])
    if 'location' in mensaje:
        nuevo_mensaje.ubicación = desempacar_ubicación(mensaje['location'])
    if 'invoice' in mensaje:
        nuevo_mensaje.factura = desempacar_factura(mensaje['invoice'])
    if 'successful_payment' in mensaje:
        nuevo_mensaje.pago_exitoso = desempacar_pagoexitoso(mensaje['successful_payment'])
    return nuevo_mensaje

def desempacar_usuario(usuario: dict) -> Usuario:
    nuevo_usuario = None
    if usuario['is_bot']:
        return desempacar_bot(usuario)
    else:
        nuevo_usuario = Usuario()
        nuevo_usuario.id = usuario['id']
        nuevo_usuario.es_bot = usuario['is_bot']
        nuevo_usuario.primer_nombre = usuario['first_name']
        if 'last_name' in usuario:
            nuevo_usuario.apellido = usuario['last_name']
        if 'username' in usuario:
            nuevo_usuario.usuario = usuario['username']
        if 'language_code' in usuario:
            nuevo_usuario.idioma = usuario['language_code']
        return nuevo_usuario

def desempacar_bot(usuario: dict) -> Bot:
    nuevo_usuario = Bot()
    nuevo_usuario.id = usuario['id']
    nuevo_usuario.es_bot = usuario['is_bot']
    nuevo_usuario.primer_nombre = usuario['first_name']
    if 'apellido' in usuario:
        nuevo_usuario.apellido = usuario['last_name']
    if 'username' in usuario:
        nuevo_usuario.usuario = usuario['username']
    if 'language_code' in usuario:
        nuevo_usuario.idioma = usuario['language_code']
    if 'can_join_groups' in usuario:
        nuevo_usuario.unible_a_grupos = usuario['can_join_groups']
    if 'can_read_all_group_messages' in usuario:
        nuevo_usuario.lee_todo = usuario['can_read_all_group_messages']
    if 'supports_inline_queries' in usuario:
        nuevo_usuario.consultas_dentro = usuario['supports_inline_queries']
    return nuevo_usuario

def desempacar_chat(chat: dict):
    # En caso de ser un ChatPrivado:
    if chat['type'] == 'private':
        return desempacar_chatprivado(chat)
    # En caso de ser Grupo
    if chat['type'] == 'group':
        return desempacar_grupo(chat)
    # En caso de ser SuperGrupo
    if chat['type'] == 'supergroup':
        return desempacar_supergrupo(chat)
    # En caso de ser Canal
    if chat['type'] == 'channel':
        return desempacar_canal(chat)

def desempacar_chatprivado(chat: dict) -> ChatPrivado:
    nuevo_chat = ChatPrivado()
    nuevo_chat.id = chat['id']
    nuevo_chat.tipo = chat['type']
    if 'photo' in chat:
        nuevo_chat.foto = desempacar_fotochat(chat['photo'])
    if 'pinned_message' in chat:
        nuevo_chat.mensaje_anclado = chat['pinned_message']
    if 'can_set_sticker_set' in chat:
        nuevo_chat.cambia_stickers = chat['can_set_sticker_set']
    nuevo_chat.usuario = chat['username']
    nuevo_chat.primer_nombre = chat['first_name']
    if 'last_name' in chat:
        nuevo_chat.apellido = chat['last_name']
    if 'bio' in chat:
        nuevo_chat.bio = chat['bio']
    return nuevo_chat

def desempacar_grupo(chat: dict) -> Grupo:
    nuevo_chat = Grupo()
    nuevo_chat.id = chat['id']
    nuevo_chat.tipo = chat['type']
    if 'photo' in chat:
        nuevo_chat.foto = desempacar_fotochat(chat['photo'])
    if 'pinned_message' in chat:
        nuevo_chat.mensaje_anclado = desempacar_mensaje(chat['pinned_message'])
    if 'can_set_sticker_set' in chat:
        nuevo_chat.cambia_stickers = chat['can_set_sticker_set']
    if 'title' in chat:
        nuevo_chat.título = chat['title']
    if 'description' in chat:
        nuevo_chat.descripción = chat['description']
    if 'invite_link' in chat:
        nuevo_chat.invitación = chat['invite_link']
    if 'permissions' in chat:
        nuevo_chat.permisos = desempacar_permisoschat(chat['permissions'])
    return nuevo_chat

def desempacar_supergrupo(chat: dict) -> SuperGrupo:
    nuevo_chat = SuperGrupo()
    nuevo_chat.id = chat['id']
    nuevo_chat.tipo = chat['type']
    if 'photo' in chat:
        nuevo_chat.foto = desempacar_fotochat(chat['photo'])
    if 'pinned_message' in chat:
        nuevo_chat.mensaje_anclado = desempacar_mensaje(chat['pinned_message'])
    if 'can_set_sticker_set' in chat:
        nuevo_chat.cambia_stickers = chat['can_set_sticker_set']
    if 'title' in chat:
        nuevo_chat.título = chat['title']
    if 'description' in chat:
        nuevo_chat.descripción = chat['description']
    if 'invite_link' in chat:
        nuevo_chat.invitación = chat['invite_link']
    if 'permissions' in chat:
        nuevo_chat.permisos = desempacar_permisoschat(chat['permissions'])
    if 'slow_mode_delay' in chat:
        nuevo_chat.retraso = chat['slow_mode_delay']
    if 'sticker_set_name' in chat:
        nuevo_chat.nombre_set_stickers = chat['sticker_set_name']
    return nuevo_chat

def desempacar_canal(chat: dict) -> Canal:
    nuevo_chat = SuperGrupo()
    nuevo_chat.id = chat['id']
    nuevo_chat.tipo = chat['type']
    if 'photo' in chat:
        nuevo_chat.foto = desempacar_fotochat(chat['photo'])
    if 'pinned_message' in chat:
        nuevo_chat.mensaje_anclado = desempacar_mensaje(chat['pinned_message'])
    if 'can_set_sticker_set' in chat:
        nuevo_chat.cambia_stickers = chat['can_set_sticker_set']
    if 'title' in chat:
        nuevo_chat.título = chat['title']
    if 'description' in chat:
        nuevo_chat.descripción = chat['description']
    if 'invite_link' in chat:
        nuevo_chat.invitación = chat['invite_link']
    return nuevo_chat

def desempacar_entidad(entidad: dict) -> EntidadMensaje:
    nueva_entidad = EntidadMensaje
    nueva_entidad.tipo = entidad['type']
    nueva_entidad.desplazo = entidad['offset']
    nueva_entidad.longitud = entidad['length']
    if 'url' in entidad:
        nueva_entidad.url = entidad['url']
    if 'user' in entidad:
        nueva_entidad.usuario = desempacar_usuario(entidad['user'])
    if 'language' in entidad:
        nueva_entidad.lenguaje = entidad['language']
    return nueva_entidad

def desempacar_animación(animación: dict) -> Animación:
    nueva_animación = Animación()
    nueva_animación.id_archivo = animación['file_id']
    nueva_animación.id_única_archivo = animación['file_unique_id']
    nueva_animación.ancho = animación['width']
    nueva_animación.alto = animación['height']
    nueva_animación.duración = animación['duration']
    if 'thumb' in animación:
        nueva_animación.miniatura = desempacar_tamañofoto(animación['thumb'])
    if 'file_name' in animación:
        nueva_animación.nombre_archivo = animación['file_name']
    if 'mime_type' in animación:
        nueva_animación.tipo_mime = animación['mime_type']
    if 'file_size' in animación:
        nueva_animación.tamaño_archivo = animación['file_size']
    return nueva_animación

def desempacar_audio(audio: dict) -> Audio:
    nuevo_audio = Audio()
    nuevo_audio.id_archivo = audio['file_id']
    nuevo_audio.id_única_archivo = audio['file_unique_id']
    nuevo_audio.duración = audio['duration']
    if 'performer' in audio:
        nuevo_audio.actor = audio['performer']
    if 'title' in audio:
        nuevo_audio.título = audio['title']
    if 'file_name' in audio:
        nuevo_audio.nombre_archivo = audio['file_name']
    if 'mime_type' in audio:
        nuevo_audio.tipo_mime = audio['mime_type']
    if 'file_size' in audio:
        nuevo_audio.tamaño_archivo = audio['file_size']
    if 'thumb' in audio:
        nuevo_audio.miniatura = desempacar_tamañofoto(audio['thumb'])
    return nuevo_audio

def desempacar_documento(documento: dict) -> Documento:
    nuevo_documento = Documento()
    nuevo_documento.id_archivo = documento['file_id']
    nuevo_documento.id_única_archivo = documento['file_unique_id']
    if 'thumb' in documento:
        nuevo_documento.miniatura = desempacar_tamañofoto(documento['thumb'])
    if 'file_name' in documento:
        nuevo_documento.nombre_archivo = documento['file_name']
    if 'mime_type' in documento:
        nuevo_documento.tipo_mime = documento['mime_type']
    if 'file_size' in documento:
        nuevo_documento.tamaño_archivo = documento['file_size']
    return nuevo_documento

def desempacar_tamañofoto(tamañofoto: dict) -> TamañoFoto:
    nuevo_tamañofoto = TamañoFoto()
    nuevo_tamañofoto.id_archivo = tamañofoto['file_id']
    nuevo_tamañofoto.id_única_archivo = tamañofoto['file_unique_id']
    nuevo_tamañofoto.ancho = tamañofoto['width']
    nuevo_tamañofoto.alto = tamañofoto['height']
    if 'file_size' in tamañofoto:
        nuevo_tamañofoto.tamaño_archivo = tamañofoto['file_size']
    return nuevo_tamañofoto

def desempacar_sticker(sticker: dict) -> Sticker:
    nuevo_sticker = Sticker()
    nuevo_sticker.id_archivo = sticker['file_id']
    nuevo_sticker.id_única_archivo = sticker['file_unique_id']
    nuevo_sticker.ancho = sticker['width']
    nuevo_sticker.alto = sticker['height']
    nuevo_sticker.es_animado = sticker['is_animated']
    if 'thumb' in sticker:
        nuevo_sticker.miniatura = desempacar_tamañofoto(sticker['thumb'])
    if 'emoji' in sticker:
        nuevo_sticker.emoji = sticker['emoji']
    if 'set_name' in sticker:
        nuevo_sticker.nombre_set = sticker['set_name']
    if 'mask_position' in sticker:
        nuevo_sticker.posición_máscara = sticker['mask_position']
    if 'file_size' in sticker:
        nuevo_sticker.tamaño_archivo = sticker['file_size']
    return nuevo_sticker

def desempacar_vídeo(vídeo: dict) -> Vídeo:
    nuevo_vídeo = Vídeo()
    nuevo_vídeo.id_archivo = vídeo['file_id']
    nuevo_vídeo.id_única_archivo = vídeo['file_unique_id']
    nuevo_vídeo.ancho = vídeo['width']
    nuevo_vídeo.alto = vídeo['height']
    nuevo_vídeo.duración = vídeo['duration']
    if 'thumb' in vídeo:
        nuevo_vídeo.miniatura = desempacar_tamañofoto(vídeo['thumb'])
    if 'file_name' in vídeo:
        nuevo_vídeo.nombre_archivo = vídeo['file_name']
    if 'mime_type' in vídeo:
        nuevo_vídeo.tipo_mime = vídeo['mime_type']
    if 'file_size' in vídeo:
        nuevo_vídeo.tamaño_archivo = vídeo['file_size']
    return nuevo_vídeo

def desempacar_vídeonota(vídeo_nota: dict) -> VídeoNota:
    nueva_vídeonota = VídeoNota()
    nueva_vídeonota.id_archivo = vídeo_nota['file_id']
    nueva_vídeonota.id_única_archivo = vídeo_nota['file_unique_id']
    nueva_vídeonota.longitud = vídeo_nota['length']
    nueva_vídeonota.duración = vídeo_nota['duration']
    if 'thumb' in vídeo_nota:
        nueva_vídeonota.miniatura = desempacar_tamañofoto(vídeo_nota['thumb'])
    if 'file_size' in vídeo_nota:
        nueva_vídeonota.tamaño_archivo = vídeo_nota['file_size']
    return nueva_vídeonota

def desempacar_notavoz(notavoz: dict) -> NotaVoz:
    nueva_notavoz = NotaVoz()
    nueva_notavoz.id_archivo = notavoz['file_id']
    nueva_notavoz.id_única_archivo = notavoz['file_unique_id']
    nueva_notavoz.duración = notavoz['duration']
    if 'mime_type' in notavoz:
        nueva_notavoz.tipo_mime = notavoz['mime_type']
    if 'file_size' in notavoz:
        nueva_notavoz.tamaño_archivo = notavoz['file_size']
    return nueva_notavoz

def desempacar_contacto(contacto: dict) -> Contacto:
    nuevo_contacto = Contacto()
    nuevo_contacto.número = contacto['phone_number']
    nuevo_contacto.primer_nombre = contacto['first_name']
    if 'last_name' in contacto:
        nuevo_contacto.apellido = contacto['last_name']
    if 'user_id' in contacto:
        nuevo_contacto.id_usuario = contacto['user_id']
    if 'vcard' in contacto:
        nuevo_contacto.tarjeta_v = contacto['vcard']

def desempacar_dado(dado: dict) -> Dado:
    nuevo_dado = Dado()
    nuevo_dado.emoji = dado['emoji']
    nuevo_dado.valor = dado['value']
    return nuevo_dado

def desempacar_juego(juego: dict) -> Juego:
    nuevo_juego = Juego()
    nuevo_juego.título = juego['title']
    nuevo_juego.descripción = juego['description']
    nuevo_juego.foto = desempacar_tamañofoto(juego['photo'])
    if 'text' in juego:
        nuevo_juego.texto = juego['text']
    if 'text_entities' in juego:
        for entidad in juego['text_entities']:
            nuevo_juego.foto.append(desempacar_entidad(entidad))
    if 'animation' in juego:
        nuevo_juego.animación = desempacar_animación(juego['animation'])
    return nuevo_juego

def desempacar_encuesta(encuesta: dict) -> Encuesta:
    nueva_encuesta = Encuesta()
    nueva_encuesta.id = encuesta['id']
    nueva_encuesta.pregunta = encuesta['question']
    for opción in encuesta['options']:
        nueva_encuesta.opciones.append(desempacar_opciónencuesta(opción))
    nueva_encuesta.conteo_voto_total = encuesta['total_voter_count']
    nueva_encuesta.cerrada = encuesta['is_closed']
    nueva_encuesta.anónima = encuesta['is_anonymous']
    nueva_encuesta.tipo = encuesta['type']
    nueva_encuesta.múltiples_respuestas = encuesta['allows_multiple_answers']
    if 'correct_option_id' in encuesta:
        nueva_encuesta.id_opción_correcta = encuesta['correct_option_id']
    if 'explanation' in encuesta:
        nueva_encuesta.explicación = encuesta['explanation']
    if 'explanation_entities' in encuesta:
        for entidad in encuesta['explanation_entities']:
            nueva_encuesta.entidades_explicación.append(desempacar_entidad(entidad))
    if 'open_period' in encuesta:
        nueva_encuesta.periodo_abierto = encuesta['open_period']
    if 'close_date' in encuesta:
        nueva_encuesta.fecha_cerrada = encuesta['close_date']
    return nueva_encuesta

def desempacar_establecimiento(establecimiento: dict) -> Establecimiento:
    nuevo_establecimiento = Establecimiento()
    nuevo_establecimiento.ubicación = desempacar_ubicación(establecimiento['location'])
    nuevo_establecimiento.título = establecimiento['title']
    nuevo_establecimiento.dirección = establecimiento['address']
    if 'foursquare_id' in establecimiento:
        nuevo_establecimiento.id_foursquare = establecimiento['foursquare_id']
    if 'foursquare_type' in establecimiento:
        nuevo_establecimiento.tipo_foursquare = establecimiento['foursquare_type']
    if 'google_place_id' in establecimiento:
        nuevo_establecimiento.id_google_place = establecimiento['google_place_id']
    if 'google_place_type' in establecimiento:
        nuevo_establecimiento.tipo_google_place = establecimiento['google_place_type']
    return nuevo_establecimiento

def desempacar_ubicación(ubicación: dict) -> Ubicación:
    nueva_ubicación = Ubicación()
    nueva_ubicación.longitud = ubicación['longitude']
    nueva_ubicación.latitud = ubicación['latitude']
    if 'horizontal_accuracy' in ubicación:
        nueva_ubicación.precisión_horizontal = ubicación['horizontal_accuracy']
    if 'live_period' in ubicación:
        nueva_ubicación.periodo_en_vivo = ubicación['live_period']
    if 'heading' in ubicación:
        nueva_ubicación.dirección = ubicación['heading']
    if 'proximity_alert_radius' in ubicación:
        nueva_ubicación.radio_alerta_proximidad = ubicación['proximity_alert_radius']
    return nueva_ubicación

def desempacar_factura(factura: dict) -> Factura:
    nueva_factura = Factura()
    nueva_factura.título = factura['title']
    nueva_factura.descripción = factura['description']
    nueva_factura.parámetro_inicio = factura['start_parameter']
    nueva_factura.moneda = factura['currency']
    nueva_factura.monto_total = factura['total_amount']
    return nueva_factura

def desempacar_pagoexitoso(pago: dict) -> PagoExitoso:
    nuevo_pagoexitoso = PagoExitoso()
    nuevo_pagoexitoso.moneda = pago['currency']
    nuevo_pagoexitoso.monto_total = pago['total_amount']
    nuevo_pagoexitoso.carga_factura = pago['invoice_payload']
    if 'shipping_option_id' in pago:
        nuevo_pagoexitoso.id_opción_envío = pago['shipping_option_id']
    if 'order_info' in pago:
        nuevo_pagoexitoso.info_orden = desempacar_infoorden(pago['order_info'])
    nuevo_pagoexitoso.id_cargo_pago_telegram = pago['telegram_payment_charge_id']
    nuevo_pagoexitoso.id_proveedor_cargo_pago = pago['provider_payment_charge_id']
    return nuevo_pagoexitoso

def desempacar_fotochat(fotochat: dict) -> FotoChat:
    nueva_fotochat = FotoChat()
    nueva_fotochat.id_foto_pequeña = fotochat['small_file_id']
    nueva_fotochat.id_único_foto_pequeña = fotochat['small_file_unique_id']
    nueva_fotochat.id_foto_grande = fotochat['big_file_id']
    nueva_fotochat.id_único_foto_grande = fotochat['big_file_unique_id']
    return nueva_fotochat

def desempacar_permisoschat(permisos: dict) -> PermisosChat:
    nuevos_permisos = PermisosChat()
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_enviar = permisos['can_send_messages']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_enviar_media = permisos['can_send_media_messages']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_encuestar = permisos['can_send_polls']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_enviar_otros = permisos['can_send_other_messages']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_agregar_páginas = permisos['can_add_web_page_previews']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_cambiar_info = permisos['can_change_info']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_invitar = permisos['can_invite_users']
    if 'can_send_messages' in permisos:
        nuevos_permisos.puede_anclar = permisos['can_pin_messages']
    return nuevos_permisos

def desempacar_opciónencuesta(opción: dict) -> OpciónEncuesta:
    nueva_opción = OpciónEncuesta()
    nueva_opción.texto = opción['text']
    nueva_opción.cuenta_de_voto = opción['voter_count']

def desempacar_infoorden(info: dict) -> InfoOrden:
    nueva_info = InfoOrden()
    if 'name' in info:
        nueva_info.nombre = info['name']
    if 'phone_number' in info:
        nueva_info.número = info['phone_number']
    if 'email' in info:
        nueva_info.email = info['email']
    if 'shipping_address' in info:
        nueva_info.dirección_envío = info['shipping_address']
    return nueva_info

# def desempacar_consultaenlínea(consulta: dict) -> tipos.