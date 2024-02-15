from app import flask_app


def main() -> None:
    flask_app.run(debug=True, host="0.0.0.0", port=3000)


# Application Entry
if __name__ == '__main__':
    main()
