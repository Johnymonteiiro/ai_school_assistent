import mysql.connector
import pandas as pd
import json


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
           results, 
           columns=[
           "matricula", "nome", "serie", "notas", "media", 
           "total_aula", "total_presenca", "total_falta", "ocorrencias",
            "turmas", "disciplinas", "ano_letivo", "semestre"
          ])
        
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
    JSON_ARRAYAGG(Nota.nota) AS notas,                  -- Cria uma lista com todas as notas
    ROUND(AVG(Nota.nota), 1) AS media,                            -- Calcula a média das notas
    COUNT(Aula.id_aula) AS total_aula, 
    COUNT(CASE WHEN Presenca.status = 'Presente' THEN Presenca.id_presenca END) AS total_presenca,
    COUNT(Aula.id_aula) - COUNT(CASE WHEN Presenca.status = 'Presente' THEN Presenca.id_presenca END) AS total_falta,
    (SELECT JSON_ARRAYAGG(Ocorrencias.descricao)
     FROM (
         SELECT DISTINCT Ocorrencia.descricao
         FROM Ocorrencia
         JOIN Historico_Ocorrencia ON Ocorrencia.id_ocorrencia = Historico_Ocorrencia.fk_Ocorrencia_id_ocorrencia
         WHERE Historico_Ocorrencia.fk_Aluno_id_aluno = Aluno.id_aluno
     ) Ocorrencias) AS ocorrencias,
    (SELECT JSON_ARRAYAGG(Turmas.nome)
     FROM (
         SELECT DISTINCT Turma.nome
         FROM Turma
         JOIN Nota ON Nota.fk_Turma_id_turma = Turma.id_turma
         WHERE Nota.fk_Aluno_id_aluno = Aluno.id_aluno
     ) Turmas) AS turmas,
    (SELECT JSON_ARRAYAGG(Disciplinas.nome_disciplina)
     FROM (
         SELECT DISTINCT Disciplina.nome_disciplina
         FROM Disciplina
         JOIN Turma ON Turma.fk_Disciplina_id_disciplina = Disciplina.id_disciplina
         JOIN Nota ON Nota.fk_Turma_id_turma = Turma.id_turma
         WHERE Nota.fk_Aluno_id_aluno = Aluno.id_aluno
     ) Disciplinas) AS disciplinas,
    Turma.ano_letivo AS ano_letivo,
    MAX(Turma.semestre) AS semestre                      -- Seleciona o semestre de forma única
FROM Aluno
LEFT JOIN Nota ON Aluno.id_aluno = Nota.fk_Aluno_id_aluno
LEFT JOIN Presenca ON Aluno.id_aluno = Presenca.fk_Aluno_id_aluno
LEFT JOIN Aula ON Presenca.fk_Aula_id_aula = Aula.id_aula
LEFT JOIN Turma ON Nota.fk_Turma_id_turma = Turma.id_turma
GROUP BY 
    Aluno.id_aluno, 
    Turma.ano_letivo;
"""
