#!/bin/bash

# Ruta al archivo .kjb
job_file_path="/home/config/Proyecto-Dockerizado-con-ETL-Oracle-y-PostgreSQL/DATA_INTEGRATION_REQ/PENTAHO/Job 1.kjb"

# Ejecutar el comando de Kitchen en Linux
/home/config/Proyecto-Dockerizado-con-ETL-Oracle-y-PostgreSQL/data-integration/kitchen.sh -file="$job_file_path"
