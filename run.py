from app import create_app, db

my_app = create_app()
with my_app.app_context():
    db.create_all()

my_app.run()
