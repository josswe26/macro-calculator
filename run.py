from prettytable import PrettyTable, ALL
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap


# COLOR TAGS

i_color = Fore.LIGHTGREEN_EX        # Input color
e_color = Back.RED + Fore.WHITE     # Error color
d_color = Fore.LIGHTYELLOW_EX       # Data color
dim = Style.DIM                     # Dim text
reset_all = Style.RESET_ALL         # Reset to normal


# OUTPUT FUNCTIONS

def welcome_message():
    '''
    Display the welcome logo and message
    '''
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
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

    print(reset_all)
    print(textwrap.fill('Use the Macro Calculator to help you discover how '
                        'much of each macronutrient you should eat every day '
                        'to reach your goals.', 80))
    print()
    print(textwrap.fill('A macronutrient (“macro”) is a nutrient that '
                        'your body needs in large amounts to survive, with '
                        'the main ones being protein, carbs, and fat. If you '
                        'want to gain muscle, lose fat, and get strong, you '
                        'generally want to follow a high-protein, moderate- '
                        'to high-carb, moderate- to low-fat diet.', 80))


def data_review(name, age, gender, weight, height,
                weight_unit, height_unit, activity_level,
                goal_data, diet):
    '''
    Display the data input by the user for review
    and allow the user to enter the data again if
    a mistake has been made
    '''
    print(f'\nThank you for your input, {name.capitalize()}.'
          '\nPlease review the data you provided:\n')

    # Create table to display data to review
    table = PrettyTable(header=False, hrules=ALL)

    table.add_row(['Name', d_color + name.capitalize() + reset_all])
    table.add_row(['Age', d_color + f'{age}' + reset_all + ' years old'])
    table.add_row(['Gender', d_color + gender.capitalize() + reset_all])

    table.add_row(['Weight', d_color + f'{weight}' +
                  reset_all + f' {weight_unit}'])
    table.add_row(['Height', d_color + f'{height}' +
                  reset_all + f' {height_unit}'])

    table.add_row(['Activity Level', d_color +
                   activity_level.capitalize() +
                   reset_all])

    # Print rate text only if rate data available. Not for Mantain weight
    if goal_data["rate"]:
        table.add_row(['Goal', d_color +
                      goal_data["goal"].capitalize() +
                      reset_all + '\nat a ' + d_color +
                      goal_data["rate"] +
                      reset_all + ' rate.'])
    else:
        table.add_row(['Goal', d_color +
                      goal_data["goal"].capitalize() +
                      reset_all])

    table.add_row(['Diet', d_color + diet.capitalize() + reset_all])

    print(table)

    data_correct = input(i_color +
                         '\nIs the data provided correct?'
                         "\nTo continue, please enter 'y'."
                         "\nTo enter the data again, "
                         "please enter 'n'.\n" +
                         reset_all).lower()

    if data_correct == 'n':
        return False
    else:
        return True


def display_data(name, bmr, tdee, activity_level,
                 goal_data, goal_calories, macro_data,
                 protein_grams, carbs_grams, fat_grams):
    '''
    Format and display the data
    '''
    print(f'\nGreat, {name.capitalize()}! Here are your results:')

    print('\nYour BMR is: ' +
          d_color +
          f'{round(bmr)} ' +
          reset_all +
          'calories.')

    print('\n' + dim +
          textwrap.fill('BMR or basal metabolic rate, is the '
                        'average amount of calories your body '
                        'requires every day to fuel essential '
                        'functions like breathing, pumping blood, '
                        'producing hormones, and so forth (basically, '
                        ' it’s how many calories you’d burn resting '
                        'for 24 hours).', 70) + reset_all)

    print('\nPracticing ' + d_color + f'{activity_level}' + reset_all +
          ' per week, your TDEE will be: ' + d_color +
          f'{round(tdee)}' + reset_all + ' calories.')
    print('\n' + dim + textwrap.fill('TDEE or total daily energy expended is '
                                     'the average amount of calories you '
                                     'burn per day.', 70) + reset_all)

    print('\nTo reach your goal of ' + d_color +
          goal_data["goal"] + reset_all, end='')

    if goal_data['rate']:
        print(' at a ' + d_color + goal_data["rate"] + reset_all + ' rate,')
    else:
        print(',')

    print('you will need to consume ' + d_color + f'{round(goal_calories)}' +
          reset_all + ' calories per day.')

    print('\nFinally, to follow a ' + d_color + macro_data["diet"] +
          reset_all + ' diet, you will need to consume the '
          'following macronutrients:\n')

    table = PrettyTable()

    # Create table to display macro data
    table.field_names = ['Macro', 'Percentage', 'Grams per day']

    table.add_row(['Protein',
                   f'{int(macro_data["protein"] * 100)}%',
                   d_color + f'{protein_grams}' +
                   reset_all + ' g'])

    table.add_row(['Carbs',
                   f'{int(macro_data["carbs"] * 100)}%',
                   d_color + f'{carbs_grams}' +
                   reset_all + ' g'])

    table.add_row(['Fat',
                   f'{int(macro_data["fat"] * 100)}%',
                   d_color + f'{fat_grams}' +
                   reset_all + ' g'])

    print(table)


