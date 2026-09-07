# biblioteka/ — źródła do kwerendy

> **Pliki książek z tego katalogu NIE trafiają do repozytorium.** Chroni je `.gitignore`
> (sprawdzone testem 2026-09-07). Do GitHuba idzie wyłącznie ten plik i puste `.gitkeep`.
> Powód: prawa autorskie — repozytorium jest publiczne.

## Instrukcja: jak wgrać książki (krok po kroku)

### Krok 1 — sprawdź, że katalogi istnieją

```
biblioteka/
├── ratzinger/     ← Joseph Ratzinger / Benedykt XVI
├── inne/          ← pozostali autorzy kartoteki
└── _tekst/        ← TU POWSTAJĄ pliki .txt (nie wrzucaj tu nic ręcznie)
```

Jeśli któregoś brakuje: `mkdir -p biblioteka/ratzinger biblioteka/inne biblioteka/_tekst`

### Krok 2 — skopiuj pliki

Przeciągnij pliki do `biblioteka/ratzinger/` (lub `inne/`). Obsługiwane: **PDF, MOBI, AZW3, EPUB, DOCX, TXT**.
Nie działają: skany bez warstwy tekstowej (potrzebny OCR) i pliki z DRM z Kindle Store.

**Nazewnictwo — proszę o trzymanie się schematu**, bo nazwa pliku trafia potem do przypisów:

```
autor_tytul-skrocony_jezyk.rozszerzenie
```

Przykłady:
```
ratzinger_wprowadzenie-w-chrzescijanstwo_pl.pdf
ratzinger_eschatologia_pl.pdf
ratzinger_eschatology_en.pdf          ← wyd. Ignatius Press
ratzinger_jezus-z-nazaretu-t2_pl.mobi
ratzinger_duch-liturgii_pl.epub
bonhoeffer_o-zyciu-wspolnym_pl.pdf
```

Sufiks `_pl` / `_en` jest istotny: decyduje, czy z pliku wolno brać cytat do tekstu głównego,
czy tylko lokalizację i sens (zasada w `narzedzia/README.md`).

### Krok 3 — sprawdź, że Git ich nie widzi

```bash
git status --short
```

W wyniku **nie może** pojawić się żadna nazwa pliku książki. Jeśli się pojawi — stop, zgłoś to,
zanim zrobisz commit.

### Krok 4 — powiedz mi, że pliki są

Resztę robię ja:

```bash
python3 narzedzia/czytaj.py biblioteka/ratzinger/     # ekstrakcja do _tekst/
python3 narzedzia/szukaj.py "samotno" --kontekst 500  # kwerenda
```

Wyniki (brzmienie + lokalizacja) trafiają do `dokumenty/05_KARTOTEKA_RATZINGEROWSKA.md`
i podnoszą pozycje z `[?]` do `✔`.

## Czego szukam w pierwszej kolejności

Lista R1–R10 w `dokumenty/05_KARTOTEKA_RATZINGEROWSKA.md` § 5. Priorytety:

| Priorytet | Pozycja | Po co |
|---|---|---|
| **1** | *Wprowadzenie w chrześcijaństwo* (masz PDF) | R1–R4: wiara i wątpienie; „zstąpił do piekieł"; osoba jako relacja — fundament trzech osi książki |
| **1** | *Eschatologia. Śmierć i życie wieczne* | R5: pracuje w czterech rozdziałach (23, 26, 47, 49); najważniejsze nieużyte źródło |
| 2 | *Jezus z Nazaretu* t. 2 | R6–R7: Getsemani, Ps 22 — dla rozdz. 25 i 48 |
| 2 | *Duch liturgii* | R8: cytowany w rękopisie bez stron |
| 3 | wywiady z Seewaldem | R9: zdania o ciemności wiary |
| — | Bonhoeffer, *O życiu wspólnym* | cytat-kotwica rozdz. 39 — bez niego rozdział traci najmocniejsze zdanie |

## Uwaga o numeracji stron

Twój PDF *Wprowadzenia* ma niewierny układ — numer strony PDF ≠ strona wydania.
**Brzmienie cytatu będzie w pełni zweryfikowane, strona nie.** Dlatego dla Ratzingera
przyjmujemy cytowanie **wg części i rozdziału** (niezależne od wydania) oraz status `[s?]`.
Szczegóły: `narzedzia/README.md`, sekcja „Problem numeracji stron".
