db = "Database Link"

class Bloxfruit(db.Model):
    __tablename__ = "fruits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    fruit = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(10), nullable=False)
    bounty = db.Column(db.Integer, nullable=False)