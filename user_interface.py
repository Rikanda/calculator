""" This file is for user interface. Coded by Alexander Konukhov. """
import sys
from excep import *


def main_menu() -> None:
    """ This function is for main menu of calculator. """
    print("""Calculator welcomes you!
    
    
Working with:
1 - rational
2 - complex
0 - exit
""")

    mode = validation_mode()
    if mode == 0:
        print("Thank you for using our calculator! See you next time.")
        sys.exit()
    choose_calculation(mode)


def choose_calculation(mode) -> None:
    """ This function is for available operations for chosen mode. """
    if mode == 1:
        print("""Operations:
1 - sum
2 - sub
3 - mult
4 - div
5 - pow
6 - sqrt
0 - previous menu
""")
        operation = validation_operation(mode)
    else:
        print("""Operations:
1 - sum
2 - sub
3 - mult
4 - div
0 - previous menu
""")
        operation = validation_operation(mode)
    if operation == 0:
        main_menu()
    else:
        input_data(mode, operation)


def input_data(number_type, main_operation) -> None:
    """ This function is for numbers input from user for mode. """
    if number_type == 1:
        number_real_1, number_real_2 = validation_rational_input(main_operation)
        print(number_real_1, number_real_2)
        if main_operation == 4:
            code_for_additional_operation = show_additional_operations(number_type)
            print(code_for_additional_operation)
    else:
        number_complex_1, number_complex_2 = validation_complex_input(main_operation)
        print(number_complex_1, number_complex_2)


def show_additional_operations(mode) -> int:
    """ This function is additional operation for div function. """
    print("""Operations:
1 - '/'
2 - '//'
3 - '%
0 - previous menu
""")
    add_operation_code = validation_additional_operation()
    if add_operation_code == 0:
        choose_calculation(mode)
    else:
        return validation_additional_operation()


#main_menu()  # - раскомментить, чтобы глянуть, как оно тут работает
# все print()-ы со значениями сейчас для отладки.
