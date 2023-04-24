
# EPR Collaborative Hub

This website serves as a hub where all other EPR sites/services will be accessible from.

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Create and Start virtual environment

```bash
  python -m venv envs/hir_env
  ../../envs/hir_venv/Scripts/Activate.ps1
```

Install python dependencies

```bash
  pip install requirements.txt 
```

Create migrations 

```bash
  python manage.py makemigrations
  python manage.py migrate 
```


Create superuser for database

```bash
  python manage.py createsuperuser
```

Update the "dev.py" file with the created username and password

Run the application

```bash
  python manage.py runserver
```

#### Start TailwindCSS

Open a different terminal to begin.

Install npm dependencies (tailwindcss)

```bash
  cd jstoolchain
  npm install
```

build the tailwindcss

```bash
  npm run-script build
```

watch for changes to html

```bash
  npx tailwindcss -i css/tailwind.css -o ../hir_backend/static/css/tailwind-output.css --watch
```

## Deployment

To deploy this project run

```docker
  docker-compose -f docker-compose.dev.yml up --build

```

Createsuperuser account

```docker
  docker-compose -f docker-compose.dev.yml exec wagtail python manage.py createsuperuser

```

List files in the container

```docker
  docker container exec -it wagtail ls /app

```
