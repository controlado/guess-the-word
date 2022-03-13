import requests


class Tips():
    def __init__(self, word: str):
        self.word = word.lower()

    def tipAbout(self):
        url = f'https://significado.herokuapp.com/{self.word}'
        request = requests.get(url=url).json()

        try:
            itemList = [item['meanings'] for item in request][0]
            return self.formatList(itemList)
        except Exception:
            return None

    # Function to take the list from another list.
    def formatList(self, iterable: list):
        # If there's more than one item,
        # it will put everything in one list.
        return [iterable[0]] if len(iterable) == 1 else list(iterable)
