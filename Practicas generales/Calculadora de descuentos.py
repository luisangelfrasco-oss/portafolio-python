


def apply_discount(price,discount):
  if isinstance(price, (int, float))!=True:
    return("The price should be a number")

  elif price <= 0 :
    return("The price should be greater than 0")

  elif isinstance(discount, (int,float))!=True:
    return("The discount should be a number")

  elif discount < 0 or discount > 100 :
    return("The discount should be between 0 and 100")
  else:
    final_price= price - (price * (discount/100))
    return final_price 
apply_discount(100 , 20)

print(apply_discount(100 ,50))
