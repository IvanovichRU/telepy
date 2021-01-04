class PrecioEtiquetado:
    def __init__(self):
        self.etiqueta = 'Sin registrar' # Etiqueta de porción.
        self.monto = 0 # El precio del producto en la unidad más pequeña de la moneda
                          # Por ejemplo para MXN$ 1.45 pasa cantidad con el valor de 145 (centavos).
                        
class Factura:
    def __init__(self):
        self.título = 'Sin registrar' # El nombre del producto.
        self.descripción = 'Sin registrar' # La descripción del producto.
        self.parámetro_inicio = 'Sin registrar' # El parámetro único de enlace-profundo al bot ' bot deep-linking' que puede ser usado para generar esta factura.
        self.moneda = 'Sin registrar' # El código de tres letras ISO-4217 de la moneda.
        self.monto_total = 0 # El precio total en la unidad más pequeña de la moneda.
                                # Por ejemplo para MXN$ 1.45 pasa este atributo con el valor de 145 (centavos).

class DirecciónEnvío:
    def __init__(self):
        self.código_país = 'Sin registrar' # El código ISO 3166-1 alpha 2 País.
        self.estado = 'Sin registrar' # El estado, de ser aplicable.
        self.ciudad = 'Sin registrar' # La ciudad, de ser aplicable.
        self.calle_1 = 'Sin registrar' # La primer línea de la dirección.
        self.calle_2 = 'Sin registrar' # La segunda línea de la dirección.
        self.código_postal = 'Sin registrar' # El código postal de la dirección.

class InfoOrden:
    def __init__(self):
        self.nombre = 'Sin registrar' # El nombre del usuario.
        self.número = 'Sin registrar' # El número telefónico del usuario.
        self.email = 'Sin registrar' # El correo electrónico del usuario.
        self.dirección_envío = 'Sin registrar' # La dirección de envío del usuario.

class PagoExitoso:
    def __init__(self):
        self.moneda = 'Sin registrar' # El código de tres letras ISO-4217 de la moneda.
        self.monto_total = 0 # El precio total en la unidad más pequeña de la moneda.
                             # Por ejemplo para MXN$ 1.45 pasa este atributo con el valor de 145 (centavos).
        self.carga_factura = 'Sin registrar' # La carga de la factura especificada por el bot.
        self.id_opción_envío = 'Sin registrar' # El identificador de la opción de envío elegida por el usario.
        self.info_orden = None # Información de la orden proporcionada por el usuario.
        self.id_cargo_pago_telegram = 'Sin registrar' # Identificador del pago de Telegram.
        self.id_proveedor_cargo_pago = 'Sin registrar' # Identificador del proveedor del pago.

class ConsultaEnvío:
    def __init__(self):
        self.id = 'Sin registrar' # El identificador único de la consulta.
        self.remitente = None # El Usuario que envió la consulta.
        self.carga_factura = 'Sin registrar' # La carga de la factura especificada por el bot.
        self.dirección_envío = None # La dirección de envío del usuario.

class ConsultaPreCobro:
    def __init__(self):
        self.id = 'Sin registrar' # El identificador único de la consulta.
        self.remitente = None  # El Usuario que envió la consulta.
        self.moneda = 'Sin registrar' # El código de tres letras ISO-4217 de la moneda.
        self.monto_total =  0 # El precio total en la unidad más pequeña de la moneda.
                              # Por ejemplo para MXN$ 1.45 pasa este atributo con el valor de 145 (centavos).
        self.carga_factura = 'Sin registrar' # La carga de la factura especificada por el bot.
        self.id_opción_envío = None # La información del envío proporcionada por el usuario.