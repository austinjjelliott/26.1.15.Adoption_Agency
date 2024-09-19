from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)




class Pet(db.Model):
    """Create a Pet Model for the adoptables """
    __tablename__ = "pets"
    
    def __repr__(self):
        pet = self
        return f"<User id ={pet.id} name = {pet.name}>"
  
    def greet(self):
        return f'Hi! I am {self.name}! I am a {self.species} and I am {self.age} years old! '


    id = db.Column(db.Integer, 
                   primary_key = True,
                   autoincrement = True)
    name = db.Column(db.Text, 
                     nullable = False)
    species = db.Column(db.Text,
                        nullable = False)
    photo_url = db.Column(db.Text,
                          nullable = True)
    age = db.Column(db.Integer, 
                    nullable = True)
    notes = db.Column(db.Text,
                      nullable = True)
    available = db.Column(db.Boolean, 
                          nullable = False,
                          default = True)