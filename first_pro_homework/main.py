from first_pro_homework.application.salary import calculate_salary as c_s
from first_pro_homework.application.db.people import get_employes as g_e
import datetime

if __name__ == "__main__":
    print(c_s())
    print(g_e())
    print(datetime.datetime.today())
