from app import create_app
from waitress import serve


def main():
    """Create the flask application"""
    flask_app = create_app()

    if flask_app.config.get("ENV") == "production":
        try:
            serve(app=flask_app, host="0.0.0.0", port=5000)
        except Exception as ex:
            print(str(ex))

    flask_app.run(host=flask_app.config.get("HOST"), port=flask_app.config.get("PORT"))


if __name__ == "__main__":
    main()
