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

Usuario_tp
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

Persona_tp
----------
| Representa un usuario el cual no es un bot, es hijo de :ref:`usuario-tp` y hereda todas sus propiedades.
| Agrega además, la de la siguiente tabla.

============= ====== =========================================================================
Propiedad     Tipo   Descripción
============= ====== =========================================================================
apellido      str    El apellido del usuario.
============= ====== =========================================================================

.. _bot-tp:

Bot_tp
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

Chat_tp
-------
| Representa un chat de Telegram. Es el padre de todos los tipos de chat.
| Estos son:

*   ChatPrivado_tp
*   Grupo_tp
*   SuperGrupo_tp
*   Canal_tp

| Contiene las propiedades mínimas que todos los chats deben tener.
| Sus propiedades son las de la siguiente tabla.

================ ========== =========================================================================
Propiedad        Tipo       Descripción
================ ========== =========================================================================
id               int        El identificador único para este chat.
tipo             str        Determina el tipo de chat que es del enlistado anterior.
foto             bytes      La foto de perfil del chat, como aparece en Telegram.
mensaje_anclado  Mensaje_tp El mensaje anclado al chat más reciente.
cambia_stickers  bool       Es True si el bot puede cambiar el set de stickers del chat.
================ ========== =========================================================================

.. _chat-privado-tp:

ChatPrivado_tp
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

Grupo_tp
--------
| Representa un grupo en Telegram en el cual puede haber hasta 200 miembros, es hijo de :ref:`chat-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

================ ================ =========================================================================
Propiedad        Tipo             Descripción
================ ================ =========================================================================
título           str              El título del grupo como aparece en Telegram.
descripción      str              La descripción del grupo como aparece en Telegram.
invitación       str              El link de invitación al grupo.
permisos         PermisosChat_tp  Los permisos por default de miembros en el grupo.
================ ================ =========================================================================

.. _supergrupo-tp:

SuperGrupo_tp
--------------
| Representa un supergrupo en Telegram, en el cual puede haber hasta 5,000 suscriptores o miembros, es hijo de :ref:`chat-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ================ =========================================================================
Propiedad            Tipo             Descripción
==================== ================ =========================================================================
título               str              El título del supergrupo como aparece en Telegram.
descripción          str              La descripción del supergrupo como aparece en Telegram.
invitación           str              El link de invitación al supergrupo.
permisos             PermisosChat_tp  Los permisos por default de miembros en el supergrupo.
retraso              int              El retraso entre mensajes del supergrupo en modo lento.
nombre_set_stickers  str              El nombre del set de stickers del supergrupo.
==================== ================ =========================================================================

.. _canal-tp:

Canal_tp
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

Mensaje_tp
----------
| Representa un mensaje leído por el bot dentro de algún chat en el que participa. Es padre de todos los tipos de mensaje.
| Estos son:

*   MensajeReenviado_tp
*   MensajeBot_tp
*   MensajeRespuesta_tp
*   MensajeMultimedia_tp
*   MensajeEncuesta_tp
*   MensajeCambios_tp
*   MensajeFactura_tp
*   MensajeVariado_tp

| Contiene las propiedades mínimas que todos los chats deben tener.
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

MensajeReenviado_tp
-------------------
| Representa un mensaje reenviado de algún lugar. Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades.
| Agrega además, las de la siguiente tabla.

==================== ================== =========================================================================
Propiedad            Tipo               Descripción
==================== ================== =========================================================================
remitente            :ref:`usuario-tp`  El usuario que envió el mensaje reenviado, del chat local.
texto                str                El texto del mensaje en UTF-8 como aparece en Telegram.
reenviado_remitente  :ref:`usuario-tp`  El usuario que envió el mensaje **original**.
reenviado_de_chat    :ref:`chat-tp`     La información de mensaje si es reenviado de un canal.
reenviado_id         int                El identificador único del mensaje **original** si es reenviado de un canal.
reenviado_firma      str                La firma del autor de la publicación si es reenviado de un canal.
reenviado_nombre     str                El nombre del remitente en caso de que no comparta su perfil completo.
reenviado_fecha      int                La fecha en la que se envió el mensaje **original** en tiempo UNIX.
==================== ================== =========================================================================

.. _mensaje-bot:

MensajeBot_tp
-------------
| Representa un mensaje proveniente de un bot. Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades.
| Agrega además, la de la siguiente tabla.

==================== ================== =========================================================================
Propiedad            Tipo               Descripción
==================== ================== =========================================================================
via_bot              Usuario_tp         El bot mediante el cual se envió el mensaje.
texto                str                El texto del mensaje en UTF-8 como aparece en Telegram.
==================== ================== =========================================================================

.. _mensaje-respuesta-tp:

MensajeRespuesta_tp
| Representa un mensaje que es respuesta a otro dentro del mismo chat. Es hijo de :ref:`mensaje-tp` y hereda todas sus propiedades.
| Agrega además, la de la siguiente tabla.

==================== ================== =========================================================================
Propiedad            Tipo               Descripción
==================== ================== =========================================================================
respuesta_a          :ref:`mensaje-tp`  El mensaje **original** al cual éste responde.
texto                str                El texto del mensaje en UTF-8 como aparece en Telegram.
==================== ================== =========================================================================

.. _mensaje-multimedia:

MensajeMultimedia_tp
--------------------
| Representa un mensaje que tiene contenido multimedia como lo son:

*   Animaciones
*   Audios
*   Documentos
*   Fotos
*   Stickers
*   Videos
*   Notas de voz