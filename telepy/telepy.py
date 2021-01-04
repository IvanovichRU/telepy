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


class Bot_TelePy:

    URL_INICIAL = 'https://api.telegram.org/bot' # Este URL es utilizado universalmente para cualquier bot que no use WebHooks
    token_bot: str # Aquí se guarda el token privado para comunicarse con un bot.
    url_def: str # La combinación de 'URL_INICIAL' y token_bot

    chats = [] # Contiene los chats en los que participa el bot. #PORHACER meter objetos Chat_TelePy aquí.
    comandos = [] # Contiene comandos que escucha el bot. #PORHACER meter objetos ComandoBot_TelePy aquí.
    actualizaciones = [] # Contiene los objetos Actualización_TelePy a ser procesados por el bot.
    ult_actualización = 0 # El contador para obtener actualizaciones y borrar las anteriores.

    def __init__(self, token: str) -> None:
        self.token_bot = token
        self.url_def = self.URL_INICIAL + self.token_bot

    def __agregar_chat(self, chat_id: str):
        """
        Agrega un nuevo chat a la lista de chats.
        """
        if chat_id not in self.chats:
            self.chats.append(chat_id)

    def __leer_actualización(self, actualización):
        print(actualización.mensaje.texto)

    def __procesar_actualizaciones(self):
        for actualización in self.actualizaciones:
            self.__leer_actualización(actualización)

    def __vaciar_actualizaciones(self, actualizaciones: list[dict]):
        for actualización in actualizaciones:
            self.actualizaciones.append({})

    """
    Aquí inician las funciones directas del 'Telegram Bot API' proporcionado en: https://core.telegram.org/bots/api
    no se recomienda utilizar estas funciones directamente, utiliza las funciones más adelante.
    """
    async def __obtener_yo(self):
        async with aiohttp.request('GET', self.url_def + '/getMe') as respuesta:
            return json.loads(await respuesta.text())

    async def __enviar_mensaje(self, chat_id: str, mensaje: str) -> dict:
        """
        Envia, mediante el bot, el mensaje dado.
        """
        async with aiohttp.request('POST', self.url_def + '/sendMessage?chat_id=' + chat_id + '&text=' + mensaje) as respuesta:
            return json.loads(await respuesta.text())

    async def __enviar_dado(self, chat_id: str) -> dict:
        """
        Envia una animación que termina en un número del 1 al 6.
        """
        async with  aiohttp.request('GET', self.url_def + '/sendDice?chat_id=' + chat_id + '&emoji=' + '🎲') as respuesta:
            return json.loads(await respuesta.text())

    async def __obtener_actualizaciones(self) -> dict:
        """
        Solo debe utilizarse para inicializar el ciclo del bot.
        """
        async with aiohttp.request('GET', self.url_def + '/getUpdates?timeout=10') as respuesta:
            return json.loads(await respuesta.text())

    async def __siguiente_actualización(self, update_id: int) -> dict:
        """
        Al llamar esta funcion, el bot lee la actualización con el id proporcionado
        solo recuerda que al hacer esto, las actualizaciones anteriores a esta, son
        eliminadas.
        """
        async with aiohttp.request('GET', self.url_def + '/getUpdates?timeout=10&offset=' + self.ult_actualización) as respuesta:
            return json.loads(await respuesta.text())

    async def __entender_mensaje(self, mensaje_leido: str) -> None:
        """
        Función para comprender el comando enviado
        """
        if mensaje_leido == '/iniciar' or mensaje_leido == '/iniciar@mi-bot':
            await self.__enviar_mensaje('chat_id', 'Andamo atibo papi')
        if mensaje_leido == '/dado' or mensaje_leido == '/dado@mi-bot':
            await self.__enviar_dado('chat_id')
        if mensaje_leido == '/omae' or mensaje_leido == '/omae@mi-bot':
            await self.__enviar_mensaje('chat_id', '🎲')

    async def bot_info(self) -> None:
        info_js =  await self.__obtener_yo()
        for key, value in info_js['result'].items():
            print(key, ':', value)

    async def iniciar(self):
        primer_actualización = await self.__obtener_actualizaciones()



# async def principal():
    # cliente = Bot_TelePy('token')
    # await cliente.iniciar()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(principal())