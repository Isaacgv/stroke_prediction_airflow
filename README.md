


# Table of contents
* [Technologies](#technologies)
* [Airflow](#airflow)
* [great_expectation - Init](#greatexpectation-init)
* [great_expectation Docs](#greatexpectation-docs)

# Technologies
Project is created with:
* Airflow: 2.3.0
* great-expectations: 0.15.8
* Flask: 2.1.2
* Docker

# Airflow
## Initial configuration 
### Build image - init
    sudo docker build . --tag stroke-airflow_v2 --no-cache
### Airflow Configuration - init
    mkdir -p ./dags ./logs ./plugins ./input_data ./output_data
### Permissions to folders - init
    sudo echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

## Start Airflow
    sudo docker-compose up
## Acess Airflow

http://localhost:8080/

- username: airflow
- password: airflow

## Airflow API
    curl --X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags"
## kill containers
    sudo docker kill $(sudo docker ps -q)


# great_expectation-Init
## Create a folder project great_expectations
    great_expectations init

## Dataset connection
    great_expectations datasource new

## create Expectation
    great_expectations suite new

## Create a new checkpoint
    great_expectations checkpoint new getting_started_checkpoint


# great_expectation-Docs

## Install requiremnets - init
    pip3 install -r requirements.txt
## Start app
    python3 docs_quality

## Documentation Acess
http://localhost:8050