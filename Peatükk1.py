
import os
import json
import random
import runpy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(BASE_DIR, "saves")

os.makedirs(SAVE_DIR, exist_ok=True)

SAVE_FILE = None

SAVE_META = {"player_name": None, "slot": None}

def _puhasta_failinimi(s):
    s = s.strip()
    if not s:
        return "player"
    lubatud = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    out = []
    for ch in s:
        if ch in lubatud:
            out.append(ch)
        elif ch.isspace():
            out.append("_")
    res = "".join(out)
    return res if res else "player"

def _ehita_save_path(player_name, slot):
    nimi = _puhasta_failinimi(player_name)
    return os.path.join(SAVE_DIR, f"{nimi}_slot{slot}.json")

def _vali_slot():
    while True:
        slot = input("Vali save slot (1-3): ").strip()
        if slot in ("1", "2", "3"):
            return slot
        print("Vale slot. Vali 1, 2 või 3.")

def _leia_save_failid():
    save_failid = []
    for nimi in os.listdir(SAVE_DIR):
        if not nimi.endswith(".json"):
            continue
        path = os.path.join(SAVE_DIR, nimi)
        if not os.path.isfile(path):
            continue
        player_name = None
        slot = None
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            meta = data.get("meta", {})
            player_name = meta.get("player_name")
            slot = meta.get("slot")
        except (OSError, json.JSONDecodeError):
            pass

        if not player_name or not slot:
            failinimi = os.path.splitext(nimi)[0]
            if "_slot" in failinimi:
                player_name, slot = failinimi.rsplit("_slot", 1)
            else:
                player_name = failinimi
                slot = "?"

        save_failid.append({
            "path": path,
            "player_name": player_name,
            "slot": str(slot),
        })

    save_failid.sort(key=lambda x: (x["player_name"].lower(), x["slot"]))
    return save_failid

def _vali_olemasolev_save():
    global SAVE_FILE, SAVE_META

    save_failid = _leia_save_failid()
    if not save_failid:
        print("Ühtegi olemasolevat save faili ei leitud.")
        return None

    print("Olemasolevad save'id:")
    for i, save in enumerate(save_failid, start=1):
        print(f"{i} - {save['player_name']} (slot {save['slot']})")

    while True:
        valik = input("Vali save number: ").strip()
        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale sisend.")
            continue

        if 0 <= idx < len(save_failid):
            valitud = save_failid[idx]
            SAVE_FILE = valitud["path"]
            SAVE_META = {
                "player_name": valitud["player_name"],
                "slot": valitud["slot"],
            }
            return valitud["path"]

        print("Vale valik.")

def _vali_profiil(mode):
    global SAVE_FILE, SAVE_META

    if mode == "lae":
        return _vali_olemasolev_save()

    player_name = input("Sisesta mängija nimi: ").strip()
    slot = _vali_slot()
    path = _ehita_save_path(player_name, slot)

    if mode == "uus":
        if os.path.exists(path):
            print("See slot on juba kasutusel.")
            while True:
                v = input("Kas kirjutad üle (j/e): ").strip().lower()
                if v in ("j", "e"):
                    break
            if v == "e":
                print("Vali teine slot või teine nimi.")
                return _vali_profiil(mode)

    SAVE_FILE = path
    SAVE_META = {"player_name": player_name, "slot": slot}
    return path

MAX_LEVEL = 20

ELEMENDID = ["tuli", "vesi", "maa", "õhk"]

def xp_vajadus_leveliks(level):
    """Progressiivne XP: iga järgmine level vajab umbes 1.5x rohkem XP-d."""
    return int(100 * (1.5 ** (level - 1)))

def lisa_xp(stats, liik, kogus, aktiveeritud_altarid=None):
    """
    Lisa XP tegelase statsidele.
    liik: "fuusiline" või elemendi nimi ("tuli", "vesi", "maa", "õhk")
    Tagastab True kui toimus level up.
    """
    if liik == "fuusiline":
        if stats["fuusiline_level"] >= MAX_LEVEL:
            print("Füüsiline treening on juba maksimum tasemel!")
            return False
        stats["fuusiline_xp"] += kogus
        vajab = xp_vajadus_leveliks(stats["fuusiline_level"])
        if stats["fuusiline_xp"] >= vajab:
            stats["fuusiline_xp"] -= vajab
            stats["fuusiline_level"] += 1
            print(f"LEVEL UP! Füüsiline level: {stats['fuusiline_level']}")
            return True
        else:
            print(f"Füüsiline XP: {stats['fuusiline_xp']}/{vajab}")
            return False

    elif liik in ELEMENDID:
        if aktiveeritud_altarid and liik not in aktiveeritud_altarid:
            print(f"Sa ei saa veel {liik} elementi mediteerida – altar pole aktiveeritud!")
            return False
        if stats["elementaalne_level"][liik] >= MAX_LEVEL:
            print(f"{liik.capitalize()} meditatsioon on juba maksimum tasemel!")
            return False
        stats["elementaalne_xp"][liik] += kogus
        vajab = xp_vajadus_leveliks(stats["elementaalne_level"][liik])
        if stats["elementaalne_xp"][liik] >= vajab:
            stats["elementaalne_xp"][liik] -= vajab
            stats["elementaalne_level"][liik] += 1
            print(f"LEVEL UP! {liik.capitalize()} elementaalne level: {stats['elementaalne_level'][liik]}")
            return True
        else:
            print(f"{liik.capitalize()} XP: {stats['elementaalne_xp'][liik]}/{vajab}")
            return False
    else:
        print(f"Tundmatu XP liik: {liik}")
        return False

def kuva_stats(mangija):
    """Kuvab kõik mängija statsid."""
    clear()
    print_status_card(mangija, "STATISTIKA")
    info_line("Füüsiline level", f"{mangija['stats']['fuusiline_level']} (XP: {mangija['stats']['fuusiline_xp']}/{xp_vajadus_leveliks(mangija['stats']['fuusiline_level'])})", ANSI_CYAN)
    print()
    print(colorize("Elementaalsed levelid", ANSI_BLUE, bold=True))
    for el in ELEMENDID:
        lv = mangija['stats']['elementaalne_level'][el]
        xp = mangija['stats']['elementaalne_xp'][el]
        vajab = xp_vajadus_leveliks(lv)
        list_dash(f"{el.capitalize()}: level {lv} (XP: {xp}/{vajab})", ANSI_BLUE)

TEGELASE_VALIKUD = {
    "1": ("Sõdalane", 120, 12),
    "2": ("Maag", 100, 5),
    "3": ("Vibulaskja", 100, 6),
    "4": ("Knitwitt", 200, 2),
    "6": ("Must Kass", 10000, 7500),
}

NAHTAVAD_TEGELASED = ["1", "2", "3", "4"]

def loo_tühi_stats():
    return {
        "fuusiline_level": 1,
        "fuusiline_xp": 0,
        "elementaalne_level": {el: 1 for el in ELEMENDID},
        "elementaalne_xp": {el: 0 for el in ELEMENDID},
    }

def loo_special_flags():
    return {
        "house_deed_applied": False,
    }

def loo_lahingu_boonused():
    return {
        "jargmise_loo_jou_boost": 0,
    }

def loo_tegelane(nimi, elud, joukus):
    return {
        "nimi": nimi,
        "elud": elud,
        "joukus": joukus,
        "inventar": [],
        "kaart": None,
        "stats": loo_tühi_stats(),
        "special_flags": loo_special_flags(),
        "lahingu_boonused": loo_lahingu_boonused(),
    }

def loo_uus_mangija_valikust(valik):
    andmed = TEGELASE_VALIKUD.get(valik, ("Knitwitt", 200, 20))
    nimi, hp, jou = andmed
    return loo_tegelane(nimi, hp, jou)

def mangija_info(mangija):
    print(f"{mangija['nimi']} — Elud: {mangija['elud']}, Tugevus: {mangija['joukus']}")

def loo_kaart(pin):
    return {"pin": pin, "kuld": 0, "hobe": 0, "vask": 0}

def kaart_lisa_vask(kaart, kogus):
    kokku = kaart["kuld"] * 100 + kaart["hobe"] * 10 + kaart["vask"] + kogus
    kaart["kuld"] = kokku // 100
    kokku %= 100
    kaart["hobe"] = kokku // 10
    kaart["vask"] = kokku % 10

def kaart_eemalda_vask(kaart, kogus):
    kokku = kaart["kuld"] * 100 + kaart["hobe"] * 10 + kaart["vask"]
    if kogus > kokku:
        return False
    kokku -= kogus
    kaart["kuld"] = kokku // 100
    kokku %= 100
    kaart["hobe"] = kokku // 10
    kaart["vask"] = kokku % 10
    return True

def kaart_saldo_str(kaart):
    return f"{kaart['kuld']} kuldset, {kaart['hobe']} hõbedast, {kaart['vask']} vaskdablooni"

def loo_kaart_mangijale(mangija):
    while True:
        pin = input("Loo oma pangakaardi PIN (4 numbrit): ")
        if len(pin) == 4 and pin.isdigit():
            mangija["kaart"] = loo_kaart(pin)
            print("Pangakaart loodud!")
            print("Sinu algne saldo:", kaart_saldo_str(mangija["kaart"]))
            break
        else:
            print("PIN peab olema täpselt 4 numbrit. Proovi uuesti.")

def kontrolli_pin(mangija, katsed=3):
    if mangija["kaart"] is None:
        print("Sul pole pangakaarti!")
        return False
    for katse in range(1, katsed + 1):
        sisestus = input("Sisesta kaardi PIN: ")
        if sisestus == mangija["kaart"]["pin"]:
            print("PIN õige.")
            return True
        alles = katsed - katse
        print(f"Vale PIN! (alles {alles} katset)")
    print("\nLiiga palju valesid PIN-katseid!")
    print("Kaart blokeeritud ja raha kadus!")
    mangija["kaart"] = None
    loo_kaart_mangijale(mangija)
    return False

def alusta_mangu():
    global SAVE_FILE, SAVE_META

    print("=== VANA KOMPASSI SALADUS ===\n")
    print("1 - Uus mäng")
    print("2 - Jätka (lae save)")
    m0 = input("Vali (1/2): ").strip()

    leitud_artefaktid = []
    aktiveeritud_altarid = set()

    if m0 == "1":
        _vali_profiil("uus")
        print("\nVali tegelane:")
        for k in NAHTAVAD_TEGELASED:
            n, hp, jou = TEGELASE_VALIKUD[k]
            print(f"{k} - {n} (Elud: {hp}, Tugevus: {jou})")
        valik = input("Sisesta number: ").strip()
        if valik not in TEGELASE_VALIKUD:
            print("Vale valik.")
            return alusta_mangu()
        mangija = loo_uus_mangija_valikust(valik)
        print("\nSinu tegelane:")
        mangija_info(mangija)
        loo_kaart_mangijale(mangija)

    elif m0 == "2":
        if _vali_profiil("lae") is None:
            print("Save puudub, alustan uut mängu.")
            return alusta_mangu()
        mangija, leitud_artefaktid, aktiveeritud_altarid = lae_mang()
        if mangija is None:
            print("Laadimine ebaõnnestus, alustan uut mängu.")
            return alusta_mangu()
    else:
        print("Vale valik, alustan uuesti.")
        return alusta_mangu()

    return mangija, leitud_artefaktid, aktiveeritud_altarid

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nVajuta Enter...")

ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_DIM = "\033[2m"
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_BLUE = "\033[34m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

def _luba_ansi_windowsis():
    if os.name != "nt":
        return
    try:
        os.system("")
    except Exception:
        pass

_luba_ansi_windowsis()

def colorize(tekst, varv="", bold=False):
    algus = ""
    if bold:
        algus += ANSI_BOLD
    algus += varv
    if not algus:
        return tekst
    return f"{algus}{tekst}{ANSI_RESET}"

def section_title(pealkiri, varv=ANSI_CYAN):
    sisu = f" {pealkiri} "
    joon = "═" * max(8, len(sisu))
    print(colorize(f"╔{joon}╗", varv, bold=True))
    print(colorize(f"║{sisu.center(len(joon))}║", varv, bold=True))
    print(colorize(f"╚{joon}╝", varv, bold=True))

def separator(varv=ANSI_DIM):
    print(colorize("─" * 36, varv))

def scene_title(pealkiri, varv=ANSI_CYAN):
    section_title(pealkiri, varv)

def list_dash(tekst, varv=""):
    print(f"  {colorize('-', varv, bold=True)} {tekst}")

def info_line(silt, vaartus, varv=ANSI_CYAN):
    print(f"{colorize(silt + ':', ANSI_DIM)} {colorize(str(vaartus), varv)}")

def teade_saadud(silt, nimi):
    print(colorize(silt, ANSI_GREEN, bold=True))
    list_dash(nimi, ANSI_GREEN)

def teade_eemaldatud(silt, nimi):
    print(colorize(silt, ANSI_RED, bold=True))
    list_dash(nimi, ANSI_RED)

HAMSTRI_SEGADUS = [
    "hamster piilub kaardi tagant: see valik läks metsa",
    "hamster krõbistab närviliselt: proovi uuesti",
    "hamster vaatas seda valikut ja jäi segadusse",
    "hamster ütleb: hmm... mitte päris see",
]

def hamster_teade(sonum=None, varv=ANSI_YELLOW):
    print(colorize("  (\\__/)", varv))
    print(colorize("  ( •ㅅ•)", varv, bold=True))
    print(colorize("  / 　 づ", varv))
    print(colorize(f"  {sonum or random.choice(HAMSTRI_SEGADUS)}", varv))

def hp_bar(vaartus, maksimum, pikkus=18):
    maksimum = max(1, int(maksimum))
    vaartus = max(0, min(int(vaartus), maksimum))
    tais = int((vaartus / maksimum) * pikkus)
    return "█" * tais + "░" * (pikkus - tais)

