"""Output expected:

[
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
    (('', '', '', '', ''), ('', '')),
]


"""


PEOPLE_IN_ROTATION = ['A', 'B', 'C', 'D', 'E']

def person_count_of_days():
    person_count_of_days = {}
    for person in PEOPLE_IN_ROTATION:
        person_count_of_days[person] = 0
    return person_count_of_days

person_count_of_days = person_count_of_days()

AMOUNT_OF_DAYS_IN_WEEK_ROTATION = 2
AMOUNT_OF_WEEKS_IN_SCHEDULE = 5


def start():
    weekdays_populated_schedule = generate_weekdays_schedule()
    schedule = populate_weekends(weekdays_populated_schedule)
    print('Finalised schedule:')
    week_number = 1
    for week_schedule in schedule:
        print(week_number, week_schedule)
        week_number += 1

def calculate_schedule_sequence(rotation_days):
    """Calculates the sequence to be used in the required schedule taking
    into account the amount of days for the rotation.

    Args:
        - rotation_days: the amount of sequenced days each person will be
        assigned to.

    Returns:
         - rotation_sequence_of_people: a sequence of assigned people to
         fill the schedule.
    """
    rotation_sequence_of_people = []
    DAYS_TO_BE_FILLED = AMOUNT_OF_WEEKS_IN_SCHEDULE * 5

    days_filled = 0
    while days_filled <= DAYS_TO_BE_FILLED:
        for person in PEOPLE_IN_ROTATION:
            for day in range(rotation_days):
                rotation_sequence_of_people.append(person)
                days_filled += 1
    return rotation_sequence_of_people


def _populate_week_and_add_to_schedule(schedule, sequence_of_available_people):
    """Populates an individual week according to the schedule sequence provided.
    At the end, appends this list to the current schedule.

    Args:
        - schedule: an ordered list of lists, one for each week
        - sequence_of_available_people: a sequence with the next people to be
        inserted into the schedule.

    Returns:
        - schedule: the original list with a new week added.
        - sequence_of_available_people: the original sequence minus the first five
        elements provided.
    """

    week_list = []
    for i in range(5):
        person = sequence_of_available_people.pop(0)
        week_list.append(person)

    schedule.append(week_list)
    return schedule, sequence_of_available_people


def generate_weekdays_schedule():
    """Generate a schedule for all weekdays by taking the available people for the
    rotation and inserting them in order into a sequence of 5-element lists, which
    refers to the amount of working days within a week.

    Returns:
        - schedule: an ordered list of lists, one for each week.
    """
    schedule = []

    calculated_schedule_sequence = calculate_schedule_sequence(AMOUNT_OF_DAYS_IN_WEEK_ROTATION)

    week_count = 0
    while week_count < AMOUNT_OF_WEEKS_IN_SCHEDULE:

        schedule, sequence_of_available_people = _populate_week_and_add_to_schedule(
                schedule, calculated_schedule_sequence)
        week_count += 1

    return schedule

# For each week list, create a weekend list
# Then make a for iteration to append all weekends to list of week
def populate_weekends(schedule):
    available_people = PEOPLE_IN_ROTATION.copy()
    # current_saturday = populate_saturday(week_number, available_people)
    # current_sunday = populate_sunday(week_number, available_people)
    return schedule

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
