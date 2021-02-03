from all_works.first_pro_package.imports_package import Track, docs
while True:
    def search():
        doc_number = input("введите номер документа:")
        result = True
        for doc_key in docs:
            if doc_number == doc_key["name"]:
                result = doc_key["doc"]
                return result
            elif doc_number != doc_key["name"]:
                result = "владелец не существует или номер введен неправильно"
        return result

    def commands():
        print("commands: a = get doc ")
        command = input("command:")
        if command == "a":
            return search()
        else:
            print(f' not command ')
            return commands()





print(commands())
a = Track("ozod", "ochilboyev")
print(a.names())
print(a.surnames())