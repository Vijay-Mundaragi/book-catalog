from app import create_app


my_app = create_app()

@my_app.route("/")
def hello():
    return "Hello All"


if __name__ == "__main__":
    my_app.run()

