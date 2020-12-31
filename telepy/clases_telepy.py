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
class Usuario:
    id: int # El identificador único para este usuario o bot.
    es_bot: bool # Es  True si el usuario es un bot.
    primer_nombre: str # El primer nombre del usuario.
    usuario: str # El nombre de usuario del usuario.
    idioma: str # Código de lenguaje IETF asignado.

class Persona(Usuario):
    apellido: str

class Mensaje_TelePy:
    id: int
    remitente: Usuario_TelePy
    chat: Chat_TelePy
    fecha: int

class Actualización_TelePy:
    id: int
    mensaje: Mensaje_TelePy

class ComandoBot_TelePy:
    pass

class Chat:
    id: int
    titulo: str
    tipo: str
    todos_admin: bool
