from flask_restful import Resource, request
from wcpy import WCExtractor, WCExtractorProcessor

class WCTextResource(Resource):
    def post(self):
        params = request.json

        if not params or "raw_text" not in params or "sorted_list" not in params:
            response = {}
            response["error"] = True
            response["error_message"] = "Raw text or sorted_list attribute was not provided."
            return response

        raw_text = params["raw_text"]
        sorted_list = params["sorted_list"]

        default_doc_name = "text_resource_api"

        lines = raw_text.split("\n")

        d_words = {}

        extractor = WCExtractor()
        for line in lines:
            extractor.extract_wc_from_line(line, default_doc_name, d_words=d_words)

        if sorted_list:
            processor = WCExtractorProcessor()
            d_list = processor.process_dict_wc_to_list(d_words)
            response = d_list

        else:
            response = d_words

        return response
