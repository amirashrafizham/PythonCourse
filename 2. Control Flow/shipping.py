
weight = 41.5  # in pounds
cost_ground = 0

# Ground Shipping

if weight <= 2:
    cost_ground = 1.5 * weight + 20
elif weight >= 2 and weight <= 6:
    cost_ground = 3 * weight + 20
elif weight >= 6 and weight <= 10:
    cost_ground = 4 * weight + 20
else:
    cost_ground = 4.75 * weight + 20

print("cost ground $", cost_ground)


# Ground Shipping Premium

cost_premium = 125.00

print("cost premium $", cost_premium)


# Drone Shipping
cost_drone = 0

if weight <= 2:
    cost_drone = 4.5 * weight
elif weight >= 2 and weight <= 6:
    cost_drone = 9 * weight
elif weight >= 6 and weight <= 10:
    cost_drone = 12 * weight
else:
    cost_drone = 14.25 * weight

print("cost drone $", cost_drone)
