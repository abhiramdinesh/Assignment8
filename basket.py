DEFAULT_INITIAL_BASKET = ["orange", "apple"]

def create_picnic_basket(healthy, hungry, initial_basket=DEFAULT_INITIAL_BASKET):
    # Bugfix - Appending to basket will modify the DEFAULT_INITIAL_BASKET as they are both pointing to the same object.
    # Assign a copy of initial_basket to basket. This creates a new object.
    basket = initial_basket.copy()
    if healthy:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket

# Verify fix
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True, ["tea"]))
print("Third basket:", create_picnic_basket(True, True))

print("AFTER FIX, ONLY 1 STRAWBERRY WHEN HEALTH AND HUNGRY?")
