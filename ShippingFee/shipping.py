#JnT shipping
weight = 12
if weight <= 2:
  cost_jnt = weight * 1.5 + 20
elif weight <= 6:
  cost_jnt = weight * 3 + 20
elif weight <= 10:
  cost_jnt = weight * 4 + 20
else:
  cost_jnt = weight * 4.75 + 20
print("JnT Shipping RM",cost_jnt)
 
#Premium shipping
cost_ground_premium = 125.00
print("Premium Shipping  RM", cost_ground_premium)

#Ninja shipping
if weight <= 2:
  cost_ninja = weight * 2 
elif weight <= 6:
  cost_ninja = weight * 4
elif weight <= 10:
  cost_ninja = weight * 5
else:
  cost_ninja = weight * 6.5
print("Ninja Shipping RM",cost_ninja)