# Сервис по отслеживанию местоположений

Django REST API сокращает ссылки и предоставляет к ним доступ, а так же дает возможность удаления и изменения.
Ссылки хранятся в БД. БД может быть абсолютно любой, SQL/NoSQL(В тестовом варианте SQLite).

## Стэк:
Django
Python 

## Предполагаемая структура данных

```jsx
// ShortUrl - ссылки хранятся в БД
{
	id: 
	url: String
	short_url: String
	create_at: Date
}
```
### GET /api/url/
```jsx
// Ответ
{
"Short_URL": [
	{
		"id": 2,
		"url": "https://proglib.io/",
		"short_url": "07ffd0b83b",
		"create_at": "2021-05-19"
	},
	{
		"id": 3,
		"url": "http://instagram.com/maxshukletsov",
		"short_url": "633b16b830",
		"create_at": "2021-05-19"
	}
	],
}
```
### POST /api/url/
```jsx
// Тело запроса
{
"Short_URL": [
    	{
		"url": "https://github.com/maxshukletsov/ShortURL"
		}
  	]
}
// Ответ, если нет такой ссылки
{
"success": "Url d76d7e6970 created successfully"
}
// Ответ, если такая ссылка имеется
{
"error": "Url d76d7e6970 already exist"
}
```
### PUT /api/url/
```jsx
// Тело запроса
{
"Short_URL":[
    {
		"url": "https://github.com/maxshukletsov/ShortURL",
      	"short_url": "d76d7e6970"
	}
  ]
}
// Ответ
{
"success": "Url 'd76d7e6970' updated successfully"
}
```
### DELETE /api/url/
```jsx
// Тело запроса
{
"Short_URL":[
    {
      	"short_url": "d76d7e6970"
	}
  ]
}
// Ответ
{
"success": "Url https://github.com/maxshukletsov/ShortURL created delete"
}
```
## GET /api/633b16b830
При GET запросе происходит редирект на полный URL
