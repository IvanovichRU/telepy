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
class ComandoBot_TelePy:
    pass

class Chat_TelePy:
    id: int
    titulo: str
    tipo: str
    todos_admin: bool

class Usuario_TelePy:
    id: int
    es_bot: bool
    nombre: str
    apellido: str
    usuario: str

class Mensaje_TelePy:
    id: int
    remitente: Usuario_TelePy
    chat: Chat_TelePy
    fecha: int

class Actualización_TelePy:
    id: int
    mensaje: Mensaje_TelePy