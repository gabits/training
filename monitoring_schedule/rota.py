"""You have a list of people who'll be assigned to take care of a system.
During the week, the system behaves differently than in the weekends, and
therefore the schedule varies according to each day:

- There'll be at least 4 people in the rotation.

- On weekdays, each person will be assigned an amount of sequenced days
which takes continuity in every working day (mon-fri).

- During the weekends, each day should be filled by a different person.
One person should not take two consecutive days or two consecutive weekends
in the rota.

- The weekend schedule should be aware of the working week schedule, so
each person assigned in the weekend will not be the same one as in the previous
or next day of the rota, e.g. the person assigned to Saturday should not be the
same one assigned on the latest friday neither in the upcoming Sunday.

This program should not consider any holidays or unexpected events initially.
"""


PEOPLE_IN_ROTATION = ['A', 'B', 'C', 'D', 'E']

AMOUNT_OF_DAYS_IN_WEEK_ROTATION = 2
AMOUNT_OF_DAYS_IN_WEEKEND_ROTATION = 1
AMOUNT_OF_WEEKS_IN_SCHEDULE = 5


def start():
    """Sets up a schedule for the PEOPLE_IN_ROTATION according to the
    AMOUNT_OF_DAYS_IN_WEEK_ROTATION and AMOUNT_OF_WEEKS_IN_SCHEDULE.
    """
    weekdays_populated_schedule = generate_weekdays_schedule()
    schedule = generate_weekend_schedule(weekdays_populated_schedule)
    print('Finalised schedule:')
    display_schedule(schedule)


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
    days_to_be_filled = AMOUNT_OF_WEEKS_IN_SCHEDULE * 5

    days_filled = 0
    while days_filled <= days_to_be_filled:
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

    schedule.append([week_list])
    return schedule, sequence_of_available_people


def generate_weekdays_schedule():
    """Generates a schedule for all weekdays by taking the available people for the
    rotation and inserting them in order into a sequence of 5-element lists, which
    refers to the amount of working days within a week.

    Returns:
        - schedule: an ordered list of lists, one for each week.
    """
    schedule = []

    schedule_sequence = calculate_schedule_sequence(AMOUNT_OF_DAYS_IN_WEEK_ROTATION)

    week_count = 0
    while week_count < AMOUNT_OF_WEEKS_IN_SCHEDULE:

        schedule, sequence_of_available_people = _populate_week_and_add_to_schedule(
                schedule, schedule_sequence)
        week_count += 1

    return schedule


# def person_count_of_days():
#     """This function mounts a dictionary to keep track of each person's rota day on
#     the weekends to be used by populate_saturday() and populate_sunday() when comparing
#     the amount of days a person has already been assigned to in a weekend.
#     """
#     person_count_of_days = {}
#     for person in PEOPLE_IN_ROTATION:
#         person_count_of_days[person] = 0
#     return person_count_of_days
#
# person_count_of_days = person_count_of_days()


def generate_weekend_schedule(schedule):
    """Generates a schedule for all weekends by taking the available people for the
    rotation and inserting them in order into a sequence of 5-element lists, which
    refers to the amount of working days within a week.

    Returns:
        - schedule: the original schedule with a weekend appended to each list.
    """
    available_people = calculate_schedule_sequence(AMOUNT_OF_DAYS_IN_WEEKEND_ROTATION)
    amount_of_weekends = AMOUNT_OF_WEEKS_IN_SCHEDULE
    weekend_rota = []
    count = 1
    for weekend in range(amount_of_weekends):
        # This will be replaced by the populate_saturday and populate_sunday methods.
        for i in range(2):
            person = available_people.pop(0)
            weekend_rota.append(person)

        schedule[weekend].insert(count, weekend_rota)
        weekend_rota = []
        count += 1
    return schedule


# def _populate_saturday(schedule, available_people):
#     return available_people[0]


# def populate_sunday(week_number, available_engineers):
#     # Get most recent saturday
#     # Get latest full weekend [this - 1]
#     pass


def display_schedule(schedule):
    week_number = 1
    for week_schedule in schedule:
        print(week_number, week_schedule)
        week_number += 1


start()
