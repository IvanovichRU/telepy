"""
Creado por Kevin Iván Domínguez Jiménez

MIT License

Copyright (c) 2020 Kevin Iván Domínguez Jiménez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import clases_telepy


def dict_a_usuario_telepy(usuario: dict) -> clases_telepy.Usuario_TelePy:
    print('dict de usuario recibido es: ', usuario)
    usuario_desempacado = clases_telepy.Usuario_TelePy()
    usuario_desempacado.id = usuario['id']
    usuario_desempacado.es_bot = usuario['is_bot']
    usuario_desempacado.nombre = usuario['first_name']
    usuario_desempacado.apellido = usuario['last_name']
    usuario_desempacado.usuario = usuario['username']
    return usuario_desempacado

def dict_a_chat_telepy(chat: dict) -> clases_telepy.Chat_TelePy:
    print('dict de chat recibido es: ', chat)
    chat_desempacado = clases_telepy.Chat_TelePy()
    chat_desempacado.id = chat['id']
    chat_desempacado.titulo = chat['title']
    chat_desempacado.tipo = chat['type']
    chat_desempacado.todos_admin = chat['all_members_are_administrators']
    return chat_desempacado

def dict_a_mensaje_telepy(mensaje: dict) -> clases_telepy.Mensaje_TelePy:
    print('dict de mensaje recibido es: ', mensaje)
    mensaje_desempacado = clases_telepy.Mensaje_TelePy()
    mensaje_desempacado.id = mensaje['message_id']
    mensaje_desempacado.remitente = dict_a_usuario_telepy(mensaje['from'])
    mensaje_desempacado.chat = dict_a_chat_telepy(mensaje['chat'])
    mensaje_desempacado.texto = mensaje['text']
    return mensaje_desempacado

def dict_a_actualización_telepy(actualización: dict) -> clases_telepy.Actualización_TelePy:
    print('dict de actualización recibido es: ', actualización)
    actualización_desempacada = clases_telepy.Actualización_TelePy()
    actualización_desempacada.id = actualización['update_id']
    actualización_desempacada.mensaje = dict_a_mensaje_telepy(actualización['message'])
    return actualización_desempacada