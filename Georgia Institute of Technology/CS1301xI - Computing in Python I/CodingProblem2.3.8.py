can_afford = True
destination_is_safe = True
educational_value = True
relatives_nearby = True
is_international = True
have_passport = True
afraid_to_fly = True
have_a_car = True
is_a_beach = True
is_warm = False
has_skiing = True
is_a_city = True
is_off_peak = True
has_attraction = False

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Imagine for a moment that you're a college student who wants
# to travel during spring break. You have a destination in
# mind. What determines whether you can go there?
#
# First, how would you pay for the trip? If you can afford it
# (can_afford), then all you need is for your parents to agree
# to let you go. Your parents will agree to let you go if the
# destination is safe (destination_is_safe).
can_pay = bool(can_afford and destination_is_safe)
#
# If you can't afford it, then you need your parents to pay for
# the trip. Your parents will pay for the trip if the destination
# is safe (destination_is_safe) and if either there is educational
# value (educational_value) or there are relatives nearby for
# you to visit (relatives_nearby).
parents_pay = bool(not can_afford and destination_is_safe and (educational_value or relatives_nearby))
#
# Second, are you sure you're able to go to this location? If
# it's international (is_international), then you'll need a
# passport (have_passport) and you can't be afraid to fly
# (afraid_to_fly). If it's not international (is_international),
# then you either must have a car (have_a_car) or you can't be
# afraid to fly (afraid_to_fly).
location_able = bool((is_international and have_passport and not afraid_to_fly) or (
            not is_international and (have_a_car or not afraid_to_fly)))
#
# Third, do you actually want to go to this location? If it's a
# beach location (is_a_beach), then you want the weather to be
# warm (is_warm). If it's instead a skiing location (has_skiing),
# you don't want it to be warm (is_warm). If it's a tourist city
# (is_a_city), then you either want it to be an off-peak travel
# time (is_off_peak) or you want there to be an attraction in
# town that week (has_attraction).
want_to_go_weather = bool((is_a_beach and is_warm) or (has_skiing and not is_warm))
want_to_go_tourism = bool(is_a_city and (is_off_peak or has_attraction))
#
# If it's both a beach and a city, then you'd decide to go if it
# meets the condition for the beach (it's warm) or for a city
# (is an off-peak time or has an attraction). If it's both a
# skiing location and a city, then you'd decide to go if it meets
# either type of location's conditions as well.
go_city = bool(want_to_go_weather or want_to_go_tourism)
#
# Your only goal here is to print True or False: True if the
# destination represented by the variables is an acceptable
# travel location, False if it is not.
#
# HINT: Don't try to do this all in one line. Break it into
# smaller parts.

# Testing each individual portion...
# print(can_pay)
# print(parents_pay)
# print(location_able)
# print(want_to_go_weather)
# print(want_to_go_tourism)
# print(go_city)

# Add your code here!
print((can_pay or parents_pay) and location_able and go_city)