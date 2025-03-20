# Book API with JWT Authentication

A Django REST API for managing books and publishers with JWT authentication.

## Setup Instructions

## 1. Clone the repository
2. Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

## 3. Install dependencies
pip install -r requirements.txt

## 4. Run migrations
python manage.py makemigrations 
python manage.py migrate

## 5. Create superuser (admin)
python manage.py createsuperuser

## 6. Run the development server
python manage.py runserver

## 7. API endpoints will be available at http://127.0.0.1:8000/api/

## API Endpoints

### Authentication
- Register: POST /api/register/
- Login: POST /api/login/
- Refresh Token: POST /api/token/refresh/

### Books
- It will show all the books:                     GET /api/books/
- Used to creating new book:                      POST /api/books/
- This is for get book details by providing 'id': GET /api/books/<id>/
- To update the book:                             PUT /api/books/<id>/
- to delete the book:                             DELETE /api/books/<id>/

### Publishers
- It will show all the publishers:             GET /api/publishers/
- Used to creating new publisher:              POST /api/publishers/
- This is for get publisher by providing 'id': GET /api/publishers/<id>/
- To update the publisher:                     PUT /api/publishers/<id>/
- To delete the publisher:                     DELETE /api/publishers/<id>/

## Usage Examples

### User Registration

POST /api/register/
{
"username": "arvind",
"email": "arvindarya@gmail.com",
"password": "zsxdzsxd"
}

### User Login
POST /api/login/
{
"username": "arvind",
"password": "zsxdzsxd"
}

### Creating a Publisher
<-----------------------------I HAVE CERATED ONE ENTRY IN PUBLISHERS TABLE USIGN POSTMAN----------------->
POST /api/publishers/
Authorization: Bearer <your_jwt_token>
{
"name": "arvind",
"address": "aryabhatta research institute of observational sciences"
}


### Creating a Book

I HAVE CREATED TWO RECORDS FOR PUBLISHER 'ARVIND'

POST /api/books/

<---------------------------------FIRST ENTRY USING POSTMAN----------------------->
Authorization: Bearer <your_jwt_token>
{
"title": "life of pie",
"author": "arvind",
"isbn": "8909876567",
"publication_date": "2003-12-02",
"publisher": 1
}
<---------------------------------SECOND ENTRY POSTMAN------------------------>
Authorization: Bearer <your_jwt_token>
{
"title": "jungle book",
"author": "arvind",
"isbn": "123456789",
"publication_date": "2002-12-02",
"publisher": 1
}

