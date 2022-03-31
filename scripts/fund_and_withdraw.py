from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_free = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_free}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_free})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({'from': account})

def main():
    fund()
    withdraw()
