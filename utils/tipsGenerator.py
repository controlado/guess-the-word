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
        if len(iterable) == 1:  # If the list contains only one item.
            return [iterable[0]]

        # If there's more than one item,
        # it will put everything in one list.
        return [items for items in iterable]
