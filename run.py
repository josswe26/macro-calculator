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
    Collect the user name to be able
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


def main():
    '''
    Run all the functions of the program.
    '''
    welcome_message()
    name = collect_name()
    unit = select_unit()


main()
