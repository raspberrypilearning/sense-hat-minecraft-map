## Set a single LED

It's possible to set each pixel individually using the `set_pixel` method. Let's learn how to do this so that we can use only one pixel to represent the current block, and make a much bigger map on the LED matrix.

+ Create a brand new Python file and save it as `pixels.py`

+ Add the code to connect to the Sense HAT and clear the display

```python
from sense_hat import SenseHat
sense  = SenseHat()

sense.clear()
```

+ Add a variable called `green` with the value (0, 255, 0).

+ Now add some code to set the top left pixel on the Sense HAT's LED matrix to green.

[[[rpi-sensehat-single-pixel]]]

+ Save and run the code. You should see a green pixel on the top left of the display (diagonally opposite the joystick).

### Challenge: colour using a loop

Try setting the whole display to green using the `set_pixel` method and NOT using the `clear` method. To do this you will need to create two `for` loops, one inside the other, to loop through setting each pixel one by one.

--- collapse ---
---
title: Challenge solution
---

```python
sense.clear()
for y in range(8):
    for x in range(8):
        sense.set_pixel(x, y, green)
```

--- /collapse ---


To create a display using the whole LED matrix, it is usually quicker to use the `set_pixels()` method which takes in a list of 64 colours.

[[[rpi-sensehat-multiple-pixels]]]

+ Test out the `set_pixels` method by creating a pattern of your choice and displaying it on the Sense HAT's LED matrix.
