# nuevo-django

1 - Correr

pip install django

pip install -r requirements.txt

2 - Migrar la base de datos con

python3 manage.py migrate

3 - Crear el entorno (SOLO LA PRIMERA VEZ)

python3 -m venv env

4 - Activarlo

. env/Scripts/activate (desactivarlo con "deactivate") -- WINDOWS

source env/bin/activate -- MAC

5 - Correr el servidor

python3 manage.py runserver

---

- Se accede al sitio a traves de

http://127.0.0.1:8000/

- Si se agrega alguna dependencia, actualizar el requirements.txt con el comando

pip freeze > requirements.txt
