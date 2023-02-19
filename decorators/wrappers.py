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

    def content_left_right(self, max_length: int, filled_characters: str = '-', content: str = '', start_from_right: bool = False) -> str:
        content_length: int = len(content)
        filled_characters_length_needed = max_length - content_length
        calculated_filled_characters = filled_characters * filled_characters_length_needed
        if start_from_right:
            return calculated_filled_characters + content
        return content + calculated_filled_characters


if __name__ == '__main__':
    wrapper = Wrapper()
    result = wrapper.content_left_right(70, '_', 'I ❤ Python')
    print(result)
    result = wrapper.content_center(70, '_', 'I ❤ Python')
    print(result)
    result = wrapper.content_left_right(70, '_', 'I ❤ Python', True)
    print(result)

    # output
    # I ❤ Python____________________________________________________________
    # ______________________________I ❤ Python______________________________
    # ____________________________________________________________I ❤ Python
