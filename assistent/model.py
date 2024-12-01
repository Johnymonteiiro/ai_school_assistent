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
                f"Total de Presenças: {res.payload['total_presenca']}, "
                f"Total de Faltas: {res.payload['total_falta']}, "
                f"Ocorrências: {', '.join(res.payload['ocorrencias'])}, "
                f"Turmas: {', '.join(res.payload['turmas'])}"
            )
            for res in resultados
        ])

        messages_role = [
            {
                "role": "system",
                "content": (
                    "Você é um modelo de IA Generativa especializado em análise educacional, previsão de evasão "
                    "escolar e estratégias de intervenção preventiva. NÃO RESPONDA perguntas ou forneça sugestões "
                    "fora dos dados fornecidos. Avalie sempre os dados antes de responder."
                    "Com base nos dados sejá capaz de fornrcer respostas curtas para perguntas direitas."
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

        # Chamada ao modelo de IA
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
