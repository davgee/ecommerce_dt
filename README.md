# ecommerce_dt
The service is implemented in Flask. It uses postgres database (which is run with docker-compose).

Running instructions:
1. Install python3.6
1. Install all python packages by running `pip install -r requirements.txt`
1. Run database container with `docker-compose up`
1. Run database migration with `make migrate_db`
1. Run service with `make run`
