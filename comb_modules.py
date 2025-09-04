# -*- coding: utf-8 -*-
"""Exercice 1

Implemente a equacão:

q = a or !b
"""

from myhdl import *


@block
def exe1(q, a, b):
    """
    q = a or !b
    """
    @always_comb
    def comb():
        q.next = a or (not b)

    return instances()


@block
def exe2(q, a, b, c):
    """
    Implemente a tabela verdade a seguir:

    A B C | Q
    ------|--
    0 0 0 | 1
    0 0 1 | 0
    0 1 0 | 0
    0 1 1 | 1
    1 0 0 | 1
    1 0 1 | 0
    1 1 0 | 0
    1 1 1 | 1

    Não utilize IF!
    """
    @always_comb
    def comb():
        # expressão lógica que corresponde à tabela
        q.next = (not b and not c) or (b and c) or a and not(b ^ c)

    return instances()


@block
def exe3(q, a, b, c, d, e):
    """
    Exercice 3

    q = (a or b) and c and d and e
    """
    @always_comb
    def comb():
        q.next = (a or b) and c and d and e

    return instances()



@block
def exe4(led, sw):
    """
    led0 é sw[0] and (não sw[1])
    """
    @always_comb
    def comb():
        led[0].next = sw[0] and (not sw[1])

    return instances()


@block
def exe5(leds, sw):
    """
    led0 é uma copia da chave sw0
    led1 é sw0 & sw1
    led2 é o led1 invertido
    led3 é xor entre sw0 e sw1
    todos os outros leds acesos
    """
    @always_comb
    def comb():
        leds[0].next = sw[0]
        leds[1].next = sw[0] and sw[1]
        leds[2].next = not leds[1]
        leds[3].next = sw[0] ^ sw[1]
        for i in range(4, len(leds)):
            leds[i].next = True

    return instances()


@block
def sw2hex(hex_pins, sw):
    """
    Faz a conversão de binário para display de 7 segmentos
    """
    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex_pins.next = "1000000"  # 0
        elif sw[4:0] == 1:
            hex_pins.next = "1111001"  # 1
        elif sw[4:0] == 2:
            hex_pins.next = "0100100"  # 2
        elif sw[4:0] == 3:
            hex_pins.next = "0110000"  # 3
        elif sw[4:0] == 4:
            hex_pins.next = "0011001"  # 4
        elif sw[4:0] == 5:
            hex_pins.next = "0010010"  # 5
        elif sw[4:0] == 6:
            hex_pins.next = "0000010"  # 6
        elif sw[4:0] == 7:
            hex_pins.next = "1111000"  # 7
        elif sw[4:0] == 8:
            hex_pins.next = "0000000"  # 8
        elif sw[4:0] == 9:
            hex_pins.next = "0010000"  # 9
        elif sw[4:0] == 10:
            hex_pins.next = "0001000"  # A
        elif sw[4:0] == 11:
            hex_pins.next = "0000011"  # b
        elif sw[4:0] == 12:
            hex_pins.next = "1000110"  # C
        elif sw[4:0] == 13:
            hex_pins.next = "0100001"  # d
        elif sw[4:0] == 14:
            hex_pins.next = "0000110"  # E
        else:
            hex_pins.next = "0001110"  # F

    return instances()
