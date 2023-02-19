import os


class Wrapper(object):
    """
    Centering string wrapped with any characters.
    """
    def content_center(self, max_length: int, filled_characters: str = '-', content: str = '') -> str:
        terminal_width, terminal_height = os.get_terminal_size()
        if terminal_width < max_length:
            max_length = terminal_width
        if not content:
            content = str(filled_characters)
        return content.center(max_length, filled_characters)


if __name__ == '__main__':
    wrapper = Wrapper()
    result = wrapper.content_center(100, '_')
    print(result)

    # output
    # ____________________________________________________________________________________________________
