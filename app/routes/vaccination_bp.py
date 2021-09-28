from flask import Blueprint
from app.controllers.vaccine_controller import get_vaccination, register_vaccination

bp = Blueprint("vaccination_bp", __name__, url_prefix="/api")

bp.post("/vaccination")(register_vaccination)
bp.get("/vaccination")(get_vaccination)
