import display
import leds
import utime
import buttons

_rand = 123456789
def rand():
    global _rand
    _rand = (1103515245 * _rand + 12345) & 0xffffff
    return _rand

gs = 160
colors = [ ((i>>2)*gs, (i>>1&1)*gs, (i&1)*gs) for i in range(1, 8) ]

nick = 'sample text'
try:
    with open('/nickname.txt') as f:
        nick = f.read()
except:
    pass

while True:
    pressed = buttons.read(
        buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT
    )

    if pressed & buttons.BOTTOM_LEFT != 0:
        with display.open() as d:
            fg = colors[rand()%len(colors)]
            nx = 80-round(len(nick)/2 * 14)
            d.clear()
            d.print(nick, fg=fg, bg=[0xff-c for c in fg], posx=(nx-8)+rand()%16, posy=22+rand()%16)
            d.update()
            d.close()
            utime.sleep_ms(500)
    elif pressed & buttons.BOTTOM_RIGHT != 0:
        with display.open() as d:
            d.clear()
            d.update()
            d.close()
    else:
        leds.set(rand() % 11, colors[rand() % len(colors)])
        leds.set_rocket(rand() % 3, rand() % 32)
        utime.sleep_ms(100)

    utime.sleep_us(1)
