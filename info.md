# Objetivos de la practica:
WEB
[X] - '/' Desde la página principal se deben ver los últimos posts publicos publicados por los usuarios
[X] - 'blogs/' Debe listar los blogs de los usuarios que hay en la plataforma.
[X] - 'blogs/<nombre_de_usuario>/' Listamos los posts de cada usuario ordenados de mas nuevo a mas antiguo
[X] - 'blogs/<nombre_de_usuario>/<post_id>' Se podrá ver el detalle de un post del usuario y ese id
[X] - 'login' Realizamos un login en la página
[X] - 'logout' Relizamos un logout de la página
[X] - 'signup' Nos podemos registrar en la página
[X] - 'new-post' Formulario para crear un post nuevo
API
[X] - put:  'user' permite registrar un usuario
[-] - get:   'user/<nombre_de_usuario>' permite ver detalles del usuario, (solo el mismo usuario o admnistrador)
[-] - put:   'user/<nombre_de_usuario>' permite editar los detalles del usuario (solo el mismo usuario o admnistrador)
[-] - delete:'user/<nombre_de_usuario>' permite eliminar un usuario (solo el mismo usuario o admnistrador)
[X] - get:   'blogs/' devuelve un listado de blogs con su url. Permite buscar por nombre de usuario y ordenar por su nombre
[ ] - 