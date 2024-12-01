
from lib.qdrant import embedding_model, qdrant_db


def store(collection_name: str = "alunos", data=[]):
    if len(data) == 0:
        print("Fail to fetch data: matricula, nome, serie, media, total_aula, total_presenca, total_falta, ocorrencias, turmas")
        return

    for _, row in data.iterrows():
        try:
            ocorrencias = row.get('ocorrencias', [])
            if not isinstance(ocorrencias, list):
                ocorrencias = [ocorrencias]

            turmas = row.get('turmas', [])
            if not isinstance(turmas, list):
                turmas = [turmas]

            content_data = (
                f"Matricula: {row['matricula']}, "
                f"Nome: {row['nome']}, "
                f"Série: {row['serie']}, "
                f"Média: {row['media']}, "
                f"Total de Aulas: {row['total_aula']}, "
                f"Total de Presenças: {row['total_presenca']}, "
                f"Total de Faltas: {row['total_falta']}, "
                f"Ocorrências: {', '.join(map(str, ocorrencias))}, "
                f"Turmas: {', '.join(map(str, turmas))}"
            )

            embedding = embedding_model.encode(content_data).tolist()
            id_value = int(''.join(filter(str.isdigit, row["matricula"])))

            qdrant_db.upsert(
                collection_name=collection_name,
                points=[{
                    "id": id_value,
                    "vector": embedding,
                    "payload": {
                        "matricula": row["matricula"],
                        "nome": row["nome"],
                        "serie": row["serie"],
                        "media": row["media"],
                        "total_aula": row["total_aula"],
                        "total_presenca": row["total_presenca"],
                        "total_falta": row["total_falta"],
                        "ocorrencias": ocorrencias,
                        "turmas": turmas
                    }
                }]
            )
            print(f"Aluno {row['nome']} indexado com sucesso!")
        except KeyError as e:
            print(f"Erro ao processar linha: Chave ausente {e}")
        except Exception as e:
            print(f"Erro inesperado ao indexar aluno: {e}")


def search_qdrant(question: str, collection_name: str, limit: int = 5):
    try:
        cleaned_question = " ".join(question.split())
        embedding_pergunta = embedding_model.encode(cleaned_question).tolist()

        question_result = qdrant_db.search(
            collection_name=collection_name,
            query_vector=embedding_pergunta,
            limit=limit
        )

        return question_result

    except ValueError as ve:
        print(f"Processing question fail: {ve}")
        return []
    except Exception as e:
        print(f"Inespected Qdrant query: {e}")
        return []
