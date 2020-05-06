
a = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
print("input_sentence : " + a)

print("\n")

b = a.replace("INDIA, ", "INDIA,\n\t").replace("SOVEREIGN, ", "SOVEREIGN, !\n\t\t").replace(
    "REPUBLIC ", "REPUBLIC \n\t\t\t")
print("Formatted sentence : \n" + b)