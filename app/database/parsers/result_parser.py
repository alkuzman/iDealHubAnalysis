from app.database.parsers.document_parser import document_parse
from app.database.parsers.word_parser import word_parse


def result_parse(result):
    result_list = []
    obj = {}
    counter = 0
    for record in result:
        counter += 1
        for node in record:
            if "Document" in record[node].labels:
                obj = document_parse(record[node])
            elif "Word" in record[node].labels:
                obj = word_parse(record[node])
            result_list.append(obj)
    if counter > 1:
        return result_list
    else:
        return obj

