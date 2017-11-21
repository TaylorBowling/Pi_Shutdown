# Pi_Shutdown

Python code for a simple shutdown button for the Raspberry Pi. After this button is pressed, the Pi will go into a sleep mode and can be safely unplugged. Alternatively, another button between GPIO pin 3 and a ground pin will create a short when pressed, which will wake the Pi out of this sleep mode, with no extra code required. Using this, one can easily create an on/off button for the Raspberry Pi by autostarting this program with systemd.

## Authors

* **Taylor Bowling** - *Initial work*


