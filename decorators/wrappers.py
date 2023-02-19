import os


class Wrapper(object):
    """
    Centering string wrapped with any characters.
    """
    def __init__(self, max_char_length):
        self.max_char_length: int = max_char_length

    def get_max_length(self) -> int:
        """
        Making sure that the character length is not greater than the terminal length.
        If it's greater, use the terminal length instead.
        """
        terminal_width, terminal_height = os.get_terminal_size()
        if terminal_width < self.max_char_length:
            self.max_char_length = terminal_width
        return self.max_char_length

    def content_center(self, filled_characters: str = '-', content: str = '') -> str:
        max_length: int = self.get_max_length()
        if not content:
            content = str(filled_characters)
        return content.center(max_length, filled_characters)

    def content_left_right(self, filled_characters: str = '-', content: str = '', start_from_right: bool = False) -> str:
        max_length: int = self.get_max_length()
        content_length: int = len(content)
        filled_characters_length_needed: int = max_length - content_length
        calculated_filled_characters: str = filled_characters * filled_characters_length_needed
        if start_from_right:
            return calculated_filled_characters + content
        return content + calculated_filled_characters


if __name__ == '__main__':
    wrapper = Wrapper(100)
    result = wrapper.content_left_right('_', 'I ❤ Python')
    print(result)
    result = wrapper.content_center('_', 'I ❤ Python')
    print(result)
    result = wrapper.content_left_right('_', 'I ❤ Python', True)
    print(result)

    # output
    # I ❤ Python____________________________________________________________
    # ______________________________I ❤ Python______________________________
    # ____________________________________________________________I ❤ Python
