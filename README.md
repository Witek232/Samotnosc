# Ołowiana samotność. Wierzę w Ciebie

Repozytorium robocze książki — konspekty, dokumentacja strukturalna i rękopis.
**Wersja obowiążąca: V3** (51 jednostek: Prolog + 49 rozdziałów + Epilog).

## Co się zmieniło w V3 (2026-09-06)

1. **Uporządkowanie wersji** — repozytorium przeszło z płaskiego katalogu (przemieszane pliki v1/v2) na strukturę teczek i archiwów.
2. **Rozszerzenie spojrzenia o wielkie tradycje** (decyzja autora):
   - **rozdz. 11 — Wschód** (buddyzm, hinduizm, taoizm, konfucjanizm) — zamyka część II;
   - **rozdz. 30 — Heschel: Bóg szuka człowieka** (judaizm po Chrystusie) — część VI;
   - **rozdz. 38 — Prawosławie: pustynia, światło, soborność** — część VII;
   - **rozdz. 39 — Protestantyzm: sam przed Bogiem — razem przez Chrystusa** (Luther + Bonhoeffer) — część VII;
   - odwołana decyzja v2 o „kartotece zachodniochrześcijańskiej" — Bonhoeffer i Heschel wracają jako pełne świadectwa.
3. **Numeracja przeliczona** — wszystkie odesłania wewnętrzne w teczce v3 zaktualizowane (kontrola: 537 zamian, 0 rozbieżności).

## Struktura repozytorium

```
Samotnosc/
├── README.md                  ← ten plik
├── konspekty_v3/              ← TECZKA AKTUALNA — 51 jednostek (JEDYNE źródło pisania)
├── konspekty_v2/              ← archiwum: teczka v2 (47 jednostek, rekonstrukcja)
├── konspekty_v1/              ← archiwum: oryginalne pliki v1 (50 szt., stara numeracja)
├── rozdzialy/                 ← rękopis (teksty pełne; patrz rozdzialy/README.md)
└── dokumenty/
    ├── STRUKTURA_V3.md        ← dokument nadrzędny (decyzje, mapy numeracji, statusy)
    ├── SPIS_PLIKOW.md         ← indeks główny (51 jednostek ze statusami)
    ├── STRUKTURA_V2.md        ← historia decyzji v2
    ├── 00_ANALIZA_PROJEKTU.md
    ├── 01_WERYFIKACJA_LITERATURY.md
    ├── 02_STYL_PISARSKI.md
    ├── 03_WERYFIKACJA_NOWYCH_GLOSOW.md   ← weryfikacja źródeł nowych rozdziałów
    ├── KARTOTEKA_ROZDZIALOW.md          ← pierwotna kartoteka źródłowa
    └── archiwum/              ← wcześniejsze wersje spisów i duplikaty
```

## Jak pracować

- **Pisanie** — wyłącznie z `konspekty_v3/` (nagłówek pliku = numer w nazwie pliku; mapa części i statusy — `dokumenty/SPIS_PLIKOW.md`).
- **Szczegóły decyzji i mapy numeracji** — `dokumenty/STRUKTURA_V3.md` (§ 1 mapa v2→v3; § 5 reguły przeliczania odesłań).
- **Archiwa** (`konspekty_v1/`, `konspekty_v2/`) — tylko referencyjne; **nie pisać** z wersji pojedynczych rozdziałów scalonych (lista w `SPIS_PLIKOW.md`).
- **Rękopis** — pełne teksty rozdziałów w `rozdzialy/` (numeracja v3; pliki lokalne autora do wgrania — instrukcja w `rozdzialy/README.md`).
- **Notacja** — ✔ potwierdzone w weryfikacji; [?] do sprawdzenia przy redakcji; „robocze zdanie/parafraza" = propozycja autorska, nie cytat.

## Zasady numeracji v3 (ściąga)

- v3 1–10 = v2 1–10;
- v3 12–30 = v2 11–29 (+1; nowy 11: Wschód);
- v3 31–34 = v2 29–32 (+2; nowy 30: Heschel);
- v3 35–37 = v2 33–35 (+2);
- v3 40–49 = v2 36–45 (+4; nowe 38: Prawosławie, 39: Protestantyzm);
- centrum książki („Zstąpił do piekieł") = **rozdz. 24**; gradacja drzwi: 24 → 26 → 47.

## Historia wersji

| Wersja | Data | Skala | Kluczowa zmiana |
|---|---|---|---|
| v1 | 2026-09-03 | Prolog + 48 + Epilog (50 konspektów) | pierwotna teczka |
| v2 | 2026-09-03 | 47 jednostek | fuzje 4+5, 11+12, 27+28; kartoteka zachodniochrześcijańska (wycofani: Bonhoeffer, Heschel); odesłania przeliczone |
| **v3** | **2026-09-06** | **51 jednostek** | **rozszerzenie o tradycje: Wschód (11), judaizm po Chrystusie (30), prawosławie (38), protestantyzm (39); kartoteka odwołana; repozytorium uporządkowane** |
