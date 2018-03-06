# manage.py
from flask.cli import FlaskGroup

from server import create_app, db
from server.models import User


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@cli.command()
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email='ad@min.com', password='admin', admin=True))
    db.session.commit()


@cli.command()
def create_data():
    """Creates sample data."""
    db.session.add(User(email='y@min.com', password='yyy'))
    db.session.commit()
if __name__ == '__main__':
    cli()
