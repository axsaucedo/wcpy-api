from flask import Flask
from flask_restful import Api

# TEMP... REMOVE FOR PROD
# Add path to the local wcpy class
import sys
sys.path.append("/Users/alejandrosaucedo/Programming/wcpy")
print(sys.path)

from config import ENV, HOST, PORT, DEBUG
from resources import WCTextProcessorResource

wc_app = Flask(__name__)
wc_api = Api(wc_app)

# This function enables CORS in all requests
#   as our backend will be at a different address
@wc_app.after_request
def after_request(response):
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
  response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
  return response

wc_api.add_resource(WCTextProcessorResource, "/text")


def run():
    wc_app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == "__main__":
    run()
