from design.menu_builder import MenuBuilder


def tell_your_name():
    name = input('My name is: ')
    return f'Hello, my name is {name}'


def solve_math():
    print(f'How much 5 + 5?')
    result = 5 + 5
    answer = int(input())
    if answer != result:
        return False
    return True


if __name__ == '__main__':
    menu = MenuBuilder('Available Menu'.upper(), 100)
    menu.register('a', 'Tell me your name!', tell_your_name)
    menu.register('b', 'Can you solve this math?', solve_math)
    menu.run()

    # output
    # ===========================================AVAILABLE MENU===========================================
    # a/ Tell me your name!
    # b/ Where do you live?
    # ====================================================================================================
