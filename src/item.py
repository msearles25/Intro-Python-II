class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, name):
        print(f'\nYou have picked up a {name}')

    def on_drop(self, name):
        print(f'\nYou have dropped a {name}')