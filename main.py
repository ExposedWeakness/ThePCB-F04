def wrong():
    global input2
    input2 = 0
    for index in range(3):
        basic.show_icon(IconNames.NO)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                63,
                5000,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)

def on_pin_pressed_p0():
    global input2
    basic.show_leds("""
        . . # . .
                . # # . .
                . . # . .
                . . # . .
                . # # # .
    """)
    if input2 == 0:
        input2 = 1
    else:
        wrong()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p2():
    global input2
    basic.show_leds("""
        . # # # .
                . . . # .
                . # # # .
                . . . # .
                . # # # .
    """)
    if input2 == 1:
        input2 = 13
    else:
        wrong()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    global input2
    basic.show_leds("""
        . # # # .
                . . . # .
                . # # # .
                . # . . .
                . # # # .
    """)
    if input2 == 13:
        input2 = 132
    else:
        wrong()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

input2 = 0
input2 = 0
password = 132
locked = 1

def on_forever():
    global input2, locked
    if password == input2:
        input2 = 0
        if locked == 1:
            pins.servo_write_pin(AnalogPin.P8, 0)
            locked = 0
        else:
            pins.servo_write_pin(AnalogPin.P8, 90)
            locked = 1
        for index2 in range(4):
            basic.show_icon(IconNames.YES)
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    5000,
                    1,
                    255,
                    0,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
basic.forever(on_forever)
