#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myhdl import *

from comb_modules import *

@block
def toplevel(LEDR, SW, HEX0, HEX1):
    # Aux signals
    ledr_s = [Signal(bool(0)) for i in range(10)]

    # Instatiations
    # ic1 = exe4(ledr_s, SW)
    ic2 = exe5(ledr_s, SW)
    ic2 = sw2hex(HEX0, SW)
    # ic3 = bin2hex(HEX1, SW)

    @always_comb
    def comb():
        for i in range(len(LEDR)):
            LEDR[i].next = ledr_s[i]

    return instances()


LEDR = Signal(intbv(0)[10:])
SW = Signal(intbv(0)[10:])
KEY = Signal(intbv(0)[4:])
HEX0 = Signal(intbv(1)[7:])
HEX1 = Signal(intbv(1)[7:])
HEX2 = Signal(intbv(1)[7:])
HEX3 = Signal(intbv(1)[7:])
HEX4 = Signal(intbv(1)[7:])
HEX5 = Signal(intbv(1)[7:])
CLOCK_50 = Signal(bool())
RESET_N = ResetSignal(0, active=0, isasync=True)

top = toplevel(LEDR, SW, HEX0, HEX1)
top.convert(hdl="verilog")
