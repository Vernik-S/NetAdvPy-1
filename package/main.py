import datetime


from application.salary import calculate_salary
from application.db.people import get_employees

from package.dirty_main import *

if __name__ == '__main__':
    today = datetime.date.today()
    print("Today's date:", today)
    calculate_salary()
    print(get_employees())

    dirty_function()
