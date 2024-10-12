# Late Show API
This is an API built with Flask and SQLAlchemy to manage episodes, guests, and their appearances. It provides endpoints for retrieving episode and guest information, as well as creating and validating guest appearances in episodes.


# Table of Contents
1.
2. 
3.


# Validations
Add validations to the `Appearance` model:

- must have a `rating` between 1 and 5 (inclusive - 1 and 5 are okay)

# Routes
### a. GET /episodes
- Returns JSON data in the format below:
    ```json
    [
      {
        "date": "2013-05-12",
        "id": 1,
        "number": 13
      },
      {
        "date": "2011-08-25",
        "id": 2,
        "number": 90
      },
    ]
    ```

### b. GET /episodes/:id
- If the `Episode` exists, returns JSON data in the format below:  
    ```json
    {
      "appearances": [
        {
          "episode_id": 2,
          "guest": {
            "id": 4,
            "name": "Jason Tran",
            "occupation": "Textile designer"
          },
          "guest_id": 4,
          "id": 2,
          "rating": 2
        }
      ],
      "date": "2011-08-25",
      "id": 2,
      "number": 90
    }
    ```
- If the `Episode` does not exist, returns the following JSON data, and a 404 status code.
    ```json
    {
      "error": "Episode not found"
    }
    ```

### c. GET /guests
- Return JSON data in the format below:
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
- This route should create a new `Appearance` that is associated with an existing `Episode` and `Guest`. It should accept an object with the following properties in the body of the request:
    ```json
    {
      "rating": 5,
      "episode_id": 100,
      "guest_id": 123
    }
    ```

- If the `Appearance` is created successfully, send back a response with the following data:
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

- If the `Appearance` is **not** created successfully, return the following JSON data, along with the appropriate HTTP status code:
    ```json
    {
      "errors": ["validation errors"]
    }
    ```
