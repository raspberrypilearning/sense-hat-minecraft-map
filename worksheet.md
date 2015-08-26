# Make a Minecraft Map with the Sense HAT

Use the Sense HAT to create a map of the world around your player in Minecraft: Pi Edition.

## Getting started with the Sense HAT's LED display

First of all, we'll look at changing the colour of the LEDs on the Sense HAT.

1. Mount the Sense HAT on your Raspberry Pi and boot up the Pi.

    ![Mounted Sense HAT](images/mounted-sense-hat.png)

1. Open the Terminal app from the applications menu:

    ![Open Python 3](images/python3-app-menu.png)

1. Create a new directory for your project by entering the following command:

    ```bash
    mkdir minecraft-map
    ```

    *`mkdir` means "make directory" - which is another word for a folder*

1. Open Python 3 from the applications menu:

    ![Open Python 3](images/python3-app-menu.png)

1. When the Python shell window opens up, click `File > New File` to open a new window. This is where you'll enter your code.

1. Save the file as `colours.py` in your new `minecraft-map` directory.

1. Enter the following code:

    ```bash
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.clear(255, 0, 0)
    ```

1. Save with `Ctrl + S` and run with `F5`.

    Your Sense HAT LEDs should now be all red!

    **How does it work?**

    - `from sense_hat import SenseHat` - this lets you use the Sense HAT module
    - `sense = SenseHat()` - this creates a connection to the Sense HAT hardware, called `sense`
    - `sense.clear(255, 0, 0)` - here we call the `clear` method (function) on the `sense` object and pass in three colour values - for red, green and blue

    **How do colours work?**

    - All colours are made up of a red value, a green value and a blue value - like mixing colour paints to make a different colour
    - Colour values go from `0` (none) to `255` (full)
    - Here we used `(255, 0, 0)` - which is full red, no green and no blue
    - Similarly, `(0, 255, 0)` is full green and `(0, 0, 255)` is full blue
    - Purple is a mix of blue and red, so `(255, 0, 255)` is purple

1. Try changing the colour to:

    - green `(0, 255, 0)`
    - blue `(0, 0, 255)`

1. More things to try (think before you try them)

    - What colour does `(255, 255, 0)` make?
    - If `(255, 0, 255)` makes purple, what would `(100, 0, 255)` and `(255, 0, 100)` look like?
    - What colour does full red, green and blue `(255, 255, 255)` make?
    - What colour does `(0, 0, 0)` make?
    - What happens if you call `sense.clear()` without any colour values?

    *Inside each of the Sense HAT's 64 LEDs are three smaller LEDs - a red, a green and a blue. All you're doing is setting the brightness of each one and it gives the whole LED a different colour*

## Exploring the colours of Minecraft

## Minecraft Sense HAT Colour Walk

## Create a map

## What next?
