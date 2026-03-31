import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeConfiguration
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB
from kmk.extensions.oled import OLED, OLED_DisplayMode

keyboard = KMKKeyboard()

keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D3, board.D7, board.D8)
keyboard.diode_orientation = DiodeConfiguration.COL2ROW

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D6, board.D9, None),)
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]

keyboard.extensions.append(MediaKeys())

rgb = RGB(pixel_pin=board.D10, num_pixels=9, val_default=50)
keyboard.extensions.append(rgb)

oled = OLED(
    scl=board.SCL,
    sda=board.SDA,
    width=128,
    height=32,
    flip=False,
    display_mode=OLED_DisplayMode.TXT,
    entries=[
        {"t": "Cosmic Girl", "x": 20, "y": 0},
        {"t": "F13-F20 | Vol", "x": 0, "y": 16},
    ]
)
keyboard.extensions.append(oled)

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F17, KC.F18,
        KC.F19, KC.F20, KC.MUTE,
    ],
]

if __name__ == '__main__':
    keyboard.go()