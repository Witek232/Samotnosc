#!/usr/bin/env python3
"""Ekstrakcja tekstu z PDF/MOBI/EPUB do postaci przeszukiwalnej.

Uzycie:
    python3 narzedzia/czytaj.py biblioteka/ratzinger/plik.pdf
    python3 narzedzia/czytaj.py biblioteka/ratzinger/          (caly katalog)

Wynik: biblioteka/_tekst/<nazwa>.txt ze znacznikami [[s.N]] / [[sek.N]].
"""
import os
import re
import sys
import glob
import shutil
import tempfile

WY = os.path.join("biblioteka", "_tekst")


def czysc(t):
    t = t.replace("\u00ad", "").replace("\ufeff", "")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def z_pdf(sciezka):
    import pymupdf
    d = pymupdf.open(sciezka)
    if d.is_encrypted and not d.authenticate(""):
        raise RuntimeError("PDF zaszyfrowany/DRM — nie da sie odczytac")
    czesci, puste = [], 0
    for i, strona in enumerate(d, 1):
        txt = strona.get_text("text")
        if not txt.strip():
            puste += 1
        czesci.append(f"\n[[s.{i}]]\n{txt}")
    if puste > len(d) * 0.8:
        print("  UWAGA: brak warstwy tekstowej na >80% stron — to prawdopodobnie skan (potrzebny OCR).")
    return "".join(czesci)


def html_na_tekst(html):
    from bs4 import BeautifulSoup
    zupa = BeautifulSoup(html, "html.parser")
    for z in zupa(["script", "style"]):
        z.decompose()
    return zupa.get_text("\n")


def z_mobi(sciezka):
    import mobi
    katalog, plik = mobi.extract(sciezka)
    try:
        pliki = sorted(glob.glob(os.path.join(katalog, "**", "*.htm*"), recursive=True))
        if not pliki and plik and os.path.exists(plik):
            pliki = [plik]
        czesci = []
        for i, p in enumerate(pliki, 1):
            with open(p, "rb") as f:
                czesci.append(f"\n[[sek.{i}]]\n" + html_na_tekst(f.read().decode("utf-8", "ignore")))
        return "".join(czesci)
    finally:
        shutil.rmtree(katalog, ignore_errors=True)


def z_epub(sciezka):
    import ebooklib
    from ebooklib import epub
    ks = epub.read_epub(sciezka)
    czesci = []
    for i, poz in enumerate(ks.get_items_of_type(ebooklib.ITEM_DOCUMENT), 1):
        czesci.append(f"\n[[sek.{i}]]\n" + html_na_tekst(poz.get_content().decode("utf-8", "ignore")))
    return "".join(czesci)


def z_txt(sciezka):
    with open(sciezka, "rb") as f:
        return f.read().decode("utf-8", "ignore")


CZYTNIKI = {
    ".pdf": z_pdf, ".mobi": z_mobi, ".azw3": z_mobi, ".azw": z_mobi,
    ".prc": z_mobi, ".epub": z_epub, ".txt": z_txt, ".md": z_txt,
}


def przetworz(sciezka):
    rozsz = os.path.splitext(sciezka)[1].lower()
    czytnik = CZYTNIKI.get(rozsz)
    if not czytnik:
        print(f"[pomijam] {sciezka} — format {rozsz} nieobslugiwany")
        return
    print(f"[czytam] {sciezka}")
    try:
        tekst = czysc(czytnik(sciezka))
    except Exception as e:
        print(f"  BLAD: {e}")
        return
    os.makedirs(WY, exist_ok=True)
    cel = os.path.join(WY, os.path.splitext(os.path.basename(sciezka))[0] + ".txt")
    with open(cel, "w", encoding="utf-8") as f:
        f.write(tekst)
    print(f"  -> {cel}  ({len(tekst.split())} slow)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            for p in sorted(glob.glob(os.path.join(arg, "**", "*"), recursive=True)):
                if os.path.isfile(p) and "_tekst" not in p:
                    przetworz(p)
        else:
            przetworz(arg)


if __name__ == "__main__":
    main()
