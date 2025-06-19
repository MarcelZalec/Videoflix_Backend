# Videoflix
![Logo](Logo.svg)
## A Netflix Clone

The [Frontend](https://github.com/MarcelZalec/videoflix_frontend) was realized with **Angular 19**,
The [Backend](https://github.com/MarcelZalec/Videoflix_Backend) was realized with **Django Rest Framework (DRF)**.

-----

Start Frontend with
<code>VS Code LiveServer<code>

1. <b>Clone the repository:</b><br>
   <code>git clone (https://github.com/MarcelZalec/Videoflix_Backend.git)</code><br>
   <code>cd Videoflix-Backend</code><br><br>

2. <b>Create a virtual environment:</b><br>
   <code>python -m venv env</code><br>
   <code>source env/bin/activate</code>  # Linux/Mac<br>
   <code>env\\Scripts\\activate</code>  # Windows<br><br>

3. <b>Install dependencies:</b><br>
   <code>pip install -r requirements.txt</code><br><br>

4. <b>Make migrations<b><br>
    <code>python manage.py makemigrations<code>
    <code>python manage.py migrate<code>

5. <b>Create a env file from .env_template<b><br>
    <code>cp .env_template .env<code>

6. <b>Start Backend with<b><br>
    <code>python3 manage.py runserver<code>