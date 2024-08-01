import json
from urllib.parse import parse_qs
from flask import request, jsonify, Blueprint

from Services.senderMailService import Sender
from Services.configCorsService import configure_cors

REQUEST_API = Blueprint('graph', __name__)

@REQUEST_API.route("/send_email", methods=['POST'])
def send_mail():
		data = request.get_json()  # Use request.get_json() para JSON
		try:
				result = Sender(data)
				if result == "E-mail enviado":
						return configure_cors(jsonify({"success": True, "message": "E-mail enviado com sucesso", "resultado": result}))
				else:
						return configure_cors(jsonify({"success": False, "message": result, "resultado": result}))
		except Exception as e:
				return configure_cors(jsonify({"success": False, "message": f"Erro ao converter os dados: {str(e)}"}))
		
		return "Ok "
