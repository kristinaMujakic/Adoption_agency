from flask import Flask, redirect, render_template, url_for

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret34'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route('/')
def homepage():
    '''List all pets'''

    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Renders pet form (GET) or handles pet form submission (POST)'''

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    '''Edit pet'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()

        return redirect(url_for('homepage'))

    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)
