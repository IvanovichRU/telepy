class BotónTecladoEnlínea:
    def __init__(self):
        self.texto = ''
        self.url = ''
        self.login_url = None
        self.datos_rellamada = ''
        self.cambiar_consulta_enlínea = ''
        self.cambiar_consulta_enlínea_chat_actual = ''
        self.juego_rellamada = None
        self.pago = False

class BotónTeclado:
    def __init__(self):
        self.texto = ''
        self.pedir_contacto = False
        self.pedir_ubicación = False
        self.pedir_encuesta = False

class RemoverTecladoRespuesta:
    def __init__(self):
        self.remover_teclado = False
        self.selectivo = False

class RespuestaTecladoMarkup:
    def __init__(self):
        self.teclado = []
        self.reescalar_teclado = False
        self.teclado_única_vez = False
        self.selectivo = False

class TecladoEnlíneaMarkup:
    def __init__(self):
        self.teclado_enlínea = []

class TipoEncuestaBotónTeclado:
    def __init__(self):
        self.tipo = ''