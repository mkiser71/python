from adafruit_circuitplayground.express import cpx

while True:
    if cpx.touch_A1:
        cpx.play_tone(100, 1.0)
    if cpx.touch_A2:
        cpx.play_tone(200, 1.0)
    if cpx.touch_A3:
        cpx.play_tone(300, 1.0)
    if cpx.touch_A4:
        cpx.play_tone(400, 1.0)
    if cpx.touch_A5:
        cpx.play_tone(500, 1.0)
    if cpx.touch_A6:
        cpx.play_tone(600, 1.0)
    if cpx.touch_A7:
        cpx.play_tone(700, 1.0)
