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
 [X] - post:   'user' permite registrar un usuario
 [X] - get:   'user/<id>' permite ver detalles del usuario, (solo el mismo usuario o admnistrador)
 [X] - put:   'user/<id>' permite editar los detalles del usuario (solo el mismo usuario o admnistrador)
 [X] - delete:'user/<id>' permite eliminar un usuario (solo el mismo usuario o admnistrador)
 [X] - get:   'blogs/' devuelve un listado de blogs con su url. Permite buscar por nombre de usuario y ordenar por su nombre
 [X] - get:   'post/<id>' Devuelve un post, si esta publicado, si no esta publicado se muestra solo si estas autenticado o admin
 [X] - put:   'post/<id>' Edita un post, solo si autor o admin.
 [X] - delete:'post/<id>' Borrado de post, solo si autor o admin.
 [X] - post:  'post/' Creación de post, solo si autenticado.
[X] - get:   'post/' Listado de posts, solo publicados, pero si es autor o admin, se ven todos

MUST FIX
[X] - Al registrar usuario hay que crear un blog automaticamente
[X] - En PostWriteSerializer no se pueden cargar dinamicamente las choices
[X] - Signup view. Utilizar solo django_login 
[ ] - ListCreateApiView utilizar searchfilter y orderingfilter de django-rest
[X] - Cambiar nombre de PostListView2
[ ] - UserRegisterSerializer comprobar la confirmación del password