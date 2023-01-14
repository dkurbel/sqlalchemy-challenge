from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import scipy.stats as st

# create engine reflect database schema
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references
Measurement = Base.classes.measurement
Station = Base.classes.station

#start session
session = Session(engine)

first_row = session.query(Measurement).order_by(desc('date')).first()
precip_12mo = session.query(Measurement).order_by('date').filter(Measurement.date >= (dt.strptime(first_row.date, '%Y-%m-%d') - timedelta(days=366)))
data_year = [{each_item.date:each_item.prcp} for each_item in precip_12mo]



# Flask setup

app = Flask(__name__)

# Flask routes

@app.route('/')
def home():
    return (
        f'Welcome to my homepage!<br/>'
        f'Available routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end><br/>'
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    return ()

@app.route('/api/v1.0/stations')
def stations():
    return ()

@app.route('/api/v1.0/tobs')
def tobs():
    return ()

@app.route('/api/v1.0/<start>')
def start():
    return ()

@app.route('/api/v1.0/<start>/<end>')
def end():
    return ()



if __name__ == "__main__":
    app.run(debug=True)