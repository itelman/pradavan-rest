# Weather Forecast REST API

## Description

This app fetches weather forecasts from OpenWeather API and manages them in SQLite Database.

## Features:

- JWT Authentication
- Interaction with OpenWeather Current Weather Data JSON API
- SQLite Database Management

## How to run

Use the link: [https://pradavan-rest.onrender.com](https://pradavan-rest.onrender.com)

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

1. Register through **/signup** endpoint (see 'Endpoints' section)
2. Authenticate through **/login** endpoint
3. Copy the access token from the JSON response
4. For all next requests, set in headers -> **{"Authorization": "Bearer {your_access_token}"}**
5. Enjoy!

## Endpoints

### Service: Users

- **Endpoint: /ping --> TEST API CONNECTION**:
    - Method: GET
    - Request: None
    - Response:
  ```json
  {
    "message": "OK",
    "test_response": dict{},
    "authenticated_user": dict{}
  }
  ```

- **Endpoint: /signup --> REGISTER USER**:
    - Method: POST
    - Type: JSON
    - Request:
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

- **Endpoint: /login --> LOGIN USER**:
    - Method: POST
    - Type: JSON
    - Request:
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
    - Errors: 401, 422

### Service: Forecasts

- **Endpoint: /user/forecasts/create?city={city_name} --> CREATE FORECAST**:
    - Method: GET
    - Request: None
    - Response:
  ```json
  {
    "message": "OK", 
    "forecast_id": "int"
  }
  ```

- **Endpoint: /user/forecasts/{id} --> GET FORECAST**:
    - Method: GET
    - Request: None
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

- **Endpoint: /user/forecasts --> GET ALL FORECASTS**:
    - Method: GET
    - Request: None
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

- **Endpoint: /user/forecasts/{id} --> DELETE FORECAST**:
    - Method: DELETE
    - Request: None
    - Response:
  ```json
  {
    "message": "OK"
  }
  ```

- **Endpoint: /user/forecasts/{id} --> UPDATE FORECAST MANUALLY**:
    - Method: PUT
    - Type: JSON
    - Request:
  ```json
   {
     "temp": "float",
     "pressure": "int",
     "humidity": "int",
     "description": "string"
   }
  ```
    - Response:
  ```json
  {
    "message": "OK"
  }
  ```

- **Endpoint: /user/forecasts/api/{id} --> UPDATE FORECAST THROUGH API**:
    - Method: PUT
    - Request: None
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