from db.database import db


class Payment(db.Model):
    def __init__(
        self,
        value=None,
        paid=None,
        bank_payment_id=None,
        qr_code=None,
        expiration_date=None,
    ):
        self.value = value
        self.paid = paid
        self.bank_payment_id = bank_payment_id
        self.qr_code = qr_code
        self.expiration_date = expiration_date

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "expiration_date": self.expiration_date,
        }
