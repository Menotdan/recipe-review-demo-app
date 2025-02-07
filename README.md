# Recipe Reviews Demo App

This is a simple app made with Vite+React.js (frontend), and Django (backend). It was built as a technical demonstration for an interview. It features a simple pizza recipe I use at home, and an interactive system to add reviews to the recipe that can be liked.

## To set up a development environment:
Note: This project requires you to install `djangorestframework` from pip.

### Backend:
(Also see `backend/asp-net/README.md` for instructions to run an alternative backend.)
- In a terminal, `cd` into the `backend/django` folder.
- Run `python manage.py makemigrations` and `python manage.py migrate` to create the database and apply all migrations.
- Run `python manage.py runserver` to start the backend's development server.

### Frontend:
- In another terminal, `cd` into the `frontend` folder. 
- Run `npm install` and `npm run dev` to start the frontend's development server.

Now, you can visit the app at the URL displayed in the frontend terminal.

Copyright 2024 (c) Menotdan

Please see LICENSE for more information.