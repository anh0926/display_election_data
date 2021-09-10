class Party:
    def __init__(self, new_name):
        self.name = new_name

    def __str__(self):
        result = f'{self.name}'
        return result

    def to_radio_party(self):
        result = f'<input type="radio" id="{self.name}" name="party" value="{self.name}">'
        result += f'<label for="{self.name}">{self.name}</label><br>'
        return result