from wtforms import Form, StringField, validators


class StaffRegistrationForm(Form):
    """A form representing Unit registration"""

    staffNo: str = StringField('staffNo', [validators.DataRequired("Staff NO is required!")])
    firstName: str = StringField('firstName', [validators.DataRequired("First Name is required!")])
    middleName: str = StringField('middleName', [validators.DataRequired("Sur Name is required!")])
    lastName: str = StringField('lastName', [validators.DataRequired("Last Name is required!")])
    natId: str = StringField('natId', [validators.DataRequired("National ID is required!")])
    mobileNo: str = StringField('mobileNo', [validators.DataRequired("Mobile Number is required!")])
    email: str = StringField('email', [validators.DataRequired("Email is required!")])
    dateOfBirth: str = StringField('dateOfBirth', [validators.DataRequired("Date of Birth is required!")])


class StaffUpdateForm(Form):
    """A form representing Unit update"""

    firstName: str = StringField('firstName', [validators.DataRequired("First Name is required!")])
    middleName: str = StringField('middleName', [validators.DataRequired("Sur Name is required!")])
    lastName: str = StringField('lastName', [validators.DataRequired("Last Name is required!")])
    natId: str = StringField('natId', [validators.DataRequired("National ID is required!")])
    mobileNo: str = StringField('mobileNo', [validators.DataRequired("Mobile Number is required!")])
    email: str = StringField('email', [validators.DataRequired("Email is required!")])
    dateOfBirth: str = StringField('dateOfBirth', [validators.DataRequired("Date of Birth is required!")])

