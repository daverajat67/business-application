# Django Business Management Application

A simple Django application for managing business information, including business name, address, owner information, and employee size.

## Features

- Create, Read, Update, and Delete (CRUD) operations for businesses.
- API endpoints for interacting with the application.
- Dockerfile for containerized deployment.
- CRUD Operations can be done by 3 ways in the project.
    - with REST APIs
    - with Django admin panel
    - with UI integrated in Django

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x)
- Django
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository or unzip the folder:


2. Create a virtual environment:
- Install virtualenv:
  ```
  pip install virtualenv
  ```
- Create a virtual environment:
  ```
  virtualenv venv
  ```

3. Activate the virtual environment:
   ```
  source venv/bin/activate
  ```

4. Install project dependencies:
    ```
    pip install -r requirements.txt
    ```

### Deployment (Docker)

1. Build the Docker image:
    ```
    docker build -t your-image-name .
    ```

2. Run the Docker container:
    ```
    docker run -p 8000:8000 your-image-name
    ```


### API Endpoints

#### REST APIs

- List businesses: [http://127.0.0.1:8000/api/businesses](http://127.0.0.1:8000/api/businesses)
- Create a business: POST to [http://127.0.0.1:8000/api/businesses](http://127.0.0.1:8000/api/businesses)
- Get a business: GET to [http://127.0.0.1:8000/api/businesses/business_id](http://127.0.0.1:8000/api/businesses/business_id)
- Update a business (PUT or PATCH): [http://127.0.0.1:8000/api/businesses/business_id](http://127.0.0.1:8000/api/businesses/business_id)
- Delete a business: [http://127.0.0.1:8000/api/businesses/business_id](http://127.0.0.1:8000/api/businesses/business_id)

#### Admin Panel

- Access the Django admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- Username: admin
- Password: admin

#### Local UI with Django Server

- Access the local UI with the Django server: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Testing

- For testing with pytest:

1. Navigate to the project directory:
    ```
    cd project
    ```


2. Install required packages:
    ```
    pip install -r requirements.txt
    ```

3. Run the tests using pytest:
   ``` 
    pytest app/tests
    ```
4. Generate the report using pytest
    ```
    pytest --cov=app
    ```
- For testing with Django's default test framework:

1. Navigate to the project directory:
    ```
    cd project
    ```
2. Run the tests using Django's test command:

    ```
    python manage.py test
    ```

### Deployment (Cloud aws)

## on aws side you should have ecs, ecr and cluster

- create the repository in aws ecr
  - deploye docker image in repository use tag latest

  - example commands to deployee image. you can found commands related to your repository in push commands option.
     
    1. ```aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 550513526501.dkr.ecr.ap-south-1.  amazonaws.com
        ```

    2.  ```
        docker build -t reponame .
        ```

    3.  ```
        docker tag reponame:latest 550513526501.dkr.ecr.ap-south-1.amazonaws.com/reponame:latest
        ``` 

    4. ```
        docker push 550513526501.dkr.ecr.ap-south-1.amazonaws.com/reponame:latest
        ```

- create the task defination use url of docker image from repository
  - select role accordingly

- create the cluster in ecs choose fargate machine
    - create the service.
        - select task defination that has created in task defination

- we can use the public ip of service task to access the application
