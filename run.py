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
        gender_selection = input('\nPlease select your gender\n'
                                 '\nFor female, please enter 1.\n'
                                 'For male, please enter 2.\n')

        if gender_selection == '1':
            print('\nFemale has been selected.')
            gender_data = {
                'gender': 'female',
                'value': -161
            }

            return gender_data

        elif gender_selection == '2':
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
        level_selection = input('\nSelect your activity level. '
                                'Please enter the value '
                                'assigned to each level:\n'
                                '\n1. No activity (sedentary).'
                                '\n2. A little activity '
                                '(1 to 3 hours of exercise or sports per week)'
                                '\n3. Some activity '
                                '(4 to 6 hours of exercise or sports per week)'
                                '\n4. A lot of activity '
                                '(7 to 9 hours of exercise or sports per week)'
                                '\n5. A TON of activity '
                                '(10+ hours of exercise or sports per week)\n')

        if level_selection == '1':
            print('\nYou selected: No activity.')
            activity_data = {
                'activity level': 'no activity',
                'value': 1.2
            }

            return activity_data

        elif level_selection == '2':
            print('\nYou selected: A little activity')
            activity_data = {
                'activity level': 'a little activity',
                'value': 1.375
            }

            return activity_data

        elif level_selection == '3':
            print('\nYou selected: Some activity')
            activity_data = {
                'activity level': 'some activity',
                'value': 1.55
            }

            return activity_data

        elif level_selection == '4':
            print('\nYou selected: A lot of activity')
            activity_data = {
                'activity level': 'a lot of activity',
                'value': 1.725
            }

            return activity_data

        elif level_selection == '5':
            print('\nYou selected: A TON of activity')
            activity_data = {
                'activity level': 'a TON of activity',
                'value': 1.9
            }

            return activity_data

        else:
            print('\nInvalid selection. '
                  'You need to enter a number between 1 and 5 '
                  'to select your activity level.')
            continue


def select_goal():
    '''
    Allow the user to select their goal and return
    a dictionary including the chosen goal, the
    selected rate and the value assigned to it
    '''
    while True:
        goal_selection = input('\nChoose your goal. '
                               'Please enter the value '
                               'assigned to each goal:\n'
                               '\n1. Lose weight.'
                               '\n2. Maintain weight'
                               '\n3. Gain weight\n')

        if goal_selection == '1':
            while True:
                rate_selection = input('\nHow would you like to lose weight? '
                                       'Please enter the value '
                                       'assigned to each rate:\n'
                                       '\n1. Slow (0.5 lb per week).'
                                       '\n2. Moderate (1 lb per week).'
                                       '\n3. Fast (2 lb per week)\n')

                if rate_selection == '1':
                    print('\nYou would like to lose weight at a slow rate.')

                    goal_data = {
                        'goal': 'lose weight',
                        'rate': 'slow',
                        'value': 0.91
                    }

                    return goal_data

                elif rate_selection == '2':
                    print('\nYou would like to lose '
                          'weight at a moderate rate.')

                    goal_data = {
                        'goal': 'lose weight',
                        'rate': 'moderate',
                        'value': 0.82
                    }

                    return goal_data

                elif rate_selection == '3':
                    print('\nYou would like to lose weight at a fast rate.')

                    goal_data = {
                        'goal': 'lose weight',
                        'rate': 'fast',
                        'value': 0.65
                    }

                    return goal_data

                else:
                    print('\nInvalid selection. '
                          'You need to enter a number between 1 and 3 '
                          'to select the desired rate.')
                    continue

        elif goal_selection == '2':
            print('\nYou would like to maintain your weight.')
            goal_data = {
                'goal': 'maintain weight',
                'value': 1
            }

            return goal_data

        elif goal_selection == '3':
            while True:
                rate_selection = input('\nHow would you like to gain weight? '
                                       'Please enter the value '
                                       'assigned to each rate:\n'
                                       '\n1. Slow (0.5 lb per week).'
                                       '\n2. Moderate (1 lb per week).'
                                       '\n3. Fast (2 lb per week)\n')

                if rate_selection == '1':
                    print('\nYou would like to gain weight at a slow rate.')

                    goal_data = {
                        'goal': 'gain weight',
                        'rate': 'slow',
                        'value': 1.08
                    }

                    return goal_data

                elif rate_selection == '2':
                    print('\nYou would like to gain '
                          'weight at a moderate rate.')

                    goal_data = {
                        'goal': 'gain weight',
                        'rate': 'moderate',
                        'value': 1.17
                    }

                    return goal_data

                elif rate_selection == '3':
                    print('\nYou would like to gain weight at a fast rate.')

                    goal_data = {
                        'goal': 'gain weight',
                        'rate': 'fast',
                        'value': 1.34
                    }

                    return goal_data

                else:
                    print('\nInvalid selection. '
                          'You need to enter a number between 1 and 3 '
                          'to select the desired rate.')
                    continue

        else:
            print('\nInvalid selection. '
                  'You need to enter a number between 1 and 3 '
                  'to select the desired goal.')
            continue


def calculate_bmr(weight, height, age, gender_value):
    '''
    Calculate the user's basal metabolic rate (BMR)
    using the data provided by the user
    '''
    bmr = (9.99 * weight) + (6.25 * height) - (4.92 + age) + gender_value

    print(f'\nYour basal metabolic rate (BMR) is {bmr} calories.')

    return bmr


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
        weight_in_lbs = collect_weight('lb')
        height_in_inch = collect_height('inch')

        weight_in_kg = convert_weight(weight_in_lbs)
        height_in_cm = convert_height(height_in_inch)

    gender_data = select_gender()
    age = collect_age()
    activity_data = select_activity_level()
    goal_data = select_goal()
    bmr = calculate_bmr(weight_in_kg, height_in_cm, age, gender_data['value'])


main()
