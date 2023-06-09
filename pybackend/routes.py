from flask import render_template, request, jsonify
from pybackend import app, db
from pybackend.models import Map, Rover, Path

import pybackend.img_proceessor as img
import json
import numpy as np
import qoi



@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return 'An error occurred while retrieving data from the database.'
    
@app.route('/api/telemetry', methods=['GET']) # retrieves the telemetry from the rover
def getTelemetry():
    try:
        id = request.args.get('id')
        # return jsonify(buffer[int(id)])
        # id = int(data)

        telemetry = Rover.query.filter_by(id=id).first()

        return jsonify({"id":telemetry.id, "position": telemetry.get_position(), "accelerometer":telemetry.get_accelerometer(), "gyroscope": telemetry.get_gyroscope(), "steps":telemetry.steps, "state":telemetry.state}), 200
        
    except Exception as e:
        return { "status": "error", "type": type(e).__name__, "message": str(e)}, 400

# @app.route('/api/map', methods=['GET']) # retrieves processed map form rover
# def getMap():
#     try:
#        
#     except Exception as e:
#        return { "status": "error", "type": type(e).__name__, "message": str(e)}, 400



# @app.route('/api/command', methods=['GET']) #decide start stop
# def Command():
#     try:
#     except Exception as e:

@app.route('/api/telemetry/add', methods=['POST'], endpoint='new_telemetry') # retrieves the telemetry from the rover
def newTelemetry():
    try:
        data = request.get_json()
        position = data['position']
        accelerometer = data['accelerometer']
        gyroscope = data['gyroscope']
        steps = data['steps']
        state = data['state']

        rover = Rover(position=position, accelerometer=accelerometer, gyroscope=gyroscope, steps=steps, state=state)

        db.session.add(rover)
        db.session.commit() 

        return jsonify({"status": "sucess", "message": f"sucessfully initialised Rover with id={rover.id}", "id":f"{rover.id}"}), 200
    except KeyError as e:
        return jsonify({"status": "error", "message": f"missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    
@app.route('/api/telemetry/update', methods=['POST'], endpoint='update_telemetry') # retrieves the telemetry from the rover
def updateTelemetry():
    try:
        data = request.get_json()
        # buffer[data['id']] = data
        id = data['id']
        position = json.dumps(data['position'])
        accelerometer = json.dumps(data['accelerometer'])
        gyroscope = json.dumps(data['gyroscope'])
        steps = data['steps']
        state = data['state']

        rover = Rover.query.get_or_404(id)

        rover.position = position
        rover.accelerometer = accelerometer
        rover.gyroscope = gyroscope
        rover.steps = steps
        rover.state = state 

        db.session.add(rover)
        db.session.commit()

        return jsonify({"status": "success", "message": f"successfully updated Rover with id={id}"}), 200
    except KeyError as e:
        return jsonify({"status": "error", "message": f"missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400



# @app.route('/api/map/add', methods=['POST']) # stores the map from the rover
#     try:
#        map_array = request.form['map_array']
#        
#        map = Map(map_array=map_array)
#        db.session.add(map)
#        db.session.commit()
#        return {"status": "sucess", "message": f"sucessfully initialised Map with id={map.id}"}, 200
#     except Exception as e:
#        return { "status": "error", "type": type(e).__name__, "message": str(e)}, 400

# @app.route('/api/path', methods=['POST']) # gives the path to the rover
# def getPath():
#     try:
#     except Exception as e:
# @app.route('/api/img_processor', methods=['POST'], endpoint='img_processor')
# def imgProcessor():
#     try:
#         compressed_img = request.data
#         image = qoi.decode(compressed_img)

#         success = img.process(image)

#         return jsonify({}), 200

#     except KeyError as e:
#         return jsonify({"status": "error", "message": f"missing key: {str(e)}"}), 400
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 400
    
