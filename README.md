# Weather Forecast REST API

## Description

This app fetches weather forecasts from OpenWeather API and manages them in SQLite Database.

## Features:

- JWT Authentication
- Interaction with OpenWeather Current Weather Data JSON API
- SQLite Database Management

## How to run

Use the link: ()[]

Or...

1. Clone repo:

```shell
git clone https://github.com/itelman/pradavan-rest.git
```

2. Open repo:

```shell
cd pradavan-rest
```

3. Run the repo:

```shell
fastapi dev main.py
```

## How to use:

1. Register through "/signup" endpoint (see 'Endpoints' section)
2. Authenticate through "/login" endpoint
3. Copy the access token from the JSON response
4. For all next requests, set in headers -> ["Authorization": "Bearer {your_access_token}"]
5. Enjoy!

## Endpoints

### Service: Users

- **Endpoint: /signup**:
    - Method: POST
    - Type: JSON
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
    - Response:
  ```json
  {
    "message": "OK"
  }
  ```
    - Errors: 409, 422

- **Endpoint: /login**:
    - Method: POST
    - Type: JSON
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
    - Response:
  ```json
  {
    "message": "OK",
    "access_token": "string", 
    "token_type": "bearer"
  }
  ```
    - Errors: 401

### Service: Forecasts

- **Endpoint: /user/forecasts/create?city={city_name}**:
    - Method: GET
    - Response:
  ```json
  {
    "message": "OK", 
    "forecast_id": "int"
  }
  ```

- **Endpoint: /user/forecasts/{id}**:
    - Method: GET
    - Response (200 OK):
  ```json
   {
     "id": "int",
     "city": "string",
     "temp": "float",
     "pressure": "int",
     "humidity": "int",
     "description": "string"
   }
  ```

- **Endpoint: /user/forecasts**:
    - Method: GET
    - Response (200 OK):
  ```json
  [
    {
     "id": "int",
     "city": "string",
     "temp": "float",
     "pressure": "int",
     "humidity": "int",
     "description": "string"
   },
  {
     "id": "int",
     "city": "string",
     "temp": "float",
     "pressure": "int",
     "humidity": "int",
     "description": "string"
   },
    ...
  ]
  ```

- **Endpoint: /user/forecasts/{id}**:
    - Method: DELETE
    - Response:
  ```json
  {
    "message": "OK"
  }
  ```

- **Endpoint: /user/forecasts/{id}**:
    - Method: PUT
    - Response:
  ```json
  {
    "message": "OK"
  }
  ```

## Errors

- **401 (Unauthorized) / 403 (Forbidden) / 409 (Conflict) / 422 (Unprocessable Entity)**:
  ```json
  {
    "message": "string",
    "details": "string" or dict{},
    "request": dict{} or null
  }
  ```

- **404 (Not Found) / 405 (Method Not Allowed)**:
  ```json
  {
    "detail": "string"
  }
  ```

- **500 (Internal Server)**:
  ```json
  {
    "message": "string",
    "details": "string"
  }
  ```