class Juego:
    def __init__(self):
        self.título = 'Sin registar' # El título del juego.
        self.descripción = 'Sin registrar' # La descripción del juego.
        self.foto = [] # Una lista de TamañoFoto que se mostrará en el mensaje del juego en chats.
        self.texto = 'Sin registrar' # Descripción breve del juego o máximas puntuaciones incluidas en el mensaje del juego.
        self.entidades_texto = [] # Entidades especiales que aparecen en el texto.
        self.animación = None # La animación que se mostrará en el mensaje del juego en chats.

class PuntuaciónMáxima:
    def __init__(self):
        self.posición = 0 # La posición en la tabla de puntuaciones para el juego.
        self.usuario = None # El usuario correspondiente.
        self.puntuación = 0 # La puntuación que asignada.