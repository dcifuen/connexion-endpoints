#!/usr/bin/env python3
import base64
import json
import connexion
import datetime
import logging

from connexion import NoContent
from flask_cors import CORS

# our memory-only pet storage
PETS = {}


def get_pets(limit, animal_type=None):
    return [pet for pet in PETS.values() if not animal_type or pet['animal_type'] == animal_type][:limit]


def get_pet(pet_id):
    pet = PETS.get(pet_id)
    return pet or ('Not found', 404)


def put_pet(pet_id, pet):
    exists = pet_id in PETS
    pet['id'] = pet_id
    if exists:
        logging.info('Updating pet %s..', pet_id)
        PETS[pet_id].update(pet)
    else:
        logging.info('Creating pet %s..', pet_id)
        pet['created'] = datetime.datetime.utcnow()
        PETS[pet_id] = pet
    return NoContent, (200 if exists else 201)


def delete_pet(pet_id):
    if pet_id in PETS:
        logging.info('Deleting pet %s..', pet_id)
        del PETS[pet_id]
        return NoContent, 204
    else:
        return NoContent, 404


def echo(message):
    return {'message': message}


def _base64_decode(encoded_str):
    # Add paddings manually if necessary.
    num_missed_paddings = 4 - len(encoded_str) % 4
    if num_missed_paddings != 4:
        encoded_str += b'=' * num_missed_paddings
    return base64.b64decode(encoded_str).decode('utf-8')


def auth_info():
    """Retrieves the authenication information from Google Cloud Endpoints."""
    encoded_info = connexion.request.headers.get('X-Endpoint-API-UserInfo', None)
    if encoded_info:
        info_json = _base64_decode(encoded_info)
        user_info = json.loads(info_json)
    else:
        user_info = {'id': 'anonymous'}
    return user_info


def auth_info_google_id_token():
    """Auth info with Google ID token."""
    return auth_info()


def auth_info_firebase():
    """Auth info with Firebase auth."""
    return auth_info()


def auth_info_oauth(token_info):
    return {'id': token_info.get('sub'), 'email': token_info.get('email')}


logging.basicConfig(level=logging.DEBUG)
app = connexion.App(__name__)
app.add_api('openapi.yaml')

CORS(app.app)

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
