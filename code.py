import sys
import math


def player(inv_0, inv_1, inv_2, inv_3, score):

    Liste_player = [inv_0, inv_1, inv_2, inv_3, score]
    print("Inventaire(4) + score : ", Liste_player, file=sys.stderr, flush=True)


def sorts(delta_0, delta_1, delta_2, delta_3):
    Liste_sorts = [delta_0, delta_1, delta_2, delta_3]
    print("Liste sorts : ", Liste_sorts, file=sys.stderr, flush=True)


class Action:
    def __init__(
        self,
        action_id,
        action_type,
        delta_0,
        delta_1,
        delta_2,
        delta_3,
        price,
        tome_index,
        tax_count,
        castable,
        repeatable,
    ):
        self.action_id = action_id
        # self TODO


# game loop
while True:

    actions = []

    action_count = int(input())  # the number of spells and recipes in play
    for i in range(action_count):

        # tome_index: in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax
        # tax_count: in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell
        # castable: in the first league: always 0; later: 1 if this is a castable player spell
        # repeatable: for the first two leagues: always 0; later: 1 if this is a repeatable player spell

        (
            action_id,
            action_type,
            delta_0,
            delta_1,
            delta_2,
            delta_3,
            price,
            tome_index,
            tax_count,
            castable,
            repeatable,
        ) = input().split()
        action_id = int(action_id)
        delta_0 = int(delta_0)
        delta_1 = int(delta_1)
        delta_2 = int(delta_2)
        delta_3 = int(delta_3)
        price = int(price)
        tome_index = int(tome_index)
        tax_count = int(tax_count)
        castable = castable != "0"
        repeatable = repeatable != "0"

    for i in range(2):
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]

        if i == 0:  # i_0 = moi, i_1 adversaire
            player(
                inv_0, inv_1, inv_2, inv_3, score
            )  # recupere mon inventaire et mon score

    sorts(delta_0, delta_1, delta_2, delta_3)

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    print("BREW", action_id)