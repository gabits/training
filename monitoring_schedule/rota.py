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

person_count_of_days = person_count_of_days()

AMOUNT_OF_DAYS_IN_WEEK_ROTATION = 2
AMOUNT_OF_WEEKS_IN_SCHEDULE = 5

rotation = []

# The final output, as a list of tuples of tuples
schedule = []

def start():
    generate_weekdays_schedule()
    # populate_weekend()
    print('Finalised schedule:')
    week_number = 1
    for week_schedule in schedule:
        print(week_number, week_schedule)
        week_number += 1

def calculate_schedule_sequence():
    rotation_sequence_of_people = []
    for person in PEOPLE:
        for day in range(AMOUNT_OF_DAYS_IN_WEEK_ROTATION):
            rotation_sequence_of_people.append(person)
            # Index 0 refers to position of weekday.
            # person_count_of_days[person] = person_count_of_days[person] + 1
    # print(person_count_of_days)
    return rotation_sequence_of_people

def _populate_week(schedule_sequence):
    week_list = []
    for i in range(5):
        person = schedule_sequence.pop(0)
        week_list.append(person)

    schedule.append(week_list)

    # TODO: Remove this; debugging purposes for now.
    print(schedule)

def generate_weekdays_schedule():
    week_count = 0
    calculated_schedule_sequence = calculate_schedule_sequence()
    schedule_sequence = calculated_schedule_sequence.copy()
    while week_count < AMOUNT_OF_WEEKS_IN_SCHEDULE:

        if schedule_sequence == []:
            schedule_sequence = calculated_schedule_sequence.copy()

        _populate_week(schedule_sequence)
        week_count += 1

# For each week list, create a weekend list
# Then make a for iteration to append all weekends to list of week
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


start()
