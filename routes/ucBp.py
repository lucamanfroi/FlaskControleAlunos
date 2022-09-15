from flask import Blueprint
from ..extensions import db
from ..models.uc import Uc

ucBp = Blueprint('ucBp', __name__)


@ucBp.route('/uc')
def uc_list():
    # db.create_all()
