# 09 — AUDYT ROZDZIAŁÓW 23–34 i 37 (rękopis odziedziczony)

**Sporządzono:** 2026-09-08 | **Zakres:** 13 plików napisanych przez poprzedniego autora na **strukturze v2**
**Cel:** ustalić, co da się poprawić, a co wymaga napisania od nowa — **przed** rozpoczęciem poprawek.

> **WNIOSEK GŁÓWNY:** rozdziały te mają **trzy wady różnej wagi**, a najpoważniejszej z nich **nie da się usunąć poprawkami**. Rekomenduję kolejność działań opisaną w § 5, a **nie** poprawianie plik po pliku od 23. Uzasadnienie poniżej. **Do decyzji autora przed dalszą pracą.**

---

## 1. WADA PIERWSZA — numeracja: wszystkie pliki mają zły numer

Rozdziały pisano na `STRUKTURA_V2`. Wersja v3 wstawiła **dwa nowe rozdziały** (30 Heschel, 38 Prawosławie, 39 Protestantyzm) i rozbiła jeden dawny. Skutek: **żaden z 12 plików nie stoi pod swoim numerem**, a jeden numer jest zajęty przez cudzą treść.

| Plik (nr v2) | Treść | Właściwy nr v3 | Przesunięcie |
|---|---|---|---|
| `23_zstapil_do_piekiel.md` | Zstąpił do piekieł — **CENTRUM KSIĄŻKI** | **24** | +1 |
| `24_glos_z_krzyza.md` | Głos z krzyża (Ps 22) | **25** | +1 |
| `25_drzwi_smierci.md` | Drzwi śmierci | **26** | +1 |
| `26_zmartwychwstanie.md` | Zmartwychwstanie | **27** | +1 |
| `27_czlowiek_jako_osoba.md` | Człowiek jako osoba | **28** | +1 |
| `28_ja_potrzebuje_ty.md` | „Ja" potrzebuje „Ty" | **29** | +1 |
| `29_wiara_jako_zaufanie.md` | Wiara jako zaufanie | **31** | **+2** |
| `30_bog_ktory_nie_jest_sam.md` | Bóg, który nie jest sam | **32** | **+2** |
| `31_syn.md` | Syn | **33** | **+2** |
| `32_christus_ty_boga_w_historii.md` | Chrystus: „Ty" w historii | **34** | **+2** |
| `33_kosciol.md` | Kościół | **35** | **+2** |
| `34_eucharystia.md` | Eucharystia | **36** | **+2** |
| `37_milosc_ktora_dziala.md` | Miłość, która działa | **37** ✔ | 0 |

**Konsekwencje, które trzeba naprawić w treści, nie tylko w nazwach plików:**

