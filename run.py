def welcome_message():
    '''
    Display the welcome message.
    '''
    print('''
    #     #
    #  #  # ###### #       ####   ####  #    # ######    #####  ####
    #  #  # #      #      #    # #    # ##  ## #           #   #    #
    #  #  # #####  #      #      #    # # ## # #####       #   #    #
    #  #  # #      #      #      #    # #    # #           #   #    #
    #  #  # #      #      #    # #    # #    # #           #   #    #
     ## ##  ###### ######  ####   ####  #    # ######      #    ####

                   #     #
                   ##   ##   ##    ####  #####   ####
                   # # # #  #  #  #    # #    # #    #
                   #  #  # #    # #      #    # #    #
                   #     # ###### #      #####  #    #
                   #     # #    # #    # #   #  #    #
                   #     # #    #  ####  #    #  ####

   #####
  #     #   ##   #       ####  #    # #        ##   #####  ####  #####
  #        #  #  #      #    # #    # #       #  #    #   #    # #    #
  #       #    # #      #      #    # #      #    #   #   #    # #    #
  #       ###### #      #      #    # #      ######   #   #    # #####
  #     # #    # #      #    # #    # #      #    #   #   #    # #   #
   #####  #    # ######  ####   ####  ###### #    #   #    ####  #    #
    ''')

    print('\nUse this calculator to help you discover how much of each '
          'macronutrient you should eat every day to reach your goals.')


def collect_name():
    '''
    Collect the user's name to be able
    to access it later in the program
    '''
    name = input('\nTo proceed, please enter your name: \n')
    print(f'\nThank you, {name.capitalize()}!')

    return name


def select_unit():
    '''
    Allow the user to make a selection of the desired
    system of measurement to be used in the program
    '''
    while True:
        unit = input('\nPlease select the system of measurement '
                     'you would like to use.\n'
                     '\nIf you would like to use the Metric system, '
                     'please enter 1.\n'
                     'If you would like to use the Imperial system, '
                     'please enter 2.\n')

        if unit == '1':
            print('\nGreat, you have selected the Metric system.')
            return 1
        elif unit == '2':
            print('\nGreat, you have selected the Imperial system.')
            return 2
        else:
            print('\nInvalid selection. You need to enter 1 or 2 '
                  'to select the desired unit.')
            continue


def validate_weight(weight):
    '''
    Validate the provided weight value.
    '''
    try:
        weight = int(weight)
        if weight < 1 or weight > 500:
            raise ValueError('The weight value must be between 1 and 500.')
    except ValueError as e:
        print(f'\nInvalid weight. {e} Please provide your weight again.')
        return False

    return True


def validate_height(height, unit):
    '''
    Validate the provided height value in cm.
    '''
    if unit == 'cm':
        max_value = 250
    else:
        max_value = 100

    try:
        height = int(height)
        if height < 1 or height > max_value:
            raise ValueError(f'The height value must be between '
                             '1 and {max_value}.')
    except ValueError as e:
        print(f'\nInvalid height. {e} Please provide your height again.')
        return False

    return True


def collect_weight(unit):
    '''
    Collect the user's weight in the selected unit
    to access it later in the program.
    '''
    while True:
        weight = input(f'\nEnter your weight in {unit}:\n')

        if validate_weight(weight):
            return int(weight)
        else:
            continue


def collect_height(unit):
    '''
    Collect the user's height in the selected unit
    to access it later in the program.
    '''
    while True:
        height = input(f'\nEnter your height in {unit}:\n')

        if validate_height(height, unit):
            return int(height)
        else:
            continue


def convert_weight(weight_in_lbs):
    '''
    Convert the weight in lbs to kg
    '''
    weight_in_kg = weight_in_lbs / 2.205

    return int(round(weight_in_kg))


def convert_height(height_in_inch):
    '''
    Convert the height in inch to cm
    '''
    height_in_cm = height_in_inch * 2.54

    return int(round(height_in_cm))


def select_gender():
    '''
    Allow the user to select their gender
    and return a dictionary including the gender and
    the value assigned to it to be used in the program
    '''
    while True:
        selection = input('\nPlease select your gender\n'
                          '\nFor female, please enter 1.\n'
                          'For male, please enter 2.\n')

        if selection == '1':
            print('\nFemale has been selected.')
            gender_data = {
                'gender': 'female',
                'value': -161
            }

            return gender_data

        elif selection == '2':
            print('\nMale has been selected')
            gender_data = {
                'gender': 'male',
                'value': 5
            }

            return gender_data

        else:
            print('\nInvalid selection. You need to enter 1 or 2 '
                  'to select your gender.')
            continue


def validate_age(age):
    '''
    Validate the provided age value.
    '''
    try:
        age = int(age)
        if age < 1 or age > 120:
            raise ValueError('The age value must be between 1 and 120.')
    except ValueError as e:
        print(f'\nInvalid age. {e} Please provide your age again.')
        return False

    return True


def collect_age():
    '''
    Collect the user's age to
    access it later in the program.
    '''
    while True:
        age = input(f'\nPlease provide your age:\n')

        if validate_age(age):
            return int(age)
        else:
            continue


def select_activity_level():
    '''
    Allow the user to select their activity level
    and return a dictionary including the chosen
    activity level and the value assigned to it
    '''
    while True:
        selection = input('\nSelect your activity level. '
                          'Please enter the value assigned to each level:\n'
                          '\n1. No activity (sedentary).'
                          '\n2. A little activity '
                          '(1 to 3 hours of exercise or sports per week)'
                          '\n3. Some activity '
                          '(4 to 6 hours of exercise or sports per week)'
                          '\n4. A lot of activity '
                          '(7 to 9 hours of exercise or sports per week)'
                          '\n5. A TON of activity '
                          '(10+ hours of exercise or sports per week)\n')

        if selection == '1':
            print('\nYou selected: No activity.')
            activity_data = {
                'activity level': 'no activity',
                'value': 1.2
            }

            return activity_data

        elif selection == '2':
            print('\nYou selected: A little activity')
            activity_data = {
                'activity level': 'a little activity',
                'value': 1.375
            }

            return activity_data

        elif selection == '3':
            print('\nYou selected: Some activity')
            activity_data = {
                'activity level': 'some activity',
                'value': 1.55
            }

            return activity_data

        elif selection == '4':
            print('\nYou selected: A lot of activity')
            activity_data = {
                'activity level': 'a lot of activity',
                'value': 1.725
            }

            return activity_data

        elif selection == '5':
            print('\nYou selected: A TON of activity')
            activity_data = {
                'activity level': 'a TON of activity',
                'value': 1.9
            }

            return activity_data

        else:
            print('\nInvalid selection. '
                  'You need to enter a number between 1 and 5 '
                  'to select your activitu level.')
            continue


def main():
    '''
    Run all the functions of the program.
    '''
    welcome_message()
    name = collect_name()
    unit = select_unit()

    weight_in_kg = None
    weight_in_lbs = None
    height_in_cm = None
    height_in_inch = None

    if unit == 1:
        weight_in_kg = collect_weight('kg')
        height_in_cm = collect_height('cm')
    elif unit == 2:
        weight_in_lbs = collect_weight('pounds')
        height_in_inch = collect_height('inch')

        weight_in_kg = convert_weight(weight_in_lbs)
        height_in_cm = convert_height(height_in_inch)

    gender_data = select_gender()
    age = collect_age()
    activity_data = select_activity_level()


main()
