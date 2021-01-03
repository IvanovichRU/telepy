class InfoWebHook:
    def __init__(self):
        self.url = '' # URL del WebHook, puede estar vacía si el WebHook no fue preparado.
        self.tiene_certificado_personalizado = False # Es True cuando un certificado personalizado fue proveído para chequeos de certificación de webhooks.
        self.contador_actualización_pendiente = 0 # Número de actualizaciones esperando entrega.
        self.dirección_ip = '' # Dirección IP utilizada actualmente para el webhook.
        self.fecha_último_error = 0 # 
        self.mensaje_último_error = None
        self.máximas_conexiones = 0
        self.actualizaciones_permitidas = []