class Encuesta:
    def __init__(self):
        self.id = ''
        self.pregunta = ''
        self.opciones = []
        self.cuenta_voto_total = 0
        self.cerrada = False
        self.anónima = False
        self.tipo = ''
        self.múltiples_respuestas = False
        self.id_opción_correcta = 0
        self.explicación = ''
        self.entidades_explicación = []
        self.periodo_abierto = 0
        self.fecha_cerrada = 0