FROM apache/airflow:2.3.0

COPY requirements_container.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip3 install -r requirements.txt

USER root
RUN sudo echo "Europe/Paris" > /etc/timezone
RUN sudo dpkg-reconfigure -f noninteractive tzdata
