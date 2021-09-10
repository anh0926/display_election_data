from electorate import Electorate

def setup():
    the_electorate = Electorate(2017,'Manukau East')
    the_electorate.add_party('Ban1080')
    the_electorate.add_party('Aotearoa Legalise Cannabis Party')
    the_electorate.add_party('ACT New Zealand')
    the_electorate.add_party('Conservative')
    the_electorate.add_party('Democrats for Social Credit')
    the_electorate.add_party('Green Party')
    the_electorate.add_party('Internet Party')
    the_electorate.add_party('Labour Party')
    the_electorate.add_party('MANA')
    the_electorate.add_party('Māori Party')
    the_electorate.add_party('National Party')
    the_electorate.add_party('New Zealand First Party')
    the_electorate.add_party("New Zealand People'" 's' " " 'Party')
    the_electorate.add_party('NZ Outdoors Party')
    the_electorate.add_party('The Opportunities Party (TOP)')
    the_electorate.add_party('United Future')

    the_electorate.add_candidate('ESERA, Saipele', 'Māori Party')
    the_electorate.add_candidate('BAKSHI,Kanwaljit Singh','National Party')
    the_electorate.add_candidate('FLESHER, William', 'New Zealand First Party')
    the_electorate.add_candidate('JOHNSTON, Edward George Tanu Faleauto', 'The Opportunities Party (TOP)')
    the_electorate.add_candidate('RICHMOND, Tamatoa', 'Independent')
    the_electorate.add_candidate('SALESA, Jennifer Teresia', 'Labour Party')
    the_electorate.add_candidate('SINGH, Bhupinder', 'ACT New Zealand')
    the_electorate.add_candidate('SINGH, Raj', 'Green Party')

    the_electorate.set_candidate_vote('ESERA, Saipele',698)
    the_electorate.set_candidate_vote('BAKSHI,Kanwaljit Singh',4813)
    the_electorate.set_candidate_vote('FLESHER, William', 1511)
    the_electorate.set_candidate_vote('JOHNSTON, Edward George Tanu Faleauto', 308)
    the_electorate.set_candidate_vote('RICHMOND, Tamatoa', 80)
    the_electorate.set_candidate_vote('SALESA, Jennifer Teresia', 17402)
    the_electorate.set_candidate_vote('SINGH, Bhupinder', 201)
    the_electorate.set_candidate_vote('SINGH, Raj', 650)

    the_electorate.calc_candidate_percentages()
    return the_electorate


if __name__ == '__main__':
    the_electorate = setup()

    print(the_electorate)
