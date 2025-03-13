#Prompts user to enter original price and discount percentage
try:
  price =int(input("Enter the original price: "))
  discount_percent= int(input("Enter your discount percentage: "))  

  #function to calculate discount
  def calculate_discount(price,discount_percent):
    
    if (discount_percent<20):
      return f"Your discounted price is {price}" 
    elif (discount_percent>=20):
      return f"Your discounted price is {((100-discount_percent)/100 )* price}"
    
    
  #calling the function
  print(calculate_discount(price,discount_percent))
except:
   print("invalid price or discount amount!!!")  