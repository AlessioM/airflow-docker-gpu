# setup

## start postgres
`docker-compose up -d postgres_airflow`

## init db and add user
`docker-compose run airflow_init`

## run webserver
`docker-compose up -d airflow_webserver`

## run scheduler
`docker-compose up  airflow_scheduler`


# running
* web server is exposed on port 9090
* login admin/airflow
* dag_id is `gpu_docker_dag`
* task logs can be found in `./logs`

# reproduce
* run dag `gpu_docker_dag`
* task `no_gpu` fails, `with_gpu` succeeds
