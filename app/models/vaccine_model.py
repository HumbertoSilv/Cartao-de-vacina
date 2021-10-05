from dataclasses import dataclass
from datetime import date, datetime, timedelta

from app.configs.database import db
from app.exc.vaccine_exc import InvalidCpfError
from sqlalchemy.orm import validates


@dataclass
class Vaccine(db.Model):
    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_card"

    cpf = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    first_shot_date = db.Column(db.DateTime, default=datetime.utcnow())
    second_shot_date = db.Column(
        db.Date, default=date.today() + timedelta(days=90)
        )
    vaccine_name = db.Column(db.String, nullable=False)
    health_unit_name = db.Column(db.String)

    @validates("cpf")
    def validate_cpf(self, key, cpf):
        if len(cpf) != 11:
            raise InvalidCpfError(
                f"CPF with {len(cpf)} digits, 11 digit limit."
            )

        if not cpf.isdigit():
            raise InvalidCpfError(
                "CPF must contain only numbers."
            )
        return cpf