def print_status_card(mangija, pealkiri=None):
    if pealkiri:
        section_title(pealkiri, ANSI_CYAN)
    nimi = SAVE_META.get("player_name") or mangija.get("nimi", "Mängija")
    klass = mangija.get("nimi", "?")
    elud = max(0, int(mangija.get("elud", 0)))
    joukus = int(mangija.get("joukus", 0))
    print(colorize(f"Nimi: {nimi}", ANSI_BOLD))
    print(colorize(f"Klass: {klass}", ANSI_MAGENTA))
    print(f"HP   : {colorize(hp_bar(elud, max(elud, 1)), ANSI_RED)} {elud}")
    print(f"Jõud : {colorize(str(joukus), ANSI_YELLOW, bold=True)}")
    if mangija.get("kaart"):
        print(f"Saldo: {colorize(kaart_saldo_str(mangija['kaart']), ANSI_YELLOW)}")
    if aktiivne_jou_boost(mangija):
        print(colorize(f"Järgmise löögi buff: +{aktiivne_jou_boost(mangija)}", ANSI_GREEN))
    separator()

FUUSILINE_KIRJELDUSED = {
    (1, 5): [
        "Teed mõned kükid ja kätekõverdused. Lihased hakkavad väsima.",
        "Jooksed aeglaselt mööda rada. Sul on raskusi hingamisel.",
        "Tõstad kive ja kannad neid. Selg on kange.",
    ],
    (6, 10): [
        "Lööd vastu puud, kuni peopesad põletavad puukoort. Vastupidavus kasvab.",
        "Harjutad mõõgatõmbeid õhus. Liigutused muutuvad sujuvamaks.",
        "Jooksed pikka ringi läbi metsa. Jalad peavad vastu.",
    ],
    (11, 15): [
        "Treenid koormatega kuni pimeduseni. Keha harjub valuga.",
        "Lööd rusikaga kivi – see praguneb. Jõud kasvab nähtavalt.",
        "Harjutad hüppeid üle kõrgete takistuste. Keha on kerge.",
    ],
    (16, 20): [
        "Sinu liigutused on nii kiired, et tuul su selja taga oigab.",
        "Treenid silmad kinni – keha teab ise, mida teha.",
        "Sa oled tipptasemel sõdalane. Iga treening täiustab sind veelgi.",
    ],
}

ELEMENTAALNE_KIRJELDUSED = {
    "tuli": {
        (1, 5): [
            "Istud lahtise leegi kõrval ja tunned soojust peopesades.",
            "Kujutad ette tuld – sõrmed soojenevad veidi.",
        ],
        (6, 10): [
            "Leek vastab sinu mõtetele, kõigub sinu poole.",
            "Suudad lühikest aega hoida väikest tulekera peopesas.",
        ],
        (11, 15): [
            "Tuli tunneb su käske. Leegid tõusevad su soovil.",
            "Meditatsioon kütab su ümber õhku – talv ei puuduta sind.",
        ],
        (16, 20): [
            "Sa oled tulelaps. Leegid tantsivad sinu ümber omal tahtel.",
            "Tuli ei põleta sind – see on sinu pikendus.",
        ],
    },
    "vesi": {
        (1, 5): [
            "Istud järve ääres ja kuulad lainete rütmi.",
            "Tunned veevoogu peopesade vahel, kui käed vette uputad.",
        ],
        (6, 10): [
            "Vesi reageerib su puudutusele – kerkib kergelt üles.",
            "Suudad veepiisas panna keerles ilma seda puudutamata.",
        ],
        (11, 15): [
            "Mõistuse jõul suunad ojake läbi eri radade.",
            "Vihm peatub su kohal – sa saad seda juhtida.",
        ],
        (16, 20): [
            "Sa oled voolav. Vesi kuulab sind nagu vana sõpra.",
            "Järved rahunevad su läheduses. Tormid hajuvad su pilgul.",
        ],
    },
    "maa": {
        (1, 5): [
            "Istud kividel ja tunned nende jaheda raskuse all.",
            "Surus sõrmed mulda ja tunned kivide kaalu sügaval.",
        ],
        (6, 10): [
            "Väike kivi liigub su käe järgi – aeglaselt, aga kindlalt.",
            "Tunned maavärinate kaugeid kajasid läbi tallad.",
        ],
        (11, 15): [
            "Käsud kivi – see tõuseb. Käsud mullal – see avaneb.",
            "Mäed mäletavad sind. Kaljud ei lagune su all.",
        ],
        (16, 20): [
            "Maapind vastab su sammudele. Sa oled selle osa.",
            "Kivi on sinu tahe tahkeks muutunud.",
        ],
    },
    "õhk": {
        (1, 5): [
            "Kuulad tuult ja proovid tajuda selle suunda.",
            "Hingad sügavalt – õhk täidab su nagu purjed.",
        ],
        (6, 10): [
            "Tuul pöördub su poole enne teiste poole.",
            "Suudad saata väikese õhupuhanguse soovitud suunas.",
        ],
        (11, 15): [
            "Hõljud hetkeks maast lahti – õhk kannab sind.",
            "Torm rahuneb su sõna peale.",
        ],
        (16, 20): [
            "Sa liigud nagu tuul – nähtamatu, kuni juba möödunud.",
            "Õhk on sinu hingus ja relv korraga.",
        ],
    },
}

def _vali_kirjeldus(kirjeldused_dict, level):
    for (min_lv, max_lv), tekstid in kirjeldused_dict.items():
        if min_lv <= level <= max_lv:
            import random
            return random.choice(tekstid)
    import random
    return random.choice(list(kirjeldused_dict.values())[-1])

def fuusiline_levelup_efekt(mangija, uus_level):
    """Annab boonuse füüsilise level up'i korral."""
    joukus_boonus = 5
    elud_boonus = 10
    mangija["joukus"] += joukus_boonus
    mangija["elud"] += elud_boonus
    print(f"  → Tugevus +{joukus_boonus} (kokku: {mangija['joukus']})")
    print(f"  → Elud +{elud_boonus} (kokku: {mangija['elud']})")

    if uus_level == 5:
        print("  → Uus valik lahingus: Raske löök saadaval!")
    elif uus_level == 10:
        print("  → Uus valik lahingus: Maru rünnak saadaval!")
    elif uus_level == 15:
        print("  → Uus valik lahingus: Purunemine saadaval!")
    elif uus_level == 20:
        print("  → Oled saavutanud füüsilise meisterlikkuse!")

def elementaalne_levelup_efekt(mangija, element, uus_level):
    """Annab boonuse elementaalse level up'i korral."""
    print(f"  → {element.capitalize()} meditatsioon süveneb.")

    if uus_level == 5:
        print(f"  → Altari juures saad nüüd lisavihje {element} mõistatusele!")
    elif uus_level == 10:
        print(f"  → {element.capitalize()} elemendi mõistatus on sulle nüüd lihtsam.")
    elif uus_level == 15:
        print(f"  → Tunned {element} altari energiat kaugelt.")
    elif uus_level == 20:
        print(f"  → Oled {element} elemendi meister!")

FUUSILINE_XP = 15

ELEMENTAALNE_XP = 12

def treeni(mangija, aktiveeritud_altarid):
    while True:
        clear()
        stats = mangija["stats"]
        print_status_card(mangija, "TREENIMINE")
        info_line("Füüsiline level", f"{stats['fuusiline_level']} (XP: {stats['fuusiline_xp']}/{xp_vajadus_leveliks(stats['fuusiline_level'])})", ANSI_CYAN)
        print()
        print("1 - Füüsiline treening")
        print(colorize("--- Elementaalne meditatsioon ---", ANSI_BLUE, bold=True))
        for i, el in enumerate(ELEMENDID, start=2):
            lv = stats["elementaalne_level"][el]
            xp = stats["elementaalne_xp"][el]
            vajab = xp_vajadus_leveliks(lv)
            saadav = colorize("✓", ANSI_GREEN, bold=True) if el in aktiveeritud_altarid else colorize("✗ (altar aktiveerimata)", ANSI_RED)
            print(f"{i} - {el.capitalize()} meditatsioon  [{saadav}]  Level {lv} ({xp}/{vajab} XP)")
        print("6 - Tagasi")

        valik = input("\nVali: ").strip()

        if valik == "1":
            lv = stats["fuusiline_level"]
            kirjeldus = _vali_kirjeldus(FUUSILINE_KIRJELDUSED, lv)
            print(f"\n{kirjeldus}")
            oli_level = lv
            oli_xp = lisa_xp(stats, "fuusiline", FUUSILINE_XP)
            if oli_xp and stats["fuusiline_level"] > oli_level:
                fuusiline_levelup_efekt(mangija, stats["fuusiline_level"])
            pause()

        elif valik in ("2", "3", "4", "5"):
            el = ELEMENDID[int(valik) - 2]
            if el not in aktiveeritud_altarid:
                print(f"\n{el.capitalize()} altar pole veel aktiveeritud.")
                print("Aktiveeri altar enne, kui saad seda elementi mediteerida.")
                pause()
                continue
            lv = stats["elementaalne_level"][el]
            kirjeldus = _vali_kirjeldus(ELEMENTAALNE_KIRJELDUSED[el], lv)
            print(f"\n{kirjeldus}")
            oli_level = lv
            tuli_levelup = lisa_xp(stats, el, ELEMENTAALNE_XP, aktiveeritud_altarid)
            if tuli_levelup and stats["elementaalne_level"][el] > oli_level:
                elementaalne_levelup_efekt(mangija, el, stats["elementaalne_level"][el])
            pause()

        elif valik == "6":
            return mangija

        else:
            print("Vigane valik.")
            pause()

def kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print_status_card(mangija, "INVENTAR")
    if mangija["inventar"]:
        print(colorize("Seljakott", ANSI_YELLOW, bold=True))
        loendur = {}
        for ese in mangija["inventar"]:
            loendur[ese["nimi"]] = loendur.get(ese["nimi"], 0) + 1
        for nimi, kogus in loendur.items():
            list_dash(f"{nimi} x{kogus}", ANSI_YELLOW)
    else:
        print("  Inventar on tühi.")

    separator()
    print(colorize("Leitud artefaktid", ANSI_MAGENTA, bold=True))
    if leitud_artefaktid:
        for a in leitud_artefaktid:
            list_dash(a, ANSI_MAGENTA)
    else:
        print("  Ühtegi artefakti pole leitud.")

    separator()
    print(colorize("Aktiveeritud altarid", ANSI_BLUE, bold=True))
    if aktiveeritud_altarid:
        for altar in aktiveeritud_altarid:
            list_dash(altar.capitalize(), ANSI_BLUE)
    else:
        print("  Ühtegi altarit pole aktiveeritud.")

    if mangija["kaart"]:
        separator()
        print(colorize("Pangakaart", ANSI_GREEN, bold=True))
        print(f"  Saldo: {colorize(kaart_saldo_str(mangija['kaart']), ANSI_YELLOW)}")

    pause()

def has_item(leitud_artefaktid, nimi):
    return nimi in leitud_artefaktid

def add_item(leitud_artefaktid, nimi):
    if nimi not in leitud_artefaktid:
        leitud_artefaktid.append(nimi)
        teade_saadud("Leidsid artefakti:", nimi)

def has_inventar(mangija, nimi):
    return any(e["nimi"] == nimi for e in mangija["inventar"])

def add_inventar(mangija, nimi):
    if not has_inventar(mangija, nimi):
        mangija["inventar"].append({"nimi": nimi})
        teade_saadud("Lisati inventari:", nimi)

VARJU_KIRJELDUSED_MADAL = [
    (
        "Miski liigub su silmanurgas.\n"
        "Pöördud – seal pole midagi.\n"
        "Kuid tunne jääb. Keegi jälgib.\n"
        "Hakkad jooksma – jalad ei kuula.\n"
        "Siis kõik läheb mustaks."
    ),
    (
        "Kuuled {player_name} – aga kedagi pole lähedal.\n"
        "Vari sirutab käe su poole.\n"
        "Sa lööd. Käsi läbib õhku.\n"
        "Kukud põlvili. Maailm pöörleb.\n"
        "Kui silmad avad, on kõik vaikne."
    ),
]

VARJU_KIRJELDUSED_KÕRGE = [
    (
        "Vari tuleb taas – aga nüüd tunned seda ette.\n"
        "Seisad rahulikult, hingad sügavalt.\n"
        "See tuleb su poole... ja peatub.\n"
        "Hetke pärast hajub see nagu suits.\n"
        "Sa pole kindel, kas see oli päris."
    ),
    (
        "Varjud on tuttavad nüüd.\n"
        "Nad ei hirmuta sind enam nii.\n"
        "Sa vaatad neile otsa, kuni nad taanduvad.\n"
        "Kuid küsimus jääb: mis nad tegelikult on?"
    ),
]

def fight_shadow(mangija):
    lv = mangija["stats"]["fuusiline_level"]
    if lv >= 10:
        kirjeldus = random.choice(VARJU_KIRJELDUSED_KÕRGE)
    else:
        kirjeldus = random.choice(VARJU_KIRJELDUSED_MADAL)
    player_name = SAVE_META.get("player_name") or mangija["nimi"]
    kirjeldus = kirjeldus.format(player_name=player_name)
    print()
    for rida in kirjeldus.split("\n"):
        print(f"  {rida}")
        input()
    print()

