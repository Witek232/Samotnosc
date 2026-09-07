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

## Co się zmieniło w v3.2 (2026-09-07)

1. **Głos wiodący — decyzja autorska.** Myśl Josepha Ratzingera / Benedykta XVI zostaje głosem wiodącym i ostatecznie dominującym książki. Rozróżnienie kluczowe: **rejestr** (jak brzmi zdanie — bez zmian, ~80%) vs **głos** (czyja teza rozstrzyga — warstwa nowa). Realizacja: `dokumenty/05_KARTOTEKA_RATZINGEROWSKA.md` (cztery osie, cytaty ✔, reguły warsztatowe) i nota nadrzędna w `dokumenty/02_STYL_PISARSKI.md` § 0.
2. **Aparat naukowy scentralizowany.** `dokumenty/06_KARTOTEKA_CYTATOW.md` — jeden rejestr wszystkich cytatów ze statusami. **Reguła bezwzględna: cudzysłów wolno postawić wyłącznie przy pozycji ✔.**
3. **Trzy warstwy przekrojowe pod kontrolą.** `dokumenty/07_REJESTR_REFRENU_SCEN_I_GLOSOW.md` — cisza refrenu w czterech rozdziałach, rejestry scen (żeby książka nie zawęziła się do jednego świata), wejście Arendt / Weil / Stein i kobiet jako podmiotów scen.
4. **Plan pisania.** `dokumenty/04_PLAN_PISANIA_I_LINIA_RATZINGEROWSKA.md` — kolejność fal (38 → 39 → 40 → 41–43 → 44 → 22–23 → finał → początek).
5. **Sprostowanie źródłowe.** „Zawsze będzie samotność" = *Deus caritas est* **§ 28b**, nie § 29 (poprawione w `01_WERYFIKACJA_LITERATURY.md` i w konspektach).
6. **Biblioteka i narzędzia.** `narzedzia/` — skrypty do odczytu PDF/MOBI/EPUB i wyszukiwania cytatów z lokalizacją; `biblioteka/` (poza repozytorium — `.gitignore`) na pliki źródłowe autora.
7. **Rękopis: wolno pisać od nowa.** Decyzja autora — istniejące rozdziały nie wiążą; przy przepisywaniu obowiązują reguły v3.2.

## Struktura repozytorium

```
Samotnosc/
├── README.md                  ← ten plik
├── konspekty_v3/              ← TECZKA AKTUALNA — 51 jednostek (JEDYNE źródło pisania)
├── konspekty_v2/              ← archiwum: teczka v2 (47 jednostek, rekonstrukcja)
├── konspekty_v1/              ← archiwum: oryginalne pliki v1 (50 szt., stara numeracja)
├── rozdzialy/                 ← rękopis (teksty pełne; patrz rozdzialy/README.md)
├── narzedzia/                 ← skrypty: odczyt PDF/MOBI/EPUB, wyszukiwanie cytatów
├── biblioteka/                ← pliki źródłowe autora (POZA repozytorium — .gitignore)
└── dokumenty/
    ├── STRUKTURA_V3.md        ← dokument nadrzędny (decyzje, mapy numeracji, statusy)
    ├── SPIS_PLIKOW.md         ← indeks główny (51 jednostek ze statusami)
    ├── STRUKTURA_V2.md        ← historia decyzji v2
    ├── 00_ANALIZA_PROJEKTU.md
    ├── 01_WERYFIKACJA_LITERATURY.md
    ├── 02_STYL_PISARSKI.md
    ├── 03_WERYFIKACJA_NOWYCH_GLOSOW.md   ← weryfikacja źródeł nowych rozdziałów
    ├── 04_PLAN_PISANIA_I_LINIA_RATZINGEROWSKA.md  ← kolejność pisania + strategia głosu wiodącego
    ├── 05_KARTOTEKA_RATZINGEROWSKA.md   ← osie myśli, cytaty ✔, reguły warsztatowe głosu
    ├── 06_KARTOTEKA_CYTATOW.md          ← rejestr zbiorczy aparatu (statusy ✔ / [?] / [tł] / [atr])
    ├── 07_REJESTR_REFRENU_SCEN_I_GLOSOW.md  ← refren, sceny, obsada głosów
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
