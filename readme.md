# Project Title

Backend for a blog CMS. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Running the tests

Explain how to run the automated tests for this system

## Web endpoints

### [main page]("/")```/```
This shows a list of current posts in application.
Just only those which publish date is reached. 

### [Blogs]("/blogs")``` /blogs```
List all blogs in the platform

### [Blogs]("/blogs/<username>")``` /blogs/<username>```
List all posts in blogs from tis user

### [Blogs]("/blogs/<username>/<id_post>")``` /blogs/<username>/id_post>```
Shows the detail of a specified post

### [login]("/login")``` /login```
Login page

### [logout]("/logout")``` /logout```
logout from app

### [signup]("/signup")``` /signup```
Signup as new user

### [new-post]("/new-post")``` /new-post```
Create a new post


## API 

### [User]("/api/v1/user")````/api/v1/user````
This endpoint manage users

**METHOD: POST**

DESCRIPTION: Create new user
PARAMETERS:
```
{
	"first_name": "desde API 2",
	"last_name": "apellido",
	"username": "usuarioAPI2",
	"email": "mail@mail.com",
	"password": "1234",
	"confirm_password": "1233"
}
```
RETURN: Status=200
```
{
    "id": 12,
    "first_name": "desde API 2",
    "last_name": "apellido",
    "username": "usuarioAPI2",
    "email": "mail@mail.com",
    "date_joined": "2019-05-26T21:05:26.739619Z"
}
```


### [User]("/api/v1/user/<id_username>")````/api/v1/user/<id_username>````

**METHOD: PUT**

DESCRIPTION: Update a new user only itself or admin
PARAMETERS:
```
{
    "id": 2,
    "first_name": "Pablosky",
    "last_name": "López C",
    "username": "Pablo",
    "email": "basanta79@gmail.com",
    "date_joined": "2019-05-13T21:27:42Z"
}
```
Must be sent user and password, of the specified user or an admin

RETURN: Status=200
```
{
    "id": 2,
    "first_name": "Pablosky",
    "last_name": "López C",
    "username": "Pablo",
    "email": "basanta79@gmail.com",
    "date_joined": "2019-05-13T21:27:42Z"
}
```
or
Status: 403 Forbidden
```
{
    "detail": "Authentication credentials were not provided."
}
```

**METHOD: GET**

DESCRIPTION: Retrieve data user. Only itself or admin
PARAMETERS: User and password
RETURN: Status=200
```
{
    "id": 2,
    "first_name": "Pablosky",
    "last_name": "López B",
    "username": "Pablo",
    "email": "basanta79@gmail.com",
    "date_joined": "2019-05-13T21:27:42Z"
}
```
or
STATUS=403 Forbidden
```
{
    "detail": "You do not have permission to perform this action."
}
```

**METHOD: DELETE**

DESCRIPTION: Delete a User
PARAMETERS: User and password
RETURN: Status = 201 No content
or
STATUS=403 Forbidden
```
{
    "detail": "You do not have permission to perform this action."
}
``` 

### [blog list]("/api/v1/blogs/") ```/api/v1/blogs/```

**METHOD: GET**

DESCRIPTION: This endpoint returns an array of JSON with the list of blogs with owner and its url.
Can be sent a JSON parameter to order by name and a field to search by title of blog.

PARAMETERS:
```
{
	"search": "pablo",
	"order": true
}
```

RETURN:
Status:200
```
[
    {
        "title": "Blog de pablo",
        "owner": 2,
        "username": "Pablo",
        "url": "/Pablo"
    },
    {
        "title": "Segundo blog de Pablo",
        "owner": 2,
        "username": "Pablo",
        "url": "/Pablo"
    }
]
```
### [Post]("/api/v1/post/<id_post>")````/api/v1/post/<id_post>````

**METHOD: GET**

DESCRIPTION: Show a post detail if its published, or all if its of your own or you are admin
PARAMETERS: not mandatory user and password
RETURN:
Status=200
```
{
    "id": 17,
    "blog": {
        "id": 3,
        "title": "Blog de Eva",
        "blog_image": "C:\\Users\\basanta79\\Documents\\bootcamp\\07_py_django\\wordplease\\images\\cabecera_blog.png",
        "owner": 3
    },
    "title": "Quinto post de Eva",
    "intro": "Introducion al quinto post de Eva",
    "body": "Contenido del quinto post de Eva",
    "image": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    "date_time_pub": "2019-05-30",
    "category": [
        {
            "id": 1,
            "cat_name": "Casa"
        },
        {
            "id": 2,
            "cat_name": "Motor"
        },
        {
            "id": 3,
            "cat_name": "Mobile"
        }
    ]
}
```

**METHOD: PUT**

DESCRIPTION: Edit a post, only if its yours or you are admin
PARAMETERS: 
```
{
    "blog": 3,
    "title": "tercer0  post de Eva",
    "intro": "Introducion al tercer post de Eva",
    "body": "Contenido del tercer post de Eva",
    "image": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    "date_time_pub": "2019-05-24",
}
```
RETURN:
Status=200

**METHOD: DELETE**

DESCRIPTION: Delete a specified post, only if its yours or you are admin
PARAMETERS: No 
RETURN: 
Status=204 No content


### [Post]("/api/v1/post/")````/api/v1/post/````

**METHOD: GET**

DESCRIPTION: Retrieves all posts in the database, only published, but all if you are admin or all that belongs to you
PARAMETERS: User and password, but not mandatory
RETURN:
Status= 200

**METHOD: POST**

DESCRIPTION: Create new post. Only in one of your blogs unless you are admin.
PARAMETERS:
```
{
    "id": 11,
    "blog": 3,
    "title": "Sexto post de Eva",
    "intro": "Introducion al sexto post de Eva",
    "body": "Contenido del sexto post de Eva",
    "image": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    "date_time_pub": "2019-05-30",
    "category": [1,2,3]
}
```
RETURN:
Status=201 created
```
{
    "id": 34,
    "blog": 3,
    "title": "Sexto post de Eva",
    "intro": "Introducion al sexto post de Eva",
    "body": "Contenido del sexto post de Eva",
    "image": "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    "date_time_pub": "2019-05-30",
    "category": [
        1,
        2,
        3
    ]
}
```
or
Status=403 Forbidden
```
{
    "error": "action forbidden"
}
```
