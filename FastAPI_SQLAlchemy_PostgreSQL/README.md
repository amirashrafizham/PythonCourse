# How to run this project
uvicorn main:app --reload

# Code Structure 
MVC Structure 

main.py :  Controllers
crud.py : Services
schemas.py : Data Transfer Objects
models.py : Models and DB Table Configuration
config.py : DB Connection Configuration 

# Building this project
The flow of building this project is as follows:
1. Configure the database connection (config.py)
2. Configure the models (models.py)
3. Configure the dtos (schemas.py)
4. Configure the crud services (crud.py)
5. Configure the controller (main.py)

# Setting up PostgreSQL
1. Provision a PostgreSQL server in Azure
2. Open PGAdmin and create a new database
3. Configure the database connection in config.py