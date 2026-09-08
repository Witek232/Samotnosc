# ORGANIZACJA REPOZYTORIUM — co jest aktualne, a co nie

**Data:** 2026-09-07 (v3.2) · **Ten plik rozstrzyga wątpliwości „z którego pliku pisać".**

---

## 1. Zasada jednego źródła

Repozytorium rosło przez trzy wersje i największym ryzykiem nie jest brak dokumentów, lecz **mieszanie się aktualnych ze starymi**. Rozwiązanie przyjęte w v3.2 jest proste: **wszystko, co nieaktualne, leży w katalogu `archiwum/`.** Jeśli plik jest poza archiwum — jest obowiązujący.

Nie tworzymy katalogu „nowe dokumenty" obok „starych", bo za trzy miesiące powstałby „najnowsze" i problem wróciłby spotęgowany. **Aktualne = w katalogu głównym swojego działu. Nieaktualne = w `archiwum/`.** Nic pośrodku.

## 2. Mapa

```
Samotnosc/
├── README.md              ← wizytówka projektu
├── ORGANIZACJA.md         ← TEN PLIK: co aktualne, co archiwalne
│
├── konspekty_v3/          ✅ JEDYNE ŹRÓDŁO PISANIA — 51 jednostek
│                             (v1 i v2 usunięte z repo; historia w git)
│
├── rozdzialy/             ✅ RĘKOPIS — teksty pełne, numeracja v3
│   └── README.md             stan, kolejność pisania, zasada „rękopis nie wiąże"
│
├── dokumenty/             ✅ DOKUMENTACJA OBOWIĄZUJĄCA (9 plików)
│   ├── STRUKTURA_V3.md       dokument nadrzędny — decyzje, mapy numeracji, aneks v3.2
│   ├── SPIS_PLIKOW.md        indeks 51 jednostek ze statusami
│   ├── 01_WERYFIKACJA_LITERATURY.md
│   ├── 02_STYL_PISARSKI.md   § 0 = nota nadrzędna o głosie wiodącym
│   ├── 03_WERYFIKACJA_NOWYCH_GLOSOW.md
│   ├── 04_PLAN_PISANIA_I_LINIA_RATZINGEROWSKA.md
│   ├── 05_KARTOTEKA_RATZINGEROWSKA.md   ← głos wiodący: osie, cytaty ✔, reguły
│   ├── 06_KARTOTEKA_CYTATOW.md          ← aparat: statusy wszystkich cytatów
│   ├── 07_REJESTR_REFRENU_SCEN_I_GLOSOW.md
│   └── archiwum/          ⛔ NIE PISAĆ Z TEGO — historia decyzji
│
├── narzedzia/             🔧 skrypty: odczyt PDF/MOBI/EPUB, wyszukiwanie cytatów
│
└── biblioteka/            📚 pliki źródłowe autora — POZA GITEM (.gitignore)
    ├── README.md             instrukcja wgrywania
    ├── ratzinger/            książki Ratzingera
    ├── inne/                 pozostali autorzy
    └── _tekst/               wynik ekstrakcji (generowany, nie edytować ręcznie)
```

## 3. Co zostało przeniesione do archiwum w v3.2

| Plik | Dlaczego |
|---|---|
| `STRUKTURA_V2.md` | historia decyzji v2; zastąpiony przez `STRUKTURA_V3.md` |
| `KARTOTEKA_ROZDZIALOW.md` | dokument założycielski; treść przeszła do konspektów v3 |
| `00_ANALIZA_PROJEKTU.md` | diagnoza merytorycznie wartościowa, ale **numeracja wg v1** — najgroźniejszy plik w repo, bo wygląda na aktualny, a jego numery rozdziałów są przesunięte o 1–4 |

**Uwaga:** archiwizacja to nie kasowanie. Pliki są w `dokumenty/archiwum/` i wolno do nich zaglądać — nie wolno z nich **pisać**.

## 4. Trzy pytania, na które odpowiada ta struktura

**„Z czego piszę rozdział?"**
→ `konspekty_v3/NN_*.md` + noty v3.2 na końcu pliku. Nic więcej nie jest potrzebne do startu.

**„Czy mogę postawić cudzysłów?"**
→ Tylko jeśli pozycja ma status ✔ w `06_KARTOTEKA_CYTATOW.md` lub `05_KARTOTEKA_RATZINGEROWSKA.md`. Inaczej parafraza.

**„Czy ten dokument jest aktualny?"**
→ Jeśli nie leży w `archiwum/` — tak.

## 5. Rytuał po napisaniu każdego rozdziału

1. Dopisz nowe cytaty do `06_KARTOTEKA_CYTATOW.md` § 3 (ze statusem i datą).
2. Uzupełnij `07_REJESTR_REFRENU_SCEN_I_GLOSOW.md`: odpowiedź refrenu (część A3) i rejestr sceny (część B2).
3. Zmień status w `SPIS_PLIKOW.md`.
4. Commit z nazwą rozdziału.

Cztery kroki, dwie minuty. Pominięte raz — nie nadrobi się przy 51 jednostkach.
