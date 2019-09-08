from flask_cors import CORS
from flask import Flask, request, json, jsonify, send_file
import os
import json
import logging
logging.getLogger().setLevel(logging.INFO)

from pyfcm import FCMNotification
app = Flask(__name__)
CORS(app)
FCM_APIKEY = 'AAAAMDfbpUs:APA91bFx3HK2UvyhzwZLEad_9N5J8leH5dK81uzzJJVt7oXHbNrKgdtryLbjp8bc4yP5MhSpH5xG0OPn6LfRKOBCAqDo53G8K1xGnLQ9fgnAQV_hrLT_1gKwlnOHTtl9gCC6XISNv7Rk'
def call2clients(registration_ids):
    push_service = FCMNotification(api_key=FCM_APIKEY)
    result = push_service.notify_multiple_devices(
        registration_ids=registration_ids,
        data_message={'phoneNumber': '18003333'})
    print(result)

# print(result)

@app.route("/pizza/call", methods=["POST"])
def call():
    if request.method == 'POST':
        registration_ids = ['eIKn6CD8Le4:APA91bH-JTx4czZH2kouyiiinjV3EcnbBjBX2EdDdNwdlHYKq1M9zUkTIKckYqoz6flhdil-r3eovb-uhZiD9ZU8MPSJuie4dM2i_kVxlD7Gr_vHWy4Sa0aYSfIbs8ViWhWsufoP64xk']
        call2clients(registration_ids)
    return json.dumps({
        'error_code': 0,
        'data_message':'Ok'
    })    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6789)