mortgage = 366323
agent_fee = .06
prorated_property_taxes = 400
prorated_mortgage_interest = 1500
other_fees = 2500
closing_costs = prorated_property_taxes + prorated_mortgage_interest + other_fees
sale_price = input('What is the sale price of your home? ')
agent_cost = agent_fee * float(sale_price)
price_per_sqft = (float(sale_price) / 3160)
proceeds = (float(sale_price) - mortgage - closing_costs - agent_cost)
print('Your closing costs will be $' + str(closing_costs))
print()
print('Your agent cost is ${:,.2f}'.format(agent_cost))
print()
print('Your price per sqft is ${:,.2f}'.format(price_per_sqft))
print()
print('Your proceeds from the sale will be ${:,.2f}'.format(proceeds))