import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine("postgresql://owner_doc_editor:owner_doc_editor@localhost:5432/doc_editor")
connection = engine.connect()


def add_doc():
    doc_number = input("Вводите номер документа:")
    doc_owner = input("Вводите имя и фамилию владельца документа(пример:Геннадий Покемонов):")
    add_doc_owner_to_database = connection.execute(f"INSERT INTO users(name)"
                                                   f"VALUES('{doc_owner}');")
    add_doc_to_database = connection.execute(f"INSERT INTO documents(docs_number, owner_id)"
                                             f"VALUES('{doc_number}', '{2}');")


def check_documents():
    check_doc = input("vvodite nomer documenta:")
    check_process = connection.execute(f"SELECT * FROM documents "
                                       f"WHERE docs_number = {check_doc}").fetchall()

    return print(check_process)


check_documents()