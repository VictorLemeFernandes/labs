# 🪂 Free Fall Simulator

A simple physics simulator written in Python that models the free fall of an object under Earth's gravity.

The project was created as a way to practice programming while revisiting classical mechanics concepts, especially uniformly accelerated motion (UAM).

## Features

- Calculates velocity over time
- Calculates displacement during free fall
- Uses Earth's gravitational acceleration (9.81 m/s²)
- Simple and easy-to-understand implementation

## Physics

The simulator is based on the basic equations of uniformly accelerated motion.

Velocity:

v = v₀ + gt

Displacement:

s = s₀ + v₀t + ½gt²

Where:

- `g = 9.81 m/s²`
- `v₀` = initial velocity
- `s₀` = initial position
- `t` = time

## Technologies

- Python 3

## Project Structure

```
free-fall-simulator/
│
├── main.py
├── simulator.py
├── physics.py
└── README.md
```

## Future Improvements

- [ ] Air resistance
- [ ] Different planets (Moon, Mars, Jupiter...)
- [ ] Graph generation (velocity × time)
- [ ] Terminal animation
- [ ] GUI version
- [ ] Unit tests

## Purpose

This repository is part of my personal study projects, where I combine software development with mathematics and physics concepts.
