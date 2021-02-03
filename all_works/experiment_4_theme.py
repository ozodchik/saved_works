import sqlalchemy
import psycopg2


create_engine = sqlalchemy.create_engine("postgresql://postgres:Ozodchik2712@localhost:5432/experiment")
# print(create_engine)


connecting = create_engine.connect()
# print(connecting)


checking_tables = create_engine.table_names()
# print(checking_tables)


checking_columns = connecting.execute("SELECT * FROM first_table").fetchall()
# print(checking_columns)


# add_attr_name = connecting.execute("""INSERT INTO first_table(name, surname)
#     VALUES ('Ozod', 'ochilboyev'), ('SHamsiya', 'dehkanova'), ('Xushvaqt', 'dehkanov'), ('Nargiza', 'ochilboyeva'), ('Oydin', 'ochilboyeva');
# """)
# print(add_attr_name)


#
# checking_attr = connecting.execute('''SELECT * FROM first_table''').fetchall()
# print(checking_attr)


# add_attr_number = connecting.execute('''INSERT INTO numbers(number)
#     VALUES ('1'), ('2'), ('3'), ('4'), ('5');
# ''')
# print(add_attr_number)


# checking_attr_number = connecting.execute('''SELECT * FROM numbers''').fetchall()
# print(checking_attr_number)


find_max_from_numbers = connecting.execute('''SELECT MAX(number) FROM numbers''').fetchall()
print(find_max_from_numbers)


find_min_from_numbers = connecting.execute('''SELECT MIN(number) FROM numbers''').fetchall()
print(find_min_from_numbers)


find_avg_from_numbers = connecting.execute('''SELECT AVG(number) FROM numbers''').fetchall()
print(find_avg_from_numbers)


find_count_unique_surnames = connecting.execute('''SELECT COUNT(DISTINCT surname) FROM first_table''').fetchall()
print(find_count_unique_surnames)


find_sum_avg_numbers = connecting.execute('''SELECT SUM(number), AVG(number) FROM numbers ''').fetchall()
print(find_sum_avg_numbers)


double_select = connecting.execute('''SELECT number FROM numbers
    WHERE number <= (
        SELECT AVG(number) FROM numbers);
''').fetchall()
print(double_select)


group_surname = connecting.execute('''SELECT surname, COUNT(*) FROM first_table
    GROUP BY surname    
''').fetchall()
print(group_surname)


#
# full_table_numbers_ids = connecting.execute('''INSERT INTO  numbers_ids(number_id)
#     VALUES ('6'), ('7'), ('8'), ('9'), ('10');
# ''')
# checking_table_numbers = connecting.execute('''SELECT number_id FROM numbers_ids''').fetchall()
# print(checking_table_numbers)


# group_surname_by_having = connecting.execute('''SELECT surname FROM first_table
#     GROUP BY surname
#     HAVING COUNT(surname) <= 1;
# ''').fetchall()
# print(group_surname_by_having)


# cut_by_surname = connecting.execute('''SELECT surname FROM first_table
#     WHERE surname LIKE '%%deh%%'
#     GROUP BY surname;
# ''').fetchall()
# print(cut_by_surname)


# cut_by_numbers = connecting.execute('''SELECT number FROM numbers
#     WHERE number > 2
#     GROUP BY number
#     HAVING COUNT(number) >= 1;
# ''').fetchall()
# print(cut_by_numbers)


#
# left_join = connecting.execute('''SELECT number FROM numbers LEFT JOIN numbers_ids ON numbers.number = numbers_ids.number_id;''').fetchall()
# print(left_join)


