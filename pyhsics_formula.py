print('choose a formula:')
print("a -> F = m * a     (Force)")
print("b -> v = d / t     (Velocity)")
print("c -> p = W / t     (Power)")
print("d -> KE = 0.5 * m * v2   (Kinetic Energy)")
print("e -> p = m / v     (Density)")

choice = input ("Enter your choice (a-e):")
if choice == "a":
    print("\nFormula selected: F = m * a (Force)")
elif choice == "b":
    print("\nFormula selected: v = d / t (Velocity)")
elif choice == "c":
    print("\nFormula selected: P = W / t (Power)")
elif choice == "d":
    print("\nFormula selected: KE = 0.5 * m * v2 (Kinetic Energy)")
elif choice == "e":
    print("\nFormula selected: p = m / V (Density)")
else:
    print("\nInvalid choice. Please enter a letter from a to e.")