def wrong():
    global input2
    input2 = 0
    for index in range(5):
        basic.show_icon(IconNames.NO)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                1,
                5000,
                255,
                255,
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

def on_button_pressed_a():
    global input2
    if input2 == 0:
        input2 = 1
    else:
        if input2 == 12:
            input2 = 123
        else:
            wrong()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global input2
    if input2 == 1:
        input2 = 12
    else:
        if input2 == 123:
            input2 = 1234
        else:
            wrong()
input.on_button_pressed(Button.B, on_button_pressed_b)

input2 = 0
input2 = 0
password = 1234

def on_forever():
    global input2
    if password == input2:
        for index2 in range(4):
            basic.show_icon(IconNames.YES)
            music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
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
        input2 = 0
basic.forever(on_forever)
