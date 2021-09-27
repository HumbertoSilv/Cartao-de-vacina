from flask import Blueprint
from app.controllers.vaccine_controller import get_vaccination, register_vaccination

bp = Blueprint("vaccination_bp", __name__, url_prefix="/vaccination")

bp.post("")(register_vaccination)
bp.get("")(get_vaccination)
