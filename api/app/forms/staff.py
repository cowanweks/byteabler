from wtforms import Form, StringField, validators


class StaffRegistrationForm(Form):
    """A form representing Unit registration"""

    staffNo = StringField('staffNo', [validators.DataRequired("Staff NO is required!")])
    firstName = StringField('firstName', [validators.DataRequired("First Name is required!")])
    middleName = StringField('middleName', [validators.DataRequired("Sur Name is required!")])
    lastName = StringField('lastName', [validators.DataRequired("Last Name is required!")])
    natId = StringField('natId', [validators.DataRequired("National ID is required!")])
    mobileNo = StringField('mobileNo', [validators.DataRequired("Mobile Number is required!")])
    email = StringField('email', [validators.DataRequired("Email is required!")])
    dateOfBirth = StringField('dateOfBirth', [validators.DataRequired("Date of Birth is required!")])


class StaffUpdateForm(Form):
    """A form representing Unit update"""

    firstName = StringField('firstName', [validators.DataRequired("First Name is required!")])
    middleName = StringField('middleName', [validators.DataRequired("Sur Name is required!")])
    lastName = StringField('lastName', [validators.DataRequired("Last Name is required!")])
    natId = StringField('natId', [validators.DataRequired("National ID is required!")])
    mobileNo = StringField('mobileNo', [validators.DataRequired("Mobile Number is required!")])
    email = StringField('email', [validators.DataRequired("Email is required!")])
    dateOfBirth = StringField('dateOfBirth', [validators.DataRequired("Date of Birth is required!")])

