from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)   
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class WardPopulation(db.Model):
    __tablename__ = 'ward_population'
    id = db.Column(db.Integer, primary_key=True)
    ward_code = db.Column(db.String(100), nullable=False, unique=True) 
    ward_name = db.Column(db.String(100), nullable=False)
    total_population = db.Column(db.Integer, nullable=False)
    population_under_15 = db.Column(db.Integer, nullable=False)
    population_age_16_24 = db.Column(db.Integer, nullable=False)
    population_age_25_49 = db.Column(db.Integer, nullable=False)
    population_age_50_64 = db.Column(db.Integer, nullable=False)
    population_over_65 = db.Column(db.Integer, nullable=False)


class WardGeneralHealth(db.Model):
    __tablename__ = 'general_health'
    id = db.Column(db.Integer, primary_key=True)
    ward_code = db.Column(db.String(100), nullable=False, unique=True)
    ward_name = db.Column(db.String(100), nullable=False)
    usual_residents = db.Column(db.Integer, nullable=False)
    residentsGoodHealth = db.Column(db.Integer, nullable=False)
    residentsFairHealth = db.Column(db.Integer, nullable=False)
    residentsBadHealth = db.Column(db.Integer, nullable=False)
    residentVeryBadHealth = db.Column(db.Integer, nullable=False)

class WardOccupation(db.Model):
    __tablename__ = 'ward_occupation'
    id = db.Column(db.Integer, primary_key=True)
    ward_code = db.Column(db.String(100), nullable=False, unique=True)
    ward_name = db.Column(db.String(100), nullable=False)
    managers_directors_senior_officials = db.Column(db.Integer, nullable=False)
    professional_occupations = db.Column(db.Integer, nullable=False)
    associate_professional_technical = db.Column(db.Integer, nullable=False)
    administrative_secretarial = db.Column(db.Integer, nullable=False)
    skilled_trades = db.Column(db.Integer, nullable=False)
    caring_leisure_service = db.Column(db.Integer, nullable=False)
    sales_customer_service = db.Column(db.Integer, nullable=False)
    process_plant_machine_operatives = db.Column(db.Integer, nullable=False)
    elementary_occupations = db.Column(db.Integer, nullable=False)                                                                                                                                                                                                                                              

class WardVehicles(db.Model):
    __tablename__ = 'vehicle_availability'
    id = db.Column(db.Integer, primary_key=True)
    ward_code = db.Column(db.String(100), nullable=False, unique=True)
    ward_name = db.Column(db.String(100), nullable=False)   
    no_cars_vans = db.Column(db.Integer, nullable=False)
    one_car_van = db.Column(db.Integer, nullable=False)
    two_cars_vans = db.Column(db.Integer, nullable=False)
    three_or_more_cars_vans = db.Column(db.Integer, nullable=False)

class WardTenures(db.Model):
    __tablename__ = 'ward_tenures'
    id = db.Column(db.Integer, primary_key=True)
    ward_code = db.Column(db.String(100), nullable=False, unique=True)
    ward_name = db.Column(db.String(100), nullable=False) 
    owns_outright = db.Column(db.Integer, nullable=False)
    owns_with_mortgage = db.Column(db.Integer, nullable=False)
    shared_ownership = db.Column(db.Integer, nullable=False)
    rents_council = db.Column(db.Integer, nullable=False)
    other_social_rented = db.Column(db.Integer, nullable=False)
    rents_private_landlord = db.Column(db.Integer, nullable=False)
    other_private_rented = db.Column(db.Integer, nullable=False)
    lives_rent_free = db.Column(db.Integer, nullable=False)