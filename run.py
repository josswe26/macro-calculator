from prettytable import PrettyTable, ALL
import textwrap


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

    print('\n' + textwrap.fill('Use this calculator to help you discover '
                               'how much of each macronutrient you should eat '
                               'every day to reach your goals.', 80))


def collect_name():
    '''
    Collect the user's name and return the value
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
    Collect the user's weight in the selected
    unit and return the value
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
    and return a dictionary including the gender data
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
    Collect the user's age and return the value
    '''
    while True:
        age = input(f'\nPlease provide your age:\n')

        if validate_age(age):
            return int(age)
        else:
            continue


def select_activity_level():
    '''
    Allow the user to select their activity level and
    return a dictionary including the activity level data
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
    a dictionary including the goal data
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
                'rate': None,
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
    Calculate the user's basal metabolic rate (BMR) using
    the data provided by the user and return the result
    '''
    print(f'\nCalculating your basal metabolic rate (BMR)...')

    bmr = (9.99 * weight) + (6.25 * height) - (4.92 + age) + gender_value

    return bmr


def calculate_tdee(bmr, activity_value):
    '''
    Calculate the user's total daily energy expenditure (TDEE)
    using the BMR data and the activity level and return the result
    '''
    print(f'\nCalculating your total daily energy expenditure (TDEE)...')

    tdee = bmr * activity_value

    return tdee


def calculate_goal_calories(tdee, goal_value):
    '''
    Calculate the total calories per day
    depending on the selected goal
    '''
    print(f'\nCalculating your total calories...')

    goal_calories = tdee * goal_value

    return goal_calories


def validate_macro(macro_percentage):
    '''
    Validate the provided macro percentage value.
    '''
    try:
        percentage = int(macro_percentage)
        if percentage < 1 or percentage > 100:
            raise ValueError('The percentage value must be between 1 and 100.')
    except ValueError as e:
        print(f'\nInvalid percentage. {e} '
              'Please provide your percentage again.')
        return False

    return True


def collect_macro(macro_type):
    '''
    Allow the user to input a custom macro
    percentage and return the value
    '''
    while True:
        macro = input(f'\nPlease enter the desired {macro_type} percentage:\n')

        if validate_macro(macro):
            return int(macro)
        else:
            continue


def validate_percentage(*args):
    '''
    Validate the total percentage value.
    '''
    try:
        percentage = 0
        for num in args:
            percentage += num
        if percentage != 100:
            raise ValueError('The total percentage value must be exactly 100.')
    except ValueError as e:
        print(f'\nInvalid input. {e} Please try again.')
        return False

    return True


def select_diet():
    '''
    Allow the user to select their prefered diet
    and return the macronutrient split data
    '''
    while True:
        diet_selection = input('\nTo be able to calculate your daily macros, '
                               'choose your prefered diet. '
                               '\nPlease enter the value '
                               'assigned to the desired diet:\n'
                               '\n1. Balanced.'
                               '\n2. Low-carb.'
                               '\n3. High-carb.'
                               '\n4. High-protein.'
                               '\n5. Ketogenic.'
                               '\n6. Custom (Advanced users only).\n')

        if diet_selection == '1':

            print('\nYou chose to follow a balanced diet.')

            macro_data = {'diet': 'balanced', 'protein': 0.4,
                          'carbs': 0.3, 'fat': 0.3}

            return macro_data

        elif diet_selection == '2':

            print('\nYou chose to follow a low-carb diet.')

            macro_data = {'diet': 'low-carb', 'protein': 0.4,
                          'carbs': 0.2, 'fat': 0.4}

            return macro_data

        elif diet_selection == '3':

            print('\nYou chose to follow a high-carb diet.')

            macro_data = {'diet': 'high-carb', 'protein': 0.3,
                          'carbs': 0.5, 'fat': 0.2}

            return macro_data

        elif diet_selection == '4':

            print('\nYou chose to follow a high-protein diet.')

            macro_data = {'diet': 'high-protein', 'protein': 0.5,
                          'carbs': 0.25, 'fat': 0.25}

            return macro_data

        elif diet_selection == '5':

            print('\nYou chose to follow a ketogenic diet.')

            macro_data = {'diet': 'ketogenic', 'protein': 0.4,
                          'carbs': 0.1, 'fat': 0.5}

            return macro_data

        elif diet_selection == '6':
            while True:
                protein = collect_macro('protein')
                carbs = collect_macro('carbs')
                fat = collect_macro('fat')

                if validate_percentage(protein, carbs, fat):

                    macro_data = {
                        'diet': 'custom', 'protein': protein / 100,
                        'carbs': carbs / 100, 'fat': fat / 100
                        }

                    return macro_data

                else:
                    continue

        else:
            print('\nInvalid selection. '
                  'You need to enter a number between 1 and 6 '
                  'to choose the desired diet.')
            continue


def calculate_macro(macro, goal_calories, percentage):
    '''
    Calculates the macronutrient
    daily grams to be consumed daily
    depending on the user's goal
    '''
    grams_per_day = goal_calories * percentage

    if macro == 'protein' or macro == 'carbs':
        grams_per_day /= 4
    elif macro == 'fat':
        grams_per_day /= 9

    return int(round(grams_per_day))


