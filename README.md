# tic-tac-toe
## Violeta Álvarez Areces
Fullstack (React + Python) technical test

## Run the app in local environment

To create the docker images and run the containers:

```bash
docker-compose up -d --build
```
Access the game at http://localhost:5173

## 1. Web service
- Python 12 and Flask.
- Clean architecture
- Sqlite for DB persistence:
    - A relational database was chosen due to the structured nature of the data and its clear relations, enforcing data integrity. The database model is shown below.
    - SQLite was selected for the sake of simplicity. 
    - TODO: *add indexes to improve performance*
- Python's standard library logging module, that uses stderr stream output.
- Dockerization 
- TO DO: 
    - *Implement tests in both client and API (unit, integration, end to end testing). Only manual testing has been performed at this point.*
    - *Implement better error handling: manage exceptions and define descriptive error messages.*


### API documentation

The API is exposed at http://localhost:5000

New swagger: [tictactoe.yml](documentation/tictactoe.yaml)

To visualize API's operations and schemas, you may copy and paste YAML file in https://editor-next.swagger.io/

To test the API, you may import [collection.json](documentation/thunder-collection_tictactoe.json) into your preferred client, for example VS Thunder client extension. 

### Database model as defined in Flask application

#### Table `match` 
| Columna         | Tipo         | Propiedades                              |
|-----------------|--------------|------------------------------------------|
| `id`            | `Integer`    | `primary_key=True`, `autoincrement=True` |
| `current_player`| `String(1)`  |                                          |
| `state`         | `String(20)` |                                          |
| `board`         | `String(250)`|                                          |

#### Tabla `movement`
| Columna        | Tipo         | Propiedades                                |
|----------------|--------------|--------------------------------------------|
| `id`           | `Integer`    | `primary_key=True`, `autoincrement=True`   |
| `match_id`     | `Integer`    | `ForeignKey("match.id")`, `nullable=False` |
| `player`       | `String(1)`  | `nullable=False`                           |
| `x_square`     | `Integer`    | `nullable=False`                           |
| `y_square`     | `Integer`    | `nullable=False`                           |
| `created_at`   | `DateTime`   | `default=datetime.now`                     |


## 2. User management service design

#### Request: Design a new user management system
The system will be responsible for registering new users, managing access to the game and keeping track of users' matches. 

As the requirement states, a basic authentication based on username and password credentials is proposed.

#### API modifications: 
Two new endpoints wil be created:
  - POST /signup to register a new user
  - POST /login to authenticate user


New swagger: [tictactoe-with-auth.yml](documentation/tictactoe-with-auth.ym.yaml)

To visualize API's operations and schemas, you may copy and paste YAML file in https://editor-next.swagger.io/

*TO DO: define and document error responses*

    
#### Data model modifications:

Create new table `user`:
| Columna         | Tipo         | Propiedades                              |
|-----------------|--------------|------------------------------------------|
| `id`            | `Integer`    | `primary_key=True`, `autoincrement=True` |
| `email         `| `String(50)` |                                          |
| `password`      | `String(20)` |                                          |
| `created_at`    | `Datetime`   |                                          |
| `updated_at`    | `Datetime`   |                                          |


Modify table `match` to add new column `user_id` as a foreign key to `user` table
| Columna         | Tipo         | Propiedades                               |
|-----------------|--------------|------------------------------------------ |
| `id`            | `Integer`    | `primary_key=True`, `autoincrement=True`  |
| `current_player`| `String(1)`  |                                           |
| `state`         | `String(20)` |                                           |
| `board`         | `String(250)`|                                           |
| `user_id`       | `Integer`    | `ForeignKey("user.id")`, `nullable=False` |


#### Architectural design changes:

Some of the adaptations needed for the use of HTTP Basic Auth in the client and API:
  - Implement middleware in the Flask web service, responsible for cheking username and password against the database.
  - When registerimg a new user, hash password before storing it in the database.
  - Encode username and password in the request headers.
  - Add forms in React app for sign-up and login.

## 3. React client
- React 18 and TypeScript
- CSS, responsive design.
- Dockerization 
- *TO DO: implement tests in both client and API (unit, integration, end to end testing). Only manual testing has been performed at this point.*


