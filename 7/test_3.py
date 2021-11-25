import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount / 100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


invoice = {
    "customer": "BigCo",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 55
        },
        {
            "playID": "as-like",
            "audience": 35
        },
        {
            "playID": "othello",
            "audience": 40
        }
    ]
}

invoice_many_seats = {
    "customer": "SomeGuy",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 1000000
        },
        {
            "playID": "as-like",
            "audience": 54654557
        },
        {
            "playID": "othello",
            "audience": 76346445
        }
    ]}
invoice_no_seats = {
    "customer": "SomeGuy",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 0
        },
        {
            "playID": "as-like",
            "audience": 0
        },
        {
            "playID": "othello",
            "audience": 0
        }
    ]}

plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}

print(statement(invoice, plays))


class Tests(unittest.TestCase):
    def test_positive_many_seats(self):
        self.assertEqual(statement(invoice_many_seats, plays), """Statement for SomeGuy
 Hamlet: $10,000,100.00 (1000000 seats)
 As You Like It: $437,236,756.00 (54654557 seats)
 Othello: $763,464,550.00 (76346445 seats)
Amount owed is $1,210,701,406.00
You earned 142931823 credits
""")

    def test_no_seats(self):
            self.assertEqual(statement(invoice_no_seats, plays), """Statement for SomeGuy
 Hamlet: $400.00 (0 seats)
 As You Like It: $300.00 (0 seats)
 Othello: $400.00 (0 seats)
Amount owed is $1,100.00
You earned 0 credits
""")

    def test_base_case(self):
            self.assertEqual(statement(invoice, plays), """Statement for BigCo
 Hamlet: $650.00 (55 seats)
 As You Like It: $580.00 (35 seats)
 Othello: $500.00 (40 seats)
Amount owed is $1,730.00
You earned 47 credits
""")
