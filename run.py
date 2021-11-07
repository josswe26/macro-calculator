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
    return input('\nTo proceed, please enter your name: \n')


def main():
    '''
    Run all the functions of the program.
    '''
    welcome_message()
    name = collect_name()
    print(f'Your name is: {name}')


main()
