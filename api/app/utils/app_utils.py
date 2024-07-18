from functools import wraps
from dotenv import load_dotenv, find_dotenv
from app.utils import bcolors


def app_setup(func):
    """Setup the environment before starting the flask app"""

    @wraps(func)
    def init():
        print(bcolors.OKGREEN + "Hello am running before flask!")

        # Load environment variables
        load_dotenv(find_dotenv(".env"))

        return func()

    return init
