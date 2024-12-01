import mysql.connector
import pandas as pd


import mysql.connector
import pandas as pd


def get_data_from_DB(query):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='school',
            user='root',
            password='master'
        )

        cursor = conn.cursor()

        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        data = pd.DataFrame(
            results, columns=["matricula", "nome", "serie", "media", "total_aula",
                              "total_presenca", "total_falta", "ocorrencias", "turmas"]
        )
        return data

    except mysql.connector.Error as db_error:
        print(f"Erro no banco de dados: {db_error}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        try:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        except NameError:
            pass


student_query = """
    SELECT 
    Aluno.matricula, 
    Aluno.nome, 
    Aluno.serie, 
    AVG(Nota.nota) AS media, 
    COUNT(Aula.id_aula) AS total_aula, 
    COUNT(CASE WHEN Presenca.status = 'Presente' THEN Presenca.id_presenca END) AS total_presenca,
    COUNT(Aula.id_aula) - COUNT(CASE WHEN Presenca.status = 'Presente' THEN Presenca.id_presenca END) AS total_falta,
    JSON_ARRAYAGG(Ocorrencia.descricao) AS ocorrencias, 
    JSON_ARRAYAGG(Turma.nome) AS turmas
FROM Aluno
LEFT JOIN Nota ON Aluno.id_aluno = Nota.fk_Aluno_id_aluno
LEFT JOIN Presenca ON Aluno.id_aluno = Presenca.fk_Aluno_id_aluno
LEFT JOIN Aula ON Presenca.fk_Aula_id_aula = Aula.id_aula
LEFT JOIN Historico_Ocorrencia ON Aluno.id_aluno = Historico_Ocorrencia.fk_Aluno_id_aluno
LEFT JOIN Ocorrencia ON Historico_Ocorrencia.fk_Ocorrencia_id_ocorrencia = Ocorrencia.id_ocorrencia
LEFT JOIN Turma ON Nota.fk_Turma_id_turma = Turma.id_turma
GROUP BY Aluno.id_aluno;
"""