# INPUT FUNCTIONS

def collect_name():
    '''
    Collect the user's name and return the value
    '''
    while True:
        name = input(i_color +
                     '\nTo proceed, please enter your name: \n' +
                     reset_all)

        if validate_name(name):
            print(f'\nThank you, {name.capitalize()}!')
            return name
        else:
            continue


def collect_age():
    '''
    Collect the user's age and return the value
    '''
    while True:
        age = input(i_color +
                    '\nPlease provide your age:\n' +
                    reset_all)

        if validate_age(age):
            return int(age)
        else:
            continue


def select_gender():
    '''
    Allow the user to select their gender
    and return a dictionary including the gender data
    '''
    while True:
        gender_selection = input(i_color +
                                 '\nPlease select your gender\n'
                                 '\nFor female, please enter 1.\n'
                                 'For male, please enter 2.\n' +
                                 reset_all)

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
            print('\n' + e_color +
                  'Invalid selection. You need to enter 1 or 2 '
                  'to select your gender.' +
                  reset_all)
            continue


def select_unit():
    '''
    Allow the user to make a selection of the desired
    system of measurement to be used in the program
    '''
    while True:
        unit = input(i_color +
                     '\nPlease select the system of measurement '
                     'you would like to use.\n'
                     '\nIf you would like to use the Metric system '
                     '(kg / cm), please enter 1.\n'
                     'If you would like to use the Imperial system '
                     '(lb / inch), please enter 2.\n' +
                     reset_all)

        if unit == '1':
            print('\nGreat, you have selected the Metric system.')
            return 1
        elif unit == '2':
            print('\nGreat, you have selected the Imperial system.')
            return 2
        else:
            print('\n' + e_color +
                  'Invalid selection. You need to enter 1 or 2 '
                  'to select the desired unit.' +
                  reset_all)
            continue


def collect_weight(unit):
    '''
    Collect the user's weight in the selected
    unit and return the value
    '''
    while True:
        weight = input(i_color +
                       f'\nEnter your weight in {unit}:\n' +
                       reset_all)

        if validate_weight(weight):
            return int(weight)
        else:
            continue


def collect_height(unit):
    '''
    Collect the user's height in the selected unit
    to access it later in the program
    '''
    while True:
        height = input(i_color +
                       f'\nEnter your height in {unit}:\n' +
                       reset_all)

        if validate_height(height, unit):
            return int(height)
        else:
            continue


def select_activity_level():
    '''
    Allow the user to select their activity level and
    return a dictionary including the activity level data
    '''
    while True:
        level_selection = input(i_color +
                                '\nSelect your activity level. '
                                '\nPlease enter a value between 1 and 5 '
                                'to select the desired level:\n'
                                '\n1. No activity (sedentary).'
                                '\n2. A little activity '
                                '(1 to 3 hours of exercise or sports per week)'
                                '\n3. Some activity '
                                '(4 to 6 hours of exercise or sports per week)'
                                '\n4. A lot of activity '
                                '(7 to 9 hours of exercise or sports per week)'
                                '\n5. A TON of activity (10+ hours of '
                                'exercise or sports per week)\n' +
                                reset_all)

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
            print('\n' + e_color +
                  'Invalid selection. '
                  'You need to enter a number between 1 and 5 '
                  'to select your activity level.' +
                  reset_all)
            continue


