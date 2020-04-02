# y1 = a1 * x + b1
# y2 = a2 * x + b2
def funkcja(a1, a2):
    if a1 == a2:
        print("Proste sa rownolegle.")
    elif a1 * a2 == -1:
        print("Proste sa prostopadle.")
    else:
        print("Proste nie sa rownolegle, nie sa prostopadle.")

funkcja(1, -1)