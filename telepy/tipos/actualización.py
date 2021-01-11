class Actualización:

    def __init__(self):
        self.id = 0 # El identificador único de la actualización.
        self.mensaje = None # Nuevo mensaje entrante de cualquier tipo, texto, foto, sticker, etc.
        self.mensaje_editado = None # La nueva versión de algún mensaje que fue editado en esta actualización.
        self.publicación_canal = None # Nueva publicación en un canal de cualquier tipo, texto, foto, sticker, etc.
        self.publicación_editada = None # La nueva versión de alguna publicación en un canal que haya sido editado.
        self.consulta_enlínea = None # Nueva ConsultaEnlínea entrante.
        self.resultado_enlínea = None # El resultado de una consulta_enlínea que fue elegida por un usuario y enviada a su compañero de chat.
        self.consulta_de_rellamada = None # Nueva ConsultaDeRellamada entrante.
        self.consulta_envío = None # Nueva ConsultaEnvío entrante, solo para facturas con precio flexible.
        self.consulta_pre_cobro = None # Nueva ConsultaPreCobro entrante, contiene información completa previa al cobro.
        self.encuesta = None # Nuevo estado de Encuesta. Los bots solo reciben información acerca de encuestas detenidas y que él mismo envía.
        self.respuesta_encueta = None # Un usuario cambió su respuesta en una encuesta no anónima. Los bots solo reciben nuevos votos en encuestas que el mismo envía.

    def __str__(self) -> str:
        cadena = type(self).__name__ + ':\n'
        for llave in self.__dict__:
            if self.__dict__[llave] is not None and self.__dict__[llave] != [] and self.__dict__[llave] != 'Sin registrar':
                cadena += str(llave) + ' -> ' + str(self.__dict__[llave]) + '\n'
        return cadena