def select_goal():
    '''
    Allow the user to select their goal and return
    a dictionary including the goal data
    '''
    while True:
        goal_selection = input(i_color +
                               '\nChoose your goal. '
                               '\nPlease enter a value between 1 and 3 '
                               'to selecet the desired goal:\n'
                               '\n1. Lose weight.'
                               '\n2. Maintain weight'
                               '\n3. Gain weight\n' +
                               reset_all)

        if goal_selection == '1':
            while True:
                rate_selection = input(i_color +
                                       '\nHow would you like to lose weight? '
                                       '\nPlease enter a value between 1 and '
                                       '3 to select the desired rate:\n'
                                       '\n1. Slow (approx. 0.25 kg / '
                                       '0.5 lb per week).'
                                       '\n2. Moderate (approx. 0.5 kg / '
                                       '1 lb per week).'
                                       '\n3. Fast (approx. 1 kg / '
                                       '2 lb per week).\n' +
                                       reset_all)

                # Select rate to lose weight
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
                    print('\n' + e_color +
                          'Invalid selection. '
                          'You need to enter a number between 1 and 3 '
                          'to select the desired rate.' +
                          reset_all)
                    continue

        # Maintain weight does not have any rate
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
                rate_selection = input(i_color +
                                       '\nHow would you like to gain weight? '
                                       '\nPlease enter a value between 1 and '
                                       '3 to select the desired rate:\n'
                                       '\n1. Slow (approx. 0.25 kg / '
                                       '0.5 lb per week).'
                                       '\n2. Moderate (approx. 0.5 kg / '
                                       '1 lb per week).'
                                       '\n3. Fast (approx. 1 kg / '
                                       '2 lb per week).\n' +
                                       reset_all)

                # Select rate to gain weight
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
                    print('\n' + e_color +
                          'Invalid selection. '
                          'You need to enter a number between 1 and 3 '
                          'to select the desired rate.' +
                          reset_all)
                    continue

        else:
            print('\n' + e_color +
                  'Invalid selection. '
                  'You need to enter a number between 1 and 3 '
                  'to select the desired goal.' +
                  reset_all)
            continue


def select_diet():
    '''
    Allow the user to select their prefered diet
    and return the macronutrient split data
    '''
    while True:
        diet_selection = input(i_color +
                               '\nTo be able to calculate your daily macros, '
                               'choose your prefered diet. '
                               '\nPlease enter a value between 1 and 6'
                               'to select the desired diet:\n'
                               '\n1. Balanced.'
                               '\n2. Low-carb.'
                               '\n3. High-carb.'
                               '\n4. High-protein.'
                               '\n5. Ketogenic.'
                               '\n6. Custom (Advanced users only).\n' +
                               reset_all)

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
            print('\n' + e_color +
                  'Invalid selection. '
                  'You need to enter a number between 1 and 6 '
                  'to choose the desired diet.' +
                  reset_all)
            continue


def collect_macro(macro_type):
    '''
    Allow the user to input a custom macro
    percentage and return the value
    '''
    while True:
        macro = input(i_color +
                      '\nPlease enter the desired '
                      f'{macro_type} percentage:\n' +
                      reset_all)

        if validate_macro(macro):
            return int(macro)
        else:
            continue


def restart_program():
    '''
    Allow the user to run the application
    once again or exit
    '''
    run_again = input(i_color +
                      '\nWould you like to run the Macro Calculator '
                      'once again?'
                      "\nTo run again, please enter 'y'."
                      "\nTo exit, please enter 'n'.\n" +
                      reset_all).lower()

    if run_again == 'n':
        print('\nThank you for using Macro Calculator. See you next time!')
        return False
    else:
        return True


# VALIDATION FUNCTIONS

def validate_name(name):
    '''
    Validate the provided name value
    '''
    try:
        # Validate that name contains any characters
        if len(name) <= 0:
            raise ValueError("The name can't be left empty.")
    except ValueError as e:
        print('\n' + e_color +
              f'Invalid name. {e} Please provide your name again.' +
              reset_all)
        return False

    return True


def validate_weight(weight):
    '''
    Validate the provided weight value
    '''
    try:
        weight = int(weight)
        if weight < 1 or weight > 500:
            raise ValueError('The weight value must be between 1 and 500.')
    except ValueError as e:
        print('\n' + e_color +
              f'Invalid weight. {e} Please provide your weight again.' +
              reset_all)
        return False

    return True


