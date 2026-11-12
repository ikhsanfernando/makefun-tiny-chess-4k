#!/usr/bin/env python3
"""Perft correctness check for a chess-engine entry (tiny-chess style).

Usage: python3 perft_check.py <main.py> [--depth 3]
Requires the engine to expose parse(fen) -> (board, side, castling, ep), legal(...),
mv(...) -> (board2, side2, castling2, ep2) and (optionally) pick/uci.
Loads the engine with MAKEFUN_ENV_URL set to a dummy so module-level main() guards skip.
"""
import argparse
import importlib.util
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("prog")
ap.add_argument("--depth", type=int, default=2)
a = ap.parse_args()

os.environ.setdefault("MAKEFUN_ENV_URL", "http://x")
spec = importlib.util.spec_from_file_location("eng", a.prog)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

CASES = [
    ("startpos", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", [20, 400, 8902]),
    ("kiwipete", "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1", [48, 2039, 97862]),
    ("pos3", "8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1", [14, 191, 2812]),
    ("pos5", "rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8", [44, 1486, 62379]),
]


def perft(b, s, c, e, d):
    if d == 0:
        return 1
    ms = m.legal(b, s, c, e)
    if d == 1:
        return len(ms)
    return sum(perft(*m.mv(b, s, c, e, x)[:4], d - 1) for x in ms)


ok = True
for name, fen, expected in CASES:
    b, s, c, e = m.parse(fen)
    for depth in range(1, min(a.depth, len(expected)) + 1):
        got = perft(b, s, c, e, depth)
        exp = expected[depth - 1]
        good = got == exp
        ok &= good
        print(f"{name} d{depth}: {got} {'OK' if good else 'FAIL expected ' + str(exp)}")
print("PERFT:", "OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
