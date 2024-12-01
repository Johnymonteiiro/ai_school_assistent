

from flask import Flask
from flask_cors import CORS
from routes import assistentAI_bp, get_users_bp
from lib.qdrant import create_qdrant_collections
from db.connection import get_data_from_DB, student_query
from assistent.student_data import store

app = Flask(__name__)
CORS(app)

collections = ["alunos"]
dimensions = 384
data = get_data_from_DB(student_query)

create_qdrant_collections(collections, dimensions)

store("alunos", data)

app.register_blueprint(assistentAI_bp)
app.register_blueprint(get_users_bp)

if __name__ == '__main__':
    app.run(debug=True)
