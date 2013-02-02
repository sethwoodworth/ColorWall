import random
import time

# A dictionary of hsv values for some common colors.
colors = {"black":(0, 0, 0), "white":(0, 0, 1), "gray":(0, 0, 0.5),
          "red":(0, 1, 1), "blue":(0.66, 1, 1), "yellow":(0.16, 1, 1),
          "purple":(0.85, 1, 0.5), "green":(0.33, 1, 0.5),
          "orange":(0.083, 1, 1), "pink":(0.9, 1, 1), "lime":(0.33, 1, 1),
          "baby blue":(0.66, 0.5, 1), "cyan":(0.5, 1, 1),
          "brown":(0.07, 0.86, 0.54), "beige":(0.083, 0.32, 1),
          "indigo":(0.75, 1, 0.5), "dark gray":(0, 0, 0.15),
          "light gray":(0, 0, 0.75), "maroon":(0, 1, 0.5),
          "navy":(0.66, 1, 0.25)}

class Effect(object):
    def __init__(self, wall):
        self.wall = wall
        self.wall.clear()

    def run(self):
        pass

class SolidColorTest(Effect):
    def run(self):
        hue = 1
        saturation = 1
        value = 1

        hsv = (hue, saturation, value)
        for x in range(self.wall.width):
            for y in range(self.wall.height):
                self.wall.set_pixel(x, y, hsv)

        self.wall.draw()
        time.sleep(2)

class HueTest(Effect):
    def run(self):
        hue = random.random()
        start_time = time.time()
        while time.time() - start_time < 5:
            hsv = (hue, 1, 1)
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, hsv)
            self.wall.draw()
            hue = (hue + .01) % 1
            time.sleep(.05)

class SaturationTest(Effect):
    def run(self):
        hue = random.random()
        saturation = 0
        start_time = time.time()
        while time.time() - start_time < 5:
            hsv = (hue, saturation, 1)
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, hsv)
            self.wall.draw()
            saturation = (saturation + .05) % 1
            time.sleep(.05)

class ValueTest(Effect):
    def run(self):
        hue = random.random()
        value = 0
        start_time = time.time()
        while time.time() - start_time < 5:
            hsv = (hue, 1, value)
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, hsv)
            self.wall.draw()
            value = (value + .05) % 1
            time.sleep(.05)

class DictionaryTest(Effect):
    def run(self):
        for color in colors.keys():
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, colors[color])
            self.wall.draw()
            time.sleep(0.5)

class Checkerboards(Effect):
    def run(self):
        for i in range(10):
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    if (x + y + i) % 2 == 0:
                        self.wall.set_pixel(x, y, colors["black"])
                    else:
                        self.wall.set_pixel(x, y, colors["yellow"])
            self.wall.draw()
            time.sleep(0.5)

Effects = [SolidColorTest, HueTest, SaturationTest, ValueTest,
           DictionaryTest, Checkerboards]
