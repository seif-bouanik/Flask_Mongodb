from flask import Flask, request, render_template, jsonify, json
from flask_pymongo import PyMongo
import bson
from bson import json_util
import db_operations 


### Calling the mongodb operations module
db_operations.createMongodb()


app = Flask("__name__",template_folder="templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_URI'] = "mongodb://svetlana:cisco123@localhost:27017/Device_Configuration"
mongo = PyMongo(app) 
json.dumps=json_util.dumps




@app.route('/<switch>/interfaces.html', methods=['GET'])
def interfaces_html(switch):
    query=mongo.db.Interfaces.find({"Switch_name":switch})
    return render_template("interfaces.html",switch=switch, result=query),200

@app.route('/<switch>/interfaces.json', methods=['GET'])
def interfaces_json(switch):
    query=mongo.db.Interfaces.find({"Switch_name":switch})
    return jsonify(query),200
    
@app.route("/<switch>/<path:interface>/details.html", methods=["GET"])
def interface_details_html(switch,interface):
    result=mongo.db.Interfaces.find_one({"Switch_name":switch,"Interface_Name":interface})
    return render_template("details.html",interface=interface ,result=result),200

@app.route("/<switch>/<path:interface>/details.json", methods=["GET"])
def interface_details_json(switch,interface):
    query=mongo.db.Interfaces.find_one({"Switch_name":switch,"Interface_Name":interface})
    return jsonify(query),200
    
@app.route("/<switch>/<ObjectId:_id>", methods=["GET","PATCH"])
def update_description_state(_id,switch):
    payload={"Description":"my cool interface" , "State":"up"}
    query=mongo.db.Interfaces.update_one(
    {"_id":_id, "Switch_name":switch},
    {"$set": payload},
    upsert=False
    )

if __name__=="__main__":
    app.run()