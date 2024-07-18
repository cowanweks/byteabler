from app.models import db, User
from app.forms.user import UserLoginForm
from app.utils.login_utils import verify_password
from flask import session
from sqlalchemy.exc import SQLAlchemyError


def login(data: dict) -> (bool, str):
    """Login user"""

    user_form = UserLoginForm(data)

    try:
        results = db.session.execute(db.select(User).where(User.username == user_form.username.data))
        user = results.scalars().first()

        if user:
            if verify_password(user_form.password.data, user.password):
                # Store session
                session["username"] = user_form.username.data

                return True, "Successfully SignedIn!"

        return False, "Incorrect username or password!"

    except SQLAlchemyError as ex:
        print(ex)
        return False, "Database error occurred!"


def logout(user_id: str):
    """Logout user"""
    return True, "Successfully SignedOut!"
