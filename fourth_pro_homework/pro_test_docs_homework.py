documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def id_doc(doc_number):
    result = True
    for doc_key in documents:
        if doc_number == doc_key["number"]:
            result = True
            return result
        elif doc_number != doc_key["number"]:
            result = False
    return result


def a_shelf(doc_number):
    result = True
    for doc_key, doc_value in directories.items():
        if doc_number in doc_value:
            result = True
            print(f"Number a shelf: {doc_key}")
            return result
        else:
            result = False
    return result


def doc_list():
    res_for_test = True
    for doc_id in documents:
        doc_type = doc_id['type']
        doc_number = doc_id['number']
        doc_name = doc_id['name']
        result = ('{0}"{1}" "{2}"'.format(doc_type, doc_number, doc_name))
    return res_for_test


def add_doc(doc_type, doc_number, person_name, doc_shelf):
    new_doc = dict(type=doc_type, number=doc_number, name=person_name)
    if doc_shelf not in directories.keys():
        return "полки не существует поэтому документ не добавлен"
    else:
        directories[doc_shelf] += [doc_number]
        documents.append(new_doc)
        if (new_doc in documents) and (doc_shelf in directories.keys()):
            res = True
            return res
        else:
            res = False
            return res


