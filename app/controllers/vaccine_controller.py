from app.exc.vaccine_exc import InvalidCpfError
from flask import request, current_app, jsonify
from app.models.vaccine_model import Vaccine


def register_vaccination():
    data = request.json
    try:
        vaccine_card = Vaccine(**data)

        current_app.db.session.add(vaccine_card)
        current_app.db.session.commit()

        return jsonify(vaccine_card), 201

    except InvalidCpfError as e:
        return {"msg": str(e)}, 400


def get_vaccination():
    all_cards = Vaccine.query.all()
    return jsonify(all_cards), 200
