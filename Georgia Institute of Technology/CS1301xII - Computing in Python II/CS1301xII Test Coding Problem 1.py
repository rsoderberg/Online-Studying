days_since_release = 144
original_price = 115
greatest_hits = True

# Write a conditional that determines the price of a
# newly-released game, movie, or album based on the time since
# it was released.
#
# Assume that a new release loses $2 off its price for every
# full week since it was released. So, two full weeks (14 days)
# after a $60 game is released, it will cost $56.
#
# However, if the release is considered a "greatest hit", it
# loses value half as fast: after two weeks, it will be $58
# instead of $56.
#
# No release will ever fall to below $20, however, no matter
# how fast it loses value or whether it's a greatest hit.
#
# Add some code below to print the current price of the release.
# For example, with the values above, it would pring $58.

# Add your code here! Make sure to print the dollar sign, too.
current_price = original_price
weeks_since_release = 0

if days_since_release >= 7:
    if days_since_release % 7 == 0:
        weeks_since_release = days_since_release / 7
    else:
        weeks_since_release = days_since_release / 7
        if weeks_since_release < round(days_since_release / 7):
            weeks_since_release = (round(days_since_release / 7) - 1)
else:
    weeks_since_release = 0

if greatest_hits:
    current_price = original_price - weeks_since_release
    if current_price <= 20:
        current_price = 20
    else:
        current_price = current_price
else:
    current_price = original_price - (weeks_since_release * 2)
    if current_price <= 20:
        current_price = 20
    else:
        current_price = current_price

print("$" + str(round(current_price)))