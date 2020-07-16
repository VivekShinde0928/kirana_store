"""
Author  : Vivek Shinde
Date    : 20/06/2020
purpose : Practice problem solving
code    : Kirana store(adding numbers till q is pressed)

"""


if __name__ == '__main__':
    my_list = []
    while True:
        input_number = input("Enter number : ")
        if input_number.isnumeric():
            x = my_list.append(int(input_number))
            # print(my_list)
        elif input_number == 'q':
            y = 0
            for i in my_list:
                i = y + i
                y = i
            print(f'\nYour result is {y}')
            break
        else:
            print("\nplease enter correct number or 'q' to print the result ")



