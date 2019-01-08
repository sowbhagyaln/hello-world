def ground_shipping(weight):
  if (weight <= 2.0):
    cost = weight*1.50
  elif (weight > 2.0) and (weight <= 6.0):
    cost = weight*3.00
  elif (weight > 6.0) and (weight <= 10.0):
    cost = weight*4.00
  else:
    cost = weight*4.75
    
  return 20+cost
  
ground_shipping_cost = ground_shipping(8.4)
print("The grounds shipping cost is:", ground_shipping_cost)
  
def drone_shipping(weight):
    if (weight < 2.0):
      cost = weight * 4.50
    elif (weight > 2.0) and (weight <= 6.0):
      cost = weight * 9.00
    elif (weight > 6.0) and (weight <= 10.0):
      cost = weight * 12.00
    else:
      cost = weight * 14.25
    
    return cost
    
drone_shipping_cost = drone_shipping(1.5)
print("The drone shipping cost is: ", drone_shipping_cost)


def best_shipping(weight):
  ground  = ground_shipping(weight)
  drone   = drone_shipping(weight)
  premium = 125.00
  if (ground < drone) and (ground < premium):
    cost = ground
    method = "Ground"
  elif (premium < ground) and (premium < drone):
    cost = premium
    method = "Premium"
  else:
    cost = drone
    method = "Drone"
    
  print("The best shipping method for your package of weight %.2f is %s Shipping. It costs you $%.2f" %(weight,method,cost))
  
      
shipping_cost = best_shipping(4.8)
print(shipping_cost)

shipping_cost = best_shipping(41.5)
print(shipping_cost)
