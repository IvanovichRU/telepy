#######################
¡Bienvenido a telepy!
#######################

telepy es una librería creada con la intención de facilitar el desarrollo de bots para la
plataforma proporcionada por `Telegram <https://es.wikipedia.org/wiki/Telegram>`_. Se pueden generar 
comandos para el bot en muy pocas líneas de código y es posible desarrollar un bot complejo sin mayor 
esfuerzo.

Ejemplo
==========
.. code-block:: python3
   :linenos:

   from telepy import *

   mi_cliente = Cliente("TOKEN DE TELEGRAM BOT")

   async def hola(cliente, actualización):
      await cliente.enviar(str(actualización.mensaje.chat.id), "Hola compañere.")
      
   cliente.agregar_comando(hola)
   cliente.iniciar()

.. toctree::
   :maxdepth: 2

   tipos
   acerca-de-mi
