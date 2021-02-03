from fifth_homework_regular.regular_homework_edit_files import open_file as o_f
import re


class BookEditor:
    @classmethod
    def edit_names(cls):
        edited_list = []
        for res in o_f("phonebook_raw.csv"):
            pattern_ = re.compile(r"\b([А-Я]\w+)\s*,*([А-Я]\w+)\s*,*([А-Я]\w+\s*)*")
            res = pattern_.sub(r"\1, \2, \3", str(res))
            edited_list.append(res)
        return edited_list


    @classmethod
    def edit_numbers(cls):
        edited_list = []
        for res in cls.edit_names():
            pattern = re.compile(r"(\+?7|\+?8)\s?\-?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{2})\s?\-?(\d{2})")
            res = re.sub(pattern, "\1(\2)\3-\4-\5", str(res))
            edited_list.append(res)
        return edited_list


    @classmethod
    def edit_extra_numbers(cls):
        edited_list = []
        for res in cls.edit_names():
            pattern = re.compile(r"\(?([д][о][б]\.?)\s+?(\d+)\)?")
            res = re.sub(pattern, "\1\2", str(res))
            edited_list.append(res)
        return edited_list


    @classmethod
    def edit_list_to_new_list(cls):
        edited_list = []
        for i in cls.edit_extra_numbers():
            i = [element.strip("'[]") for element in i.split(", ")]
            edited_list.append(i)
        return edited_list


    @classmethod
    def edit_dublicate(cls):
        edited_list = []
        for one_row in cls.edit_list_to_new_list():
            if not one_row[0][0:7] in [i[0][0:7] for i in edited_list]:
                edited_list.append(one_row)
        return edited_list


a = BookEditor
print(a.edit_names())
print(a.edit_numbers())
print(a.edit_extra_numbers())
print(a.edit_list_to_new_list())
print(a.edit_dublicate())

