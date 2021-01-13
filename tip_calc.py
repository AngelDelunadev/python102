total_bill = float(input("Total bill amount? "))
tip = 0
service_level = input("Level of service? ")
split = int(input("Split how many ways? "))
totalpp=0
if service_level == "good":
    tip = total_bill * .20
    print("Tip amount:$ %s"% "%.2f" % tip)
    total_bill = total_bill + tip
    print("Total amount: $ %s"% "%.2f" %  total_bill)
    totalpp = total_bill/split
    print("Amount per person: $%s" % "%.2f" % totalpp)
     
elif service_level == "fair":
    tip = total_bill * .15
    print("Tip amount: %s"% "%.2f" %  tip)
    total_bill = total_bill + tip
    print("Total amount: $%s"% "%.2f" %  total_bill)
    totalpp = total_bill/split
    print("Amount per person: $%s" % "%.2f" % totalpp)

elif service_level == "bad":
    tip = total_bill * .10
    print("Tip amount:$ %s"% "%.2f" %  tip)
    total_bill = total_bill + tip
    print("Total amount: $%s"% "%.2f" %  total_bill)
    totalpp = total_bill/split
    print("Amount per person: $%s" % "%.2f" % totalpp)

else:
    print("try again")

