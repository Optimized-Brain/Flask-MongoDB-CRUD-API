# Flask MongoDB CRUD API

A simple RESTful API built with Flask and MongoDB, supporting basic CRUD operations easily deployable with docker

## 🛠️ Tech Stack

- Python 3.x
- Flask
- MongoDB
- Flask-PyMongo
- Docker

## Prerequisites
- [Docker](https://www.docker.com/get-started/)
- [Python 3.x](https://www.python.org/downloads/) and [MongoDB](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-8.0.10-signed.msi) (Optional for running it locally)

---

## Installation & Running

### with Docker
1. Clone the repo

```powershell
git clone https://github.com/Optimized-Brain/Flask-MongoDB-CRUD-API.git
cd Flask-MongoDB-CRUD-API
```
By default, the app reads MONGO_URI from environment. In docker-compose.yml, it’s set to mongodb://mongo:27017/Users.

2. Start services
```powershell
docker-compose up --build
```
### Without Docker

1. Create and activate a virtualenv:

```
python3 -m venv venv
source venv/bin/activate
```
2. Install required dependencies.
```
pip install -r requirements.txt
```
3. Create and Connect local server of MongoDB.
4. Configure MONGO_URI in app.py accordingly.
5. Run app.py
```
python app.py
```
---

## API Reference
| Method | Endpoint      | Description                     | Required Parameters                                        |
| ------ | ------------- | ------------------------------- | ---------------------------------------------------------- |
| POST   | `/users`      | Create a new user               | `name`, `email`, `password` *(in JSON)*                    |
| GET    | `/users`      | Get a list of all users         | *None*                                                     |
| GET    | `/users/<id>` | Retrieve a single user by `_id` | `id` (MongoDB ObjectId in URL)                             |
| PUT    | `/users/<id>` | Update an existing user         | `id` (in URL), `name/email/password` *(in JSON)* |
| DELETE | `/users/<id>` | Delete a user by `_id`          | `id` (MongoDB ObjectId in URL)                             |


