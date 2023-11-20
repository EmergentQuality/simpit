# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Microsoft Teams client for CONTROL

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'ADV-CAM', # App name is menu item
    'macros' : [             
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'CAM-1', [Keycode.F4, Keycode.KEYPAD_ONE, '1', -Keycode.F4]), # 
        (0x004000, 'CAM-2', [Keycode.F4, Keycode.KEYPAD_TWO, '2', -Keycode.F4]), # 
        (0x004000, 'CAM-3', [Keycode.F4, Keycode.KEYPAD_THREE, '3', -Keycode.F4]), # 
        # 2nd row ----------
        (0x004000, 'CAM-4', [Keycode.F4, Keycode.KEYPAD_FOUR, '4', -Keycode.F4]), # 
        (0x004000, 'CAM-5', [Keycode.F4, Keycode.KEYPAD_FIVE, '5', -Keycode.F4]), # 
        (0x004000, 'CAM-6', [Keycode.F4, Keycode.KEYPAD_SIX, '6', -Keycode.F4]), # 
        # 3rd row ----------
        (0x004000, 'CAM-7', [Keycode.F4, Keycode.KEYPAD_SEVEN, '7', -Keycode.F4]), # 
        (0x004000, 'CAM-8', [Keycode.F4, Keycode.KEYPAD_EIGHT, '8', -Keycode.F4]), # 
        (0x004000, 'CAM-9', [Keycode.F4, Keycode.KEYPAD_NINE, '9', -Keycode.F4]), # 
        # 4th row ----------
        (0x004000, 'SS', [Keycode.F4, Keycode.KEYPAD_ZERO, '0', -Keycode.F4]), # 
        (0x004000, 'F4', [Keycode.F4, Keycode.F14, 'F14', -Keycode.F4]), # 
        (0x004000, 'RESET', [Keycode.F4, Keycode.F15, 'F15', -Keycode.F4]), # 
        # Encoder button ---
        (0x000000, '', [Keycode.KEYPAD_, Keycode.TAB]) # 
    ]
}
