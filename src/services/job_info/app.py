from flask import Flask, request, jsonify
from driver import main
from supabase_client import supabase_client
from flask_cors import CORS, cross_origin


'''
Flask endpoint that express.js will communicate with
This is a microservice
'''


app = Flask(__name__)
cors = CORS(app, supports_credentials=True)

@app.route("/")
def defaultPage():
    return (
        "<title> Flask Scraper/Crawler Microservice </title>"
        "<html>    "
        "<h1>This is the homepage for the Scraper/Crawler microservice.</h1>"
        "<h3><strong>How to use the microservice:</strong></h3>"
        "<p>To trigger the endpoint: Point the browser to \"/scrape/[limit]\" with \'limit\' being a number.</p>"
        "<p></p>"
        ""
        ""
        ""
        ""
        "</html>" 
    )

'''
This is the route that triggers scrape job (located in driver.py)
'''

@app.route("/scrape/<int:scrape_limit>", methods=["GET", "POST"])
@cross_origin()
def run_pipeline(scrape_limit):
    print("Attempting to run pipeline from Flask pipeline...")
    try:
        print("running pipeline from Flask endpoint...")
        json_result_container = []
        result = main(supabase_client, scrape_limit, json_result_container)
        return jsonify({"status": "success", "data": json_result_container}), 200
    except Exception as error:
        return jsonify({"status": "error", "message": str(error)}), 500


    