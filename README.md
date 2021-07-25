# CLOUDSEK API TASK
## Calculate 2 number sum api using django python
---
## Build and preview the api locally

### Solution #1
On your local machine, clone this repo:

```bash
git clone https://github.com/Abhishekkumar02/Rest_api.git
cd Rest_api
```
Then build and run the documentation with [Docker Compose](https://docs.docker.com/compose/)

```bash
docker-compose build
docker-compose up
```
> If you don't have Docker Compose installed, [follow these installation instructions](https://docs.docker.com/compose/install/).

Once the container is built and running, visit [http://localhost:8000](http://localhost:8000)

To stop the staging container, use the `docker-compose down` command:

```bash
docker-compose down
```

To access the database, use the `docker-compose exec` command:

```bash
docker ps
sudo docker exec -it MYSQL-CONTAINER-ID mysql -u root -p
```

### Solution #2

* Clone the repository
	> git clone https://github.com/Abhishekkumar02/Rest_api.git
	>
	> cd Rest_api

* Make virtual environment (optional)
	* linux
		> sudo apt install python3-venv
		>
		> python3 -m venv my-project-env
		>
		> source my-project-env/bin/activate
	* Windows
		> pip install virtualenv
		>
		> virtualenv my-project-env
		>
		> my-project-env/Script/activate
	
  
* Run requirements.txt file
  ```bash
   pip install -r requirements.txt
  ```
* Start Mysql and create database using the following command
  ```bash
   mysql -u root -p
   create database Calculate_Sum;
   use Calculate_Sum;
   exit;
  ```
* To run the project goto the project dir (Rest_api) and run the following command
    ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     python3 manage.py runserver
    ```
   Once the server is start and running, visit [http://localhost:8000](http://localhost:8000)
