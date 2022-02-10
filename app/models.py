class User:
    class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30),nullable=False, unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(255),nullable=False)


     @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
 

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password