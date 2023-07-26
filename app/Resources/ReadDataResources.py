import pandas as pd
from app.Models.database import db
from app.Models.netflix import netflix
from flask_restful import Resource


class readData(Resource):
    def get(self):
        datos = pd.read_csv("app/data/netflix_titles.csv")
        datos.fillna("",inplace=True)

        for key,data in datos.iterrows():
            print("Registro número: {} procesado.".format(key))
            net = netflix()
            
            net.show_id = data["show_id"]
            net.type = data["type"]
            net.title = data["title"]
            net.director = data["director"]
            net.cast = data["cast"]
            net.country = data["country"]
            net.date_added = data["date_added"]
            net.release_year = data["release_year"]
            net.rating = data["rating"]
            net.duration = data["duration"]
            net.listed_in = data["listed_in"]
            net.description = data["description"]

            db.session.add(net)
            db.session.commit()

        return {'status':'Done', 'message':'Rows added successfully.'}