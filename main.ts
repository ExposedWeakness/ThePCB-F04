function wrong () {
    input2 = 0
    for (let index = 0; index < 5; index++) {
        basic.showIcon(IconNames.No)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1, 5000, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
}
input.onButtonPressed(Button.A, function () {
    if (input2 == 0) {
        input2 = 1
    } else {
        if (input2 == 12) {
            input2 = 123
        } else {
            wrong()
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (input2 == 1) {
        input2 = 12
    } else {
        if (input2 == 123) {
            input2 = 1234
        } else {
            wrong()
        }
    }
})
let input2 = 0
input2 = 0
let password = 1234
basic.forever(function () {
    if (password == input2) {
        for (let index = 0; index < 4; index++) {
            basic.showIcon(IconNames.Yes)
            music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 5000, 1, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
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
