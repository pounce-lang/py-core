import asyncio
# import board
# import keypad

from pounce_parser import parse_next
from runtime import isValue
from runtime import isArray
from runtime import isRecord
from runtime import isfunction
from runtime import words

src_code = ""
src_wd = {}
src_pl = []
res_st = []
async def catch_input(src):
    global src_code
    while True:
        event = src.events.get()
        if event:
            if event.newline:
                src_code = event.src
        await asyncio.sleep(0)

async def parrrse():
    global src_code, src_wd, src_pl
    
    while True: 
        if src_pl == "":
            await asyncio.wait(src_code)
        src_pl = []
        i = 0
        s = src_code
        ls = len(s)
        w = ''
        while i < ls:
            w, i = parse_next(s, i, ls)
            if w != '' and w != None:
                src_pl.append(w)
            await asyncio.sleep(0)
        src_pl = ""


async def compose():
    global src_wd, src_pl
    while True:
        if src_pl == []:
            await asyncio.wait(src_pl)
        vs = []
        wd = src_wd
        pl = src_pl
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
            elif next == "compose" :
                if len(vs) >= 2 :
                    quoted_name = vs.pop()
                    phrase = vs.pop()
                    if quoted_name and phrase:
                        wd[ quoted_name[0] ] = phrase
                    else:
                        print('stack too small for :', next)
                else:
                    print('stack too small for :', next)
            await asyncio.sleep(0)
        src_wd = wd

async def purrr():
    global src_wd, src_pl, res_st

    while True:
        if src_pl == []:
            await asyncio.wait(src_pl)
        vs = []
        wd = src_wd
        pl = src_pl
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
        res_st = vs
        print('result stack', vs)
        src_pl = []


async def repl():
    cmt_parrrse = asyncio.create_task(parrrse())
    cmt_purrr = asyncio.create_task(compose())
    cmt_purrr = asyncio.create_task(purrr())
    watch_input = asyncio.create_task(catch_input("ble"))
    await asyncio.gather(cmt_parrrse, cmt_purrr, watch_input)

asyncio.run(repl())