def pohja_vasak_rada(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== PÕHI – VASAK RADA ===\n")

    if has_item(leitud_artefaktid, "Veider kompass"):
        print("Kõnnid mööda tuttavat rada.")
        print("Kivine postament seisab seal nagu alati – vaikne ja ootav.")
        pause()
        return

    if "tuli" in aktiveeritud_altarid:
        print("Postament on tühi. Kompass on juba täitnud oma rolli.")
        pause()
        return

    print("Teed keerduvad tiheda puude vahel.")
    input("  (edasi...)\n")
    print("Leiad vana kivise postamendi.")
    print("Selle peal lamab kummaline ese –")
    input("  (edasi...)\n")
    add_item(leitud_artefaktid, "Veider kompass")
    print("\nKompass on külm ja raske. Nõel tiirleb ilma otsata.")
    pause()

def pohja_parem_rada(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== PÕHI – PAREM RADA ===\n")

    print("Luud ja vanad puud ümbritsevad sind.")
    print("Õhk on raske ja niiske.")
    input("  (edasi...)\n")

    fight_shadow(mangija)

    print("Ärkad. Oled maha kukkunud.")
    print("Käed on värisevad.")
    input("  (edasi...)\n")

    if has_inventar(mangija, "Maagiline lamp"):
        print("Lamp on juba su käes – see särab nõrgalt taskust.")
    else:
        print("Märkad midagi läikivat enda kõrval maas.")
        print("Keegi on selle siin maha jätnud – või mõni osa sinust tõi selle siia.")
        add_inventar(mangija, "Maagiline lamp")
        print("\nLamp on jahe puudutusele, kuid miski sees selles pulbitseb.")

    pause()

def Pohhi(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        scene_title("PÕHI", ANSI_CYAN)
        lv = mangija["stats"]["fuusiline_level"]
        if lv >= 6:
            print("Tunned end siin kindlamalt. Mets ei tundu enam nii ähvardav.\n")
        print("1 - Uuri vasakut rada")
        print("2 - Uuri paremat rada")
        print("3 - Kasuta kompassi siin")
        print("4 - Treeni")
        print("5 - Inventar")
        print("6 - Tagasi kaardile")

        valik = input("\nVali: ").strip()

        if valik == "1":
            pohja_vasak_rada(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2":
            pohja_parem_rada(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "3":
            kasuta_kompassi_asukohas("põhi", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "4":
            treeni(mangija, aktiveeritud_altarid)
        elif valik == "5":
            kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "6":
            return mangija
        else:
            hamster_teade()
            pause()

def louna_jarv(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== LÕUNA – JÄRV ===\n")

    el_lv = mangija["stats"]["elementaalne_level"]["vesi"]

    print("Jõuad järve äärde.")
    print("Vesi on ebaloomulikult vaikne – ükski laine, ükski tuul.")
    input("  (edasi...)\n")

    if el_lv >= 5:
        print("Su vee-elementaalne tunnetus ärkab.")
        print("Järv on sama mis idas – sa näed seda teiselt poolt.")
        print("Kaks randa, üks vesi. Idakalda varjud on näha udus.")
    else:
        print("Järv peegeldab taevast täiuslikult.")
        print("Tunne, et see ulatub kaugele – võib-olla idasse.")
        print("Aga sa pole kindel.")

    input("  (edasi...)\n")
    print("Vaikuse all on midagi. Sa ei tea mis.")
    pause()

def louna_maja(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== LÕUNA – VANA MAJA ===\n")

    print("Lähened vanale majale.")
    print("Uks on kinni. Aknad on mustad.")
    input("  (edasi...)\n")

    if has_inventar(mangija, "Kadunud Riikide Foliant"):
        print("Oled siin juba käinud.")
        print("Raamat on su käes – maja on jälle vaikne.")
        pause()
        return

    if not has_inventar(mangija, "Maagiline lamp"):
        print("Miski jälgib sind seestpoolt.")
        print("Uks ei avane. Pimedad aknad ei näita midagi.")
        print("\nVihje: Sul on vaja midagi, mis valgustaks teed.")
        pause()
        return

    print("Võtad lambi välja.")
    print("See süttib iseenesest – leek on sinakasvalge.")
    input("  (edasi...)\n")
    print("Uks avaneb.")
    input("  (edasi...)\n")
    print("Sees on tolm ja vaikus.")
    print("Riiulitel on tühjad kohad – keegi on juba viinud kõik.")
    print("Peaaegu kõik.")
    input("  (edasi...)\n")
    print("Nurgas, laua all, on raske raamat.")
    print("Kaas on kulunud ja kiri peal on arusaamatu.")
    input("  (edasi...)\n")
    add_inventar(mangija, "Kadunud Riikide Foliant")
    print("\nRaamat on raske ja hingab omamoodi soojust.")
    print("Sa ei suuda kaant lugeda – aga tead, et see on tähtis.")
    pause()

def Louna(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        scene_title("LÕUNA", ANSI_BLUE)
        el_lv = mangija["stats"]["elementaalne_level"]["vesi"]
        if el_lv >= 8:
            print("Vesi siin vastab su hingamisele. Tunned end kodus.\n")
        maja_nahtav = has_inventar(mangija, "Maagiline lamp")
        print("1 - Mine järve äärde")
        if maja_nahtav:
            print("2 - Mine vana maja juurde")
        else:
            print("2 - ? ? ?")
        print("3 - Kasuta kompassi siin")
        print("4 - Treeni")
        print("5 - Inventar")
        print("6 - Tagasi kaardile")

        valik = input("\nVali: ").strip()

        if valik == "1":
            louna_jarv(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2":
            if maja_nahtav:
                louna_maja(mangija, leitud_artefaktid, aktiveeritud_altarid)
            else:
                print("Udu taga on justkui midagi, aga sa ei näe teed selleni.")
                print("Vihje: valgus võib paljastada selle, mis seni peidus oli.")
                pause()
        elif valik == "3":
            kasuta_kompassi_asukohas("lõuna", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "4":
            treeni(mangija, aktiveeritud_altarid)
        elif valik == "5":
            kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "6":
            return mangija
        else:
            hamster_teade()
            pause()

def ida_rand(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== IDA – RAND ===\n")

    print("Jõuad randa.")
    print("Järv on siin sama vaikne kui lõunas – teine kallas.")
    input("  (edasi...)\n")

    lv = mangija["stats"]["fuusiline_level"]
    if lv >= 8:
        print("Seisad kindlalt. Vaatad vett.")
        print("Lõunakalda maja siluett on näha udus.")
    else:
        print("Lained ei liigu. Vesi on nagu peegel.")
        print("Kaugel lõunas on midagi – maja? Vari?")

    input("  (edasi...)\n")
    fight_shadow(mangija)
    print("Rand on tühi. Sa oled üksi.")
    pause()

def Ida(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        scene_title("IDA", ANSI_YELLOW)
        el_lv = mangija["stats"]["elementaalne_level"]["maa"]
        if el_lv >= 6:
            print("Kaldakivid tunnevad su jalgu. Maa mäletab sind.\n")
        print("1 - Mine randa")
        print("2 - Mine paatide juurde")
        print("3 - Kasuta kompassi siin")
        print("4 - Treeni")
        print("5 - Inventar")
        print("6 - Tagasi kaardile")

        valik = input("\nVali: ").strip()

        if valik == "1":
            ida_rand(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2":
            uus_mangija = ida_paadid(mangija, leitud_artefaktid, aktiveeritud_altarid)
            if uus_mangija is not None:
                mangija = uus_mangija
        elif valik == "3":
            kasuta_kompassi_asukohas("ida", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "4":
            treeni(mangija, aktiveeritud_altarid)
        elif valik == "5":
            kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "6":
            return mangija
        else:
            hamster_teade()
            pause()

def laas_ruiinid(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== LÄÄS – RUIINID ===\n")

    el_lv_maa = mangija["stats"]["elementaalne_level"]["maa"]
    el_lv_tuli = mangija["stats"]["elementaalne_level"]["tuli"]

    print("Uurid lagunenud kive.")
    print("Iidsed sümbolid on kulunud aja hammasrataste all.")
    input("  (edasi...)\n")

    if not has_inventar(mangija, "Kadunud Riikide Foliant"):
        print("Kivid jäävad su ees suletuks.")
        print("Sümbolid on olemas, aga sa ei mõista neid.")
        print("\nVihje: enne pead leidma Kadunud Riikide Foliandi lõuna majast.")
        pause()
        return

    print("Foliant soojeneb su käes.")
    print("Nüüd suudad ruunidest aru saada.")
    input("  (edasi...)\n")

    if not WORLD_STATE["laane_altariruum_avatud"]:
        print("Üks kivisein nihkub aeglaselt paigast.")
        print("Sümbolite taha oli peidetud käik altarite ruumi.")
        WORLD_STATE["laane_altariruum_avatud"] = True
        input("  (edasi...)\n")

    if el_lv_maa >= 5:
        print("Su maa-elementaalne tunnetus ärkab.")
        print("Kivid räägivad: 'Neli elementi, neli altarit, neli võtit.'")
        input("  (edasi...)\n")

    if el_lv_tuli >= 5:
        print("Tule energia pulseerib ühes kivisümbolis.")
        print("See on sama märk mis tule altaril.")
        input("  (edasi...)\n")

    if len(aktiveeritud_altarid) == 4:
        if has_item(leitud_artefaktid, "Iidne Tee"):
            print("Iidne Tee on juba su käes. Ruiinid on vaiksed.")
        else:
            print("Kõik neli elementi on äratatud.")
            input("  (edasi...)\n")
            print("Ruiinide keskel avaneb kivi.")
            print("Seest tõuseb kaart, aga mitte paber.")
            print("See on valgusest ja varjust, elav.")
            input("  (edasi...)\n")
            add_item(leitud_artefaktid, "Iidne Tee")
            print("\nIidne Tee vibreerib su käes.")
            print("Sa tead nüüd kuhu minna.")
    else:
        puudu = 4 - len(aktiveeritud_altarid)
        print(f"Ruiinid on veel vaiksed. {puudu} elementi ootab äratamist.")
        if el_lv_maa >= 3:
            print("\nKivide kiri ütleb: 'Vii elemendid altarile, siis avaneb tee.'")

    pause()

def laas_pood(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== LÄÄS – POOD ===\n")

    print("Pood on tühi.")
    print("Riiulitel on kummaline tolm – nagu keegi on alles lahkunud.")
    input("  (edasi...)\n")

    if has_inventar(mangija, "Unustatud päevik"):
        print("Päevik on su käes – tolmused lehed nagu alati.")
        print("\nAvad selle uuesti...")
        input("  (edasi...)\n")
        _loe_paevik(mangija, leitud_artefaktid)
        pause()
        return

    print("Nurgas, riiuli all, on midagi.")
    print("Tolm on paks, aga midagi paistab alt välja.")
    input("  (edasi...)\n")
    add_inventar(mangija, "Unustatud päevik")
    print("\nPäevik on vana ja pleekinud.")
    print("Avad esimese lehe...")
    input("  (edasi...)\n")
    _loe_paevik(mangija, leitud_artefaktid)
    pause()

def _loe_paevik(mangija, leitud_artefaktid):
    el_sum = sum(mangija["stats"]["elementaalne_level"][el] for el in ELEMENDID)
    foliant = has_inventar(mangija, "Kadunud Riikide Foliant")

    print("─" * 40)

    if not foliant:
        print("Leheküljed on täis kirja – aga kiri on võõras.")
        print("Sa ei suuda lugeda ühtegi sõna.")
        print("\n[Foliant aitaks sul seda lugeda]")
    else:
        print("Foliant aitab sul kirja mõtestada.")
        input("  (edasi...)\n")

        if el_sum < 12:
            print("'Kes seda loeb – pöördu tagasi.'")
            print("'Neli altarit ootavad. Ära mine saarele enne kui kõik on äratatud.'")
            print("'Kompass näitab teed – aga ainult neile, kes küsivad.'")
        elif el_sum < 24:
            print("'Ma leidsin saare. Rüütel seisis koopa ees.'")
            print("'Ta ei lasknud mind läbi – kuid ta ei ründanud ka.'")
            print("'Võib-olla ta ootab kedagi. Mitte mind.'")
        else:
            print("'Koopa sügavuses on midagi, mis ei peaks olema päris.'")
            print("'Aga mina olin juba liiga kaugel – ja liiga nõrk.'")
            print("'Palun – kes iganes sa oled – ole tugevam kui mina olin.'")

    print("─" * 40)

def Laas(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        scene_title("LÄÄS", ANSI_MAGENTA)
        el_lv = mangija["stats"]["elementaalne_level"]["õhk"]
        if el_lv >= 6:
            print("Tuul siin kuulab sind. Pilved liiguvad su soovil.\n")
        print("1 - Uuri ruiine")
        print("2 - Mine sügavatesse ruiinidesse")
        print("3 - Mine poodi")
        print("4 - Kasuta kompassi siin")
        if WORLD_STATE["laane_altariruum_avatud"]:
            print("5 - Mine altarite ruumi")
        else:
            print("5 - ? ? ?")
        print("6 - Treeni")
        print("7 - Inventar")
        print("8 - Tagasi kaardile")

        valik = input("\nVali: ").strip()

        if valik == "1":
            laas_ruiinid(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2":
            laas_sygavad_ruiinid(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "3":
            laas_pood(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "4":
            kasuta_kompassi_asukohas("lääs", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "5":
            if not WORLD_STATE["laane_altariruum_avatud"]:
                print("Sa ei leia veel teed sinna.")
                print("Vihje: foliant võib aidata sul ruiinide sümboleid mõista.")
                pause()
            else:
                altarite_ruum(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "6":
            treeni(mangija, aktiveeritud_altarid)
        elif valik == "7":
            kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "8":
            return mangija
        else:
            hamster_teade()
            pause()

KOMPASSI_JARGUD = [
    {
        "vana_kompass": "Veider kompass",
        "uus_kompass": "Leekiv kompass",
        "amulet": "Tule amulet",
        "altar": "tuli",
        "vastus": "tuli",
        "vihje": "Kompass kuumeneb ja osutab põlenud kivivälja poole.",
        "asukoht": "põhi",
        "mõistatus": "Ma söön kõike, mida puudutan. Kui mulle vett annad, siis suren. Mis ma olen?",
        "lisavihje_level": 5,
        "lisavihje_tekst": "Su tule-meditatsioon sosistab: 'See, mis hävitab, on ka see, mis soojendab.'"
    },
    {
        "vana_kompass": "Leekiv kompass",
        "uus_kompass": "Udukompass",
        "amulet": "Vee amulet",
        "altar": "vesi",
        "vastus": "vesi",
        "vihje": "Kompass kattub niiskusega ja osutab vaikse järve poole.",
        "asukoht": "lõuna",
        "mõistatus": "Mul pole jalgu, aga jooksen. Mul pole suud, aga neelan. Mis ma olen?",
        "lisavihje_level": 5,
        "lisavihje_tekst": "Su vee-meditatsioon sosistab: 'See, mis voolab, ei peatu kunagi.'"
    },
    {
        "vana_kompass": "Udukompass",
        "uus_kompass": "Kivisüda kompass",
        "amulet": "Maa amulet",
        "altar": "maa",
        "vastus": "maa",
        "vihje": "Kompass muutub raskeks ja tõmbab sind kivise koopa poole.",
        "asukoht": "ida",
        "mõistatus": "Ma olen vaikne, raske ja kannan metsi ning mägesid. Mis ma olen?",
        "lisavihje_level": 5,
        "lisavihje_tekst": "Su maa-meditatsioon sosistab: 'See, mis kannab kõike, on ise liikumatu.'"
    },
    {
        "vana_kompass": "Kivisüda kompass",
        "uus_kompass": "Tormikompass",
        "amulet": "Õhu amulet",
        "altar": "õhk",
        "vastus": "õhk",
        "vihje": "Kompass väriseb ja osutab kaljuservale, kus tuul ulgub.",
        "asukoht": "lääs",
        "mõistatus": "Mind ei näe, aga mind tuntakse. Ma liigun kõikjal. Mis ma olen?",
        "lisavihje_level": 5,
        "lisavihje_tekst": "Su õhu-meditatsioon sosistab: 'See, mida ei näe, on tihtipeale kõige olulisem.'"
    },
]

def leia_aktiivne_kompass(leitud_artefaktid):
    for jark in KOMPASSI_JARGUD:
        if has_item(leitud_artefaktid, jark["vana_kompass"]):
            return jark
    return None

def leia_jark_altari_jargi(altar):
    for jark in KOMPASSI_JARGUD:
        if jark["altar"] == altar:
            return jark
    return None

def kasuta_kompassi_asukohas(asukoht, mangija, leitud_artefaktid, aktiveeritud_altarid):
    jark = leia_aktiivne_kompass(leitud_artefaktid)

    if not jark:
        print("\nSul pole aktiivset kompassi.")
        pause()
        return

    if jark["asukoht"] != asukoht:
        print(f"\nKompass väriseb nõrgalt, aga siin ta sind edasi ei juhi.")
        print(f"Vihje: {jark['vihje']}")
        pause()
        return

    print(f"\nKompass reageerib!")
    print(f"{jark['vihje']}")
    input("  (edasi...)\n")
    print("Jõuad peidetud paika.")
    print("Seal ootab sind mõistatus.\n")
    print(f"  \"{jark['mõistatus']}\"\n")

    el = jark["altar"]
    el_lv = mangija["stats"]["elementaalne_level"][el]
    if el_lv >= jark["lisavihje_level"]:
        print(f"[{jark['lisavihje_tekst']}]\n")

    vastus = input("Sisesta vastus: ").strip().lower()

    if vastus == jark["vastus"]:
        if not has_item(leitud_artefaktid, jark["amulet"]):
            print("\nÕige vastus!")
            add_item(leitud_artefaktid, jark["amulet"])
        else:
            print("\nSa oled selle amuleti juba leidnud.")
    else:
        print("\nVale vastus. Saladus jääb suletuks.")

    pause()

def aktiveeri_altar(altar, mangija, leitud_artefaktid, aktiveeritud_altarid):

    jark = leia_jark_altari_jargi(altar)

    if not jark:
        print("See altar ei reageeri.")
        pause()
        return

    if altar in aktiveeritud_altarid:
        print("See altar on juba aktiveeritud.")
        pause()
        return

    amulett = jark["amulet"]
    vana_kompass = jark["vana_kompass"]
    uus_kompass = jark["uus_kompass"]

    if not has_item(leitud_artefaktid, amulett):
        print(f"Sul pole veel eset: {amulett}")
        print(f"Vihje: {jark['vihje']}")
        pause()
        return

    print(f"\nAsetad {amulett} altarile...")
    input("  (edasi...)\n")
    leitud_artefaktid.remove(amulett)
    teade_eemaldatud("Kasutasid / eemaldasid artefakti:", amulett)
    aktiveeritud_altarid.add(altar)

    if has_item(leitud_artefaktid, vana_kompass):
        print(f"{vana_kompass} hakkab pragunema...")
        leitud_artefaktid.remove(vana_kompass)
        teade_eemaldatud("Eemaldati artefakt:", vana_kompass)
        input("  (edasi...)\n")

    if uus_kompass:
        print("Altari keskosa avaneb.")
        print(f"Sealt tõuseb uus kompass: {colorize(uus_kompass, ANSI_GREEN, bold=True)}")
        add_item(leitud_artefaktid, uus_kompass)
    else:
        print("Altari jõud vaibub. Rohkem kompasse ei ilmu.")

    print(f"\nAktiveerisid {altar} altari – elementaalne energia voolab sinusse.")
    lisa_xp(mangija["stats"], altar, 30, aktiveeritud_altarid)

    pause()

def altarite_ruum(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        print("=== ALTARITE RUUM ===\n")

        altarid = ["tuli", "vesi", "maa", "õhk"]
        for i, altar in enumerate(altarid, start=1):
            staatus = "✓ aktiveeritud" if altar in aktiveeritud_altarid else "○ ootab"
            print(f"{i} - {altar.capitalize()} altar  [{staatus}]")

        print("5 - Vaata inventari")
        print("6 - Mine tagasi")

        valik = input("\nVali: ").strip()

        if valik == "1":
            aktiveeri_altar("tuli", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2":
            aktiveeri_altar("vesi", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "3":
            aktiveeri_altar("maa", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "4":
            aktiveeri_altar("õhk", mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "5":
            kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "6":
            return
        else:
            print("Vigane valik.")
            pause()

VAENLASED = [
    {"nimi": "Ork",      "elud": 200,  "joukus": 12},
    {"nimi": "Luukere",  "elud": 400,  "joukus": 5},
    {"nimi": "Draakon",  "elud": 2000, "joukus": 60},
    {"nimi": "Zombi",    "elud": 200,  "joukus": 8},
    {"nimi": "Hiid",     "elud": 500,  "joukus": 15},
    {"nimi": "Goblin",   "elud": 300,  "joukus": 10},
    {"nimi": "Maha",     "elud": 10,   "joukus": 50},
    {"nimi": "Cerberus", "elud": 1000, "joukus": 40},
]

BOSS_VAENLASED = [
    {"nimi": "Kuri Maha", "elud": 5000, "joukus": 100},
    {"nimi": "Jae Chan",  "elud": 9999, "joukus": 999},
    {"nimi": "Urr",       "elud": 3000, "joukus": 80},
]

DABLOON_VASK_VAARTUS = {
    "Kuldne Dabloon":   100,
    "Hõbedane Dabloon": 10,
    "Vask Dabloon":     1,
}

VAENLASE_DROPID = {
    "Ork":      [("Kont", 0.30), ("Mädanenud Liha", 0.40), ("Vask Dabloon", 0.05), ("Orgi Mäss", 0.10)],
    "Luukere":  [("Luukere Tuum", 0.05), ("Kont", 0.20), ("Hõbedane Dabloon", 0.05)],
    "Draakon":  [("Draakoni Soomus", 0.01), ("Kuldne Dabloon", 0.10), ("Hõbedane Dabloon", 0.20), ("Vask Dabloon", 0.30)],
    "Zombi":    [("Mädanenud Liha", 0.60), ("Zombi Sõrm", 0.30), ("Vask Dabloon", 0.40)],
    "Hiid":     [("Hiiglase Silm", 0.20), ("Vask Dabloon", 0.15), ("Hõbedane Dabloon", 0.10)],
    "Goblin":   [("Goblini Kihv", 0.40), ("Vask Dabloon", 0.20)],
    "Maha":     [("Maha Unibrow", 0.30), ("Hõbedane Dabloon", 0.10)],
    "Cerberus": [("Cerberuse Karv", 0.60), ("Kuldne Dabloon", 0.15)],
    "Kuri Maha":[("Kuldne Dabloon", 0.20), ("Hõbedane Dabloon", 0.40),
                 ("Maha Unibrow", 0.30), ("Cerberuse Karv", 0.10),
                 ("Maha Tups", 0.025), ("Kuri Maha Sarv", 0.005)],
    "Jae Chan": [("Jae Chani Kingitus", 0.03), ("Kuldne Dabloon", 0.30)],
    "Urr":      [("Urr'i Hammas", 0.01), ("Hõbedane Dabloon", 0.20)],
}

LAHINGU_VALIKUD = {
    1:  {"nimi": "Ründa",        "dmg_kordaja": 1.0,  "kirjeldus": "Lööd vaenlast."},
    5:  {"nimi": "Raske löök",   "dmg_kordaja": 1.8,  "kirjeldus": "Aeglane aga võimas löök."},
    10: {"nimi": "Maru rünnak",  "dmg_kordaja": 2.5,  "kirjeldus": "Kiire löökide sari."},
    15: {"nimi": "Purunemine",   "dmg_kordaja": 4.0,  "kirjeldus": "Kõik jõud ühte lööki."},
}

def vali_vaenlane():
    mall = random.choice(VAENLASED)
    return {"nimi": mall["nimi"], "elud": mall["elud"], "joukus": mall["joukus"]}

def vali_boss():
    mall = random.choice(BOSS_VAENLASED)
    return {"nimi": mall["nimi"], "elud": mall["elud"], "joukus": mall["joukus"]}

def anna_drop(vaenlase_nimi):
    dropid = VAENLASE_DROPID.get(vaenlase_nimi, [])
    saadud = []
    for ese_nimi, toenaosus in dropid:
        if random.random() < toenaosus:
            saadud.append({"nimi": ese_nimi})
    return saadud

def arvuta_löök(joukus):
    kas_crit = random.random() < 0.10
    crit_bonus = 10 if kas_crit else 0
    return joukus + crit_bonus, kas_crit, crit_bonus

def töötle_drop(mangija, dropid):
    if dropid:
        print(colorize("Saadud esemed", ANSI_GREEN, bold=True))
        for ese in dropid:
            nimi = ese["nimi"]
            list_dash(nimi, ANSI_GREEN)
            if nimi in DABLOON_VASK_VAARTUS:
                vask = DABLOON_VASK_VAARTUS[nimi]
                if mangija["kaart"] is not None:
                    kaart_lisa_vask(mangija["kaart"], vask)
                    print(f"    {colorize('→', ANSI_YELLOW, bold=True)} Kanti kaardile ({vask} vaskdablooni). Saldo: {kaart_saldo_str(mangija['kaart'])}")
                else:
                    mangija["inventar"].append(ese)
                    print("     (Sul pole kaarti, dabloon jäi inventari.)")
            else:
                mangija["inventar"].append(ese)
    else:
        print("  Vaenlane ei dropinud midagi.")

def saadavad_lahinguvalikud(fuusiline_level):
    valikud = []
    for level_vajab, andmed in sorted(LAHINGU_VALIKUD.items()):
        if fuusiline_level >= level_vajab:
            valikud.append((level_vajab, andmed))
    return valikud

def anna_lahingu_xp(mangija):
    """Annab füüsilist XP lahinguvõidu eest."""
    xp_kogus = random.randint(8, 20)
    oli_level = mangija["stats"]["fuusiline_level"]
    tuli_levelup = lisa_xp(mangija["stats"], "fuusiline", xp_kogus)
    print(f"  [+{xp_kogus} füüsiline XP võidu eest]")
    if tuli_levelup and mangija["stats"]["fuusiline_level"] > oli_level:
        fuusiline_levelup_efekt(mangija, mangija["stats"]["fuusiline_level"])

def kasuta_ravim_lahingus(mangija):
    saadaval = []
    for idx, ese in enumerate(mangija["inventar"]):
        if "hp_restore" in ese or "jou_boost" in ese:
            saadaval.append((idx, ese))

    if not saadaval:
        hamster_teade("hamster kobab taskutes: ravimeid ei ole")
        return

    print("Ravimid:")
    print("0 - Ära kasuta")
    for nr, (idx, r) in enumerate(saadaval, start=1):
        hp = r.get("hp_restore", 0)
        jou = r.get("jou_boost", 0)
        osad = []
        if hp:
            osad.append(f"+{hp} HP")
        if jou:
            osad.append(f"+{jou} Jõud")
        print(f"{nr} - {r['nimi']} ({', '.join(osad)})")

    valik = input("Vali: ").strip()
    if valik == "0":
        return
    try:
        nr = int(valik)
        if 1 <= nr <= len(saadaval):
            idx, ravim = saadaval[nr - 1]
            if "hp_restore" in ravim:
                mangija["elud"] += ravim["hp_restore"]
                print(f"{colorize(ravim['nimi'], ANSI_RED, bold=True)} taastab {ravim['hp_restore']} elu.")
            if "jou_boost" in ravim:
                mangija.setdefault("lahingu_boonused", loo_lahingu_boonused())
                mangija["lahingu_boonused"]["jargmise_loo_jou_boost"] += ravim["jou_boost"]
                print(f"{colorize(ravim['nimi'], ANSI_RED, bold=True)} tõstab jõudu {ravim['jou_boost']} võrra.")
            mangija["inventar"].pop(idx)
            teade_eemaldatud("Kasutasid / eemaldasid eseme:", ravim["nimi"])
        else:
            hamster_teade()
    except ValueError:
        hamster_teade("hamster ei saanud sellest sisendist aru")

def full_reset(mangija, leitud_artefaktid, aktiveeritud_altarid):
    print("\nSu tegelane suri.")
    print("Vali, mida teha edasi.\n")

    while True:
        print("1 - Lae viimane save / checkpoint")
        print("2 - Loo uus tegelane")
        valik = input("Vali: ").strip()

        if valik == "1":
            laetud_mangija, laetud_artefaktid, laetud_altarid = lae_mang()
            if laetud_mangija is None:
                print("Viimast save faili ei leitud.")
                print("Vali uus tegelane või salvesta mäng enne suuremat riski.")
                continue
            print("\nJätkad viimase salvestatud tegelasega.")
            return laetud_mangija, laetud_artefaktid, laetud_altarid

        if valik == "2":
            print("\nVali uus tegelane:")
            for k, (n, hp, jou) in TEGELASE_VALIKUD.items():
                print(f"{k} - {n} (Elud: {hp}, Tugevus: {jou})")

            klassi_valik = input("Vali: ").strip()
            m = loo_uus_mangija_valikust(klassi_valik)
            loo_kaart_mangijale(m)
            print("\nUus tegelane valitud!")
            return m, leitud_artefaktid, aktiveeritud_altarid

        print("Vale valik.")

def mangija_on_klass(mangija, klassi_nimi):
    return mangija.get("nimi") == klassi_nimi

def kriitilise_toenaosus(mangija):
    if mangija_on_klass(mangija, "Vibulaskja"):
        return 0.25
    return 0.10

def leveli_baas_dmg(level):
    return 40 + (level - 1) * 20

def rynnaku_level(mangija, tyyp):
    if tyyp == "fuusiline":
        return mangija["stats"]["fuusiline_level"]
    return mangija["stats"]["elementaalne_level"][tyyp]

def rynnaku_nimi(tyyp):
    nimed = {
        "fuusiline": "Füüsiline löök",
        "tuli": "Tulelöök",
        "vesi": "Veelöök",
        "maa": "Maalöök",
        "õhk": "Õhulöök",
    }
    return nimed.get(tyyp, tyyp.capitalize())

def combo_nimi(tyyp1, tyyp2):
    return f"{rynnaku_nimi(tyyp1)} + {rynnaku_nimi(tyyp2)}"

COMBO_LEVELID = [3]

RYNNAKU_TYYBID = ["fuusiline", "tuli", "vesi", "maa", "õhk"]

def aktiivne_jou_boost(mangija):
    return mangija.get("lahingu_boonused", {}).get("jargmise_loo_jou_boost", 0)

def tarbi_jou_boost(mangija):
    mangija.setdefault("lahingu_boonused", loo_lahingu_boonused())
    boost = mangija["lahingu_boonused"].get("jargmise_loo_jou_boost", 0)
    mangija["lahingu_boonused"]["jargmise_loo_jou_boost"] = 0
    return boost

def arvuta_lahingu_dmg(mangija, tyyp="fuusiline", lisa_boost=True):
    baas_joukus = max(1, int(mangija["joukus"])) + (aktiivne_jou_boost(mangija) if lisa_boost else 0)
    dmg = baas_joukus

    if tyyp in ELEMENDID:
        level = rynnaku_level(mangija, tyyp)
        dmg = int(baas_joukus * (1 + level * 0.10))

    if tyyp == "fuusiline" and mangija_on_klass(mangija, "Sõdalane"):
        dmg = int(dmg * 1.20)
    elif tyyp in ELEMENDID and mangija_on_klass(mangija, "Maag"):
        dmg = int(dmg * 1.20)
    elif tyyp == "õhk" and mangija_on_klass(mangija, "Vibulaskja"):
        dmg = int(dmg * 1.15)

    return max(1, dmg)

def arvuta_combo_dmg(mangija, tyyp1, tyyp2):
    boost = aktiivne_jou_boost(mangija)
    dmg = int((arvuta_lahingu_dmg(mangija, tyyp1, lisa_boost=False) + arvuta_lahingu_dmg(mangija, tyyp2, lisa_boost=False) + boost) * 1.3)

    if mangija_on_klass(mangija, "Sõdalane") and "fuusiline" in (tyyp1, tyyp2):
        dmg = int(dmg * 1.10)
    elif mangija_on_klass(mangija, "Maag") and tyyp1 in ELEMENDID and tyyp2 in ELEMENDID:
        dmg = int(dmg * 1.10)
    elif mangija_on_klass(mangija, "Vibulaskja") and "õhk" in (tyyp1, tyyp2):
        dmg = int(dmg * 1.10)

    return max(1, dmg)

def saadavad_elementaarsed_runnakud(mangija, aktiveeritud_altarid=None):
    if aktiveeritud_altarid is None:
        return []
    aktiivsed_elemendid = [el for el in ELEMENDID if el in aktiveeritud_altarid]
    return [el for el in aktiivsed_elemendid if rynnaku_level(mangija, el) >= 1]

def saadavad_combod(mangija, aktiveeritud_altarid=None):
    saadavad_tyybid = ["fuusiline"] + saadavad_elementaarsed_runnakud(mangija, aktiveeritud_altarid)
    combo_list = []
    unlock = COMBO_LEVELID[0]
    for i, tyyp1 in enumerate(saadavad_tyybid):
        for tyyp2 in saadavad_tyybid[i + 1:]:
            l1 = rynnaku_level(mangija, tyyp1)
            l2 = rynnaku_level(mangija, tyyp2)
            if l1 >= unlock and l2 >= unlock:
                combo_list.append((tyyp1, tyyp2, unlock))
    return combo_list

def rakenda_mangija_runnak(mangija, vaenlane, tyyp, dmg_kordaja=1.0):
    dmg = arvuta_lahingu_dmg(mangija, tyyp)
    crit = random.random() < kriitilise_toenaosus(mangija)
    crit_bonus = 10 if crit else 0
    dmg = int((dmg + crit_bonus) * dmg_kordaja)
    vaenlane["elud"] -= dmg
    tarbi_jou_boost(mangija)
    return dmg, crit, crit_bonus

def rakenda_combo(mangija, vaenlane, tyyp1, tyyp2):
    dmg = arvuta_combo_dmg(mangija, tyyp1, tyyp2)
    crit = random.random() < kriitilise_toenaosus(mangija)
    crit_bonus = 10 if crit else 0
    dmg += crit_bonus
    vaenlane["elud"] -= dmg
    tarbi_jou_boost(mangija)
    return dmg, crit, crit_bonus

def arvuta_vaenlase_dmg(vaenlase_joukus, mangija=None):
    dmg, crit, crit_bonus = arvuta_löök(vaenlase_joukus)
    if mangija_on_klass(mangija or {}, "Sõdalane"):
        dmg = max(1, int(dmg * 0.85))
    return dmg, crit, crit_bonus

def rakenda_house_deed_boonus(mangija, leitud_artefaktid):
    if not isinstance(mangija, dict):
        return False
    if "special_flags" not in mangija or not isinstance(mangija["special_flags"], dict):
        mangija["special_flags"] = loo_special_flags()
    if mangija.get("nimi") != "Knitwitt":
        return False
    if "House deed" not in leitud_artefaktid:
        return False
    if mangija["special_flags"].get("house_deed_applied", False):
        return False
    mangija["elud"] *= 1000
    mangija["joukus"] *= 1000
    mangija["special_flags"]["house_deed_applied"] = True
    return True

def laas_sygavad_ruiinid(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== LÄÄS – SÜGAVAD RUIINID ===\n")

    if mangija.get("nimi") != "Knitwitt":
        print("Kivide vahele jääb kitsas lõhe.")
        print("Sa näed seda, aga tee ei ava end sulle.")
        print("Midagi siin all ootab kedagi teistsugust.")
        pause()
        return

    if not has_inventar(mangija, "Kadunud Riikide Foliant"):
        print("Lõhe viib pimedusse, aga ruunid jäävad mõistetamatuks.")
        print("Vihje: enne vajad Kadunud Riikide Folianti.")
        pause()
        return

    if "House deed" in leitud_artefaktid:
        print("Sügav kamber on tühi.")
        print("Sa tunned siiski veel seda veidrat jõudu seintes.")
        pause()
        return

    print("Foliant väriseb su käes.")
    print("Üks kiviplokk nihkub kõrvale ja avab peidetud laskumise.")
    input("  (edasi...)\n")
    print("Lähed sügavamale ruiinidesse.")
    print("Tolmune kamber ootab sind nagu oleks see alati sinu oma olnud.")
    input("  (edasi...)\n")
    print("Maas lebab kokku volditud paber vana pitseriga.")
    print("Sellel seisab ainult üks nimi.")
    print("Knitwitt.")
    input("  (edasi...)\n")
    print("Leidsid: House deed")
    leitud_artefaktid.append("House deed")
    if rakenda_house_deed_boonus(mangija, leitud_artefaktid):
        print("\nMiski murdub sinu sees lahti.")
        print("Ruiinid vastavad sulle nagu oleksid sa alati siia kuulunud.")
        print("Elud ja tugevus kasvavad mõõtmatult.")
        print(f"Uued elud: {mangija['elud']}")
        print(f"Uus tugevus: {mangija['joukus']}")
    pause()

def fight_monsters(mangija, leitud_artefaktid=None, aktiveeritud_altarid=None):
    clear()
    section_title("LAHING", ANSI_RED)
    print_status_card(mangija)
    vaenlane = vali_vaenlane()
    fuusiline_level = mangija["stats"]["fuusiline_level"]

    if fuusiline_level >= 16:
        print(f"Kohtad vaenlast: {vaenlane['nimi']}. Su silmad hindavad teda hetkega.")
    elif fuusiline_level >= 11:
        print(f"Kohtad vaenlast: {vaenlane['nimi']}. Sa oled kindel.")
    elif fuusiline_level >= 6:
        print(f"Kohtad vaenlast: {vaenlane['nimi']}. Tunned adrenaliini.")
    else:
        print(f"Kohtad vaenlast: {vaenlane['nimi']}. Süda läheb kiiremini.")

    print(colorize(f"Vaenlane: {vaenlane['nimi']}", ANSI_RED, bold=True))
    print(f"Elud: {colorize(str(vaenlane['elud']), ANSI_RED)} | Tugevus: {colorize(str(vaenlane['joukus']), ANSI_YELLOW)}\n")

    valikud = saadavad_lahinguvalikud(fuusiline_level)

    while mangija["elud"] > 0 and vaenlane["elud"] > 0:
        separator()
        print(colorize(f"Sinu käik | HP {max(mangija['elud'], 0)}", ANSI_CYAN, bold=True))
        print("Mida teed?")

        menu = []
        idx = 1

        print("-- Füüsilised rünnakud --")
        for _, andmed in valikud:
            print(f"{idx} - {andmed['nimi']} ({andmed['kirjeldus']})")
            menu.append(("physical_skill", andmed))
            idx += 1

        print("-- Elementaalsed rünnakud --")
        for el in saadavad_elementaarsed_runnakud(mangija, aktiveeritud_altarid):
            dmg = arvuta_lahingu_dmg(mangija, el)
            print(f"{idx} - {rynnaku_nimi(el)} ({el.capitalize()}, {dmg} dmg)")
            menu.append(("element", el))
            idx += 1

        combod = saadavad_combod(mangija, aktiveeritud_altarid)
        if combod:
            print("-- Combod --")
            for tyyp1, tyyp2, unlock in combod:
                dmg = arvuta_combo_dmg(mangija, tyyp1, tyyp2)
                print(f"{idx} - {combo_nimi(tyyp1, tyyp2)} [Lv {unlock}] ({dmg} dmg)")
                menu.append(("combo", (tyyp1, tyyp2, unlock)))
                idx += 1

        print(f"{idx} - Kasuta ravimit")
        ravimi_index = idx

        valik = input("Vali: ").strip()

        if valik == str(ravimi_index):
            kasuta_ravim_lahingus(mangija)
            continue

        try:
            chosen = int(valik) - 1
        except ValueError:
            hamster_teade("hamster ei saanud sellest lahinguvalikust aru")
            continue

        if not (0 <= chosen < len(menu)):
            hamster_teade()
            continue

        tegevus, payload = menu[chosen]

        if tegevus == "physical_skill":
            dmg_kordaja = payload["dmg_kordaja"]
            dmg, crit, crit_bonus = rakenda_mangija_runnak(mangija, vaenlane, "fuusiline", dmg_kordaja)
            if crit:
                print(f"CRIT! Kasutasid {payload['nimi']} ja lõid {vaenlane['nimi']}le {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid {payload['nimi']} ja lõid {vaenlane['nimi']}le {dmg} dmg.")
        elif tegevus == "element":
            el = payload
            dmg, crit, crit_bonus = rakenda_mangija_runnak(mangija, vaenlane, el)
            if crit:
                print(f"CRIT! Kasutasid {rynnaku_nimi(el)} ja lõid {vaenlane['nimi']}le {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid {rynnaku_nimi(el)} ja lõid {vaenlane['nimi']}le {dmg} dmg.")
        else:
            tyyp1, tyyp2, unlock = payload
            dmg, crit, crit_bonus = rakenda_combo(mangija, vaenlane, tyyp1, tyyp2)
            if crit:
                print(f"CRIT! Kasutasid combot {combo_nimi(tyyp1, tyyp2)} ja lõid {vaenlane['nimi']}le {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid combot {combo_nimi(tyyp1, tyyp2)} ja lõid {vaenlane['nimi']}le {dmg} dmg.")

        print(f"{vaenlane['nimi']} elud: {max(vaenlane['elud'], 0)}")

        if vaenlane["elud"] <= 0:
            print(f"\nVõit! {vaenlane['nimi']} on kukkunud.")
            dropid = anna_drop(vaenlane["nimi"])
            print(f"{vaenlane['nimi']} dropib:")
            töötle_drop(mangija, dropid)
            anna_lahingu_xp(mangija)
            pause()
            return mangija, leitud_artefaktid, aktiveeritud_altarid

        separator()
        print(colorize(f"{vaenlane['nimi']} käik", ANSI_RED, bold=True))
        dmg_v, crit_v, crit_bonus_v = arvuta_vaenlase_dmg(vaenlane["joukus"], mangija)
        mangija["elud"] -= dmg_v

        if crit_v:
            print(f"CRIT! {vaenlane['nimi']} lööb sulle {dmg_v} dmg (+{crit_bonus_v} kriitiline).")
        else:
            print(f"{vaenlane['nimi']} lööb sulle {dmg_v} dmg.")
        print(f"Sinu elud: {max(mangija['elud'], 0)}")

        if mangija["elud"] <= 0:
            pause()
            return full_reset(mangija, leitud_artefaktid, aktiveeritud_altarid)

    return mangija, leitud_artefaktid, aktiveeritud_altarid

def fight_boss(mangija, leitud_artefaktid=None, aktiveeritud_altarid=None):
    clear()
    section_title("BOSS LAHING", ANSI_MAGENTA)
    print_status_card(mangija)
    vaenlane = vali_boss()
    fuusiline_level = mangija["stats"]["fuusiline_level"]

    print(colorize(f"BOSS: {vaenlane['nimi']}!", ANSI_MAGENTA, bold=True))
    print(f"Elud: {colorize(str(vaenlane['elud']), ANSI_RED)} | Tugevus: {colorize(str(vaenlane['joukus']), ANSI_YELLOW)}\n")

    valikud = saadavad_lahinguvalikud(fuusiline_level)

    while mangija["elud"] > 0 and vaenlane["elud"] > 0:
        separator()
        print(colorize(f"Sinu käik | HP {max(mangija['elud'], 0)}", ANSI_CYAN, bold=True))
        print("Mida teed?")

        menu = []
        idx = 1

        print("-- Füüsilised rünnakud --")
        for _, andmed in valikud:
            print(f"{idx} - {andmed['nimi']} ({andmed['kirjeldus']})")
            menu.append(("physical_skill", andmed))
            idx += 1

        print("-- Elementaalsed rünnakud --")
        for el in saadavad_elementaarsed_runnakud(mangija, aktiveeritud_altarid):
            dmg = arvuta_lahingu_dmg(mangija, el)
            print(f"{idx} - {rynnaku_nimi(el)} ({el.capitalize()}, {dmg} dmg)")
            menu.append(("element", el))
            idx += 1

        combod = saadavad_combod(mangija, aktiveeritud_altarid)
        if combod:
            print("-- Combod --")
            for tyyp1, tyyp2, unlock in combod:
                dmg = arvuta_combo_dmg(mangija, tyyp1, tyyp2)
                print(f"{idx} - {combo_nimi(tyyp1, tyyp2)} [Lv {unlock}] ({dmg} dmg)")
                menu.append(("combo", (tyyp1, tyyp2, unlock)))
                idx += 1

        print(f"{idx} - Kasuta ravimit")
        ravimi_index = idx

        valik = input("Vali: ").strip()

        if valik == str(ravimi_index):
            kasuta_ravim_lahingus(mangija)
            continue

        try:
            chosen = int(valik) - 1
        except ValueError:
            hamster_teade("hamster ei saanud sellest lahinguvalikust aru")
            continue

        if not (0 <= chosen < len(menu)):
            hamster_teade()
            continue

        tegevus, payload = menu[chosen]

        if tegevus == "physical_skill":
            dmg_kordaja = payload["dmg_kordaja"]
            dmg, crit, crit_bonus = rakenda_mangija_runnak(mangija, vaenlane, "fuusiline", dmg_kordaja)
            if crit:
                print(f"CRIT! Kasutasid {payload['nimi']} ja lõid {vaenlane['nimi']}le {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid {payload['nimi']} ja lõid {vaenlane['nimi']}le {dmg} dmg.")
        elif tegevus == "element":
            el = payload
            dmg, crit, crit_bonus = rakenda_mangija_runnak(mangija, vaenlane, el)
            if crit:
                print(f"CRIT! Kasutasid {rynnaku_nimi(el)} ja lõid {vaenlane['nimi']}le {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid {rynnaku_nimi(el)} ja lõid {vaenlane['nimi']}le {dmg} dmg.")
        else:
            tyyp1, tyyp2, unlock = payload
            dmg, crit, crit_bonus = rakenda_combo(mangija, vaenlane, tyyp1, tyyp2)
            if crit:
                print(f"CRIT! Kasutasid combot {combo_nimi(tyyp1, tyyp2)} ja lõid {vaenlane['nimi']}le {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid combot {combo_nimi(tyyp1, tyyp2)} ja lõid {vaenlane['nimi']}le {dmg} dmg.")
        print(f"{vaenlane['nimi']} elud: {max(vaenlane['elud'], 0)}")

        if vaenlane["elud"] <= 0:
            print(f"\nBOSS ALISTATUD! {vaenlane['nimi']} on langenud!")
            dropid = anna_drop(vaenlane["nimi"])
            print(f"{vaenlane['nimi']} dropib:")
            töötle_drop(mangija, dropid)
            anna_lahingu_xp(mangija)
            pause()
            return mangija, leitud_artefaktid, aktiveeritud_altarid

        separator()
        print(colorize(f"{vaenlane['nimi']} käik", ANSI_MAGENTA, bold=True))
        dmg_v, crit_v, crit_bonus_v = arvuta_vaenlase_dmg(vaenlane["joukus"], mangija)
        mangija["elud"] -= dmg_v

        if crit_v:
            print(f"CRIT! {vaenlane['nimi']} lööb sulle {dmg_v} dmg (+{crit_bonus_v} kriitiline).")
        else:
            print(f"{vaenlane['nimi']} lööb sulle {dmg_v} dmg.")
        print(f"Sinu elud: {max(mangija['elud'], 0)}")

        if mangija["elud"] <= 0:
            pause()
            return full_reset(mangija, leitud_artefaktid, aktiveeritud_altarid)

    return mangija, leitud_artefaktid, aktiveeritud_altarid

pohhi = Pohhi

louna = Louna

ida = Ida

laas = Laas

has_artefakt = has_item

def kasuta_kompassi(mangija, leitud_artefaktid, aktiveeritud_altarid, asukoht):
    return kasuta_kompassi_asukohas(asukoht, mangija, leitud_artefaktid, aktiveeritud_altarid)

RAVIMID = [
    {"nimi": "Tervendav salv",    "hp_restore": 200,                          "hind_dabloonides": 2},
    {"nimi": "Jõu eliksiir",                         "jou_boost": 200,        "hind_dabloonides": 3},
    {"nimi": "Elu potion",        "hp_restore": 500,                          "hind_dabloonides": 5},
    {"nimi": "Kuldne õun",        "hp_restore": 150,                          "hind_dabloonides": 1},
    {"nimi": "Topelt juustuburger","hp_restore": 400,                         "hind_dabloonides": 3},
    {"nimi": "Energia jook",      "hp_restore": 1000, "jou_boost": 300,       "hind_dabloonides": 6},
    {"nimi": "Värske",            "hp_restore": 550,  "jou_boost": 550,       "hind_dabloonides": 7},
]

ESEMETE_HINNAD = {
    "Kont": 50, "Mädanenud Liha": 50, "Draakoni Soomus": 600,
    "Goblini Kihv": 100, "Orgi Mäss": 100, "Hiiglase Silm": 200,
    "Zombi Sõrm": 100, "Luukere Tuum": 300, "Maha Unibrow": 1000,
    "Cerberuse Karv": 900, "Maha Tups": 1500, "Kuri Maha Sarv": 1500,
    "Jae Chani Kingitus": 5000, "Urr'i Hammas": 1500,
    "Kuldne Dabloon": 0, "Hõbedane Dabloon": 0, "Vask Dabloon": 0,
}

def trader_menu(mangija):
    def ravimi_kirjeldus(ravim):
        osad = []
        if "hp_restore" in ravim:
            osad.append(f"+{ravim['hp_restore']} HP")
        if "jou_boost" in ravim:
            osad.append(f"+{ravim['jou_boost']} Jõud")
        return ", ".join(osad)

    while True:
        clear()
        print_status_card(mangija, "TRADER")
        if mangija["kaart"]:
            info_line("Saldo", kaart_saldo_str(mangija['kaart']), ANSI_YELLOW)
        else:
            print("Sul pole pangakaarti!")

        print("1 - Vaata ravimeid")
        print("2 - Osta ravim nimekirjast")
        print("3 - Müü ese")
        print("4 - Tagasi")

        valik = input("Vali: ").strip()

        if valik == "1":
            clear()
            scene_title("RAVIMID", ANSI_GREEN)
            for i, r in enumerate(RAVIMID, start=1):
                print(f"{i} - {r['nimi']} ({ravimi_kirjeldus(r)}) - {r['hind_dabloonides']} vaskdablooni")
            pause()

        elif valik == "2":
            if not mangija["kaart"]:
                print("Sul pole pangakaarti!")
                pause()
                continue

            while True:
                clear()
                scene_title("OSTA RAVIM", ANSI_GREEN)
                info_line("Saldo", kaart_saldo_str(mangija['kaart']), ANSI_YELLOW)
                for i, r in enumerate(RAVIMID, start=1):
                    print(f"{i} - {r['nimi']} ({ravimi_kirjeldus(r)}) - {r['hind_dabloonides']} vaskdablooni")
                print("0 - Tagasi")

                v = input("Vali, mida tahad osta: ").strip()
                if v == "0":
                    break

                try:
                    idx = int(v) - 1
                except ValueError:
                    hamster_teade("hamster ei oska seda ostu lugeda")
                    pause()
                    continue

                if not (0 <= idx < len(RAVIMID)):
                    hamster_teade()
                    pause()
                    continue

                ravim = RAVIMID[idx]
                hind = ravim["hind_dabloonides"]

                kogus_input = input(f"Mitu tk '{ravim['nimi']}' soovid osta? ").strip()
                try:
                    kogus = int(kogus_input)
                except ValueError:
                    print("Sisesta täisarv.")
                    pause()
                    continue

                if kogus <= 0:
                    print("Kogus peab olema vähemalt 1.")
                    pause()
                    continue

                koguhind = hind * kogus
                print(f"Ostad: {ravim['nimi']} x{kogus}")
                print(f"Koguhind: {koguhind} vaskdablooni")

                kinnita = input("Kas kinnitad ostu? (j/e): ").strip().lower()
                if kinnita != "j":
                    print("Ost tühistatud.")
                    pause()
                    continue

                if not kontrolli_pin(mangija):
                    pause()
                    continue

                if not kaart_eemalda_vask(mangija["kaart"], koguhind):
                    print("Pole piisavalt raha!")
                    pause()
                    continue

                for _ in range(kogus):
                    mangija["inventar"].append(ravim.copy())

                print(f"Ostsid: {colorize(ravim['nimi'], ANSI_GREEN, bold=True)} x{kogus}")
                print(f"Uus saldo: {kaart_saldo_str(mangija['kaart'])}")
                pause()

        elif valik == "3":
            clear()
            print("=== MÜÜ ESE ===")
            myydavad = [e for e in mangija["inventar"]
                        if e["nimi"] not in ("Kuldne Dabloon", "Hõbedane Dabloon", "Vask Dabloon")]

            if not myydavad:
                print("Sul pole müüa midagi.")
                pause()
                continue

            loendur = {}
            for e in myydavad:
                loendur[e["nimi"]] = loendur.get(e["nimi"], 0) + 1

            unikaalsed = list(loendur.keys())
            for i, nimi in enumerate(unikaalsed, start=1):
                hind = ESEMETE_HINNAD.get(nimi, 1)
                print(f"{i} - {nimi} x{loendur[nimi]} - {hind} vaskdablooni")
            print("0 - Tagasi")

            v = input("Vali number: ").strip()
            if v == "0":
                continue
            try:
                idx = int(v) - 1
                if 0 <= idx < len(unikaalsed):
                    ese_nimi = unikaalsed[idx]
                    hind = ESEMETE_HINNAD.get(ese_nimi, 1)
                    for e in mangija["inventar"]:
                        if e["nimi"] == ese_nimi:
                            mangija["inventar"].remove(e)
                            break
                    kaart_lisa_vask(mangija["kaart"], hind)
                    teade_eemaldatud("Müüsid / eemaldasid eseme:", ese_nimi)
                    print(f"Saad raha: {colorize('+' + str(hind) + ' vaskdablooni', ANSI_GREEN, bold=True)}")
                    print(f"Uus saldo: {kaart_saldo_str(mangija['kaart'])}")
                else:
                    print("Vale valik.")
            except ValueError:
                print("Vale sisend.")
            pause()

        elif valik == "4":
            return

        else:
            hamster_teade()
            pause()

WORLD_STATE = {
    "tormikompass_aktiivne": False,
    "vunts_alistatud": False,
    "kauged_maad_avastatud": False,
    "laane_altariruum_avatud": False,
    "tempel_avastatud": False,
    "tempel_labitutud": False,
}

def loo_world_state_vaikimisi():
    return {
        "tormikompass_aktiivne": False,
        "vunts_alistatud": False,
        "kauged_maad_avastatud": False,
        "laane_altariruum_avatud": False,
        "tempel_avastatud": False,
        "tempel_labitutud": False,
    }

def _paranda_world_state(data=None):
    global WORLD_STATE
    vaikimisi = loo_world_state_vaikimisi()
    if isinstance(data, dict):
        vaikimisi.update({k: v for k, v in data.items() if k in vaikimisi})
    WORLD_STATE = vaikimisi
    return WORLD_STATE

_paranda_world_state()

def kaivita_teine_peatukk():
    peatukk2_path = os.path.join(BASE_DIR, "Peatükk2.py")
    if not os.path.exists(peatukk2_path):
        print("Peatükk 2 faili ei leitud.")
        print("Küsi Peatükk2.py fail ja pane see samasse kausta.")
        pause()
        return

    print("Käivitan 2. peatüki...")
    pause()
    runpy.run_path(peatukk2_path, run_name="__main__")

def salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid):
    if not SAVE_FILE:
        print("Save slot pole valitud.")
        return
    data = {
        "meta": SAVE_META,
        "mangija": mangija,
        "leitud_artefaktid": leitud_artefaktid,
        "aktiveeritud_altarid": list(aktiveeritud_altarid),
        "world_state": WORLD_STATE,
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Mäng salvestatud: {SAVE_FILE}")

def lae_mang():
    if not SAVE_FILE:
        print("Save slot pole valitud.")
        return None, [], set()
    if not os.path.exists(SAVE_FILE):
        print("Save faili ei leitud.")
        return None, [], set()
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    mangija = data["mangija"]
    if "stats" not in mangija:
        mangija["stats"] = loo_tühi_stats()
    if "special_flags" not in mangija or not isinstance(mangija["special_flags"], dict):
        mangija["special_flags"] = loo_special_flags()
    else:
        vaikimisi = loo_special_flags()
        vaikimisi.update(mangija["special_flags"])
        mangija["special_flags"] = vaikimisi
    mangija["lahingu_boonused"] = loo_lahingu_boonused()
    leitud_artefaktid = data.get("leitud_artefaktid", data.get("leitud_artifaktid", []))
    aktiveeritud_altarid = set(data.get("aktiveeritud_altarid", []))
    _paranda_world_state(data.get("world_state"))
    rakenda_house_deed_boonus(mangija, leitud_artefaktid)
    print("Mäng laetud!")
    mangija_info(mangija)
    return mangija, leitud_artefaktid, aktiveeritud_altarid

FRAGMENDID = ["Kaose fragment", "Harmoonia fragment", "Aja fragment"]

KROONI_NIMI = "Kadunud Ajastu Kroon"

def koik_elemendid_vahemalt(mangija, tase):
    for el in ELEMENDID:
        if mangija["stats"]["elementaalne_level"][el] < tase:
            return False
    return True

def koik_fragmendid_leitud(leitud_artefaktid):
    return all(f in leitud_artefaktid for f in FRAGMENDID)

def vuntsi_dialoog(leitud_artefaktid):
    clear()
    print("=== VUNTS ===\n")
    print("Vunts langetab lusika.")
    print("Ta hingab raskelt, aga ei ründa enam.")
    input("(edasi...)\n")
    print("Sa arvad, et linn kukkus kokku, sest keegi tegi vea.")
    print("Ei.")
    input("(edasi...)\n")
    print("Me õppisime elemendid lahti võtma.")
    print("Aga me ei õppinud neid uuesti kokku panema.")
    input("(edasi...)\n")
    print("Tuli, vesi, maa, õhk.")
    print("Eraldi on nad jõud.")
    print("Koos on nad maailm.")
    input("(edasi...)\n")
    print("Kui side murdus, murdus ka aeg.")
    print("Ruiinid ei ole minevik.")
    print("Need kukuvad siiani.")
    input("(edasi...)\n")
    print("On üks koht. Ajalõhe tempel.")
    print("Aga enne seda on sul vaja midagi muud.")
    input("(edasi...)\n")
    print("Kadunud Ajastu Kroon murdus tükkideks.")
    print("Kolm fragmenti kadusid kohtadesse, kuhu maailm ise enam hästi ei ulatu.")
    print("Kaose fragment. Harmoonia fragment. Aja fragment.")
    input("(edasi...)\n")
    print("Tormikompass ei näita enam teed.")
    print("See tuleb kõigepealt äratada.")
    pause()

def aktiveeri_tormikompass(mangija, leitud_artefaktid, aktiveeritud_altarid):
    if "Tormikompass" not in leitud_artefaktid:
        print("Sul pole Tormikompassi.")
        pause()
        return
    if not WORLD_STATE["vunts_alistatud"]:
        print("Vunts ei usalda sind veel.")
        pause()
        return
    if WORLD_STATE["tormikompass_aktiivne"]:
        print("Tormikompass on juba aktiivne.")
        pause()
        return
    clear()
    print("Vunts võtab kompassi oma kätte.")
    print("Ta asetab selle kivile ja puudutab korraks selle serva.")
    input("(edasi...)\n")
    print("Neli altarit vastavad sinus korraga.")
    print("Kompass hakkab pöörlema, siis peatub järsult.")
    input("(edasi...)\n")
    print("See ei osuta enam maale.")
    print("See osutab tormi poole.")
    WORLD_STATE["tormikompass_aktiivne"] = True
    print("\nTormikompass on aktiveeritud.")
    pause()

def _fragmenti_hook(leitud_artefaktid):
    if koik_fragmendid_leitud(leitud_artefaktid):
        clear()
        print("Kolm fragmenti resoneerivad omavahel.")
        print("Miski suurem tahab kuju võtta.")
        print(f"Sa tunned nime: {KROONI_NIMI}.")
        print("Aga kroon ise ei ole veel sinu käes.")
        pause()

def kaose_laburint(mangija, leitud_artefaktid):
    clear()
    print("=== KAUGED MAAD - KAOSE LABÜRINT ===\n")
    if "Kaose fragment" in leitud_artefaktid:
        print("Koridorid pöörduvad taas iseendasse.")
        print("Kaose fragment on siit juba leitud.")
        pause()
        return mangija
    print("Seinad liiguvad aeglaselt, justkui nad ei oleks otsustanud, kus nad olla tahavad.")
    print("Iga samm muudab rada.")
    input("(edasi...)\n")
    print("Kahe ukse ees seisavad kaks valvurit.")
    print("Üks valetab alati. Teine räägib alati tõtt.")
    input("(edasi...)\n")

    while True:
        clear()
        print("=== KAOSE VALVURID ===\n")
        print("Vasak valvur ütleb: 'Parempoolne valvur räägib tõtt.'")
        print("Parem valvur ütleb: 'Vasak valvur valetab.'")
        print()
        print("1 - Mine vasakust uksest")
        print("2 - Mine paremast uksest")
        valik = input("Vali: ").strip()

        if valik == "2":
            print("\nParempoolne uks avaneb kriuksudes.")
            print("Kaos taandub hetkeks, nagu oleksid vastuolu õigesti läbi näinud.")
            input("(edasi...)\n")
            print("Labürindi keskel hõõgub katkine tükk tumepunases valguses.")
            print("Leiad: Kaose fragment")
            leitud_artefaktid.append("Kaose fragment")
            _fragmenti_hook(leitud_artefaktid)
            pause()
            return mangija
        if valik == "1":
            print("\nVasak uks viib sind tagasi samasse saali.")
            print("Kaos naerab su üle. Midagi siin ei klapi.")
            pause()
            continue

        print("Vale valik.")
        pause()

def harmoonia_laburint(mangija, leitud_artefaktid):
    clear()
    print("=== KAUGED MAAD - HARMOONIA LABÜRINT ===\n")
    if "Harmoonia fragment" in leitud_artefaktid:
        print("Vaikus seisab siin endiselt paigal.")
        print("Harmoonia fragment on siit juba leitud.")
        pause()
        return mangija
    print("Siin ei ava teed jõud, vaid tasakaal.")
    print("Ukseraamid helisevad tasaselt, kui neist möödud.")
    input("(edasi...)\n")
    while True:
        clear()
        print("=== HARMONIA KATSE ===\n")
        print("Helendav tahvel küsib sinult ühe küsimuse.")
        print("Mis autoga põgeneb mängija Need for Speed: Most Wanted (2005) lõpus?")
        print()
        print("1 - BMW M3 GTR")
        print("2 - Mitsubishi Lancer Evolution VIII")
        print("3 - Mazda RX-7")
        valik = input("Vali: ").strip()

        if valik == "1":
            print("\nTahvel heliseb puhtalt ja uks avaneb.")
            print("Keskel lebab hele killuke, mis pulseerib ühtlases rütmis.")
            print("Leiad: Harmoonia fragment")
            leitud_artefaktid.append("Harmoonia fragment")
            _fragmenti_hook(leitud_artefaktid)
            pause()
            return mangija
        if valik in ("2", "3"):
            print("\nRuum läheb korraks häälest ära.")
            print("Vale vastus. Harmoonia ei võta sind veel omaks.")
            pause()
            continue

        print("Vale valik.")
        pause()

def aja_laburint(mangija, leitud_artefaktid):
    clear()
    print("=== KAUGED MAAD - AJA LABÜRINT ===\n")
    if "Aja fragment" in leitud_artefaktid:
        print("Ruumid korduvad endiselt.")
        print("Aja fragment on siit juba leitud.")
        pause()
        return mangija
    print("Mõned sammud kõlavad ette, mõned kõlavad tagantjärele.")
    print("Sa ei ole kindel, kas liigud edasi või tagasi.")
    input("(edasi...)\n")
    oige_sammud = 4
    progress = 0

    while True:
        clear()
        print("=== AJA SILMUS ===\n")
        print("Labürint tundub lõputu.")
        print("Sama ristmik tuleb aina tagasi, aga miski ütleb, et ainult üks suund viib edasi.")
        print(f"Õigeid samme järjest: {progress}/{oige_sammud}")
        print()
        print("1 - Vasakule")
        print("2 - Otse")
        print("3 - Paremale")
        valik = input("Vali: ").strip()

        if valik == "3":
            progress += 1
            if progress >= oige_sammud:
                print("\nLõpuks muutub õhk teistsuguseks.")
                print("Aeg laseb sind läbi.")
                input("(edasi...)\n")
                print("Viimases kambris hõljub külm hõbedane tükk.")
                print("Leiad: Aja fragment")
                leitud_artefaktid.append("Aja fragment")
                _fragmenti_hook(leitud_artefaktid)
                pause()
                return mangija
            print("\nSeekord jõudsid natuke kaugemale.")
            pause()
            continue

        if valik in ("1", "2"):
            progress = 0
            print("\nRuum voldib end kokku ja oled jälle alguses.")
            print("Aeg nõuab järjekindlust.")
            pause()
            continue

        print("Vale valik.")
        pause()

def kauged_maad(mangija, leitud_artefaktid, aktiveeritud_altarid):
    WORLD_STATE["kauged_maad_avastatud"] = True
    while True:
        clear()
        print("=== KAUGED MAAD ===\n")
        print("Maailm on siin nihkes.")
        print("Trepid lõpevad tühjuses. Vesi voolab vahel üles.")
        print()
        print("1 - Kaose labürint")
        print("2 - Harmoonia labürint")
        print("3 - Aja labürint")
        print("4 - Salvesta mäng")
        print("5 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "1":
            mangija = kaose_laburint(mangija, leitud_artefaktid)
        elif valik == "2":
            mangija = harmoonia_laburint(mangija, leitud_artefaktid)
        elif valik == "3":
            mangija = aja_laburint(mangija, leitud_artefaktid)
        elif valik == "4":
            salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
            pause()
        elif valik == "5":
            return mangija
        else:
            print("Vigane valik.")
            pause()

def saab_templisse(mangija, leitud_artefaktid):
    if not koik_elemendid_vahemalt(mangija, 10):
        return False
    if not koik_fragmendid_leitud(leitud_artefaktid):
        return False
    if not WORLD_STATE["tormikompass_aktiivne"]:
        return False
    return True

def kaose_katse():
    clear()
    print("=== AJALÕHE TEMPEL - KAOS ===\n")
    print("Saal väriseb. Sambad nihkuvad nagu nad otsiksid uut kuju.")
    print("Siin ei päästa sind toores jõud.")
    input("(edasi...)\n")
    print("Sa hoiad end tagasi.")
    print("Kaos ei vaibu, aga ta lakkab sind murdmast.")
    pause()

def harmoonia_katse():
    while True:
        clear()
        print("=== AJALÕHE TEMPEL - HARMONIA ===\n")
        print("Neli märki süttivad põrandal.")
        print("Tempel ootab, et mäletaksid järjekorda.")
        print("Sisesta: tuli vesi maa õhk")
        valik = input("Järjekord: ").strip().lower()
        if valik == "tuli vesi maa õhk":
            print("Märgid joondavad end ja helisevad korraga.")
            pause()
            return
        print("Järjekord laguneb laiali.")
        pause()

def aja_katse():
    clear()
    print("=== AJALÕHE TEMPEL - AEG ===\n")
    print("Sisened ruumi, mida oled nagu juba näinud.")
    input("(edasi...)\n")
    print("Sama samm. Sama hingamine. Sama vaikus.")
    input("(edasi...)\n")
    print("Ainult üks detail on muutunud.")
    print("Sa märkad seda. Sellepärast tempel laseb sul edasi minna.")
    pause()

def kokkupaneku_saal(mangija, leitud_artefaktid):
    clear()
    print("=== KOKKUPANEKU SAAL ===\n")
    print("Kaose fragment. Harmoonia fragment. Aja fragment.")
    print("Need tõusevad su kotist enne, kui jõuad neid puudutada.")
    input("(edasi...)\n")
    kaose_katse()
    harmoonia_katse()
    aja_katse()
    clear()
    print("=== KOKKUPANEKU SAAL ===\n")
    print("Kolm fragmenti ei tõuka enam üksteist eemale.")
    print("Need pöörlevad aeglaselt ühe telje ümber.")
    input("(edasi...)\n")
    if KROONI_NIMI not in leitud_artefaktid and "Ajastute Mõõk" not in leitud_artefaktid:
        print(f"Saad: {colorize(KROONI_NIMI, ANSI_GREEN, bold=True)}")
        leitud_artefaktid.append(KROONI_NIMI)
    else:
        print(f"{KROONI_NIMI} vastab sulle taas.")
    input("(edasi...)\n")
    print("Kroon ei jää terveks krooniks.")
    print("Ta murdub valguseks ja voolab ühte terasse.")
    input("(edasi...)\n")
    if KROONI_NIMI in leitud_artefaktid:
        leitud_artefaktid.remove(KROONI_NIMI)
    if "Ajastute Mõõk" not in leitud_artefaktid:
        print(f"Saad: {colorize('Ajastute Mõõk', ANSI_GREEN, bold=True)}")
        leitud_artefaktid.append("Ajastute Mõõk")
    else:
        print("Ajastute Mõõk on juba sinu käes.")
    pause()

def ajalohe_kamber(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    print("=== AJALÕHE KAMBER ===\n")
    print("Kamber ei ole päris ruum.")
    print("See on lõhe, mis hoiab koos liiga palju hetki korraga.")
    input("(edasi...)\n")
    print("Näed varemeid.")
    print("Näed tervet linna.")
    print("Näed hetke, mil kõik hakkab murduma.")
    input("(edasi...)\n")
    if "Ajastute Mõõk" not in leitud_artefaktid:
        print("Sul puudub Ajastute Mõõk.")
        pause()
        return mangija
    print("Mõõk muutub su käes raskeks.")
    print("Nagu hoiaksid metalli asemel ajastut ennast.")
    input("(edasi...)\n")
    valik = input("Kas raiud ajasse tee? (j/e): ").strip().lower()
    if valik != "j":
        print("Lõhe tõmbub tagasi ja jätab su seisma piiri peale.")
        pause()
        return mangija
    print("Tõstad mõõga.")
    input("(edasi...)\n")
    print("Raiud.")
    input("(edasi...)\n")
    print("Puruneb mitte kivi, vaid aeg.")
    input("(edasi...)\n")
    print("Sa ei kuku edasi. Maailm liigub sinu ümber.")
    input("(edasi...)\n")
    print("Linn on terve.")
    print("Tuli ei ole veel taevast söönud.")
    print("Kivid ei ole veel murdunud.")
    input("(edasi...)\n")
    print("Sa oled enne langust.")
    print("Seekord jõudsid enne varemeid.")
    WORLD_STATE["tempel_labitutud"] = True
    print()
    print("Aitäh mängimast, see on esimese peatüki lõpp!")
    print("Mäng salvestatakse automaatselt.")
    salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
    kaivita_teine_peatukk()
    return mangija

def ajalohe_tempel(mangija, leitud_artefaktid, aktiveeritud_altarid):
    clear()
    if WORLD_STATE["tempel_labitutud"]:
        print("Ajalõhe tempel on sulle juba oma tee avanud.")
        print("Minevik ootab sind edasi seal, kuhu mõõgaga lõikasid.")
        print("Aitäh mängimast, see on esimese peatüki lõpp!")
        print()
        print("  (\\__/)")
        print("  ( •ㅅ•)")
        print("  / 　 づ")
        print("  hamter says: aitäh")
        kaivita_teine_peatukk()
        return mangija
    if not koik_elemendid_vahemalt(mangija, 10):
        print("Tempel ei vasta sulle veel.")
        print("Vihje: vii kõik neli elementi vähemalt tasemele 10.")
        pause()
        return mangija
    if not koik_fragmendid_leitud(leitud_artefaktid):
        print("Tee templisse jääb poolikuks.")
        print("Vihje: leia Kaose fragment, Harmoonia fragment ja Aja fragment.")
        pause()
        return mangija
    if not WORLD_STATE["tormikompass_aktiivne"]:
        print("Tormikompass on veel uinunud.")
        pause()
        return mangija
    WORLD_STATE["tempel_avastatud"] = True
    print("=== AJALÕHE TEMPEL ===\n")
    print("Tempel ei avane. Ta nihkub sinu ette nagu oleks ta sind oodanud.")
    input("(edasi...)\n")
    print("Fragmendid hakkavad helendama.")
    print("Kivi vastab neile, mitte sulle.")
    input("(edasi...)\n")
    print("Sul on veel hetk aega end kinnitada.")
    print("1 - Salvesta mäng")
    print("2 - Astu templisse")
    valik = input("Vali: ").strip()
    if valik == "1":
        salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
        pause()
        return mangija
    kokkupaneku_saal(mangija, leitud_artefaktid)
    return ajalohe_kamber(mangija, leitud_artefaktid, aktiveeritud_altarid)

def vunts_menu(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        print("=== VUNTS ===\n")
        print("1 - Kuula Vuntsi juttu")
        print("2 - Aktiveeri Tormikompass")
        print("3 - Treeni")
        print("4 - Proovi leida tee Ajalõhe templisse")
        print("5 - Salvesta mäng")
        print("6 - Lahku")
        valik = input("\nVali: ").strip()

        if valik == "1":
            vuntsi_dialoog(leitud_artefaktid)
        elif valik == "2":
            aktiveeri_tormikompass(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "3":
            treeni(mangija, aktiveeritud_altarid)
        elif valik == "4":
            mangija = ajalohe_tempel(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "5":
            salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
            pause()
        elif valik == "6":
            return mangija
        else:
            print("Vigane valik.")
            pause()

def fight_vunts(mangija, leitud_artefaktid=None, aktiveeritud_altarid=None):
    clear()
    print("=== VUNTSI DUELL ===\n")
    vaenlane = {"nimi": "Vunts", "elud": 1200, "joukus": 65}
    fuusiline_level = mangija["stats"]["fuusiline_level"]
    valikud = saadavad_lahinguvalikud(fuusiline_level)

    print("Vunts tõstab puulusika nagu relva.")
    print("See ei tundu naljana.")
    pause()

    while mangija["elud"] > 0 and vaenlane["elud"] > 0:
        print(f"\nSinu elud: {max(mangija['elud'], 0)}")
        print(f"Vuntsi elud: {max(vaenlane['elud'], 0)}")

        menu = []
        idx = 1

        print("-- Füüsilised rünnakud --")
        for _, andmed in valikud:
            print(f"{idx} - {andmed['nimi']} ({andmed['kirjeldus']})")
            menu.append(("physical_skill", andmed))
            idx += 1

        elemendid = saadavad_elementaarsed_runnakud(mangija, aktiveeritud_altarid)
        if elemendid:
            print("-- Elementaalsed rünnakud --")
            for el in elemendid:
                dmg = arvuta_lahingu_dmg(mangija, el)
                print(f"{idx} - {rynnaku_nimi(el)} ({el.capitalize()}, {dmg} dmg)")
                menu.append(("element", el))
                idx += 1

        combod = saadavad_combod(mangija, aktiveeritud_altarid)
        if combod:
            print("-- Combod --")
            for tyyp1, tyyp2, unlock in combod:
                dmg = arvuta_combo_dmg(mangija, tyyp1, tyyp2)
                print(f"{idx} - {combo_nimi(tyyp1, tyyp2)} [Lv {unlock}] ({dmg} dmg)")
                menu.append(("combo", (tyyp1, tyyp2, unlock)))
                idx += 1

        print(f"{idx} - Kasuta ravimit")
        ravimi_index = idx
        valik = input("Vali: ").strip()

        if valik == str(ravimi_index):
            kasuta_ravim_lahingus(mangija)
            continue

        try:
            chosen = int(valik) - 1
        except ValueError:
            print("Vale sisend.")
            continue

        if not (0 <= chosen < len(menu)):
            print("Vale valik.")
            continue

        tegevus, payload = menu[chosen]

        if tegevus == "physical_skill":
            dmg_kordaja = payload["dmg_kordaja"]
            dmg, crit, crit_bonus = rakenda_mangija_runnak(mangija, vaenlane, "fuusiline", dmg_kordaja)
            if crit:
                print(f"CRIT! Kasutasid {payload['nimi']} ja lõid Vuntsile {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid {payload['nimi']} ja lõid Vuntsile {dmg} dmg.")
        elif tegevus == "element":
            el = payload
            dmg, crit, crit_bonus = rakenda_mangija_runnak(mangija, vaenlane, el)
            if crit:
                print(f"CRIT! Kasutasid {rynnaku_nimi(el)} ja lõid Vuntsile {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid {rynnaku_nimi(el)} ja lõid Vuntsile {dmg} dmg.")
        else:
            tyyp1, tyyp2, unlock = payload
            dmg, crit, crit_bonus = rakenda_combo(mangija, vaenlane, tyyp1, tyyp2)
            if crit:
                print(f"CRIT! Kasutasid combot {combo_nimi(tyyp1, tyyp2)} ja lõid Vuntsile {dmg} dmg (+{crit_bonus} kriitiline).")
            else:
                print(f"Kasutasid combot {combo_nimi(tyyp1, tyyp2)} ja lõid Vuntsile {dmg} dmg.")

        print(f"Vuntsi elud: {max(vaenlane['elud'], 0)}")

        if vaenlane["elud"] <= 0:
            print("\nVunts langetab lusika.")
            WORLD_STATE["vunts_alistatud"] = True
            anna_lahingu_xp(mangija)
            pause()
            return mangija, leitud_artefaktid, aktiveeritud_altarid

        dmg_v, crit_v, crit_bonus_v = arvuta_vaenlase_dmg(vaenlane["joukus"], mangija)
        mangija["elud"] -= dmg_v
        if crit_v:
            print(f"CRIT! Vunts lööb sulle {dmg_v} dmg (+{crit_bonus_v} kriitiline).")
        else:
            print(f"Vunts lööb sulle {dmg_v} dmg.")

        if mangija["elud"] <= 0:
            pause()
            return full_reset(mangija, leitud_artefaktid, aktiveeritud_altarid)

    return mangija, leitud_artefaktid, aktiveeritud_altarid

def saar(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        print("=== SAAR ===\n")
        print("Udu hajub aeglaselt.")
        print("Saar on kivine ja vaikne. Midagi vana ootab siin.")
        print()
        print("1 - Uuri randa")
        print("2 - Mine koopa juurde")
        print("3 - Mine tagasi paatide juurde")
        valik = input("\nVali: ").strip()

        if valik == "1":
            clear()
            print("=== SAAR - RAND ===\n")
            print("Liiv on tume ja märg.")
            print("Lained on liiga vaiksed.")
            if len(aktiveeritud_altarid) < 4:
                print("Midagi jääb puudu. Saar hoiab end tagasi.")
            else:
                print("Kõik neli elementi pulseerivad sinus. Saar vastab sulle.")
            pause()
        elif valik == "2":
            clear()
            print("=== SAAR - KOOPASUU ===\n")
            print("Koopa ees seisab vana rüütel.")
            print("Tema soomus on mõranenud, aga valve pole lõppenud.")
            input("  (edasi...)\n")
            if len(aktiveeritud_altarid) < 4:
                print("Rüütel ei lase sind mööda.")
                print("Päeviku hoiatus oli tõsi. Sa pole veel valmis.")
                pause()
                continue
            if not WORLD_STATE["vunts_alistatud"]:
                print("1 - Salvesta mäng")
                print("2 - Astu koopasse")
                print("3 - Tagasi")
                v = input("\nVali: ").strip()
                if v == "1":
                    salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
                    pause()
                    continue
                if v == "3":
                    continue
                print("Rüütel astub kõrvale.")
                print("Koopa sügavusest kostab raske hingamine.")
                input("  (edasi...)\n")
                mangija, leitud_artefaktid, aktiveeritud_altarid = fight_boss(mangija, leitud_artefaktid, aktiveeritud_altarid)
                if mangija is None or mangija["elud"] <= 0:
                    return mangija
                print("\nKoobas vaikib.")
                print("Aga sa pole siin üksi.")
                input("  (edasi...)\n")
                mangija, leitud_artefaktid, aktiveeritud_altarid = fight_vunts(mangija, leitud_artefaktid, aktiveeritud_altarid)
                if mangija is None or mangija["elud"] <= 0:
                    return mangija
            return vunts_menu(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "3":
            return mangija
        else:
            print("Vigane valik.")
            pause()

def ida_paadid(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        print("=== IDA - PAADID ===\n")
        print("Paatide juures on vaikne.")
        print("Mõned neist on lagunenud, üks peab veel vastu.")
        print()
        print("1 - Sõua saarele")
        if WORLD_STATE["tormikompass_aktiivne"]:
            print("2 - Lase tormil viia sind Kaugetesse Maadesse")
            print("3 - Tagasi")
        else:
            print("2 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "1":
            if not has_item(leitud_artefaktid, "Iidne Tee"):
                print("Üks paat tundub tugevam.")
                print("Aga kuhu minna? Udu peidab kõik.")
                print("Vihje: Sul on vaja Iidset Teed.")
                pause()
                continue
            print("Võtad Iidse Tee välja.")
            print("See hõõgub nõrgalt ja nool osutab udu sisse.")
            input("  (edasi...)\n")
            return saar(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2" and WORLD_STATE["tormikompass_aktiivne"]:
            if "Tormikompass" not in leitud_artefaktid:
                print("Sul pole Tormikompassi.")
                pause()
                continue
            clear()
            print("Tormikompass pöörleb metsikult.")
            print("Paat ei lähe enam üle vee, vaid läbi tormi.")
            input("(edasi...)\n")
            return kauged_maad(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif (valik == "2" and not WORLD_STATE["tormikompass_aktiivne"]) or (valik == "3" and WORLD_STATE["tormikompass_aktiivne"]):
            return
        else:
            print("Vigane valik.")
            pause()

def pohikaart(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        clear()
        if mangija is None:
            print("Viga: mangija puudub.")
            return None, leitud_artefaktid, aktiveeritud_altarid
        section_title("VANA KOMPASSI SALADUS", ANSI_CYAN)
        print_status_card(mangija)
        if WORLD_STATE["tormikompass_aktiivne"]:
            print(colorize("Tormikompass: aktiivne", ANSI_BLUE, bold=True))
        print()
        print("  1 - Põhi")
        print("  2 - Lõuna")
        print("  3 - Ida")
        print("  4 - Lääs")
        print(colorize("  ─────────────────────────────", ANSI_DIM))
        print("  5 - Treeni")
        print("  6 - Trader")
        print("  7 - Boss lahing")
        print(colorize("  ─────────────────────────────", ANSI_DIM))
        print("  8 - Inventar ja artefaktid")
        print("  9 - Statistika")
        print(colorize("  ─────────────────────────────", ANSI_DIM))
        print("  10 - Salvesta mäng")
        print("  11 - Lae mäng")
        print("  0  - Välju")

        valik = input("\nVali: ").strip()

        if valik == "1":
            mangija = pohhi(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "2":
            mangija = louna(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "3":
            mangija = ida(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "4":
            mangija = laas(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "5":
            treeni(mangija, aktiveeritud_altarid)
        elif valik == "6":
            trader_menu(mangija)
        elif valik == "7":
            uus, leitud_artefaktid, aktiveeritud_altarid = fight_boss(mangija, leitud_artefaktid, aktiveeritud_altarid)
            if uus is not None:
                mangija = uus
        elif valik == "8":
            kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "9":
            kuva_stats(mangija)
            pause()
        elif valik == "10":
            while True:
                v = input("Salvestan praegusesse slotti (j) või vali uus (u): ").strip().lower()
                if v in ("j", "u"):
                    break
            if v == "u":
                _vali_profiil("uus")
            salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
            pause()
        elif valik == "11":
            if _vali_profiil("lae") is None:
                print("Laadimine ebaõnnestus.")
                pause()
            else:
                tmp_m, tmp_leitud, tmp_altarid = lae_mang()
                if tmp_m is not None:
                    mangija = tmp_m
                    leitud_artefaktid = tmp_leitud
                    aktiveeritud_altarid = tmp_altarid
                    print("Mäng laetud!")
                else:
                    print("Laadimine ebaõnnestus.")
                pause()
        elif valik == "0":
            print("\nNägemist!")
            break
        else:
            hamster_teade()
            pause()

    return mangija, leitud_artefaktid, aktiveeritud_altarid

if __name__ == "__main__":
    _paranda_world_state()
    mangija, leitud_artefaktid, aktiveeritud_altarid = alusta_mangu()
    pohikaart(mangija, leitud_artefaktid, aktiveeritud_altarid)
