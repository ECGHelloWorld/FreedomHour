from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String)
    salt = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    verified = db.Column(db.Boolean)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email
        self.salt = bcrypt.gensalt()
        self.pw_hash = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        self.timestamp = datetime.datetime.utcnow()
        self.verified = False

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        """Return True if the user is verified."""
        return self.verified

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def check_password(self, password):
        return self.pw_hash == bcrypt.hashpw(password.encode('utf-8'), self.salt)

    def is_admin(self):
        return self.email in ['daynb@guilford.edu']:

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)