def data_review(name, age, gender, weight, height,
                weight_unit, height_unit, activity_level,
                goal_data, diet):
    '''
    Display the data input by the user for review
    and allow the user to enter the data again if
    a mistake has been made
    '''
    print(f'\nThank you for you input, {name.capitalize()}.'
          '\nPlease review the data you provided:\n')

    table = PrettyTable(header=False, hrules=ALL)

    table.add_row(['Name', name.capitalize()])
    table.add_row(['Age', f'{age} years old'])
    table.add_row(['Gender', gender.capitalize()])

    table.add_row(['Weight', f'{weight} {weight_unit}'])
    table.add_row(['Height', f'{height} {height_unit}'])

    table.add_row(['Activity Level', activity_level.capitalize()])

    if goal_data["rate"]:
        table.add_row(['Goal', f'{goal_data["goal"].capitalize()}'
                       f'\nat a {goal_data["rate"]} rate.'])
    else:
        table.add_row(['Goal', f'{goal_data["goal"].capitalize()}'])

    table.add_row(['Diet', diet.capitalize()])

    print(table)

    data_correct = input('\nIs the data provided correct?'
                         "\nTo continue, please enter 'y'."
                         "\nTo enter the data again, "
                         "please enter 'n'.\n").lower()

    if data_correct == 'n':
        main()


def display_data(name, bmr, tdee, activity_level,
                 goal_data, goal_calories, macro_data,
                 protein_grams, carbs_grams, fat_grams):
    '''
    Format and display the data
    '''
    print(f'\nGreat, {name.capitalize()}! Here are your results:')

    print(f'\nYour BMR is: {round(bmr)} calories.')
    print('\n' + textwrap.fill('BMR or basal metabolic rate, is the '
                               'average amount of calories your body '
                               'requires every day to fuel essential '
                               'functions like breathing, pumping blood, '
                               'producing hormones, and so forth (basically, '
                               ' it’s how many calories you’d burn resting '
                               'for 24 hours).', 70))

    print(f'\nPracticing {activity_level} per week, your TDEE will be: '
          f'{round(tdee)} calories.')
    print('\n' + textwrap.fill('TDEE or total daily energy expended is '
                               'the average amount of calories you '
                               'burn per day.', 70))

    print(f'\nTo reach your goal of {goal_data["goal"]}', end='')

    if goal_data['rate']:
        print(f' at a {goal_data["rate"]} rate,')
    else:
        print(',')

    print(f'you will need to consume {round(goal_calories)} calories per day.')

    print(f'\nFinally, following a {macro_data["diet"]} diet, '
          'you will need to consume the following macronutrients:\n')

    table = PrettyTable()

    table.field_names = ['Macro', 'Percentage', 'Grams per day']

    table.add_row(['Protein',
                   f'{int(macro_data["protein"] * 100)}%',
                   f'{protein_grams}g'])

    table.add_row(['Carbs',
                   f'{int(macro_data["carbs"] * 100)}%',
                   f'{carbs_grams}g'])

    table.add_row(['Fat',
                   f'{int(macro_data["fat"] * 100)}%',
                   f'{fat_grams}g'])

    print(table)


def main():
    '''
    Run all the functions of the program.
    '''
    name = collect_name()

    age = collect_age()
    gender_data = select_gender()

    unit = select_unit()

    weight_in_kg = None
    weight_in_lbs = None
    height_in_cm = None
    height_in_inch = None

    if unit == 1:
        weight_in_kg = collect_weight('kg')
        height_in_cm = collect_height('cm')
    elif unit == 2:
        weight_in_lb = collect_weight('lb')
        height_in_inch = collect_height('inch')

        weight_in_kg = convert_weight(weight_in_lb)
        height_in_cm = convert_height(height_in_inch)

    activity_data = select_activity_level()

    goal_data = select_goal()

    macro_data = select_diet()

    if unit == 1:
        data_review(name, age,
                    gender_data['gender'],
                    weight_in_kg, height_in_cm, 'kg', 'cm',
                    activity_data['activity level'],
                    goal_data, macro_data['diet'])
    if unit == 2:
        data_review(name, age,
                    gender_data['gender'],
                    weight_in_lb, height_in_inch, 'lb', 'inch',
                    activity_data['activity level'],
                    goal_data, macro_data['diet'])

    bmr = calculate_bmr(weight_in_kg, height_in_cm, age, gender_data['value'])

    tdee = calculate_tdee(bmr, activity_data['value'])

    goal_calories = calculate_goal_calories(tdee, goal_data['value'])

    protein_grams = calculate_macro('protein',
                                    goal_calories,
                                    macro_data['protein'])
    carbs_grams = calculate_macro('carbs',
                                  goal_calories,
                                  macro_data['carbs'])
    fat_grams = calculate_macro('fat',
                                goal_calories,
                                macro_data['fat'])

    display_data(name, bmr, tdee, activity_data['activity level'],
                 goal_data, goal_calories, macro_data,
                 protein_grams, carbs_grams, fat_grams)


welcome_message()
main()
