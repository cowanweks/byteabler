from wtforms import Form, StringField, validators


class ClassRegistrationForm(Form):
    """A form representing Class registration"""

    classId = StringField('Class ID', [validators.DataRequired("Class Id is required!")])


class ClassUpdateForm(Form):
    """A form representing Class update"""

    classId: str = StringField('Class Id', [validators.DataRequired("Class ID is required!")])
