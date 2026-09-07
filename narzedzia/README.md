# narzedzia/ — obsługa biblioteki źródeł

## Co mogę odczytać (sprawdzone 2026-09-07)

| Format | Status | Czym |
|---|---|---|
| **PDF (tekstowy)** | ✔ w pełni | PyMuPDF — tekst + numery stron PDF |
| **PDF (skan, bez warstwy tekstowej)** | ✖ | wymagałby OCR; jeśli taki się trafi — zgłoszę |
| **MOBI** | ✔ | biblioteka `mobi` (rozpakowanie do HTML) + BeautifulSoup |
| **EPUB** | ✔ | `ebooklib` |
| **AZW3** | ✔ zwykle | ta sama ścieżka co MOBI |
| **AZW / KFX (DRM)** | ✖ | DRM nie do obejścia — potrzebna wersja bez DRM |
| DOCX, TXT, HTML, RTF | ✔ | standardowo |

**Uwaga o DRM:** pliki kupione w Kindle Store bywają zabezpieczone. Jeśli plik się nie otworzy, przyczyną jest niemal zawsze DRM — proszę wtedy o wersję z innego źródła (np. PDF wydawcy).

## Jak wgrać książki

Katalog `biblioteka/` (dodany do `.gitignore` — **pliki nie trafiają do repozytorium**, zostają lokalnie/w sesji roboczej; to świadoma decyzja: prawa autorskie).

```
biblioteka/
├── ratzinger/     ← teksty Ratzingera/Benedykta XVI
├── inne/          ← pozostali autorzy kartoteki
```

Nazewnictwo plików — swobodne, ale pomocne: `ratzinger_wprowadzenie_w_chrzescijanstwo_pl.pdf`,
`ratzinger_eschatology_ignatius_en.pdf`.

## Skrypty

### `czytaj.py` — ekstrakcja tekstu do postaci przeszukiwalnej

```bash
python3 narzedzia/czytaj.py biblioteka/ratzinger/plik.pdf
```
Tworzy `biblioteka/_tekst/plik.txt` z **znacznikami stron** w formie `[[s.123]]`
(dla PDF: numer strony PDF; dla MOBI/EPUB: numer sekcji `[[sek.12]]`).

### `szukaj.py` — wyszukiwanie fraz z lokalizacją

```bash
python3 narzedzia/szukaj.py "samotność" --kontekst 400
python3 narzedzia/szukaj.py "loneliness" --plik eschatology
```
Zwraca fragment + numer strony/sekcji — czyli dokładnie to, czego potrzebuje przypis.

## Problem numeracji stron — czytać uważnie

Autor zgłosił, że jego PDF *Wprowadzenia w chrześcijaństwo* **nie ma wiernego układu książki**.
To znaczy, że numer strony PDF ≠ numer strony wydania. Konsekwencja dla aparatu naukowego:

- **Nie wolno** podawać w przypisach numerów stron odczytanych z takiego PDF-a jako stron wydania.
- Cytat pozostaje w pełni użyteczny — **dosłowne brzmienie jest zweryfikowane**, co jest ważniejsze.
- W przypisie stosujemy wtedy zapis: `[wyd. i strona do uzupełnienia — brzmienie zweryfikowane z egz. autora]`
  i oznaczamy `[s?]` zamiast `[?]` (rozróżnienie: `[?]` = niepewne brzmienie, `[s?]` = pewne brzmienie, niepewna strona).
- Alternatywa mocniejsza: cytować **wg części i rozdziału** (np. „cz. I, rozdz. 1"), co jest niezależne od wydania
  i w książce eseistycznej wygląda równie dobrze. **Rekomendacja: przyjąć to jako standard dla Ratzingera.**

## Wydania angielskie (Ignatius Press) — zasada

Autor dysponuje głównie wydaniami angielskimi. Zasada dla książki polskiej:

1. **Cytat w tekście głównym musi być polski.** Nie tłumaczymy sami z angielskiego, jeśli istnieje przekład polski —
   przekład własny z przekładu jest podwójnym oddaleniem od oryginału niemieckiego.
2. Wydanie angielskie służy do: **znalezienia miejsca**, sprawdzenia kontekstu, upewnienia się co do sensu.
3. Jeśli polskiego wydania nie mamy pod ręką: zapisujemy w kartotece treść i lokalizację (rozdział), a w tekście
   dajemy **parafrazę oznaczoną jako parafraza** — nigdy cudzysłów. Cudzysłów zostaje zarezerwowany dla brzmień
   sprawdzonych w wydaniu polskim.
4. Gdzie oryginał niemiecki jest dostępny i wątpliwość dotyczy terminu kluczowego — odnotować termin niemiecki.
