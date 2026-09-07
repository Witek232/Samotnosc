#!/usr/bin/env python3
"""Wyszukiwanie fraz w wyekstrahowanych tekstach, z lokalizacja strony/sekcji.

Uzycie:
    python3 narzedzia/szukaj.py "samotnosc"
    python3 narzedzia/szukaj.py "loneliness" --plik eschatology --kontekst 600
    python3 narzedzia/szukaj.py "credere in Deum" --max 5
"""
import os
import re
import sys
import glob
import unicodedata

KAT = os.path.join("biblioteka", "_tekst")


def uprosc(s):
    """Bez ogonkow i wielkosci liter — zeby 'samotnosc' znajdowalo 'samotność'."""
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def lokalizacja(tekst, poz):
    frag = tekst[:poz]
    ost = None
    for m in re.finditer(r"\[\[(s|sek)\.(\d+)\]\]", frag):
        ost = m
    if not ost:
        return "poczatek pliku"
    return ("s. " if ost.group(1) == "s" else "sekcja ") + ost.group(2)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    fraza = sys.argv[1]
    args = sys.argv[2:]

    def opcja(nazwa, dom):
        return args[args.index(nazwa) + 1] if nazwa in args else dom

    filtr = opcja("--plik", "")
    kontekst = int(opcja("--kontekst", 350))
    limit = int(opcja("--max", 20))

    if not os.path.isdir(KAT):
        print(f"Brak katalogu {KAT} — najpierw uruchom narzedzia/czytaj.py")
        sys.exit(1)

    igla = uprosc(fraza)
    trafien = 0
    for sciezka in sorted(glob.glob(os.path.join(KAT, "*.txt"))):
        if filtr and filtr.lower() not in os.path.basename(sciezka).lower():
            continue
        tekst = open(sciezka, encoding="utf-8").read()
        stog = uprosc(tekst)
        start = 0
        while trafien < limit:
            i = stog.find(igla, start)
            if i < 0:
                break
            trafien += 1
            a, b = max(0, i - kontekst // 2), min(len(tekst), i + kontekst)
            frag = re.sub(r"\s+", " ", tekst[a:b]).strip()
            frag = re.sub(r"\[\[(s|sek)\.\d+\]\]", " ", frag)
            print(f"\n--- {os.path.basename(sciezka)} | {lokalizacja(tekst, i)} ---")
            print(f"...{frag}...")
            start = i + len(igla)
    if trafien == 0:
        print("Brak trafien.")
    else:
        print(f"\n[razem: {trafien}]")


if __name__ == "__main__":
    main()
