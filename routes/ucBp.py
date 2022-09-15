from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Uc

ucBp = Blueprint('ucBp', __name__)


@ucBp.route('/uc')
def uc_list():
    #    return "Teste"
    #    db.create_all()
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_query)
