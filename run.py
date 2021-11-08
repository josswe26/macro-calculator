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

    print('\nUse this calculator to help you discover how much of each macronutrient you should eat every day to reach your goals.')


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
    unit = input('\nPlease select the system of measurement you would like to use.\n'
    '\nIf you would like to use the Metric system, please enter 1.\n'
    'If you would like to use the Imperial system, please enter 2.\n')

    if unit == '1':
        print('\nGreat, you have selected the Metric system.')
        return 1
    elif unit == '2':
        print('\nGreat, you have selected the Imperial system.')
        return 2
    else:
        print('\nInvalid selection. You need to enter 1 or 2 to select the desired unit.')
        select_unit()


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
            raise ValueError(f'The height value must be between 1 and {max_value}.')
    except ValueError as e:
        print(f'\nInvalid height. {e} Please provide your height again.')
        return False

    return True


def collect_weight(unit):
    '''
    Collect the user's weight in the selected unit
    to access it later in the program.
    '''
    weight = input(f'\nEnter your weight in {unit}:\n')

    if validate_weight(weight):
        return int(weight)
    else:
        collect_weight(unit)


def collect_height(unit):
    '''
    Collect the user's height in the selected unit
    to access it later in the program.
    '''
    height = input(f'\nEnter your height in {unit}:\n')

    if validate_height(height, unit):
        return int(height)
    else:
        collect_height(unit)


def convert_weight(weight_in_lbs):
    '''
    Convert the weight in lbs to kg
    '''
    weight_in_kg = weight_in_lbs / 2.205

    return int(round(weight_in_kg))


def main():
    '''
    Run all the functions of the program.
    '''
    welcome_message()
    name = collect_name()
    unit = select_unit()

    if unit == 1:
        weight_in_kg = collect_weight('kg')
        collect_height('cm')
    elif unit == 2:
        weight_in_lbs = collect_weight('pounds')
        collect_height('inch')

        weight_in_kg = convert_weight(weight_in_lbs)


main()
