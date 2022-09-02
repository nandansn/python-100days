
installement = {
    '3':4,
    '6':2,
    '12':1
}

def total_maturity_amount(tenure, amount, interest, yrs):
    count = yrs * installement.get(tenure)
    m_amount = amount
    while count > 0:
        total_interest = ((amount * interest) / 1200) * int(tenure)
        m_amount = m_amount + total_interest
        count -= 1
    return m_amount

print(total_maturity_amount('3',10000000,5.59, 25))


 

