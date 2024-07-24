from wtforms import Form, StringField, validators


class ClassRepRegistrationForm(Form):
    """A form representing Class registration"""

    regNo = StringField('Registration No', [validators.DataRequired()])
    firstName = StringField('FirstName', [validators.DataRequired()])
    middleName = StringField('MiddleName', [validators.DataRequired()])
    lastName = StringField('LastName', [validators.DataRequired()])
    phoneNo = StringField('Phone No', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])


class ClassRepUpdateForm(Form):
    """A form representing Class update"""

    regNo = StringField('Registration No', [validators.DataRequired()])
    firstname = StringField('FirstName', [validators.DataRequired()])
    middleName = StringField('MiddleName', [validators.DataRequired()])
    lastName = StringField('LastName', [validators.DataRequired()])
    phoneNo = StringField('Phone No', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
