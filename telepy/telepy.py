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
        self.id_última_actualización = 0

    async def __iniciar_actualizaciones(self):
        async with aiohttp.request('GET', self.url_default + '/getUpdates?timeout=3') as respuesta:
            dict_respuesta = json.loads(await respuesta.text())
            for actualización in dict_respuesta['result']:
                self.actualizaciones.append(conversiones.desempacar_actualización(actualización))


    """
    Aquí inician las funciones directas del 'Telegram Bot API' proporcionado en: https://core.telegram.org/bots/api
    no se recomienda utilizar estas funciones directamente, utiliza las funciones más adelante.
    """
    # async def __enviar_mensaje(self, chat_id: str, mensaje: str) -> dict:
    #     """
    #     Envia, mediante el bot, el mensaje dado.
    #     """
    #     async with aiohttp.request('POST', self.url_def + '/sendMessage?chat_id=' + chat_id + '&text=' + mensaje) as respuesta:
    #         return json.loads(await respuesta.text())

    # async def __obtener_actualizaciones(self) -> dict:
    #     """
    #     Solo debe utilizarse para inicializar el ciclo del bot.
    #     """
    #     async with aiohttp.request('GET', self.url_def + '/getUpdates?timeout=10') as respuesta:
    #         return json.loads(await respuesta.text())

    # async def __siguiente_actualización(self, update_id: int) -> dict:
    #     """
    #     Al llamar esta funcion, el bot lee la actualización con el id proporcionado
    #     solo recuerda que al hacer esto, las actualizaciones anteriores a esta, son
    #     eliminadas.
    #     """
    #     async with aiohttp.request('GET', self.url_def + '/getUpdates?timeout=2&offset=' + str(update_id)) as respuesta:
    #         return json.loads(await respuesta.text())

    async def iniciar(self):
        await self.__iniciar_actualizaciones()



async def principal():
    cliente = Cliente('token')
    await cliente.iniciar()
    for act in cliente.actualizaciones:
        print(act)

loop = asyncio.get_event_loop()
loop.run_until_complete(principal())