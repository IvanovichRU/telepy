"""
Creado por Kevin Iván Domínguez Jiménez

MIT License
Copyright (c) 2020 Kevin Iván Domínguez Jiménez
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp
import asyncio
import json
import conversiones

class Cliente:

    URL_INICIAL = 'https://api.telegram.org/bot' # Este URL es utilizado universalmente para cualquier bot que no use WebHooks.

    def __init__(self, token: str) -> None:
        self.token_bot = token
        self.url_default = self.URL_INICIAL + self.token_bot
        self.chats = []
        self.comandos = []
        self.actualizaciones = []
        self.id_siguiente_actualización = 0


# FUNCIONES PRIVADAS

    async def __obtener_actualizaciones(self):
        """
        Esta funcion obtiene las actualizaciones acumuladas en el API, las guarda en
        el miembro: `actualizaciones`.
        """
        async with aiohttp.request('GET', self.url_default + '/getUpdates?timeout=10') as respuesta:
            dict_respuesta = json.loads(await respuesta.text())
            for actualización in dict_respuesta['result']:
                self.actualizaciones.append(conversiones.desempacar_actualización(actualización))

    async def __limpiar_actualizaciones(self):
        async with aiohttp.request('GET', self.url_default + '/getUpdates?timeout=5&offset=' + str(self.id_siguiente_actualización)) as respuesta:
            dict_respuesta = json.loads(await respuesta.text())

    def __leer_actualizaciones(self):
        """
        Esta función lee cada una de los objetos `Actualización` guardadas en `actualizaciones` 
        para procesar lo que haya dentro de ellas mediante la función `__procesar_actualización`.
        Al mismo tiempo, deja la lista de actualizaciones vacia y prepara la variable `id_siguiente_actualización`
        para vaciar el API.
        """
        for index in range(len(self.actualizaciones)):
            self.__procesar_actualización(self.actualizaciones[0])
            self.id_siguiente_actualización = self.actualizaciones[0].id + 1
            self.actualizaciones.pop(0)

    def __procesar_actualización(self, actualización):
        """
        Aquí se lee la información dentro de la `Actualización` pasada a esta función,
        de igual manera se clasifica correspondientemente.
        """
        if actualización.mensaje.entidades:

            # Agregar el chat del cual se recibió el mensaje el bot.
            if str(actualización.mensaje.chat.id) not in self.chats:
                self.__agregar_chat(str(actualización.mensaje.chat.id))

            for entidad in actualización.mensaje.entidades:
                if entidad.tipo == 'bot_command':
                    pass

    def __agregar_chat(self, chat_id: str):
        self.chats.append(chat_id)

    async def __encender(self):
        while True:
            await self.__obtener_actualizaciones()
            self.__leer_actualizaciones()
            await self.__limpiar_actualizaciones()
            await asyncio.sleep(1)



# FUNCIONES PÚBLICAS



    async def enviar(self, chat: str, mensaje: str):
        async with aiohttp.request('GET', self.url_default + '/sendMessage?' + "chat_id=" + chat + "&text=" + mensaje) as respuesta:
            dict_respuesta = json.loads(await respuesta.text())

    def iniciar(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__encender())