from tipos import chats, mensajes, usuarios

def clasificar_actualización(objeto: dict):
    if 'message' in objeto:
        clasificar_mensaje(objeto['message'])

def clasificar_mensaje(mensaje: dict):
