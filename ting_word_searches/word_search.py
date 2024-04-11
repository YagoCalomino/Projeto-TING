def exists_word(word, instance):
    result = []  # Resultado inicial
    for item in instance.items:
        file_path = item['nome_do_arquivo']
        occurrences = []  # Ocorrências iniciais
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Encontrar ocorrências
            line_numbers = [index for index, line in enumerate(lines, start=1)
                            if word.lower() in line.lower()]
            occurrences = [{'linha': num} for num in line_numbers]
        if occurrences:  # Adicionar ao resultado
            result.append({
                'palavra': word,
                'arquivo': file_path,
                'ocorrencias': occurrences
            })
    return result  # Retornar resultado


def search_by_word(word, instance):
    result = []  # Resultado inicial
    for item in instance.items:
        file_path = item['nome_do_arquivo']
        occurrences = []  # Ocorrências iniciais
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                if word.lower() in line.lower():
                    occurrence = {'linha': idx, 'conteudo': line.strip()}
                    occurrences.append(occurrence)
            if occurrences:  # Adicionar ao resultado
                result_item = {
                    "palavra": word,
                    "arquivo": file_path,
                    "ocorrencias": occurrences
                }
                result.append(result_item)
    return result  # Retornar resultado
