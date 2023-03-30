#!bin/python3
total = int(input("what is the bill? "))
people = int(input("how many people? "))
tip = float(input("what percentage would you like to tip? "))
tip = tip*.01
final_tip = (total/people)*tip
final_tip_str = str(final_tip)
print(f"this is the tip for {people} people with a bill of {total} " + final_tip_str)
