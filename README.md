
# Test task: Build a Django CRUD API with Swagger Documentation

A simple CRUD API implemented using Django and Django REST Framework. This project provides a basic setup for managing a weekly schedule with operations to Create, Read, Update, and Delete entries.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following tools installed:
- Python 3
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Installing

Follow these steps to get your development environment running:

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```

2. **Set up a virtual environment (Optional)**

   - For Unix/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

### Configuring the database

This project uses SQLite by default which is Django's default database. You can start using the application with SQLite without any further configuration. If you need to use another database, update the `DATABASES` configuration in `settings.py`.

### Running migrations

Before running the server, you need to apply migrations to set up your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the development server

To start the development server, run:

```bash
python manage.py runserver
```

This will start the server on `http://127.0.0.1:8000/`. You can access the API endpoints via this URL.

### Accessing the Admin Panel

To create an admin user, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the user. Afterward, you can log in to the admin panel at `http://127.0.0.1:8000/admin/`.

## Using the API

You can interact with the API through a web browser, curl, or any other HTTP client like Postman.

- **Create** a new entry: `POST /api/slot/`
- **Read** all entries: `GET /api/slot/`
- **Read** a single entry: `GET /api/slot/{id}/`
- **Update** an entry: `PUT /api/slot/{id}/`
- **Delete** an entry: `DELETE /api/slot/{id}/`

## Documentation

To view the API documentation and interact with the API via Swagger, navigate to `http://127.0.0.1:8000/swagger/`.

## Running Tests

To run tests, execute:

```bash
python manage.py test
```

## Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change or add.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
