from assistent.model import assistent_model
from assistent.student_data import search_qdrant


def get_question(question: str):
    colletion_name = "alunos"
    limit = 8
    resut_search_query = search_qdrant(question, colletion_name, limit)
    answear = assistent_model(question, resut_search_query)

    return answear
