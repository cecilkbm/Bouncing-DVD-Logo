# 📀 Bouncing DVD Logo (Enhanced Edition)
A fun, terminal-based Python project that recreates the classic bouncing DVD logo by Al Sweigart. I enhanced it with multiple logos, speed variation, combo tracking, and rainbow effects.

Built as a playful exercise in game-loop logic, state management, and real-time terminal rendering, this project goes beyond the classic version by introducing mechanics you’d expect in a simple game engine.

---

## Technologies
  - Python 3
  - bext (terminal control & color rendering)
  - Standard Library (sys, random, time)
  - Cross-platform terminal animation
#

## Features
  - Multiple independently moving DVD logos
  - Real-time terminal animation
  - Accurate edge and corner collision detection
  - Corner bounce combo system
  - Speed increases based on combo streaks
  - Temporary rainbow mode at higher combos 🌈
  - Dyamic color changes on bounces
  - Live statistics display (corner bounces & combos)
  - Graceful shutdown with Ctrl+C
#

## 🧠 The Process
This project started as a traditional bouncing DVD animation, but I intentionally pushed it further to explore stateful animation logic.
Each logo is treated as its own entity with independent state:
    - Position
    - Direction
    - Speed
    - Combo count
    - Timers for combo decay and rainbow mode
    
From there, I layered in mechanics:
    - Corner bounces trigger combo chains
    - Combos increase movement speed
    - Sustained combos unlock rainbow color cycling
    - Timers reset state to avoid runaway behavior
    
The result is a terminal animation that feels closer to a mini game loop than a simple script.
#

## What I Learned
  - How to structure real-time loops in Python
  - Managing per-object state cleanly using dictionaries
  - Implementing collision detection and response
  - Using timers to control temporary effects
  - Balancing visual flair with readable terminal output
  - Why even small simulations benefit from clear constants and constraints
    
This project reinforced the importance of controlling complexity early, especially in interactive programs.
#

## How It Works
  - The terminal size is dynamically detected
  - Each logo moves diagonally across the screen
  - Logos bounce off edges and corners
  - Corner bounces:
    - Increment combo counters
    - Increase speed (up to a capped maximum)
    - Trigger rainbow mode at higher streaks
  - Combos decay if no corner bounce occurs within a time window
  - Frame timing adapts based on the fastest logo
#

## ▶️ Running the Project
1. Install the required dependency
    - pip install bext
2. Clone the repository
    - git clone https://github.com/cecilkbm/Bouncing-DVD-Logo.git
3. Run the script
    - python bouncing_dvd.py
4. Press Ctrl+C to exit
#

## 🎮 Combo System Explained
  - Corner bounce → combo increases
  - Combo timeout → resets combo & speed
  - Combo ≥ 3 → rainbow mode activated 🌈
  - Higher combos → faster movement & visual emphasis
    
This system was intentionally added to practice state transitions and time-based effects.

## 📷 Preview
![BouncingDVD](https://github.com/user-attachments/assets/4f815aaf-982c-4ccb-b19a-0ecfcf695434)
