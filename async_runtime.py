import asyncio
import board
import keypad

from runtime import isValue
from runtime import isArray
from runtime import isRecord
from runtime import isfunction
from runtime import words


async def catch_pin_transitions(pin):
    """Print a message when pin goes low and when it goes high."""
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("pin went low", pin)
                elif event.released:
                    print("pin went high", pin)
            await asyncio.sleep(0)

async def purrr(pl, wd=words, debug = False, stack = []):
    vs = []
    while pl != None and len(pl) > 0:
        next = pl[0]
        pl = pl[1:]
        if isValue(next, wd) or isArray(next) or isRecord(next):
            if next == 'true':
                vs.append(True)
            elif next == 'false':
                vs.append(False)
            else:
                vs.append(next)
        elif next in wd.keys():
            if isfunction(wd[next]):
                (vs, pl) = wd[next](vs, pl)
            elif isRecord(wd[next]):
                if 'args' in wd[next].keys():
                    arg_rec = {}
                    while len(wd[next].args) > 0:
                        arg_rec[wd[next].args.pop()] = s.pop()
                    (vs, pl) =  wd[next].func(vs, pl, arg_rec)
            else:
                pl = wd[next] + pl
        else:
            print('unknown term or word:', next)
        await asyncio.sleep(0)
    return vs


async def repl():
    # interrupt_task10 = asyncio.create_task(catch_pin_transitions(board.D10))
    # interrupt_task9 = asyncio.create_task(catch_pin_transitions(board.D9))
    watch_input = asyncio.create_task(catch_input("ble"))
    await asyncio.gather(watch_input)

asyncio.run(repl())
