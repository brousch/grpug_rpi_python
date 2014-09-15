import datetime
from BreakfastSerial import Arduino, Led, Button

board = Arduino()
led13 = Led(board, 13)
ledg = Led(board, 9)
ledr = Led(board, 10)
btn = Button(board, 2)

def btn_up_cb():
    ledg.off()
    ledr.off()

def btn_down_cb():
    ledg.on()
    ledr.off()

def btn_hold_cb():
    ledg.blink(200)
    second = datetime.datetime.now().second
    print("Current second: {}".format(second))
    bspeed = second * 1000 / 60
    ledr.blink(bspeed)

if __name__=="__main__":
    btn.up(btn_up_cb)
    btn.down(btn_down_cb)
    btn.hold(btn_hold_cb)

    led13.blink(1000)
    print("Ready.")
    print("Press ctrl + c to quit.")
    while True:
        pass
