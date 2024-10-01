# USER INPUT DATA: PROGRAM 
# username = input ("Enter your Username:")
# print("Username is","\n" + username)

# F-STRING
xyz = "Rehan Developer"
txt =f"My self {xyz}:"
print(txt)


#FLOOR
price = 59
txt =f"My price is {price:.2f} dollars"
print(txt)

txt =f"My price is {95:.2f} dollars"
print(txt)


# MATH OPERATORS: 
txt =f"My price is {24 + 12} dollars"
print(txt)
txt =f"My price is {24 - 12} dollars"
print(txt)
txt =f"My price is {24 * 12} dollars"
print(txt)
txt =f"My price is {24 / 12} dollars"
print(txt)
txt =f"My price is {24 % 12} dollars"
print(txt)


#ADD TAX BEFORE PRICE:
price = 59
tax = 0.28
txt = f"My price is {price +(price * tax):.2f} dollars"
print(txt)


#if and else statement:
price = 50
txt = f"It's very {'Expensive' if price >= 50 else 'cheap'}"
print(txt)


#UPPER CASE and LOWERCASE:F-STRING
fruit = "apple"  #UPPERCASE
txt = f"i love {fruit.upper()}"
print(txt)

fruit = "MANGO"  #LOWERCASE
txt = f"I Love {fruit.lower()}"
print(txt)


#def converts feet:

def converter(x):
    return x * 0.3900
txt = f"travel in metro at a {converter(3900)} in home"
print(txt)


#comma as a thousand separator
#exp 48,000,000
price = 48000000
txt = f"my price is {price:,} dollars"
print(txt)

#emp 48_000_000
txt = f"my brother are donates {48000000:_} in hospital"
print(txt)


#FORMATTING STRING:
#{value :> space value}
txt = f"my money are {4900:>8} is safe in bank account"
print(txt)

#{value :^ space value}
txt = f"my money are {5000:^9} is safe in bank account"
print(txt)

#{value :< space value}
txt = f"my money are {4900:<8} is safe in bank account"
print(txt)

#{- := space value} exp (-       36)
txt = f"today temperature is {-36:=8} in degree"
print(txt)


#ADD PLACEHOLDER 
price = 50
txt = "my price is {} dollars"
print(txt.format(price))

#ADD MORE PLACEHOLDER
item = 2
weight = 30
price = 790
txt = "I will but {} item, than weight is {}kg and price is {} dollars"
print(txt.format(item,weight,price))