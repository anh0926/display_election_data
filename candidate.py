class Candidate:
    def __init__(self, new_name, the_party):
        self.name = new_name
        self.my_party = the_party
        self.total_votes = 0
        self.percent_votes = 0

    def __str__(self):
        result = f'{self.name} {self.my_party}'
        return result

    def to_radio_cand(self):
        result = f'<input type= "radio" id="{self.name}" "{self.my_party}"' \
                 f' name="Candidate" value="{self.name}" "{self.my_party}"' \
                 f'<label for = "{self.name}" "{self.my_party}"> {self.name} {self.my_party}</lable><br>'
        return result

    def to_table_row(self):
        result = '<tr>'
        result += f'<td>{self.name}</td> <td> {self.my_party}</td>'
        result += '</tr>'
        return result

    def set_total_votes(self, new_total_votes):
        self.total_votes = new_total_votes

    def set_percent_votes(self, new_percent_votes):
        self.percent_votes = new_percent_votes

    def to_results (self):
        result = f'{self.name} - {self.my_party} {self.total_votes} {self.percent_votes} % \n '
        return result

    def to_results_table_row (self):
        result = '<tr>'
        result += f'<td>{self.name}</td> <td> {self.total_votes}</td> <td> {self.percent_votes}</td>'
        result += '</tr>'
        return result

    def to_results_input(self):
        result = f'<input type= "number" id="quantity" name="quantity" min="0" max=20000>'
        result += f'<label for = "quantity">{self.name}-{self.my_party}</label> <br>'
        return result


