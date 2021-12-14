from src import initialize_api
from settings import PORT


def main():
    app = initialize_api()
    app.run(port=PORT)


if __name__ == '__main__':
    main()
