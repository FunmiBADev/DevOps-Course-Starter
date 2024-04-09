# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

# Getting started with the Project

For universal access to our To Do items - we will be saving our Items in Trello using REST API calls. To get started:

1. Register for a if you do not have one already [Trello account](https://trello.com/signup)

2. Generate an API Key and Token [here](https://trello.com/app-key)

3. Add Handy PowerUp App [API Developer ID Helper](https://trello.com/power-ups) to help with extracting board and List IDs.

4. Save these credentials and IDs by updating the`.env` file from exercise 1:

   ```
   # Trello Api Management
   TRELLO_API_KEY=<FILL ME>
   TRELLO_TOKEN=<FILL ME>
   BOARD_ID=<FILL ME>
   TRELLO_DONE=<FILL ME>
   TRELLO_IN_PROGRESS=<FILL ME>
   TRELLO_TO_DO=<FILL ME>
   BASE_URL='https://api.trello.com/1/'

   ```

5. The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install the newly added `requests` packages, run the following from your preferred shell:

```bash
$ poetry install
```

6. Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:

```bash
$ poetry run flask run
```

# Running project test

To run the test in the project - at the root folder run the following command:

```bash
$ poetry run pytest
```

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:

```bash
$ poetry run flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

# Controller Node - Host management using Ansible

1. Install Ansible by running:

```bash
$ brew install ansible
```

Or Use pip install

```bash
$ pip install ansible
```

2. Ensure ansible installation is successfull by running

```bash
$ ansible --version
```

3. In VS Code install the following extension -> Remote - SSH for convinently managing ssh connections and files

4. Have availalble your controller and managed nodes IP and Passwords

5. In VS code with Remote - SSH extention now installed:

   - click on the Remote Explorer icon
   - on the SSH tab click on the '+' icon to connect to the Controller Node:
     - enter: ssh ec2-user@<controller-ip-address>
     - then enter password

6. Once connected to the Controller Node run the following command then enter password when prompted:

```bash
$ ssh-keygen
```

7. Then run the following command:

```bash
$ ssh-copy-id ec2-user@<controller-ip-address>
```

8. To grant the Controller Node Permission to read and write to the Managed hosts, do the following from the controller node terminal for each individual host you have:

   - enter: ssh ec2-user@<host-ip-address>
   - then enter password
   - finally ssh-copy-id ec2-user@<host-ip-address>

9. With the necessary permissions granted in the Remote File explorer if the Ansible folder is mssing you can at the stage copy and paste the ansible folder from the code base as well as the .env.js file to the controller node.

10. to test connection from the controller node to the managed hosts run the following command:

```bash
$ ansible webservers -i  inventory.ini -m ping
```

A sucessful connection should return the following

```bash
[WARNING]: Platform linux on host 18.170.243.22 is using the discovered Python interpreter at /usr/bin/python3.9, but future installation of another Python interpreter could change the meaning
of that path. See https://docs.ansible.com/ansible-core/2.15/reference_appendices/interpreter_discovery.html for more information.
18.170.243.22 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "changed": false,
    "ping": "pong"
}
```

11. With connection successfully tested - run the the following ansible command to excute all task in the playbook:

```bash
$ ansible-playbook todoapp-playbook.yml -i inventory.ini
```

# Run Todo App in Docker container in Dev and Prod Environments

1. To make sure the newly added 'gunicorn' dependency is installed, run:

```bash
$ poetry install
```

2. To run on the dev environment use:

```bash
$ docker-compose up
```

3. To run on the prod environment use:

```bash
$ docker build --target production --tag todo-app:prod .
```

```bash
$ docker run -p 3000:3000 --env-file .env todo-app:prod
```

# Test Container

The test container is used to run the unit and integration tests for the To Do App. To build the test container, run the following command:

```bash
$ docker build --target test --tag todo-app:test .
```

```bash
$ run: docker run --env-file ./.env.test todo-app:test
```
## Manual Deployment
Find the Docker images for this project [here](https://hub.docker.com/repository/docker/funmibadev/todo-app/tags).

### Release Docker Image to DockerHub
To release the Docker image to DockerHub, you first need to build the production container using the following command:
```bash
$ docker build --target production --tag funmibadev/todo-app:dev .
```
Then you need to push the image to docker using the following command:
```bash
$ docker push funmibadev/todo-app:dev
```
### Deploy App on Azure

#### Create WebApp:
##### Portal:
- Create a Resource -> Web App
- Select your Project Exercise resource group.
- In the “Publish” field, select “Docker Container”
- Under “App Service Plan”, it should default to creating a new one, which is correct. Just change the “Sku and size” to “B1”.
- On the next screen, select Docker Hub in the “Image Source” field, and enter the details of your image.

##### CLI:
- First create an App Service Plan: az appservice plan create --resource-group <resource_group_name> -n <appservice_plan_name> --sku B1 --is-linux
- Then create the Web App: az webapp create --resource-group <resource_group_name> --plan <appservice_plan_name> --name <webapp_name> --deployment-container-image-name docker.io/<dockerhub_username>/<container-image-name>:<tagname>

#### Set up Environment Variables:
##### Portal:
- Settings -> Configuration in the Portal
- Add all the environment variables as “New application setting” as available in the .env file

##### CLI:
- Enter them individually via az webapp config appsettings set -g <resource_group_name> -n <webapp_name> --settings FLASK_APP=todo_app/app.

#### Find the Webhook URL:
The Webhook URL is located under Deployment Center on the app service’s page in the Azure portal.
#### Test the Webhook:
Copy the webhook URL and add in a backslash to escape the `$`. Run the following command replacing `<webhook>` with the actual webhook:
```bash
$ curl -dH -X POST "<webhook>"
```
It should look as follows:
```bash
$ curl -dH -X POST "https://\$<deployment_username>:<deployment_password>@<webapp_name>.scm.azurewebsites.net/docker/hook"
```
Upon successfully triggering the webhook, you should receive a link to a log-stream related to the re-pulling of the image and restarting the app.
Find the deployed website [here](https://funmitodoapp.azurewebsites.net/).
