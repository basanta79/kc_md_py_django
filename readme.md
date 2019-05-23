# Project Title

Backend for a blog CMS. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Running the tests

Explain how to run the automated tests for this system

## Web endpoints

### [main page]("/")
This shows a list of current posts in application.
Just only those which publish date is reached. 


## API 
### [blog list]("/api/v1/blogs/") ```/api/v1/blogs/```
This endpoint returns an array of JSON with the list of blogs with owner and its url.
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

