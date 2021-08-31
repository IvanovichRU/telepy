##################
Tipos
##################
Los tipos dentro de esta librería estan diseñados a partir del `Telegram Bot API <https://core.telegram.org/bots/api>`_.
La librería es inteligente y entenderá qué tipo debe asignar al JSON obtenido mediante el API. A continuación se encuentran
todos los tipos de la librería.

.. _seccion-usuarios:

Usuarios
========
| A continuación están todos los tipos de usuario disponibles en telepy.


.. _usuario-tp:

Usuario
----------

| Representa un usuario de Telegram, es posible que sea un bot o un usuario real.
| Este tipo es el padre de los dos tipos de usuario, los cuales son :ref:`persona-tp` y :ref:`bot-tp`.
| Contiene las propiedades mínimas que todos los usuarios deben tener.
| Sus propiedades son las de la siguiente tabla.

============= ====== =========================================================================
Propiedad     Tipo   Descripción
============= ====== =========================================================================
id            int    El identificador único para este usuario o bot.
es_bot        bool   Es True si el usuario es un bot. Es automáticamente ajustado por telepy.
primer_nombre str    El primer nombre del usuario.
usuario       str    El nombre de usuario del usuario.
idioma        str    Código de lenguaje IETF asignado.
============= ====== =========================================================================

.. _persona-tp:

Persona
----------
| Representa un usuario el cual no es un bot, es hijo de :ref:`usuario-tp` y hereda todas sus propiedades.
| Agrega además, la de la siguiente tabla.

============= ====== =========================================================================
Propiedad     Tipo   Descripción
============= ====== =========================================================================
apellido      str    El apellido del usuario.
============= ====== =========================================================================

.. _bot-tp:

Bot
------
| Representa un usuario bot, es hijo de :ref:`usuario-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

================ ====== =========================================================================
Propiedad        Tipo   Descripción
================ ====== =========================================================================
unible_a_grupos  bool   Es True si el bot puede unirse a grupos.
lee_todo         bool   Es True si el bot lee todos los mensajes dentro de un grupo.
consultas_dentro bool   Es True si el bot soporta el modo dentro de linea "inline mode".
================ ====== =========================================================================

.. _sección-chats:

Chats
=====
| A continuación están todos los tipos de chat disponibles en telepy.

.. _chat-tp:

Chat
-------
| Representa un chat de Telegram. Es el padre de todos los tipos de chat.
| Estos son:

*   ChatPrivado
*   Grupo
*   SuperGrupo
*   Canal

| Contiene las propiedades mínimas que todos los chats deben tener.
| Sus propiedades son las de la siguiente tabla.

================ =================== =========================================================================
Propiedad        Tipo                Descripción
================ =================== =========================================================================
id               int                 El identificador único para este chat.
tipo             str                 Determina el tipo de chat que es del enlistado anterior.
foto             bytes               La foto de perfil del chat, como aparece en Telegram.
mensaje_anclado  :ref:`mensaje-tp`   El mensaje anclado al chat más reciente.
cambia_stickers  bool                Es True si el bot puede cambiar el set de stickers del chat.
================ =================== =========================================================================

.. _chat-privado-tp:

ChatPrivado
--------------
| Representa un chat privado en Telegram, en este solo participan dos personas, es hijo de :ref:`chat-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

================ ========== =========================================================================
Propiedad        Tipo       Descripción
================ ========== =========================================================================
usuario          str        El nombre de usuario de la otra persona en un chat privado.
primer_nombre    str        El primer nombre de la otra persona en el chat privado.
apellido         str        El apellido de la otra persona en el chat privado.
bio              str        La bio de la otra persona en el chat privado.
================ ========== =========================================================================

.. _grupo-tp:

Grupo
--------
| Representa un grupo en Telegram en el cual puede haber hasta 200 miembros, es hijo de :ref:`chat-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

================ ================ =========================================================================
Propiedad        Tipo             Descripción
================ ================ =========================================================================
título           str              El título del grupo como aparece en Telegram.
descripción      str              La descripción del grupo como aparece en Telegram.
invitación       str              El link de invitación al grupo.
permisos         PermisosChat     Los permisos por default de miembros en el grupo.
================ ================ =========================================================================

.. _supergrupo-tp:

SuperGrupo
--------------
| Representa un supergrupo en Telegram, en el cual puede haber hasta 5,000 suscriptores o miembros, es hijo de :ref:`chat-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ================ =========================================================================
Propiedad            Tipo             Descripción
==================== ================ =========================================================================
título               str              El título del supergrupo como aparece en Telegram.
descripción          str              La descripción del supergrupo como aparece en Telegram.
invitación           str              El link de invitación al supergrupo.
permisos             PermisosChat     Los permisos por default de miembros en el supergrupo.
retraso              int              El retraso entre mensajes del supergrupo en modo lento.
nombre_set_stickers  str              El nombre del set de stickers del supergrupo.
==================== ================ =========================================================================

.. _canal-tp:

