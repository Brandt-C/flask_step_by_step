
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class epCreate(FlaskForm):
    epchoice = IntegerField("Episode # (1-51)", validators=[DataRequired()] )
    lochoice = IntegerField("location # (1-126)", validators=[DataRequired()] )
    