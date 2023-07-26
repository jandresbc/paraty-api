import pandas as pd
from app.Models.database import db
from app.Models.netflix import netflix
from flask_restful import Resource
from flask import request
import json

class viewData(Resource):
    def get(self):
        net = netflix.query

        if "id" in request.json:
            id = request.json["id"]
            net = net.filter(netflix.id == id)

        if "type" in request.json:
            type = request.json["type"]
            net = net.filter(netflix.type == type)

        if "release_year" in request.json:
            year = request.json["release_year"]
            net = net.filter(netflix.release_year == year)
        
        result = []
        
        net = net.all()
        
        for i,e in enumerate(net):
            data = {}
            data["id"] = e.id
            data["show_id"] = e.show_id
            data["type"] = e.type
            data["title"] = e.title
            data["director"] = e.director
            data["cast"] = e.cast
            data["country"] = e.country
            data["date_added"] = e.date_added
            data["release_year"] = e.release_year
            data["rating"] = e.rating
            data["duration"] = e.duration
            data["listed_in"] = e.listed_in
            data["description"] = e.description
            data["created_at"] = str(e.created_at)
            data["updated_at"] = str(e.updated_at)

            result.append(data)

        return {'status':'Done',"message":"Process Done","data":result}