from flask_restful import Resource, request
from wcpy import WCExtractor

class WCTextProcessorResource(Resource):
    def post(self):
        response = {}
        params = request.json

        if "raw_text" not in params:
            response["error"] = True
            response["error_message"] = "Raw text to process was not provided."

        raw_text = params["raw_text"]

        print(raw_text)


        return response
