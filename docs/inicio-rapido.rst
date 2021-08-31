################
Inicio Rápido
################

En esta sección econtrarás una guía para comenzar a utilizar telepybots rápidamente, si buscas la documentación 
del API, da click :doc:`aqui <docs-api>`.

.. _seccion-instalacion:

Instalación
=================
1. Aún no existe un paquete en PyPI, pero se está trabajando en ello y se podrá 
   instalar fácilmente con el uso del comando:

   .. code-block:: bash

      $ pip install telepybots

   .. Note::
      Por ahora sólo es posible descargar el código mediante `GitHub <https://github.com/IvanovichRU/telepy>`_, es posible 
      también contribuir a la librería en GitHub, en este momento solo es mantenida por un desarrollador y 
      se beneficiaría bastante si recibe apoyo externo.

   2. **telepybots** tiene una sola dependencia, `aiohttp <https://docs.aiohttp.org/en/stable/>`_ 
   actualmente necesita ser instalada manualmente, mediante PyPI será instalada automáticamente al 
   instalarse **telepybots**. De igual manera puede ser instalada fácilmente usando pip:

   .. code-block:: bash

      $ pip install aiohttp

   3. Finalmente, importamos el módulo mediante la siguiente línea:

   .. code-block::

      from telepy import *

.. _seccion-ejemplo:

Ejemplo
==========
.. code-block:: python3
   :linenos:
   :caption: Programa ejemplo para demostrar el sencillo uso de telepy.

   from telepy import *

   mi_cliente = Cliente("TOKEN DE TELEGRAM BOT")

   async def hola(cliente, actualización):
      await cliente.enviar(str(actualización.mensaje.chat.id), "Hola, humano.")

   cliente.agregar_comando(hola)
   cliente.iniciar()

En el código de arriba podemos ver el proceso para implementar código sencillamente con información 
obtenida mediante interacciones llevadas a cabo en un chat con el bot de telegram. Con el código anterior, 
al enviar un mensaje en Telegram en un chat donde participe algún bot con el contenido 
``"hola"``, el bot responderá con un mensaje diciendo ``"Hola, humano."``. Se puede acceder a una gran variedad de 
información mediante el objeto llamado actualización.