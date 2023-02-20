from design import character_wrappers


class MenuBuilder(object):
    menu: list = []
    menu_desc = None
    wrapper = None
    wrap_char = None
    state = True

    def __init__(self, menu_desc: str = 'MAIN MENU', max_char_length: int = 50, wrap_char: str = '='):
        self.menu_desc = menu_desc
        self.wrapper = character_wrappers.Design(max_char_length)
        self.wrap_char = wrap_char

    def register(self, key: str, value: str, fn=None):
        new_menu = {
            'key': str(key),
            'value': str(value),
            'fn': fn
        }
        self.menu.append(new_menu)

    def get_menu(self):
        print(self.wrapper.content_center(self.wrap_char, content=self.menu_desc))
        for menu_item in self.menu:
            print(menu_item['key'] + '/', menu_item['value'])
        print(self.wrapper.content_center(self.wrap_char))

    def process_menu(self, selected_menu):
        for menu_item in self.menu:
            if selected_menu == 'q' or 'Q':
                self.stop()
            if selected_menu == menu_item['key']:
                print(menu_item['fn']())
                print(self.wrapper.content_left_right('_', '(Press enter to continue.)', True))
                input()
                break

    def run(self):
        while self.state:
            self.get_menu()
            print()
            selected_menu = input('Select a menu: ')
            self.process_menu(selected_menu)

    def stop(self):
        self.state = False
