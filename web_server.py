"""
A first simple Cloud Foundry Flask app
Author: Ian Huston
License: See LICENSE.txt
"""
from flask import Flask
import os
import time
import datetime
import threading

# ============ CONSTANTS ===============================================================================================

PORT = 9099
NAME = "Web Server"

# ============ LOCAL VARIABLES =========================================================================================

app = Flask(NAME)
port = int(os.getenv("PORT", PORT))
stats_dictionary = {}


# ============ FUNCTIONS ===============================================================================================

def _run():
    app.run(host='0.0.0.0', port=port)

def run():
    thread = threading.Thread(target=_run)
    thread.start()

# ============ ROUTES ==================================================================================================

@app.route('/')
def index():
    return "Hey there! Test app seems to be up and running just fine!<br><br>" \
           "Up time: {0}<br>".format(str(datetime.timedelta(seconds=(time.time() - stats_dictionary["start_time"]))))


# ============ MAIN ====================================================================================================

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    run()


