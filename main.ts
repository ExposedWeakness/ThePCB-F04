function wrong () {
    input2 = 0
    for (let index = 0; index < 3; index++) {
        basic.showIcon(IconNames.No)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 63, 5000, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
}
input.onPinPressed(TouchPin.P0, function () {
    basic.showLeds(`
        . . # . .
        . # # . .
        . . # . .
        . . # . .
        . # # # .
        `)
    if (input2 == 0) {
        input2 = 1
    } else {
        wrong()
    }
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showLeds(`
        . # # # .
        . . . # .
        . # # # .
        . . . # .
        . # # # .
        `)
    if (input2 == 1) {
        input2 = 13
    } else {
        wrong()
    }
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showLeds(`
        . # # # .
        . . . # .
        . # # # .
        . # . . .
        . # # # .
        `)
    if (input2 == 13) {
        input2 = 132
    } else {
        wrong()
    }
})
let input2 = 0
pins.servoSetPulse(AnalogPin.P8, 1500)
input2 = 0
let password = 132
let locked = 1
basic.forever(function () {
    if (password == input2) {
        if (locked == 1) {
            pins.servoWritePin(AnalogPin.P8, 180)
            locked = 0
        } else {
            pins.servoWritePin(AnalogPin.P8, 0)
            locked = 1
        }
        for (let index = 0; index < 4; index++) {
            basic.showIcon(IconNames.Yes)
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 5000, 1, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
        input2 = 0
    }
})
