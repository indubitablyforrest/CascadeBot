import random

# number_revealed = int  #= int #random.randint(0,51) #assuming 60 card deck, on play, no mull/cycle T3 deck size
# surprise_factor = int  #= int #random.randint(1,100)
# normal_result = 'You revealed Living End after flipping ' + str(number_revealed) + ' cards.'
initiate_list = ['Veil of Summer', "Tormod's Crypt", 'Spell Pierce', 'Lightning Bolt', 'Pact of Negation']


def alternate_cascade(revealed_card, num) -> str:
    return "You revealed " + revealed_card + " after flipping " + str(num) + ' cards.'


def cascade_resolved() -> str:
    # global number_revealed
    number_revealed = random.randint(1, 51)
    # global surprise_factor
    surprise_factor = random.randint(1, 100)
    # condition = (number_revealed,surprise_factor)
    num = number_revealed
    match number_revealed:
        case 1 | 2 | 3 if surprise_factor <= 10:
            # if surprise_factor <= 10:
            return 'You Revealed Brainstorm after fli... wait is this Legacy? I miss shardless BUG :('

        case 1:
            return 'The Top card was Living End, Nice'

        case 51:
            return "you revealed all 51 cards in your deck without a legal target... let's assume you ment to do that."

# the following cases order is important to keep the odds accurate.
# it executes in order so the second case in the list excludes any cases (values) preceding it.
        case _ if surprise_factor <= 5:  # 5% chance
            return 'you flipped ' + num + ' cards with no legal target. Ope, last copy is in your hand XD'

        case _ if surprise_factor <= 10:  # 5% chance
            return 'you flipped ' + num + " cards with no legal target. Guess you didn't side in the 4th copy"

        case _ if surprise_factor <= 14:  # 4% chance cmc < 3
            return alternate_cascade((random.choice(initiate_list)), num) + 'You should check out #living-end-initiates'

        case _ if surprise_factor <= 34:  # 20% chance SB Rhinos
            return alternate_cascade('Crashing Footfalls', num) + ' The ole sideboard juke.'

        case _ if surprise_factor <= 40:  # 6% chance
            return alternate_cascade('Restore Balance', num) + " I haven't heard that name in years!"

        case _ if surprise_factor <= 45:  # 5% change
            return alternate_cascade('Inevitable Betrayal', num) + " huh, super secret tech?"
# --------end of the order importance section---------------
        case _ if surprise_factor == 100:
            return alternate_cascade("Living End", num) + " It Must've taken years to fully pimp out the deck!"
        case _ if surprise_factor == 1:
            return alternate_cascade("Living End",
                                     num) + " It's a little late now but maybe look into sleeves for the future."
        case _:
            return alternate_cascade("Living End", num)

# print("# revealed:" + str(number_revealed) + ' surprise:' + str(surprise_factor))
# print(cascade_resolved())
