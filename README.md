

# Build image
sudo docker build . --tag stroke-airflow:2.3.0

# Airflow Configuration

mkdir -p ./dags ./logs ./plugins ./input_data ./output_data

## permissions to folders
sudo echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

## Init airflow
docker-compose up

localhos:8080

http://localhost:8080/
username:airflow
password:airflow

## Airflow API
curl --X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags"