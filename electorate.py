from party import Party
from candidate import Candidate

class Electorate:
    def __init__(self, new_year, new_name):
        self.year = new_year
        self.name = new_name
        self.all_my_parties = []
        self.all_my_candidates = []

    def add_party(self, new_name):
        a_party = Party(new_name)
        self.all_my_parties.append(a_party)

    def find_party(self, target_party_id):
        return next((a_party for a_party in self.all_my_parties if a_party.name == target_party_id), None)

    def sort_parties(self):
        self.all_my_parties.sort(key=lambda a_party: a_party.name)

    def add_candidate(self, new_name, new_party):
        a_candidate = Candidate(new_name, new_party)
        self.all_my_candidates.append(a_candidate)

    def sort_candidates_by_name(self):
        self.all_my_candidates.sort(key=lambda a_candidate: a_candidate.name)

    def find_candidate(self, target_name):
        return next((a_candidate for a_candidate in self.all_my_candidates if a_candidate.name == target_name), None)

    def set_candidate_vote(self, target_name, new_total_votes):
        the_candidate = self.find_candidate(target_name)
        the_candidate.set_total_votes(new_total_votes)

    def calc_candidate_percentages(self):
        total = 0
        for a_candidate in self.all_my_candidates:
            total += a_candidate.total_votes
        one_percent = total / 100
        for a_candidate in self.all_my_candidates:
            percent = a_candidate.total_votes / one_percent
            percent = round(percent, 2)
            a_candidate.set_percent_votes(percent)


    def __str__(self):
        result = f'{self.name} {self.year}<br>'
        self.sort_parties()
        for a_party in self.all_my_parties:
            result += f'{a_party}<br>'
        for a_candidate in self.all_my_candidates:
            result += f'{a_candidate}<br>'
        return result

    def to_party_ballot(self):
        result = f'<form> {self.name} {self.year}<br> '
        for a_party in self.all_my_parties:
            result += a_party.to_radio_party()
        result += '</form>'
        return result

    def to_candidate_ballot(self):
        self.sort_candidates_by_name()
        result = f'<form> Candidate votes <br>'
        for a_candidate in self.all_my_candidates:
            result += a_candidate.to_radio_cand()
        result += '</form>'
        return result

    def to_candidate_table(self):
        self.sort_candidates_by_name()
        result = f'<table><tr><th colspan="2">Candidate votes</th></tr>'
        for a_candidate in self.all_my_candidates:
            result += a_candidate.to_table_row()
        result += '</table>'
        return result

    def sort_candidates_by_votes(self):
        self.all_my_candidates.sort(key=lambda a_candidate: a_candidate.total_votes)

    def to_candidate_results(self):
        self.sort_candidates_by_votes()
        result = f''
        for a_candidate in self.all_my_candidates:
            result += f'{a_candidate.to_results()}<br>'
        return result

    def to_candidate_results_table(self):
        self.sort_candidates_by_name()
        result = f'<table><tr><th>{self.name}</th><th colspan="2"> {self.year}</th></tr>'
        for a_candidate in self.all_my_candidates:
            result += a_candidate.to_results_table_row()
        result += '</table>'
        return result

    def to_candidate_results_form(self):
        self.sort_candidates_by_name()
        result = f'<form> Manukau East 2017 Candidate Vote Total Entry <br>'
        for a_candidate in self.all_my_candidates:
            result += a_candidate.to_results_input()
        result += '</form>'
        return result
