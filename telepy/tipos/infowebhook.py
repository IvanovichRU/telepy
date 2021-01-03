class InfoWebhook:
    def __init__(self):
        self.url = '' # URL del WebHook, puede estar vacía si el WebHook no fue preparado.
        self.tiene_certificado_personalizado = False # Es True cuando un certificado personalizado fue proveído para chequeos de certificación de webhooks.
        self.contador_actualización_pendiente = 0 # Número de actualizaciones esperando entrega.
        self.dirección_ip = '' # Dirección IP utilizada actualmente para el webhook.
        self.fecha_último_error = 0 # Fecha del error más reciente al intentar entregar una actualización.
        self.mensaje_último_error = None # Mensaje escrito del error más reciente.
        self.máximas_conexiones = 0 # Número máximo de conexiones HTTPS simultáneas permitidas.
        self.actualizaciones_permitidas = [] # Una lista de tipos de actualización a los que el bot está suscrito.