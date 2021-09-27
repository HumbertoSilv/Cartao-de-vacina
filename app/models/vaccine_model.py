from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Vaccine(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_card"

    cpf = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    first_shot_date = db.Column(db.Date)
    second_shot_date = db.Column(db.Date)
    vaccine_name = db.Column(db.String, nullable=False)
    health_unit_name = db.Column(db.String)
