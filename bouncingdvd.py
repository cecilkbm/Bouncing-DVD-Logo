# Enhanced Bouncing DVD Logo with Speed Variations and Combo System
# Press Ctrl-C to stop.

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUMBER_OF_LOGOS = 5
BASE_PAUSE = 0.2
MIN_PAUSE = 0.05  # Maximum speed

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'
SPEED = 'speed'
COMBO = 'combo'
COMBO_TIMER = 'combo_timer'
RAINBOW_MODE = 'rainbow_mode'
RAINBOW_TIMER = 'rainbow_timer'

# Combo settings:
COMBO_TIMEOUT = 50  # Frames before combo resets
RAINBOW_DURATION = 30  # Frames for rainbow mode

def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS),
            SPEED: 1.0,
            COMBO: 0,
            COMBO_TIMER: 0,
            RAINBOW_MODE: False,
            RAINBOW_TIMER: 0
        })
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    cornerBounces = 0
    frame = 0
    rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

    while True:
        frame += 1
        
        for logo in logos:
            # Erase the logo's current location
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]
            isCornerBounce = False

            # See if the logo bounces off the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
                isCornerBounce = True
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
                isCornerBounce = True
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
                isCornerBounce = True
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
                isCornerBounce = True
        
            # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge:
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            # Handle corner bounce effects
            if isCornerBounce:
                # Increment combo
                if logo[COMBO_TIMER] > 0:
                    logo[COMBO] += 1
                else:
                    logo[COMBO] = 1
                logo[COMBO_TIMER] = COMBO_TIMEOUT
                
                # Speed boost based on combo
                logo[SPEED] = min(3.0, 1.0 + (logo[COMBO] * 0.3))
                
                # Activate rainbow mode at combo 3+
                if logo[COMBO] >= 3:
                    logo[RAINBOW_MODE] = True
                    logo[RAINBOW_TIMER] = RAINBOW_DURATION
                
                # Change color
                logo[COLOR] = random.choice(COLORS)
                
            elif logo[DIR] != originalDirection:
                # Regular bounce color change
                logo[COLOR] = random.choice(COLORS)

            # Update combo timer
            if logo[COMBO_TIMER] > 0:
                logo[COMBO_TIMER] -= 1
                if logo[COMBO_TIMER] == 0:
                    logo[COMBO] = 0
                    logo[SPEED] = 1.0  # Reset speed when combo ends

            # Update rainbow mode
            if logo[RAINBOW_MODE]:
                logo[RAINBOW_TIMER] -= 1
                # Cycle through rainbow colors
                logo[COLOR] = rainbow_colors[frame % len(rainbow_colors)]
                if logo[RAINBOW_TIMER] <= 0:
                    logo[RAINBOW_MODE] = False

            # Move the logo with speed multiplier
            move_amount = int(2 * logo[SPEED])
            if logo[DIR] == UP_RIGHT:
                logo[X] = min(WIDTH - 3, logo[X] + move_amount)
                logo[Y] = max(0, logo[Y] - 1)
            elif logo[DIR] == UP_LEFT:
                logo[X] = max(0, logo[X] - move_amount)
                logo[Y] = max(0, logo[Y] - 1)
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] = min(WIDTH - 3, logo[X] + move_amount)
                logo[Y] = min(HEIGHT - 1, logo[Y] + 1)
            elif logo[DIR] == DOWN_LEFT:
                logo[X] = max(0, logo[X] - move_amount)
                logo[Y] = min(HEIGHT - 1, logo[Y] + 1)

        # Display statistics
        bext.goto(5, 0)
        bext.fg('white')
        print(f'Corner bounces: {cornerBounces}', end='  ')
        
        # Display combo info for each logo
        bext.goto(5, 1)
        combo_info = []
        for i, logo in enumerate(logos):
            if logo[COMBO] > 0:
                combo_text = f"Logo{i+1}: x{logo[COMBO]}"
                if logo[RAINBOW_MODE]:
                    combo_text += " 🌈RAINBOW!"
                combo_info.append(combo_text)
        
        if combo_info:
            print('COMBOS: ' + ' | '.join(combo_info) + '    ', end='')
        else:
            print(' ' * 60, end='')

        for logo in logos:
            # Draw the logos at their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            
            # Add visual flair for high combos
            if logo[COMBO] >= 5:
                print('***', end='')
            elif logo[COMBO] >= 3:
                print('DVD', end='')
            else:
                print('DVD', end='')

        bext.goto(0, 0)
        sys.stdout.flush()
        
        # Adjust pause based on fastest logo
        max_speed = max(logo[SPEED] for logo in logos)
        adjusted_pause = max(MIN_PAUSE, BASE_PAUSE / max_speed)
        time.sleep(adjusted_pause)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Enhanced Bouncing DVD Logo with Speed & Combos")
        print("By Nostripeszebra - Enhanced Edition")
        sys.exit()