from app import create_app, db


if __name__ == "__main__":
    my_app = create_app('prod')
    with my_app.app_context():
        db.create_all()

    my_app.run()
    
