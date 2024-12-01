from flask import Blueprint, request, jsonify
from assistent.main import get_question

assistentAI_bp = Blueprint('assistentAI', __name__)


@assistentAI_bp.route('/assistent/question', methods=['POST'])
def ask_question():
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "A 'question' field is required"}), 400

    question = data["question"]
    answer = get_question(question)
    return jsonify({
        "result": {
            "user": {
                   "question": question,
                   },
            "assistent": {
                "answer": answer,
            }
        }
    }), 200


@assistentAI_bp.route('/assistent/answer', methods=['GET'])
def get_answer():
    return jsonify({"message": "Here is your answer"}), 200