- **Brakuje rozdz. 23 „Czym jest śmierć? (fenomenologia)"** — v3 przewiduje go przed centrum. Nie istnieje.
- **Brakuje rozdz. 30 „Heschel: Bóg szuka człowieka"** — nowy w v3, wstawiony **w środek** części VI, między „Ja potrzebuje Ty" a „Wiarę jako zaufanie". To on powoduje przesunięcie +2.
- **W tekstach są dziesiątki odesłań wewnętrznych** („rozdział dwudziesty ósmy skończył się…", „rozdz. 15 czytał Ratzingera o erosie", „pełne użycie Marcela po rozdz. 25") — **wszystkie wskazują na złe numery**. Część odsyła do rozdziałów, które w v3 mają zupełnie inną treść.
- Nagłówki plików odsyłają do `konspekty_v2/` i `STRUKTURA_V2.md` — **katalogi te są w archiwum**.

**To jest praca mechaniczna, ale nie trywialna:** przenumerowania nie da się zrobić prostym `sed`, bo odesłania są **słowne** („rozdział dwudziesty ósmy") i wymagają rozstrzygnięcia, czy odsyłają do treści, czy do numeru.

---

## 2. WADA DRUGA — przypisy: cytaty bez pokrycia, w tym **dwa błędy rzeczowe**

Wszystkie 13 plików mają sekcję `**Przypisy:**` (nie `## Przypisy`), a w niej — konsekwentnie — formuły **„brzmienie robocze", „robocza parafraza", „[?]"**. To jest uczciwe jako notatka warsztatowa. Problem polega na tym, że **w tekście głównym te same frazy stoją w cudzysłowie**, czyli czytelnik dostaje je jako cytaty. Poprzedni autor sam to oznaczył — ale oznaczył **w przypisie, nie w tekście**.

### 2a. Błąd rzeczowy nr 1 — **zła atrybucja, potwierdzona u źródła** ⚠️

`28_ja_potrzebuje_ty.md`, przyp. 4:
> ⁴ Benedykt XVI, *Deus caritas est* § 16: „człowiek staje się w pełni sobą, kiedy daje się za darmo"

**To jest nieprawda.** Sprawdziłem *Deus caritas est* na vatican.va:
- Fraza „człowiek staje się w pełni sobą" **występuje w DCE § 5**, ale w zupełnie innym kontekście — dotyczy **jedności ciała i duszy**: „Jedynie wówczas, kiedy obydwa wymiary stapiają się naprawdę w jedną całość, człowiek staje się w pełni sobą". **Nie ma tam mowy o darze z siebie.**
- Myśl o darze pochodzi z ***Gaudium et spes* 24**: „człowiek […] nie może odnaleźć się w pełni inaczej jak tylko poprzez **bezinteresowny dar z siebie samego**". ✔ zweryfikowane.

**Do naprawy:** albo cytat z GS 24 (pewny, dostępny, darmowy), albo usunięcie. **Obecna forma to cytat przypisany dokumentowi, w którym go nie ma.**

### 2b. Błąd rzeczowy nr 2 — Buber, brzmienie niepoprawne ⚠️

`28_ja_potrzebuje_ty.md` i `25_drzwi_smierci.md` cytują:
> „**Wszystkie** prawdziwe życie jest spotkaniem"

To jest **niepoprawne po polsku** („wszystkie… życie"). W obiegu funkcjonują warianty „Wszelkie prawdziwe życie…" i „Całe prawdziwe życie…". **Nie wiemy, który jest u Doktóra** — a to najsłynniejsze zdanie Bubera i jedyne, które pada w cudzysłowie. Przypis sam przyznaje: „brzmienia robocze, do potwierdzenia z wydaniem [?]".
**Do czasu weryfikacji: usunąć cudzysłów albo zdanie.** Patrz dok. 08 § A1 pkt 2.

### 2c. Cytaty w cudzysłowie bez zweryfikowanego źródła — pełna lista

| Plik | Cytat | Przypisany | Status |
|---|---|---|---|
| 27 (→28) | „Między «coś» a «kogoś» jest różnica, której nie da się przełożyć na różnicę wartości użytkowej" | Spaemann | przypis mówi **„parafraza"**, a w tekście jest cudzysłów — **sprzeczność** |
| 27 (→28) | „osoba oznacza to, co jest najdoskonalsze w całej naturze" | Tomasz, STh I q.29 a.3 | przypis: „robocza parafraza" — **sprzeczność** |
| 27 (→28) | „naturae rationalis individua substantia" | Boecjusz | łacina prawdopodobnie OK, **przekład polski `[?]`** |
| 28 (→29) | „Wszystkie prawdziwe życie jest spotkaniem" | Buber | **błędne brzmienie**, patrz 2b |
| 28 (→29) | „człowiek staje się w pełni sobą, kiedy daje się za darmo" | DCE 16 | **błędna atrybucja**, patrz 2a |
| 23 (→24) | „zjednoczył się z nimi w sensie duchowym" | — | źródło nieustalone |
| 26 (→27) | „Siane w słabości, powstaje w mocy" | 1 Kor 15,43 | biblijny — **do sprawdzenia z Biblią Tysiąclecia** |
| 29 (→31) | „sprawiedliwy żyje z wierności" | Ha 2,4 | jw. |
| 29 (→31) | „trwali w nauce Apostołów…" | Dz 2,42 | jw. |

**Uwaga o skali:** liczba wystąpień formuły „brzmienie robocze"/„parafraza" w przypisach: rozdz. 33 — **6**, rozdz. 28 i 34 — **4**, rozdz. 25, 26, 29, 30, 31, 32 — po **3**.

### 2d. Czego brakuje wobec obecnego standardu

Rozdziały 40–46 (pisane teraz) mają w przypisach: **wydanie, stronę/lokalizację, znacznik ✔ weryfikacji, klauzule metodologiczne** i notę redakcyjną z punktami do rozstrzygnięcia. Rozdziały 23–37 mają **notatkę bibliograficzną z `[?]`**. To są dwa różne standardy w jednej książce.

---

## 3. WADA TRZECIA — styl i forma: mniejszy problem, niż się wydaje

Wbrew obawom autora **styl nie jest zły**. Sprawdziłem:

- **Superlatywów wobec Ratzingera praktycznie nie ma** (zakaz dok. 04 § 3): dwa trafienia w 13 plikach. To lepiej niż w niejednym rozdziale pisanym teraz.
- **Zdania są dobre.** Przykład z 29 (→31): *„Słowo «wierzyć» jest w polszczyźnie zużyte jak schód w bloku: nosi wszystko"*. To jest dobra proza.
- **Sceny są konkretne** (dziecko przy poręczy basenu, pusty kościół w Wielką Sobotę).

**Rzeczywiste wady formalne:**

1. **Zero cytatów blokowych** w 11 z 13 plików. Wszystko wpisane w tok zdania — przez co cytat i parafraza są **wizualnie nierozróżnialne**. To pogłębia wadę drugą.
2. **Długości niezgodne z v3.** Cel dla szablonu lekkiego: 2,3–2,6 tys. Mamy: rozdz. 23 → **3543**, 25 → **3662**, 29 → **3470**, 30 → **3244**. Cztery rozdziały są o **30–45% za długie**. (Reszta mieści się w widełkach.)
3. **Znaczniki „ruchów" I–VIII** zostały w tekście; nota mówi, że mają zniknąć w druku — ale w 40–46 stosujemy inną konwencję.
4. **Brak noty redakcyjnej** w obecnym formacie (punkty do rozstrzygnięcia przez autora).

---

## 4. Czego te rozdziały potrzebują ze źródeł

Zbiorczo, z odesłaniem do dok. 08:

| Rozdział (v3) | Potrzebuje | Priorytet w dok. 08 |
|---|---|---|
| 28 Człowiek jako osoba | **Spaemann**, Boecjusz, Tomasz STh I q.29, Maritain, Wojtyła *Osoba i czyn* | C / B1 |
| 29 „Ja" potrzebuje „Ty" | **Buber** ⚠️, **Marcel**, **Wojtyła** | **A1, A2, B1** |
| 26 Drzwi śmierci | **Marcel** (problem/tajemnica), Buber | **A2** |
| 31 Wiara jako zaufanie | Ratzinger ✔ (mamy), Biblia Tysiąclecia | — |
| 24, 25, 27 | Ratzinger ✔, KKK 632–637, Biblia | kwerenda własna |
| 35, 36 | Ratzinger ✔ (*Duch liturgii* — **uwaga:** rozdz. 34/v2 zawiera formułę „z «ja» do «my»", **której nie ma w *Duchu liturgii***; do usunięcia) | — |
| 37 Miłość, która działa | **Wojtyła *Miłość i odpowiedzialność***, DCE ✔ | B2 |

---

## 5. REKOMENDACJA — dlaczego nie „po kolei od 23"

Autor polecił: „sprawdź i popraw po kolei". **Odradzam** i proszę o decyzję, bo widzę tu ryzyko zmarnowanej pracy.

**Powody:**

1. **Rozdz. 29 („Ja" potrzebuje „Ty") nie da się dziś poprawić.** Jego dwa główne cytaty są: jeden błędnie przypisany (DCE), drugi w niepewnym brzmieniu (Buber). Bez *Ja i Ty* i Marcela mogę tylko **usunąć cudzysłowy** — a rozdział, którego głosem wiodącym jest Buber, zostanie bez jednego cytatu z Bubera. **Poprawianie go teraz = poprawianie go dwa razy.**
2. **Rozdz. 30 (Heschel) nie istnieje i musi powstać między 29 a 31.** Napisanie go zmieni odesłania w sąsiadach. Poprawianie 29 i 31 przed napisaniem 30 to znowu praca dwukrotna.
3. **Brakuje rozdz. 23**, który poprzedza centrum książki.
4. **Autor sam zastrzegł** (stała instrukcja): napisane rozdziały wolno **napisać od nowa** wedle nowej koncepcji, zamiast korygować. Cztery z nich są o 30–45% za długie i mają zerową liczbę cytatów blokowych — to bliżej przepisania niż korekty.

**Proponowana kolejność:**

- **Krok 1 (mogę zrobić od razu, bez żadnych źródeł):** przenumerowanie wszystkich 13 plików na v3 + naprawa odesłań wewnętrznych + ujednolicenie nagłówków (konspekty_v3, STRUKTURA_V3). **Czysto porządkowe, nic nie traci.**
- **Krok 2 (też od razu):** **usunięcie dwóch błędów rzeczowych** — zła atrybucja DCE → GS 24, oraz zdjęcie cudzysłowu z Bubera i ze Spaemanna/Tomasza tam, gdzie przypis sam mówi „parafraza". To jest naprawa **nierzetelności**, nie stylu, i nie może czekać na książki.
- **Krok 3 (od razu):** kwerendy darmowe — KKK 632–637, Biblia Tysiąclecia dla wszystkich cytatów biblijnych, GS 24, *Spe salvi* 32–33. Zamknie to znaczną część `[?]` w rozdz. 24–27 i 31.
- **Krok 4 (po zdobyciu Bubera/Marcela):** rozdz. **29** — **napisać od nowa**, nie poprawiać.
- **Krok 5:** rozdz. **23** i **30** — napisać (nie istnieją).
- **Krok 6:** skrócenie czterech przerośniętych rozdziałów i dorobienie not redakcyjnych w standardzie 40–46.

**Alternatywa, jeśli autor chce jednak „po kolei":** zaczynam od 23 (→24) i idę w dół, ale wtedy rozdziały 28, 29 i 37 zostaną w kroku pierwszym tylko „odkażone" (usunięte fałszywe cytaty) i **wrócą do przepisania później**. To jest wykonalne — chcę tylko, żeby było jasne, że tak będzie.

---

## 6. Co w tych rozdziałach jest dobre i czego nie ruszać

Żeby audyt nie brzmiał jak wyrok:

- **Scena Wielkiej Soboty** (23→24) — pusty kościół, otwarte tabernakulum, „świątynia otwarta jak dom, w którym umarł ktoś bliski". Bardzo dobra. Zostaje.
- **Scena dziecka przy poręczy basenu** (29→31) — model wiary jako zaufania, bez ani jednego słowa teologicznego. Zostaje.
- **Obrona Bubera przed sentymentalizmem** (28→29): akapit o tym, że świat „Ono" jest niezbędny i że filozofia spotkania robi się sentymentalna dokładnie wtedy, gdy temu przeczy. To jest dokładnie tryb wymagany przez dok. 04 § 3 (wzmacniać przeciwnika). Zostaje nawet przy przepisaniu.
- **Rygor gramatyczny jako metoda** w 29→31 („da się ją obronić gramatyką") — dobry pomysł konstrukcyjny, zgodny z linią Ratzingerowską (credere in Deum).

---

# AKTUALIZACJA 2026-09-08 — kroki 1–3 wykonane

## Status paragrafów audytu

| § audytu | Problem | Status |
|---|---|---|
| § 1 | Niezgodność numeracji z v3 | ✅ **ZAMKNIĘTE** — commit `db35cb3` |
| § 2 | Przypisy `[?]` / „brzmienia robocze" | 🟡 **CZĘŚCIOWO** — zob. niżej |
| § 3 | Fałszywa atrybucja DCE § 16 | ✅ **ZAMKNIĘTE** — commit `623a954` (poprawnie: GS 24) |
| § 4 | Fałszywa formuła „przejście z «ja» do «my»" | ✅ **ZAMKNIĘTE** — commit `1deb00c` |

## Co zweryfikowano u źródła (✔ = można cytować bez zastrzeżeń)

**Ratzinger — potwierdzone w wydaniu (`biblioteka/_tekst/`):**
- ✔ **„Śmierć to po prostu samotność"** — *Wprowadzenie w chrześcijaństwo*, s. 246–247. Rozdz. 24, przyp. 2. Dotąd oznaczone jako „formuła robocza" — **niepotrzebnie**, brzmienie jest dokładne.
  - Odkrycie uboczne: obraz **„bramy śmierci"** oraz zdanie „Wszelka trwoga na świecie jest ostatecznie tylko trwogą przed ową samotnością" są **u samego Ratzingera**, w tym samym akapicie. Metafora drzwi (rozdz. 26) ma więc pokrycie źródłowe.
- ✔ **Spe salvi § 32** — „Pierwszym istotnym miejscem uczenia się nadziei jest modlitwa…" — sprawdzone z tekstem na vatican.va, **zgodne co do słowa**, numer paragrafu poprawny. Rozdz. 26 bez zmian.

**Biblia Tysiąclecia — sprawdzone brzmienia:**

| Miejsce | Rozdz. | Wynik |
|---|---|---|
| J 1,14 | 34 | ✔ zgodne, bez zmian |
| Dz 2,42 | 31 | ✏️ poprawione do wyd. V („w modlitwach"; wyd. IV: „w modlitwie") |
| Ha 2,4 | 31 | ✏️ cudzysłów zdjęty — „sprawiedliwy żyje z wierności" **nie jest brzmieniem BT** |
| 1 Kor 15,43 | 27 | ✏️ „Siane w słabości…" to **Biblia Warszawska** → „sieje się słabe — powstaje mocne" |
| Łk 24,35 | 36 | ✏️ BT ma „**przy** łamaniu chleba", i to w **24,35**, nie 24,30–31 |
| 1 Kor 10,17 | 36 | ✔ zweryfikowane, brzmienie wpisane do przypisu |

## Zaległości — co jeszcze zostało

1. **§ 2 nie jest zamknięty.** Znaczniki `[?]` pozostają wszędzie tam, gdzie potrzeba **fizycznego egzemplarza**: numery stron wyd. polskiego (KKK, *Spe salvi*, *Duch liturgii*), Buber (przekł. Doktóra, PAX 1992), Marcel, Wojtyła, Pieper, Balthasar. To **nie jest wada do usunięcia zdalnie** — `[?]` jest tu uczciwą informacją, nie niedoróbką.
2. **Cytaty biblijne w rozdz. 24, 26, 27, 29 pozostają niesprawdzone co do słowa**: Rdz 3,9; J 13,1; Ef 4,9; Łk 23,46; Rz 8,38–39; J 20,17; Mk 16,6; Mt 27,46; Ps 22,2. W tekście funkcjonują jako **krótkie frazy**, więc ryzyko jest małe — ale przed drukiem wymagają przebiegu takiego jak powyżej.
3. **Rozdziały za długie** wobec celu 2,3–2,6 tys. słów: **24** (3543), **26** (3662), **31** (3470), **32** (3244). Fragmenty do zachowania przy skracaniu: scena Wielkiej Soboty (24), dziecko przy poręczy basenu (31), akapit broniący Bubera przed sentymentalizmem (29), „obrona gramatyką" (31).
4. **Kryteria z pkt. 3** (`04_PLAN_PISANIA…`) — limit 2 cytatów na rozdział i „ostatnie słowo przed puentą dla linii Ratzingerowskiej" — **nie były jeszcze audytowane** w rozdziałach odziedziczonych.

## Wniosek metodologiczny

Przypisy w rozdziałach 23–37 pisano bez dostępu do źródeł i **dwa z nich okazały się fałszywe** (DCE § 16; „przejście z «ja» do «my»"), a **dwa cytaty biblijne pochodziły z innego przekładu** niż deklarowany. Jednocześnie jeden cytat oznaczony jako niepewny („Śmierć to po prostu samotność") okazał się **dokładny**. Ostrożność działała więc w obie strony. Zasada na dalszą pracę pozostaje bez zmian: **cytat bez weryfikacji w wydaniu nie wchodzi do tekstu w cudzysłowie** — może być referowany własnymi słowami, co w kilku miejscach zastosowano.

---

# AKTUALIZACJA 2026-09-08 (2) — kwerenda KKK i Lumen gentium

Użytkownik udostępnił Katechizm online (katechizm.opoka.org.pl). Wykorzystane do domknięcia wszystkich `[?]` przy dokumentach kościelnych dostępnych cyfrowo.

## Zweryfikowane

| Miejsce | Rozdz. | Wynik |
|---|---|---|
| **KKK 632–637** | 24 | ✔ brzmienia 632, 633, 637 wpisane do przypisu; klauzula anty-apokatastatyczna ma pełne pokrycie w 633 |
| **KKK 1324–1327** | 36 | ✏️ **„źródło i szczyt" to skrót obiegowy** — wydanie polskie ma „**źródłem i zarazem szczytem całego życia chrześcijańskiego**" |
| **Lumen gentium 1** | 35 | ✏️ skrót roboczy gubił **„niejako"** (*veluti*) oraz **oś pionową** („wewnętrznego zjednoczenia z Bogiem") |

## Dlaczego dwie ostatnie korekty nie są kosmetyczne

**KKK 1324.** „Źródło i szczyt" to formuła, którą wszyscy znają i której nikt nie sprawdza — dlatego właśnie była w tekście. Wydanie ma pełniejsze brzmienie i to nie jest różnica stylistyczna: „całego życia chrześcijańskiego" określa **zakres**, którego skrót nie oddaje.

**Lumen gentium 1.** Skrót „sakrament, znak i narzędzie jedności" gubił dwie rzeczy, obie potrzebne rozdziałowi 35:
- **„niejako"** — zastrzeżenie soborowe chroniące przed utożsamieniem Kościoła z sakramentami i przed jego przebóstwieniem. Dla rozdziału, który broni Kościoła przed zarzutem instytucjonalizmu, jest to **argument, nie kłopot**;
- **dwa człony jedności** — „z Bogiem" (oś pionowa) i „całego rodzaju ludzkiego" (oś pozioma). Skrót zostawiał samą poziomą, czyli dokładnie tę wersję, którą zarzuca się Kościołowi jako socjologiczną.

## Odkrycie uboczne — KKK 635

*Katechizm* cytuje starożytną **homilię na Wielką Sobotę** (PG 43): „Wielka cisza spowiła ziemię; wielka na niej cisza i pustka. Cisza wielka, bo Król zasnął… Zbudź się, który śpisz! Nie po to bowiem cię stworzyłem, byś pozostawał spętany w Otchłani."

Tekst mówi dokładnie to, co scena otwierająca rozdz. 24 oddaje obrazem pustego kościoła. **Nie wprowadziłem go do tekstu** — rozdział ma już dwa cytaty Ratzingera i jeden blok, a jest najdłuższy w książce. Zapisany jako nota redakcyjna w przypisach rozdz. 24; **decyzja o użyciu należy do autora**.

## Co po tej kwerendzie zostaje z `[?]`

Wyłącznie pozycje wymagające **fizycznego egzemplarza**: numery stron wyd. polskich (Ratzinger — Znak; KKK; *Spe salvi*), Buber (przekł. Doktóra, PAX 1992), Marcel, Wojtyła, Pieper, Balthasar, *Duch liturgii*. Dokumenty dostępne online (KKK, LG, GS, DCE, *Spe salvi*, Biblia Tysiąclecia) są **sprawdzone w całości**.