Canal
--------
| Representa un canal en Telegram, el cual puede tener un número ilimitado de suscriptores, es hijo de :ref:`chat-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ================ =========================================================================
Propiedad            Tipo             Descripción
==================== ================ =========================================================================
título               str              El título del canal como aparece en Telegram.
descripción          str              La descripción del canal como aparece en Telegram.
invitación           str              El link de invitación al canal.
==================== ================ =========================================================================

.. _sección-mensajes:

Mensajes
========
| A continuación están todos los tipos de mensaje disponibles en telepy.

.. _mensaje-tp:

Mensaje
----------
| Representa un mensaje leído por el bot dentro de algún chat en el que participa. Es padre de todos los tipos de mensaje.
| Estos son:

*   MensajeReenviado
*   MensajeBot
*   MensajeRespuesta
*   MensajeMultimedia
*   MensajeCambios
*   MensajeVariado

| Contiene las propiedades mínimas que todos los mensajes deben tener.
| Sus propiedades son las de la siguiente tabla.

==================== ================ =========================================================================
Propiedad            Tipo             Descripción
==================== ================ =========================================================================
id                   int              El identificador único para este mensaje dentro de este chat.
fecha                int              La fecha en la que se envió el mensaje en tiempo UNIX.
chat                 :ref:`chat-tp`   El chat al que pertenece este mensaje.
fecha_editado        int              La fecha en la que se editó el mensaje por última vez.
==================== ================ =========================================================================

.. _mensaje-reenviado-tp:

MensajeReenviado
-------------------
| Representa un mensaje reenviado de algún lugar. Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ===================== ===============================================================================
Propiedad            Tipo                  Descripción
==================== ===================== ===============================================================================
remitente            :ref:`usuario-tp`     El usuario que envió el mensaje reenviado, del chat local.
texto                str                   El texto del mensaje en UTF-8 como aparece en Telegram.
entidades            list[EntidadMensaje]  Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.
reenviado_remitente  :ref:`usuario-tp`     El usuario que envió el mensaje **original**.
reenviado_de_chat    :ref:`chat-tp`        La información de mensaje si es reenviado de un canal.
reenviado_id         int                   El identificador único del mensaje **original** si es reenviado de un canal.
reenviado_firma      str                   La firma del autor de la publicación si es reenviado de un canal.
reenviado_nombre     str                   El nombre del remitente en caso de que no comparta su perfil completo.
reenviado_fecha      int                   La fecha en la que se envió el mensaje **original** en tiempo UNIX.
==================== ===================== ===============================================================================

.. _mensaje-bot:

MensajeBot
-------------
| Representa un mensaje proveniente de un bot. Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ================== =========================================================================
Propiedad            Tipo               Descripción
==================== ================== =========================================================================
via_bot              Usuario            El bot mediante el cual se envió el mensaje.
texto                str                El texto del mensaje en UTF-8 como aparece en Telegram.
entidades            list[Entidad]      Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.
==================== ================== =========================================================================

.. _mensaje-respuesta-tp:

MensajeRespuesta_tp
| Representa un mensaje que es respuesta a otro dentro del mismo chat. Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ================== =========================================================================
Propiedad            Tipo               Descripción
==================== ================== =========================================================================
respuesta_a          :ref:`mensaje-tp`  El mensaje **original** al cual éste responde.
texto                str                El texto del mensaje en UTF-8 como aparece en Telegram.
entidades            list[Entidad]      Una lista de entidades en el mensaje, tales como usuarios, URLs, comandos, etc.
==================== ================== =========================================================================

.. _mensaje-multimedia-tp:

MensajeMultimedia
--------------------
| Representa un mensaje con contenido multimedia como lo son:

*   Animaciones
*   Audios
*   Documentos
*   Fotos
*   Stickers
*   Videos
*   Notas de voz

| Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades. En general, un objeto de este tipo tendrá solo **una**
  de las propiedades en la siguiente tabla aparte de las que hereda de Mensaje. Sin embargo, por simplicidad, todas se
  contienen en este tipo.

==================== ================== ===============================================================================
Propiedad            Tipo               Descripción
==================== ================== ===============================================================================
animacion            Animación          El mensaje contiene una Animación que se almacena en esta propiedad.
audio                Audio              El mensaje contiene un Audio que se almacena en esta propiedad.
documento            Documento          El mensaje contiene un Documento que se almacena en esta propiedad.
foto                 list[Foto]         El mensaje contiene una lista de Fotos  que se almacena en esta propiedad.
sticker              Sticker            El mensaje contiene un Sticker que se almacena en esta propiedad.
vídeo                Video              El mensaje contiene un Vídeo que se almacena en esta propiedad.
vídeo_nota           VideoNota          El mensaje contiene una VídeoNota que se almacena en esta propiedad.
nota_voz             NotaVoz            El mensaje contiene una NotaVoz que se almacena en esta propiedad.
leyenda              str                La leyenda o nota al pie de la animación, audio, documento, foto, vídeo o voz.
entidades            list[Entidad]      La lista de entidades en la leyenda, tales como usuarios, URLs, comandos, etc.
==================== ================== ===============================================================================

.. _mensaje-cambios-tp:

MensajeCambios
---------------
| Representa un mensaje que registra un cambio en el :ref:`chat-tp` donde se recibió este mensaje. Es hijo de
  :ref:`mensaje-tp` y hereda todas sus propiedades. En general, un objeto de este tipo tendrá solo **algunas**
  de las propiedades en la siguiente tabla aparte de las que hereda de Mensaje. Sin embargo, por simplicidad,
  todas se contienen un este tipo.

==================== ========================= =============================================================================================
Propiedad            Tipo                      Descripción
==================== ========================= =============================================================================================
nuevos_miembros      list[:ref:`usuario-tp`]   La lista de miembros nuevos que fueron agregados al :ref:`chat-tp` o :ref:`supergrupo-tp`
miembro_eliminado    :ref:`usuario-tp`         El miembro que fue removido en este mensaje.
nuevo_título         str                       El nuevo título del :ref:`chat-tp` que se cambió en este mensaje.
nueva_foto           list[TamañoFoto]          La nueva foto del :ref:`chat-tp` que se cambió en este mensaje.
id_chat_supergrupo   int                       El identificador único del :ref:`supergrupo-tp` en el cual este :ref:`grupo-tp` se convirtió.
id_supergrupo_chat   int                       El identificador único del :ref:`grupo-tp` en el cual este :ref:`supergrupo-tp` se convirtió.
mensaje_anclado      :ref:`mensaje-tp`         El Mensaje que fue anclado a este :ref:`chat-tp` en este mensaje.
==================== ========================= =============================================================================================

.._mensaje-variado:

MensajeVariado
--------------
| Representa un mensaje que no envía ni una de las especificaciones de los anteriores tipos.
| Más específicamente:

*   Contacto
*   Dado
*   Juego
*   Encuesta
*   Establecimiento
*   Ubicación

| Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades. Y almacena también las necesarias para manejar
| los mensajes que contienen información de los tipos en el listado anterior.

==================== ========================= =============================================================================================
Propiedad            Tipo                      Descripción
==================== ========================= =============================================================================================
contacto             Contacto                  El mensaje contiene un Contacto compartido que se almacena en esta propiedad.
dado                 Dado                      El mensaje contiene un Dado con un valor aleatorio que se almacena en esta propiedad.
juego                Juego                     El mensaje contiene un Juego que se almacena en esta propiedad.
encuesta             Encuesta                  El mensaje contiene una Encuesta que se almacena en esta propiedad.
establecimiento      Establecimineto           El mensaje contiene un Establecimineto que se almacena en esta propiedad.
ubicación            Ubicación                 El mensaje contiene una Ubicación compartida que se almacena en esta propiedad.
factura              Factura                   El mensaje contiene una Factura que se almacena en esta propiedad.
pago_exitoso         PagoExitoso               El mensaje contiene un PagoExitoso que se almacena en esta propiedad.
==================== ========================= =============================================================================================

.. _seccion-utilidad-mensajes:

Utilidad de Mensajes
====================

.. _id-mensaje:

IdMensaje
---------
| Representa un identificador único de un mensaje, es utilizado en el método copiar_mensaje.
| Tiene una sola propiedad:

==================== ========================= =============================================================================================
Propiedad            Tipo                      Descripción
==================== ========================= =============================================================================================
id_mensaje           int                       El identificador único del mensaje.
==================== ========================= =============================================================================================


.. _entidad-mensaje:

EntidadMensaje
--------------
| Representa una entidad especial dentro de un mensaje de texto, tales como hashtags, nombres de usuario, URLs, etc.
| Es padre de todos los tipos de entidad los cuales son:

*   EntidadUrl
*   EntidadMención
*   EntidadCódigo

| Hay más tipos de entidad, sin embargo, sólo existe manejo de información para los tipos de la lista anterior.
| A continuación una lista de todos los tipos de entidad:

*   mención (@nombredeusuario)
*   hasthag (#hashtag)
*   moneda ($MXN)
*   comando (/start@mi_bot)
*   url (https://telegram.org)
*   email (no-contestar@telegram.org)
*   teléfono (+52-111-222-3333)
*   negritas (**texto en negritas**)
*   cursiva (*texto en cursiva*)
*   subrayado (texto subrayado)
*   tachado (texto tachado)
*   código (cadena monoancha)
*   pre (bloque monoancho)
*   enlace (para enlaces clickables)
*   mención_texto (para usuarios sin nombre de usuario)

| Sus propiedades son las de la siguiente tabla.

==================== ========================= =============================================================================================
Propiedad            Tipo                      Descripción
==================== ========================= =============================================================================================
tipo                 str                       El tipo de la entidad. Vea la lista anterior.
desplazo             int                       El desplazo en unidades de código UTF-16 hasta el inicio de la entidad dentro del texto.
longitud             int                       La longitud de la entidad en unidades de código UTF-16.
url                  str                       El url al que lleva el enlace al darle click. **sólo para enlace, no para url**.
usuario              :ref:`usuario-tp`         El usuario mencionado. **sólo para mención_texto, no para mención**
lenguaje             str                       El lenguaje de programación usado en la entidad de texto. **sólo para pre, no para código**
==================== ========================= =============================================================================================