from flask import Flask, jsonify, make_response, request
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
    return "<h1> Welcome to Late Show, Your home of new shows</h1>\
            <p>1. To GET all episodes visit: <strong>/episodes</strong></p>\
            <p>2. To GET a single episode enter the episode id: <strong>/episodes/id</strong></p>\
            <p>3. To GET all guests: <strong>/guests</strong></p>\
            <p>4. To POST a new appearance: <strong>/appearances</strong></p>"
        
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

        return make_response(jsonify(episodes_list), 200)  

class EpisodeID(Resource):
    def get(self, id):
        episode = Episode.query.filter(Episode.id == id) .first()  

        if episode:
            return make_response(jsonify(episode.to_dict()), 200) 
    
        return make_response(jsonify({'error': "Episode not found"}), 404)
    
class Guests(Resource):
    def get(self):
        guests = [guest.to_dict() for guest in Guest.query.all()]

        return make_response(jsonify(guests), 200)

class Appearances(Resource):
    def post(self):
        data = request.json
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        if rating is None or not (1 <= rating <=5) or not isinstance(rating, int): #validates rating
            return make_response(jsonify({'error': "Rating must be a whole number between 1 and 5!"}), 400) 
        
        if episode_id is None or guest_id is None:
            return make_response(jsonify({'error': "Missing required fields!!!"}), 404)

        episode = Episode.query.filter_by(id = episode_id).first()
        guest =  Guest.query.filter_by(id = guest_id).first()

        if not episode:
            return make_response(jsonify({'error': 'Episode does not exist'}), 404)
        
        if not guest:
            return make_response(jsonify({'error': 'Guest does not exist'}), 404)
                                          
         #create a new appearance if all checks pass
        if episode and guest:
            new_appearance = Appearance(
                rating = rating, 
                episode_id = episode_id,
                guest_id= guest_id)
            
            db.session.add(new_appearance)
            db.session.commit()
            return make_response(jsonify(new_appearance.to_dict()), 201)

api.add_resource(Episodes, '/episodes')
api.add_resource(EpisodeID, '/episodes/<int:id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
