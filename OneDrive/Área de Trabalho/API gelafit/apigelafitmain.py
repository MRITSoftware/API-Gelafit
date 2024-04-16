from flask import Flask, jsonify

from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
)

ACCESS_ID = "uaudm3vf4ay5dj4t8rxj"
ACCESS_KEY = "040d52898c314df5a66fe8e16263b322"
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"

app = Flask(_name_)

# Inicializa a API Tuya
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Inicializa o serviço de fila de mensagens
open_pulsar = TuyaOpenPulsar(
    ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
)

@app.route('/ligar_placa', methods=['POST'])
def ligar_placa():
    device_id = "eb7774abb31d1903d1ip7l"
    response = openapi.post(f"/v1.0/devices/{device_id}/commands", {
        "commands": [{
            "code": "countdown_1",
            "value": 2
        }]
    })
    return jsonify({"status": "Placa ligada com sucesso!"})

if _name_ == '_main_':
    app.run(host='192.168.56.1', debug=False)