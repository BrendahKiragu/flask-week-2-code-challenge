# Late Show API
This is an API built with Flask and SQLAlchemy to manage episodes, guests, and their appearances. It provides endpoints for retrieving all episodes, all guests and an individual episode information, as well as creating a new appearance with the existing episode and guest instances.

# Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Models](#models)
4. [Routes](#routes)
5. [Running the Endpoints](#running-the-endpoints)
6. [Conclusion](#conclusion)

## Requirements
- This project requires Python version 3.8 or later.

## Installation
To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone git@github.com:BrendahKiragu/flask-week-2-code-challenge.git
    cd flask-week-2-code-challenge/
    ```
2. Install the required dependencies and enter a virtual environment for this project:
    ```bash
    pipenv install 
    pipenv shell
    ```
3. The database has already been set up. In case it is missing run the following command to upgrade the migration:
    ```bash
      flask db upgrade
    ```
4. packages installation: You will need to install the following packages using pip
    ```bash
    pip install flask flask_migrate flask_restful sqlalchemy_serializer faker
    ```

4. Seed the Database. To populate the database with test data, run the following command:
    ```bash
    python seed.py
    ```  

5. Start the API
- To start the API, set the necessary environment variables and then run the application with the following commands:
     ```bash
     export FLASK_APP=app.py
     export FLASK_RUN_PORT=5555
     flask run
     ```
- Your app will run on port:5555
    ```arduino
    http://127.0.0.1:5555


## Models
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

## Routes
- You can use either of the following to test the endpoints: [Postman](https://postman.com), [Insomnia](https://insomnia.rest), or [Thunder Client](https://www.thunderclient.com)
- Make sure the server is running for the endpoints to work `flask run`

### a. GET /episodes
- http://127.0.0.1:5555/episodes Returns a list of all episodes in the following format:
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
- http://127.0.0.1:5555/episodes/2 Returns details of a specific episode, including the guest appearances. Example response:
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
- http://127.0.0.1:5555/guests Returns a list of all guests:
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
- http://127.0.0.1:5555/appearances Creates a new appearance for a guest on an episode. To test the 'POST' request on this endpoint, use this example request body:
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

## Running the Endpoints
You run the endpoints on the terminal with `curl` interact with the API in case you cannot access the suggested tools:[Postman](https://postman.com), [Insomnia](https://insomnia.rest), or [Thunder Client](https://www.thunderclient.com)

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
- Example for GET all guests:
    ```bash
    curl http://127.0.0.1:5555/guests
    ```  

## Conclusion
Thank you for exploring this API! We hope this guide has helped you set up and test the application smoothly. If you have any questions or encounter any issues, feel free to reach out [MyGithub](https://github.com/BrendahKiragu) or check the documentation for further assistance. Happy coding!
