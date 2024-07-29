from wtforms import Form, StringField, validators


class ClassRegistrationForm(Form):
    """A form representing Class registration"""

    classId = StringField('Class ID', [validators.DataRequired("Class Id is required!")])
    classRep = StringField('Class Rep', [validators.DataRequired("Class Rep is required!")])


class ClassUpdateForm(Form):
    """A form representing Class update"""

    classRep = StringField('Class Rep', [])
    classId = StringField('Class Id', [])
