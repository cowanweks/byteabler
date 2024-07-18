from wtforms import Form, StringField, PasswordField, validators, FieldList


class UserRegistrationForm(Form):
    """A form representing User registration"""

    staff_no: str = StringField('staff_no', [validators.DataRequired("Staff Number is required!")])
    username: str = StringField('username', [validators.DataRequired("Username is required!")])
    password: str = PasswordField('password', [validators.DataRequired("Password is required!"),
                                               validators.EqualTo('confirm_password',
                                                                  "Password don't match!")])
    confirm_password: str = PasswordField('confirm_password', [validators.DataRequired("Confirmation "
                                                                                       "password is required!")])
    roles: str = StringField('roles', [validators.DataRequired("User roles is required!")])


class UserUpdateForm(Form):
    """A form representing User update"""

    password: str = PasswordField('password', [validators.DataRequired("Password is required!")])
    roles: str = StringField('roles', [])


class UserUpdatePasswordForm(Form):
    """A form representing password change"""

    password: str = PasswordField('password', [validators.DataRequired("Password is required!"),
                                               validators.EqualTo('confirm_password',
                                                                  "Password don't match!")])
    confirm_password: str = PasswordField('confirm_password', [])


class UserLoginForm(Form):
    """A form representing User login"""

    username: str = StringField('username', [validators.DataRequired("Username is required!")])
    password: str = PasswordField('password', [validators.DataRequired("Password is required!")])
