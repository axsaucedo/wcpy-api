from flask import Flask
from flask_restful import Api

# TEMP... REMOVE FOR PROD
# Add path to the local wcpy class
import sys
sys.path.append("/Users/alejandrosaucedo/Programming/wcpy")

from resources import WCTextResource
from config import ENV, HOST, PORT, DEBUG

server = Flask(__name__)
api = Api(server)

# This function enables CORS in all requests
#   as our backend will be at a different address
@server.after_request
def after_request(response):
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
  response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
  return response

api.add_resource(WCTextResource, "/raw_text")


def run():
    server.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == "__main__":
    run()
