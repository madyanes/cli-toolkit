import character_wrappers


class MenuBuilder(object):
    menu: list = []
    menu_desc = None
    wrapper = None
    wrap_char = None

    def __init__(self, menu_desc: str = 'MAIN MENU', max_char_length: int = 50, wrap_char: str = '='):
        self.menu_desc = menu_desc
        self.wrapper = character_wrappers.Design(max_char_length)
        self.wrap_char = wrap_char

    def register(self, key: str, value: str, fn=None):
        new_menu = {
            'key': str(key),
            'value': str(value)
        }
        self.menu.append(new_menu)

    def get_menu(self):
        print(self.wrapper.content_center(self.wrap_char, content=self.menu_desc))
        for menu_item in self.menu:
            print(menu_item['key'] + '/', menu_item['value'])
        print(self.wrapper.content_center(self.wrap_char))


if __name__ == '__main__':
    menu = MenuBuilder('Available Menu'.upper())
    menu.register('a', 'Tell me your name!')
    menu.register('b', 'Where do you live?')
    menu.get_menu()

    # output
    # ==================AVAILABLE MENU==================
    # a/ Tell me your name!
    # b/ Where do you live?
    # ==================================================
