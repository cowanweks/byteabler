from wtforms import Form, StringField, validators, FieldList


class UnitRegistrationForm(Form):
    """A form representing Unit registration"""

    unitCode = StringField('unit_code', [validators.DataRequired("Unit Code is required!")])
    unitName = StringField('unit_name', [validators.DataRequired("Unit Name is required!")])


class UnitUpdateForm(Form):
    """A form representing Unit update"""

    unitCode = StringField('unit_code', [])
    unitName = StringField('unit_name', [])
