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
from datetime import datetime, timezone

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
        async with aiohttp.request('GET', self.url_default + '/getUpdates?timeout=1') as respuesta:
            dict_respuesta = json.loads(await respuesta.text())
            for actualización in dict_respuesta['result']:
                self.actualizaciones.append(conversiones.desempacar_actualización(actualización))

    async def __limpiar_actualizaciones(self):
        async with aiohttp.request('GET', self.url_default + '/getUpdates?timeout=5&offset=' + str(self.id_siguiente_actualización)) as respuesta:
            dict_respuesta = json.loads(await respuesta.text())

    async def __leer_actualizaciones(self):
        """
        Esta función lee cada una de los objetos `Actualización` guardadas en `actualizaciones` 
        para procesar lo que haya dentro de ellas mediante la función `__procesar_actualización`.
        Al mismo tiempo, deja la lista de actualizaciones vacia y prepara la variable `id_siguiente_actualización`
        para vaciar el API.
        """
        for i in range(len(self.actualizaciones)):
            await self.__procesar_actualización(self.actualizaciones[0])
            self.id_siguiente_actualización = self.actualizaciones[0].id + 1
            self.actualizaciones.pop(0)

    async def __procesar_actualización(self, actualización):
        """
        Aquí se lee la información dentro de la `Actualización` pasada a esta función,
        de igual manera se clasifica correspondientemente.
        """
        print("Actualización leída, su id es: " + str(actualización.id))

        if actualización.mensaje.entidades:
            actualización.usuario = actualización.mensaje.remitente.usuario
            actualización.hora = str(datetime.utcfromtimestamp(actualización.mensaje.fecha - 3600 * 5).strftime("%H:%M:%S"))

            for entidad in actualización.mensaje.entidades:
                if entidad.tipo == 'bot_command':
                    comando = actualización.mensaje.texto[entidad.desplazo:entidad.desplazo+entidad.longitud]
                    for func in self.comandos:
                        if (func.__name__ == comando[1:]):
                            await func(self, actualización)
                            
                            

    async def __encender(self):
        print("Bot iniciado con token " + self.token_bot + "...")
        while True:
            print("Revisando API ...")
            await self.__obtener_actualizaciones()
            await self.__leer_actualizaciones()
            await self.__limpiar_actualizaciones()
            await asyncio.sleep(1)



# FUNCIONES PÚBLICAS

    async def enviar(self, chat: str, mensaje: str, image = None):
        async with aiohttp.request('GET', self.url_default + '/sendMessage?' + "chat_id=" + chat + "&text=" + mensaje) as respuesta:
            dict_respuesta = json.loads(await respuesta.text())

    def agregar_comando(self, función):
        self.comandos.append(función)


    def iniciar(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__encender())