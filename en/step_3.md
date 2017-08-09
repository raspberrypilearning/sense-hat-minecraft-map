## Getting started with the Sense HAT's LED display

The Sense HAT has an 8x8 LED matrix. That's 64 full-colour LEDs which you can set to any colour using the Sense HAT Python module, to learn about how colour displays in electronic systems work.

- Mount the Sense HAT on your Raspberry Pi and boot up the Pi, referring to the [assembly instructions](https://projects.raspberrypi.org/en/projects/astro-pi-guide/assemble.md) in the Sense HAT guide if neccessary.

- Open the Terminal app from the applications menu, under **Accessories**, or from the taskbar:

    ![Open Terminal](images/terminal-app-menu.png)

- Create a new directory for your project by entering the following command:

    ```bash
    mkdir minecraft-map
    ```

    `mkdir` means "make directory"; "directory" is another word for a folder.

- Open Python 3 from the applications menu, under **Programming**:

    ![Open Python 3](images/python3-app-menu.png)

- When the Python shell window opens up, click `File > New Window` to open a new window. This is where you'll enter your code.

- Save the file as `colours.py` in your new `minecraft-map` folder.

- Enter the following code:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.clear(255, 0, 0)
    ```

- Save with `Ctrl + S` and run with `F5`.

    Your Sense HAT LEDs should now all be red!

    **How does it work?**

    - `from sense_hat import SenseHat`: this lets you use the Sense HAT module.
    - `sense = SenseHat()`: this creates a connection to the Sense HAT hardware, called `sense`.
    - `sense.clear(255, 0, 0)`: here we call the `clear` method (function) on the `sense` object and pass in three colour values, for red, green and blue.

    **How do colour displays work?**

    - All colours displayed in electronic systems are made up of a red value, a green value, and a blue value which can be combined to give a wide range of colours, a bit like mixing coloured paints.
    - Colour values go from `0` (none) to `255` (full).
    - Here we used `(255, 0, 0)`, which is full red, no green and no blue.
    - Similarly, `(0, 255, 0)` is full green and `(0, 0, 255)` is full blue.
    - Purple is a mix of blue and red, so `(255, 0, 255)` is purple.

- Try changing the colour to:

    - green `(0, 255, 0)`
    - blue `(0, 0, 255)`

- More things to try (think before you try them)

    - What colour does `(255, 255, 0)` make?
    - If `(255, 0, 255)` makes purple, what would `(100, 0, 255)` and `(255, 0, 100)` look like?
    - What colour does full red, green and blue `(255, 255, 255)` make?
    - What colour does `(0, 0, 0)` make?
    - What happens if you call `sense.clear()` without any colour values?

    Inside each of the Sense HAT's 64 LEDs are three smaller LEDs: a red, a green, and a blue. All you're doing is setting the brightness of each one and it gives the whole LED a different colour.

**Download a copy of [colour.py](resources/colour.py)**

