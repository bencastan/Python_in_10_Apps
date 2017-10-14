import datetime


def header():
    print('-------------------------------')
    print('         BIRTHDAY APP')
    print('-------------------------------')
    print()


def get_brithday_from_user():
    print('When were you born ')
    year = int(input('What year were you born [YYYY]?'))
    month = int(input('What month were you born [MM]?'))
    day = int(input('What day were you born[DD]?'))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def compute_years_old(original_date, target_date):
    years_old = target_date.year - original_date.year
    return years_old


def print_birthday_information(days, my_birthday, today, years):
    if days < 0:
        print("You had you birthday {} days ago this year.".format(-days))
        print("You were {} years old.".format(years))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
        print("You will be {} years old.".format(years))
    else:
        print("Happy Birthday!!!")
        print("You are {} years old today!!!".format(years))


def main():
    header()
    my_birthday = get_brithday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(my_birthday, today)
    years = compute_years_old(my_birthday, today)
    print_birthday_information(number_of_days, my_birthday, today, years)


main()
