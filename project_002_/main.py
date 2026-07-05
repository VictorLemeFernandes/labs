from math import *
import matplotlib.pyplot as plt

gravity: float = 9.81

theta: float = float(input(f"Enter the angle (in °): "))
theta = radians(theta)
initial_speed: float = float(input(f"Enter the initial speed (m/s): "))

delta_t: float = 0  # Time in seconds
points: list = []

position_x: float = 0
position_y: float = 0
speed_x: float = initial_speed * cos(theta)
speed_y: float = initial_speed * sin(theta)
vetorial_speed: float = 0

while True:
    if position_y < 0:
        break

    position_x += speed_x * delta_t
    position_y += speed_y * delta_t
    
    speed_y -= gravity * delta_t
    vetorial_speed = sqrt((pow(speed_x, 2) + pow(speed_y, 2)))

    point: dict = {
        'x': position_x,
        'y': position_y,
        'point': (position_x, position_y),
        'speed': vetorial_speed
    }

    delta_t += 0.01
    
    points.append(point)

x = [p["x"] for p in points]
y = [p["y"] for p in points]

plt.figure(figsize=(10, 6))

plt.plot(x, y, linewidth=2, label="Trajectory")

plt.scatter(x[0], y[0], s=80, label="Launch")
plt.scatter(x[-1], y[-1], s=80, label="Impact")

plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")

plt.grid(True)
plt.legend()

plt.show()
