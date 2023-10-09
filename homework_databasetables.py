db = "Database Link"

class Naruto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    justu_type = db.Column(db.String(50), nullable=False)


class Onepiece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fruit = db.Column(db.String(40), nullable=False)
    weakness = db.Column(db.String(40), nullable=False)
    picture = db.Column(db.byte, nullable=False)

class Footballers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.String(50), nullable=False)
    shots = db.Column(db.String(100), nullable=False)
    heading = db.Column(db.String(40), nullable=False)

