# Flex Test

Тестовое задание от компании [Flexsites](https://flexites.org/)

# Интсрукции для тестирования

Запуск реализован с помощью docker, сделайте следующее: 

- git clone данную репазиторию
- запускаете docker на своей машине
- docker-compose build
- docker-compose --env-file .env  up -d


Ps. container Nginx в docker слушает порт 80, проверьте если он не занят

Или можно пройти по [ip address](http://95.163.233.100), не сделал домен и SSL сертификат, это только виртуальный сервер для тестирования.

## Для входа в панель admin:
username: admin@gmail.com <br />
password: 123123123

# Мини-документация 


## `POST` *login*

 **Метод принимает данные пользователя для авторизации

```json
{
	"email": "exampl@gmail.com",
	"password": "12345678"
}
```

и возвращает фамилию и имя пользователя и токены для авторизации по JWT

```json
{
    "data": "Мулхам Шахин",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NzMyNzI2OCwiaWF0IjoxNjc3MjQwODY4LCJqdGkiOiIyY2FlMDBlMmUwMGM0YzdmOGNkYzEwMTRhZDIyZjI4ZCIsInVzZXJfaWQiOjF9.buJf_eywaCZh-mr6ExjYvCpYJsF1RCCaMzQr_EfbHac",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MjQxMTY4LCJpYXQiOjE2NzcyNDA4NjgsImp0aSI6ImU5YzU5MjBhMmE2YTQwNjVhNmJkYzM0NGRjYTY2MWFjIiwidXNlcl9pZCI6MX0.64X1C3P96qb1kH-C-k4TDrD2nG9JT4o7M0SnmqKpyRI"
}
```

## `POST` signup

 **Метод принимает данные для создания нового пользователя и затем авторизации этого же пользователя.

```json
{
	"email": "exampl@gmail.com",
	"password": "12345678",
	"first_name": "Mulham",
	"last_name": "Shaheen",
	"phone": "+79123456789", // или 89123456789 
}
```

и возвращает данные модели `User`и токены для авторизации по JWT

```json
{
    "data": {
				"email": "exampl@gmail.com",
				"password": "12345678",
				"first_name": "Mulham",
				"last_name": "Shaheen",
				"phone": "+79123456789",
				"icon": "",
				"organizations": []			
		},
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NzMyNzI2OCwiaWF0IjoxNjc3MjQwODY4LCJqdGkiOiIyY2FlMDBlMmUwMGM0YzdmOGNkYzEwMTRhZDIyZjI4ZCIsInVzZXJfaWQiOjF9.buJf_eywaCZh-mr6ExjYvCpYJsF1RCCaMzQr_EfbHac",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MjQxMTY4LCJpYXQiOjE2NzcyNDA4NjgsImp0aSI6ImU5YzU5MjBhMmE2YTQwNjVhNmJkYzM0NGRjYTY2MWFjIiwidXNlcl9pZCI6MX0.64X1C3P96qb1kH-C-k4TDrD2nG9JT4o7M0SnmqKpyRI"
}
```

## `POST` profile/edit/

Метод редактирования профиля, для выполнения необходимво в headers добавит параметр  `Authorization` и передать в нём токен access JWT. А в теле передать те параметры которые нужно обновить  

```json
"headers":{
	...
	"Authorization": "Bearer <access token>" 
}
{

	"phone": "+79987654321",
}
```

и возвращает новые данные модели `User`

```json
{
    "email": "exampl@gmail.com",
		"password": "12345678",
		"first_name": "Mulham",
		"last_name": "Shaheen",
		"phone": "+79987654321",
		"icon": "",
		"organizations": []		
}
```

## `GET` users/all/

Метод возврощается список всех пользователей

```json
[
    {
        "email": "admin@gmail.com",
        "password": "pbkdf2_sha256$390000$kIKp84iskmgON8L5jw7o25$CtRZGzW+7oID44ARMOrYpF4ai7eKM0HTAKEJgPbxKiE=",
        "first_name": "Мулхам",
        "last_name": "Шахин",
        "icon": "/uploads/users/Mulham.jpg",
        "phone": "+79026121473",
        "organizations": []
    },
    {
        "email": "mul@gmail.com",
        "password": "pbkdf2_sha256$390000$RPDc7lqpSIUAJEjUrJ2l0k$ht9bZGpIqAEuAbYy0duIclhPjdC73KX/GWi1dxbpMEE=",
        "first_name": "Мулхам",
        "last_name": "Shaheen",
        "icon": "/uploads/users/2.jpg",
        "phone": "+79026121473",
        "organizations": [
            {
                "name": "Flexsites",
                "description": "Создание и продвижение сайтов в Челябинске"
            },
            {
                "name": "ЮУрГУ",
                "description": "Южноуральский государственный университет"
            }
        ]
    },
    
]
```

## `GET` users/int:id/

Метод возврощается пользователя с идентификатором id

```json
{
    "email": "mul@gmail.com",
    "password": "pbkdf2_sha256$390000$RPDc7lqpSIUAJEjUrJ2l0k$ht9bZGpIqAEuAbYy0duIclhPjdC73KX/GWi1dxbpMEE=",
    "first_name": "Мулхам",
    "last_name": "Shaheen",
    "icon": "/uploads/users/2.jpg",
    "phone": "+79026121473",
    "organizations": [
        {
            "name": "Flexsites",
            "description": "Создание и продвижение сайтов в Челябинске"
        },
        {
            "name": "ЮУрГУ",
            "description": "Южноуральский государственный университет"
        }
    ]
}
```

## `POST` organization/create/

Метод создания организации

```json
{
    "name": "test",
    "description":"12sa dasdasd asd "
}
```

Возвращает модель новой орнагизации

```json
{
    "name": "test",
    "description":"12sa dasdasd asd "
}
```

## `GET` organization/all/

Метод возврощается список всех пользователей

```json
[
    {
        "name": "Flexsites",
        "description": "Создание и продвижение сайтов в Челябинске",
        "users": [
            {
                "email": "mul@gmail.com",
                "first_name": "Мулхам",
                "last_name": "Shaheen"
            }
        ]
    },
    {
        "name": "ЮУрГУ",
        "description": "Южноуральский государственный университет",
        "users": [
            {
                "email": "mul@gmail.com",
                "first_name": "Мулхам",
                "last_name": "Shaheen"
            }
        ]
    },
    {
        "name": "ООО Тестовое",
        "description": "Общество с ограниченной ответственностью для тестирования метода API",
        "users": []
    },
    {
        "name": "test",
        "description": "12sa dasdasd asd",
        "users": []
    }
]
```