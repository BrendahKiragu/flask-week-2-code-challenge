# Late Show API
This is an API built with Flask and SQLAlchemy to manage episodes, guests, and their appearances. It provides endpoints for retrieving episode and guest information, as well as creating and validating guest appearances in episodes.

# Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Requirements](#requirements)
4. [Models](#models)
5. [Routes in app.py](#routes-in-app.py)
6. [Running the Endpoints](#running-the-endpoints)

## 1. Overview
The Late Show API is designed to manage episodes, guests, and their appearances on the show. It supports creating new appearances and retrieving information on episodes and guests through various endpoints.

## 2. Installation
To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/late-show-api.git
    cd late-show-api
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the database:
    ```bash
    flask db upgrade
    ```
4. Run the application:
    ```bash
    flask run
    ```

## 3. Requirements
This project requires Python version 3.8 or later.

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful

## 4. Models
### a. Episode
Represents an episode of the show, with the following fields:
- `id` (Integer, primary key)
- `date` (String, representing the date of the episode)
- `number` (Integer, the episode number)

### b. Guest
Represents a guest on the show, with the following fields:
- `id` (Integer, primary key)
- `name` (String, name of the guest)
- `occupation` (String, occupation of the guest)

### c. Appearance
Represents a guest's appearance on an episode, with the following fields:
- `id` (Integer, primary key)
- `rating` (Integer, rating of the guest's appearance, must be between 1 and 5)
- `episode_id` (ForeignKey, referencing the `Episode` model)
- `guest_id` (ForeignKey, referencing the `Guest` model)

## 5. Routes in app.py
### a. GET /episodes
- Returns a list of all episodes in the following format:
    ```json
    [
      {
        "id": 1,
        "date": "2013-05-12",
        "number": 13
      },
      {
        "id": 2,
        "date": "2011-08-25",
        "number": 90
      }
    ]
    ```

### b. GET /episodes/:id
- Returns details of a specific episode, including the guest appearances. Example response:
    ```json
    {
      "id": 2,
      "date": "2011-08-25",
      "number": 90,
      "appearances": [
        {
          "id": 2,
          "rating": 2,
          "episode_id": 2,
          "guest_id": 4,
          "guest": {
            "id": 4,
            "name": "Jason Tran",
            "occupation": "Textile designer"
          }
        }
      ]
    }
    ```

### c. GET /guests
- Returns a list of all guests:
    ```json
    [
      {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      {
        "id": 2,
        "name": "Sandra Bernhard",
        "occupation": "Comedian"
      },
      {
        "id": 3,
        "name": "Tracey Ullman",
        "occupation": "television actress"
      }
    ]
    ```

### d. POST /appearances
- Creates a new appearance for a guest on an episode. Example request body:
    ```json
    {
      "rating": 5,
      "episode_id": 100,
      "guest_id": 123
    }
    ```

- If created successfully, the response will be:
    ```json
    {
      "id": 162,
      "rating": 5,
      "guest_id": 3,
      "episode_id": 2,
      "episode": {
        "date": "1/12/99",
        "id": 2,
        "number": 2
      },
      "guest": {
        "id": 3,
        "name": "Tracey Ullman",
        "occupation": "television actress"
      }
    }
    ```

- If there are validation errors, the response will include an error message:
    ```json
    {
      "errors": ["validation errors"]
    }
    ```

## 6. Running the Endpoints
To run the endpoints locally, you can use tools like [Postman](https://www.postman.com/) or `curl` to interact with the API:

- Example request to get all episodes:
    ```bash
    curl http://127.0.0.1:5555/episodes
    ```

- Example request to create an appearance:
    ```bash
    curl -X POST http://127.0.0.1:5555/appearances \
    -H "Content-Type: application/json" \
    -d '{"rating":5, "episode_id":1, "guest_id":1}'
    ```
