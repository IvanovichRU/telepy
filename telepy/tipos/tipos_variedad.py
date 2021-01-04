class Archivo:
    def __init__(self):
        self.id_archivo = 'Sin registrar' # El identificador de este archivo, usado para descargar o reutilizar el archivo.
        self.id_única_archivo = 'Sin registrar' # El identificador único de este archivo, para largo plazo.
        self.tamaño_archivo = 0 # Tamaño de archivo, si es conocido.
        self.directorio_archivo = 'Sin registrar' # El directorio del archivo.

class Contacto:
    def __init__(self):
        self.número = 'Sin registrar' # El número telefónico del contacto.
        self.primer_nombre = 'Sin registrar' # El primer nombre del contacto.
        self.apellido = 'Sin registrar' # El apellido del contacto.
        self.id_usuario = 0 # Identificador del usuario de Telegram enlazado con el contacto.
        self.tarjeta_v = 'Sin registrar' # Información adicional acerca del contacto en forma de una vCard.

class Dado:
    def __init__(self):
        self.emoji = 'Sin registrar' # El emoji en el cual el lanzamiento está basado.
        self.valor = 0 # El valor en que reuslta el dado.

class DisparadorProximidad:
    def __init__(self):
        self.viajero = None # El usuario que disparó la alerta.
        self.espectador = None # El usuario que puso la alerta.
        self.distancia = 0 # La distancia entre usuarios.

class Encuesta:
    def __init__(self):
        self.id = 'Sin registrar' # Identificador único de la encuesta.
        self.pregunta = 'Sin registrar' # La pregunta que hace la encuesta.
        self.opciones = [] # Una lista de OpcionEncuesta.
        self.conteo_voto_total = 0 # Número total de usuarios que han votado.
        self.cerrada = False # Es True si la encuesta está cerrada.
        self.anónima = False # Es True si la encuesta es anónima.
        self.tipo = 'Sin registrar' # El tipo de encuesta, puede ser 'regular' o 'examen'.
        self.múltiples_respuestas = False # Es True si la encuesta permite múltiples respuestas.
        self.id_opción_correcta = 0 # Identificador de la respuesta correcta mediante una OpciónEncuesta.
        self.explicación = 'Sin registrar' # El texto mostrado cuando un usuario selecciona un respuesta incorrecta.
        self.entidades_explicación = [] # Entidades especiales en la explicación como usuarios, URLs, etc.
        self.periodo_abierto = 0 # La cantidad de tiempo en segundos que la encuesta estará abierta.
        self.fecha_cerrada = 0 # El punto en el tiempo en que se cerrará automáticamente la encuesta en tiempo Unix.

class Establecimiento:
    def __init__(self):
        self.ubicación = None # La Ubicación del establecimiento.
        self.título = 'Sin registrar' # El nombre del establecimiento.
        self.dirección = 'Sin registrar' # La dirección o dimicilio del establecimiento.
        self.id_foursquare = 'Sin registrar' # Identificador para foursquare del establecimiento.
        self.tipo_foursquare = 'Sin registrar' # El tipo de establecimiento para foursquare.
        self.id_google_place = 'Sin registrar' # Identificador para google place del establecimiento.
        self.tipo_google_place = 'Sin registrar' # El tipo de establecimiento para google place.

class FotosPerfilUsuario:
    def __init__(self):
        self.cuenta_total = 0 # El número total de fotos que el usuario tiene.
        self.fotos = [] # Fotos de perfil solicitadas.

class OpciónEncuesta:
    def __init__(self):
        self.texto = 'Sin registrar' # El texto con la opción de la encuesta.
        self.cuenta_de_voto = 0 # El número de usuarios que han votado por esta opción.

class RespuestaEncuesta:
    def __init__(self):
        self.id_encuesta = 'Sin registrar' # El identificador único de la encuesta.
        self.usuario = None # El usuario que haya cambiado la respuesta de la encuesta.
        self.id_opciones = [] # Identificadores de opciones de respuesta.

class Ubicación:
    def __init__(self):
        self.longitud = 0.0 # El valor de la longitud en coordenadas geográficas.
        self.latitud = 0.0 # El valor de la latitud en coordenadas geográficas.
        self.precisión_horizontal = 0.0 # El radio de incertidumbre para la ubicación, varía de 0 a 1500 m.
        self.periodo_en_vivo = 0 # El tiempo en segundos que durarán las actualizaciones desde el envío del mensaje.
        self.dirección = 0 # El ángulo de dirección en el que se está moviendo el usario.
        self.radio_alerta_proximidad = 0 # Distancia máxima para alertas de proximidad.

class UrlLogin:
    def __init__(self):
        self.url = 'Sin registrar' # Un URL HTTP a ser abierto con datos de autorización de un usuario.
        self.texto_reenviado = 'Sin registrar' # El nuevo texto del botón en mensajes reenviados.
        self.usuario_bot = '' # El nombre de usuario del bot que será utilizado para autorización.
        self.solicitar_acceso_escritura = False # Proporciona True a la solicitud de permiso para que el bot envíe mensajes al usuario.

class ConsultaRellamada:
    def __init__(self):
        self.id = 'Sin registrar' # Identificador único para esta consulta.
        self.remitente = None # El Usuario remitente de la consulta.
        self.mensaje = None # El Mensaje con el botón de rellamada que originó la consulta.
        self.id_mensaje_enlínea = 'Sin registrar' # El identificador del mensaje enviado via el bot en mod enlínea.
        self.instancia_chat = 'Sin registrar' # Identificador global, correspondiente al chat al cual el mensaje con el botón de rellamada fue enviado.
        self.datos = 'Sin registrar' # Los datos asociados con el botón de rellamada.
        self.nombre_corto_juego = 'Sin registrar' # Nombre corto del Juego a ser regresado, funciona como identificador único del juego.

class ForzarRespuesta:
    def __init__(self):
        self.forzar_respuesta = True # Muestra la interfaz de respuesta al usuario.
        self.selectivo = False # Usa este parámetro si deseas forzar la respuesta solamente de cierto usuarios.

class ComandoBot:
    def __init__(self):
        self.commando = 'Sin registrar' # El texto del comando, de 1 a 32 caractéres. Solo puede contener letras minúsculas en inglés, dígitos y guiones bajos.
        self.descripción = 'Sin registrar' # La descripción del comando.

class ParámetrosRespuesta:
    def __init__(self):
        self.id_chat_supergrupo = 0 # El grupo ha sido migrado a un supergrupo con el identificador especificado.
        self.reintentar_tras = 0 # En caso de exceder el control de inundación, el número de segundos restantes a esperar para que se repita la solicitud.