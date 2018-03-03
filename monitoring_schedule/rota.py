"""Output expected:

[
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
]


"""


PEOPLE = ['A', 'B', 'C', 'D', 'E']
DAYS_OF_THE_WEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
WEEKDAYS = DAYS_OF_THE_WEEK[:5]
WEEKENDS = DAYS_OF_THE_WEEK[5:]

def person_count_of_days():
    person_count_of_days = {}
    for person in PEOPLE:
        person_count_of_days[person] = 0
    return person_count_of_days

week_number = 0

person_count_of_days = person_count_of_days()

AMOUNT_OF_DAYS_IN_WEEK_ROTATION = 2
ROTATION_WEEKS = 5

rotation = []

# The final output, as a list of tuples of tuples
schedule = []

def start(week_number):
    populate_week()
    week_number =+ 1
    print(f'Finalise week {week_number}.')

def structure_week():
    count = 0
    while count <= ROTATION_WEEKS:
        schedule.append((('', '', '', '', ''), ('', '')))
        count += 1
    for i in schedule:
        print(i)

structure_week()

def _populate_schedule():
    number = 0
    count = 0
    while count < 5:
        schedule[number][0]
    count = 0

# For each week list, create a weekend list
# Then make a for iteration to append all weekends to list of week


def populate_week():
    for person in PEOPLE:
        for day in range(AMOUNT_OF_DAYS_IN_WEEK_ROTATION):
            # Index 0 refers to position of weekday.
            person_count_of_days[person] = person_count_of_days[person] + 1
    print(person_count_of_days)
    print(rotation)

def populate_weekends(week_number):
    available_engineers = PEOPLE.copy()
    current_saturday = populate_saturday(week_number, available_engineers)
    current_sunday = populate_sunday(week_number, available_engineers)
    # Then append to the lists.

def populate_saturday(week_number, available_engineers):
    pass

def populate_sunday(week_number, available_engineers):
    # Get most recent saturday
    # Get latest full weekend [this - 1]
    pass

def display_schedule():
    # people_schedule =
    pass

def consider_holidays():
    # to be implemented
    pass


start(week_number)
