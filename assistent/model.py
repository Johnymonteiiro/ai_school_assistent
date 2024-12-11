from assistent.assistent_prompt import assistent_prompt as prompt
from lib.openAI import client


def assistent_model(question: str, resultados: list) -> str:

    try:
        # Construção do contexto com os dados fornecidos
        contexto = "\n".join([
            (
                f"Matricula do aluno: {res.payload['matricula']}, "
                f"Nome: {res.payload['nome']}, "
                f"Série: {res.payload['serie']}, "
                f"Média: {res.payload['media']}, "
                f"Total de Aulas: {res.payload['total_aula']}, "
                f"Semestre: {res.payload['semestre']}, "
                f"Ano letivo: {res.payload['ano_letivo']}, "
                f"Total de Presenças: {res.payload['total_presenca']}, "
                f"Total de Faltas: {res.payload['total_falta']}, "
                f"Ocorrências: {
                    ', '.join(map(str, res.payload['ocorrencias'] or ['Nenhuma ocorrência']))}, "
                f"Turmas: {
                    ', '.join(map(str, res.payload['turmas'] or ['Nenhuma turma']))}, "
                f"Disciplinas: {
                    ', '.join(map(str, res.payload['disciplinas'] or ['Nenhuma disciplina']))}, "
                f"Notas: {
                    ', '.join(map(str, res.payload['notas'] or ['Sem notas']))}"
            )
            for res in resultados
        ])

        # Definindo o papel de "system" e "user"
        messages_role = [
            {
                "role": "system",
                "content": (
                    "Você é um modelo de IA Generativa especializado em análise educacional, previsão de evasão "
                    "Apresente sempre dados numericos se possível as percentagem e os insights "
                    "escolar e estratégias de intervenção preventiva. NÃO RESPONDA perguntas ou forneça sugestões "
                    "fora dos dados fornecidos. Avalie sempre os dados antes de responder. "
                    "Com base nos dados fornecidos, seja capaz de fornecer respostas curtas para perguntas diretas."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"{prompt}\n\n"
                    f"[DADOS FORNECIDOS]\n{contexto}\n\n"
                    f"[PERGUNTA]\n{question}"
                ),
            },
        ]

        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_role,
            temperature=0.4,
            max_tokens=5000,
        )

        return resposta.choices[0].message.content

    except KeyError as e:
        return f"Erro: Dados ausentes ou inválidos ({e})."
    except Exception as e:
        return f"Erro inesperado: {e}"
