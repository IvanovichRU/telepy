class InfoWebHook:
    def __init__(self):
        self.url = ''
        self.tiene_certificado_personalizado = False
        self.contador_actualización_pendiente = 0
        self.dirección_ip = ''
        self.fecha_último_error = 0
        self.mensaje_último_error = None
        self.máximas_conexiones = 0
        self.actualizaciones_permitidas = []