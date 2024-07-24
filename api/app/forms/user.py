from wtforms import Form, StringField, PasswordField, validators, FieldList


class UserRegistrationForm(Form):
    """A form representing User registration"""

    staff_no = StringField('staff_no', [validators.DataRequired("Staff Number is required!")])
    username = StringField('username', [validators.DataRequired("Username is required!")])
    password = PasswordField('password', [validators.DataRequired("Password is required!"),
                                               validators.EqualTo('confirm_password',
                                                                  "Password don't match!")])
    confirm_password = PasswordField('confirm_password', [validators.DataRequired("Confirmation "
                                                                                       "password is required!")])
    roles = StringField('roles', [validators.DataRequired("User roles is required!")])


class UserUpdateForm(Form):
    """A form representing User update"""

    password = PasswordField('password', [validators.DataRequired("Password is required!")])
    roles = StringField('roles', [])


class UserUpdatePasswordForm(Form):
    """A form representing password change"""

    password = PasswordField('password', [validators.DataRequired("Password is required!"),
                                               validators.EqualTo('confirm_password',
                                                                  "Password don't match!")])
    confirm_password = PasswordField('confirm_password', [])


class UserLoginForm(Form):
    """A form representing User login"""

    username = StringField('username', [validators.DataRequired("Username is required!")])
    password = PasswordField('password', [validators.DataRequired("Password is required!")])
