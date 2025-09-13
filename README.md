# recipe-api

# Virtual Environment
python3 -m venv mypy_env
source mypy_env/bin/activate

# https://mypy.readthedocs.io/en/stable/running_mypy.html
pip install mypy

# Build Docker
sudo docker build .

# Run Docker
sudo docker compose up

# flake 8 linting
sudo docker-compose run --rm app sh -c "flake8" 

# tests
sudo docker-compose run --rm app sh -c "python manage.py test" 

# install Django
sudo docker-compose run --rm app sh -c "django-admin startproject app ." 

# new app
sudo docker-compose run --rm app sh -c "python manage.py startapp core" 

# test the custom wait_for_db Django command to check DB availalbe or not
 sudo docker-compose run --rm app sh -c "python manage.py wait_for_db"
 