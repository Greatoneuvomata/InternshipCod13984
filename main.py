db = "Database Link"

class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    video_link = db.Column(db.String(200), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    sub = db.Column(db.Integer, nullable=False)