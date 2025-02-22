from flask import Flask, request, render_template, redirect, flash, session 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()  only need to do this once, done in terminal...


@app.route('/')
def list_pets():
    """Show a list of all pets on the website"""
    pets = Pet.query.order_by(Pet.available.desc()).all()
    return render_template('all_pets.html', pets = pets)

@app.route('/add', methods = ["GET", "POST"])
def add_pet():
    """Add another pet to the database"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()

        flash(f'Added New Pet: Name is {name} and species is {species}')

        return redirect("/")
    else:
        return render_template("add_pet_form.html", form = form)
    
@app.route('/<int:pet_id>', methods = ["GET", "POST"])
def show_and_edit_pet_details(pet_id):
    """Show the details and edit form for one pet at a time"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)
  #How to handle the edits when they are made: 
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f'Pet Has Been Updated!')
        return redirect("/")
    else:
        return render_template('edit_pet_form.html', pet = pet, form = form)

