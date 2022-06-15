

# Build image
sudo docker build . --tag stroke-airflow_v2 --no-cache

# Airflow Configuration

mkdir -p ./dags ./logs ./plugins ./input_data ./output_data

## permissions to folders
sudo echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

## Init airflow
sudo docker-compose up

localhos:8080

http://localhost:8080/
username:airflow
password:airflow

## Airflow API
curl --X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags"

## kill containers
sudo docker kill $(sudo docker ps -q)


#Great Expectation

#Create a folder project great_expectations
great_expectations init

#Dataset connection
great_expectations datasource new

#create Expectation
great_expectations suite new

#Create a new checkpoint
great_expectations checkpoint new getting_started_checkpoint

file_name (str)
run_name (str)
run _time (time_date)
success_percent (int)
link (str)
alert(bool)