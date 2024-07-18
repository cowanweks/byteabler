from uuid import uuid4
from app.models import db, User
from app.forms.user import UserRegistrationForm, UserUpdateForm, UserLoginForm, UserUpdatePasswordForm
from app.utils.login_utils import hash_password, verify_password
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def new_user(data: dict) -> (bool, str):
    """A controller that handles new user registrations"""

    try:
        new_user_form = UserRegistrationForm(data)

        if new_user_form.validate():
            db.session.execute(
                db.insert(User).values(
                    user_id=str(uuid4()),
                    staff_no=new_user_form.staff_no.data,
                    username=new_user_form.username.data,
                    roles=new_user_form.roles.data,
                    password=hash_password(new_user_form.password.data)
                )
            )
            db.session.commit()
            return True, "Successfully Created new User!"

        else:
            print(new_user_form.errors)
            return False, new_user_form.errors

    except IntegrityError as ex:
        print(ex)
        return False, "User already exists!"


def get_users(user_id: str):
    """A controller that handles getting users"""

    try:
        if user_id:
            users = (
                db.session.execute(
                    db.select(User)
                    .where(User.user_id == user_id)
                    .order_by(User.user_id)
                )
                .scalars()
                .all()
            )
        else:
            users = (
                db.session.execute(db.select(User).order_by(User.user_id)).scalars().all()
            )

        serialized_users = [user.serialize() for user in users]
        return True, serialized_users

    except Exception as ex:
        print(ex)
        return False, "Database error occurred!"


def update_user(user_id: str, data: dict):
    """Update user"""
    try:
        updated_user_form = UserUpdateForm(data)

        if updated_user_form.validate():
            db.session.execute(
                db.update(User)
                .where(User.user_id == user_id)
                .values(roles=updated_user_form.roles.data)
            )
            db.session.commit()
            return True, "Successfully Updated User!"

        else:
            return False, updated_user_form.errors

    except SQLAlchemyError as ex:
        print(ex)
        return False, "Database error occurred!"


def delete_user(user_id: str):
    """A controller that Deletes user"""
    try:
        db.session.execute(db.delete(User).where(User.user_id == user_id))
        db.session.commit()
        db.session.close()
        return True, "Successfully Deleted User!"

    except SQLAlchemyError as ex:
        print(ex)
        db.session.close()
        return False, "Database error occurred!"
