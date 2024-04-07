FROM python:3.9-slim-buster as base
# Install poetry
RUN pip install poetry
WORKDIR /opt
# Expose the port that we want the host to listen to
EXPOSE 3000
# Copy across the project files
COPY . /opt

#--- DEV STEPS ----

FROM base as development
ENV FLASK_ENV=development
# Install the project dependencies
RUN poetry install
# Set the script to run as development on startup of the container
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=8000"]

#--- PROD STEPS ----

FROM base as production
# Install the project dependencies
RUN poetry install
# Set the script to run as production on startup of the container

ENTRYPOINT ["poetry","run","gunicorn","-w","4","-b","0.0.0.0:3000","todo_app.wsgi:app"]

#--- TEST STEPS ----
FROM base as test

# poetry install
RUN poetry install

# copy across tests 
COPY ./tests ./tests

# Define entrypoint 
ENTRYPOINT ["poetry", "run", "pytest", "-v"]