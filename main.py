bids = {}
bidding_finished = False

def find_highest_bidding(total_bids):
    highest_bids = 0
    winner = ""
    for bids in total_bids:
        bids_amount = total_bids[bids]
        if bids_amount > highest_bids:
            highest_bids = bids_amount
            winner = bids
        print(f"The winner is {bids} with bid of ${highest_bids}")

while not bidding_finished:
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid? $"))
    bids[name] = bid_amount
    Should_continue = input("Is there any other user who want to bid? type yes or no: ")
    if Should_continue == "no":
        bidding_finished = True
        find_highest_bidding(bids)


