from services.physics import Physics

physics = Physics()

g = physics.gravity
height = float(input("Enter the height (in meters): "))

print(f"The height is: {height} m and the gravity is: {g} m/s²\n")

delta_t: float = 0  # Time step in seconds

while height >= 0:
    print(f"Tempo: {delta_t:.2f} s")
    print(f"Altura: {height:.2f} m")
    print(f"Velocidade: {g * delta_t:.2f} m/s\n")

    delta_t += 0.1  # Increment time by 0.1 seconds
    height = height - 0.5 * g * (delta_t ** 2)  # Update height using the free fall formula

print(80 * '*')
print("The object has hit the ground.")
print(f"Total time of fall: {delta_t:.2f} seconds")
print(f"Final velocity upon impact: {g * delta_t:.2f} m/s or {g * delta_t * 3.6:.2f} km/h")
print(80 * '*')
