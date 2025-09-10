# Initialization script to create database tables for the Flask app
# Run this inside the backend container before the app handles requests:
# python init_db.py

import sys


def get_app_and_db():
    """Attempt to import the Flask application factory and the SQLAlchemy db object.
    Tries a couple of common import locations to be resilient to project layout.
   """
    # First try: app.create_app and app.db
    try:
        from app import create_app, db
        app = create_app()
        return app, db
    except Exception:
        pass

    # Second try: create_app in app and db defined in app.models.models
    try:
        from app import create_app
        from app.models.models import db
        app = create_app()
        return app, db
    except Exception as e:
        print("Failed to import Flask app and db:", e)
        sys.exit(1)


if __name__ == '__main__':
    app, db = get_app_and_db()
    with app.app_context():
        db.create_all()
        print('Database tables created (or already exist).')
