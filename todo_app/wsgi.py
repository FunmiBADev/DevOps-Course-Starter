
from todo_app.app import create_app

# Create the Flask application
app = create_app()

# This is the entry point for the WSGI server to interact with the application
if __name__ == "__main__":
    app.run()
