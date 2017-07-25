## Setting individual LEDs on the Sense HAT

Until now, all you've done is set the whole Sense HAT LED display to the same colour. It's possible to set each pixel individually using the Sense Hat module's `set_pixel` method.

- Create a new Python file and save it as `pixels.py`.

- Write the following code:

    ```python
    from sense_hat import SenseHat
    from time import sleep

    sense  = SenseHat()

    sense.clear()
    sense.set_pixel(0, 0, 255, 255, 255)
    ```

- Save and run the code. It should clear the display and set the top left pixel to white.

    **How does it work?**

    The `sense.set_pixel` method is used to set a particular pixel to a particular colour. The pixel is given as `x` and `y` and the colour is given as `R`, `G` and `B`. There are two ways of using the method:

    - pass in the `R`, `G` and `B` values separately:

    ```python
    sense.set_pixel(x, y, r, g, b)
    ```

    - use a 3-tuple for the colour and pass it in as a variable:

    ```python
    white = (255, 255, 255)
    sense.set_pixel(x, y, white)
    ```

- Try a loop:

    ```python
    sense.clear()
    for y in range(8):
        for x in range(8):
            sense.set_pixel(x, y, 255, 0, 0)
            sleep(0.1)
    ```

    **Things to try:**

    - What happens when you reverse the order of the loops? Try `for x in range(8)` then `for y in range(8)`.
    - What happens if you add a `sense.clear()` before `sense.set_pixel()`?
    - What happens if you try `range(8, -1, -1)`?

- Try this example using rows of colours:

    ```python
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    colours = [white, red, white, green, white, blue, white, yellow]

    sense.clear()
    for y in range(8):
        colour = colours[y]
        for x in range(8):
            sense.set_pixel(x, y, colour)
            sleep(0.1)
    ```

- You can also use the `set_pixels()` method which takes in a list of 64 colour tuples. Try the following code as an example:

    ```python
    r = red
    b = blue

    pixels = [
        r, b, r, b, r, b, r, b,
        b, r, b, r, b, r, b, r,
        r, b, r, b, r, b, r, b,
        b, r, b, r, b, r, b, r,
        r, b, r, b, r, b, r, b,
        b, r, b, r, b, r, b, r,
        r, b, r, b, r, b, r, b,
        b, r, b, r, b, r, b, r,
    ]

    sense.set_pixels(pixels)
    ```

    This should give you a checkerboard of red and blue pixels.

**Download a copy of [pixels.py](resources/pixels.py)**

