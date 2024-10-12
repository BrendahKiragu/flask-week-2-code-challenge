from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Episode, Appearance, Guest

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "<h1> Welcome to Late Show, Your home of new shows</h1> <p>To view all episodes visit: /episodes</p> <p>To visit a single episode enterr the episode id: /episodes/id</p>"

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()

        episodes_list = []
        for episode in episodes:
            episode_dict = {
                'id':  episode.id,
                'date': episode.date,
                'number': episode.number,
            }
            episodes_list.append(episode_dict)

        return make_response(episodes_list, 200)  
   

class Appearance(Resource):
    def get(self):
        pass

api.add_resource(Episodes, '/episodes')
api.add_resource(EpisodeID, '/episodes/<int:id>')
# api.add_resource(Appearance, '/appearances')

if __name__ == '__main__':
    app.run(port=5555, debug=5555)
