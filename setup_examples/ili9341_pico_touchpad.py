# ili9341_pico_touchpad.py Customise for your hardware config

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2026 Peter Hinch

# As written, supports:
# ili9341 240x320 displays on Pi Pico with touchpad input
# Edit the driver import for other displays.

# Demo of initialisation procedure designed to minimise risk of memory fail
# when instantiating the frame buffer. The aim is to do this as early as
# possible before importing other modules.

from machine import Pin, SPI, freq
import gc

from drivers.ili93xx.ili9341 import ILI9341 as SSD

freq(250_000_000)  # RP2 overclock
# Create and export an SSD instance
prst = Pin(9, Pin.OUT, value=1)
pcs = Pin(10, Pin.OUT, value=1)
pdc = Pin(8, Pin.OUT, value=0)  # Arbitrary pins
spi = SPI(0, sck=Pin(6), mosi=Pin(7), miso=Pin(4), baudrate=30_000_000)
gc.collect()  # Precaution before instantiating framebuf
ssd = SSD(spi, pcs, pdc, prst, usd=True)
gc.collect()
from gui.core.ugui import Display, quiet

# quiet()
# Create and export a Display instance
# Define control buttons
nxt = Pin(27, Pin.IN, Pin.PULL_DOWN)  # Move to next control
sel = Pin(17, Pin.IN, Pin.PULL_DOWN)  # Operate current control
prev = Pin(26, Pin.IN, Pin.PULL_DOWN)  # Move to previous control
increase = Pin(28, Pin.IN, Pin.PULL_DOWN)  # Increase control's value
decrease = Pin(16, Pin.IN, Pin.PULL_DOWN)  # Decrease control's value
# Pass RP2 touch config args
display = Display(ssd, nxt, sel, prev, increase, decrease, False, (7, 0, 500))
