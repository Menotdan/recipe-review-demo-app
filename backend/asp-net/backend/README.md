# ASP.NET Backend
This is an alternative backend for the recipe review project. It uses ASP.NET and Entity Framework (connected to an SQLite database).

## To set up a development environment:
- Open the solution `asp-net/backend/backend.sln` in Visual Studio.
- Open `asp-net/backend` in a terminal, and run `dotnet ef database update --connection "Data Source=recipe_reviews.db"` to create the database and apply migrations.
- Run the solution from Visual Studio.
- Select `http` from the run options, and a browser tab should open to the Swagger UI where you can test exclusively the backend. Otherwise, start a development server of the frontend and the website should work as intended.