def validate_height(height, unit):
    '''
    Validate the provided height value in cm
    '''
    if unit == 'cm':
        max_value = 250
    else:
        max_value = 100

    try:
        height = int(height)
        if height < 1 or height > max_value:
            raise ValueError(f'The height value must be between '
                             f'1 and {max_value}.')
    except ValueError as e:
        print('\n' + e_color +
              f'Invalid height. {e} Please provide your height again.' +
              reset_all)
        return False

    return True


def validate_age(age):
    '''
    Validate the provided age value
    '''
    try:
        age = int(age)
        if age < 1 or age > 120:
            raise ValueError('The age value must be between 1 and 120.')
    except ValueError as e:

        print('\n' + e_color +
              f'Invalid age. {e} Please provide '
              'your age again.' +
              reset_all)

        return False

    return True


def validate_macro(macro_percentage):
    '''
    Validate the provided macro percentage value
    '''
    try:
        percentage = int(macro_percentage)
        if percentage < 1 or percentage > 100:
            raise ValueError('The percentage value must be between 1 and 100.')
    except ValueError as e:
        print('\n' + e_color +
              f'Invalid percentage. {e} '
              'Please provide your percentage again.' +
              reset_all)
        return False

    return True


def validate_percentage(*args):
    '''
    Validate the total percentage value
    '''
    try:
        percentage = 0
        for num in args:
            percentage += num
        if percentage != 100:
            raise ValueError('The total percentage value must be exactly 100.')
    except ValueError as e:
        print('\n' + e_color +
              f'Invalid input. {e} Please try again.' +
              reset_all)
        return False

    return True


# CONVERSION FUNCTIONS

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


# CALCULATION FUNCTIONS


def calculate_bmr(weight, height, age, gender_value):
    '''
    Calculate the user's basal metabolic rate (BMR) using
    the data provided by the user and return the result
    '''
    print(dim +
          '\nCalculating your basal metabolic rate (BMR)...' +
          reset_all)

    # Mifflin-St Jeor formula to caculate BMR
    # Male BMR =
    # [9.99 x weight (kg)] + [6.25 x height (cm)] – [4.92 x age (years)] + 5
    # Female BMR =
    # [9.99 x weight (kg)] + [6.25 x height (cm)] – [4.92 x age (years)] – 161
    bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) + gender_value

    return bmr


def calculate_tdee(bmr, activity_value):
    '''
    Calculate the user's total daily energy expenditure (TDEE)
    using the BMR data and the activity level and return the result
    '''
    print(dim +
          '\nCalculating your total daily energy expenditure (TDEE)...' +
          reset_all)

    # Calculate TDEE depending on the activity level
    tdee = bmr * activity_value

    return tdee


def calculate_goal_calories(tdee, goal_value):
    '''
    Calculate the total calories per day
    depending on the selected goal
    '''
    print(dim +
          '\nCalculating your total calories...' +
          reset_all)

    # Calculate goalcalories depending on the user's goal
    goal_calories = tdee * goal_value

    return goal_calories


def calculate_macro(macro, goal_calories, percentage):
    '''
    Calculates the macronutrient
    daily grams to be consumed daily
    depending on the user's goal
    '''
    print(dim + f'\nCalculating {macro}...' + reset_all)

    grams_per_day = goal_calories * percentage

    if macro == 'protein' or macro == 'carbs':
        grams_per_day /= 4
    elif macro == 'fat':
        grams_per_day /= 9

    return int(round(grams_per_day))


# MAIN FUNCTION

def main():
    '''
    Run all the functions of the program.
    '''
    welcome_message()

    while True:
        name = collect_name()

        age = collect_age()
        gender_data = select_gender()

        unit = select_unit()

        # Collect weight and height depending on the unit selected
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

        data_correct = True

        # Display the data depending on the unit selected
        if unit == 1:
            data_correct = data_review(name, age,
                                       gender_data['gender'],
                                       weight_in_kg, height_in_cm,
                                       'kg', 'cm',
                                       activity_data['activity level'],
                                       goal_data, macro_data['diet'])
        if unit == 2:
            data_correct = data_review(name, age,
                                       gender_data['gender'],
                                       weight_in_lb, height_in_inch,
                                       'lb', 'inch',
                                       activity_data['activity level'],
                                       goal_data, macro_data['diet'])

        # Restart the program if the user does not approve the data
        if not data_correct:
            continue

        bmr = calculate_bmr(weight_in_kg, height_in_cm,
                            age, gender_data['value'])

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

        run_again = restart_program()

        # Exit or run program again depending on user's request
        if not run_again:
            break


main()
