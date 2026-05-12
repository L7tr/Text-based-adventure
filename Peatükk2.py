import random

import Peatükk1 as peatukk1


JUHUSLIKUD_KOHTUMISED = {
    "pohhi": [
        "Puude vahel liigub metsik variolend, aga kaob enne, kui talle päriselt lähened.",
        "Metsast tormab välja marutõbine hunt ja sunnib sind mõõga käepidet haarama.",
    ],
    "louna": [
        "Kõrges rohus sahiseb midagi, mis liigub liiga sihikindlalt, et olla loom.",
        "Maja ümber hiilib luust maskiga rändur, kes põgeneb, kui teda märkad.",
    ],
    "ida": [
        "Kai all sulpsatab miski suurem kui kala ja väiksem kui laev.",
        "Soolases udus komistad rannaröövli otsa, kes lootis lihtsat saaki.",
    ],
    "laas": [
        "Rahvahulga sees riivab sind õlaga taskuvaras, kes tõmbab noa välja liiga kiiresti.",
        "Üks tänavanurk vaikib järsku maha. Midagi kiskjalikku jälgib sind varikatuste alt.",
    ],
    "kirre": [
        "Soomülkast tõuseb mudane olevus, kes kannab endal pooleldi kustunud ruune.",
        "Pilliroo vahelt jälgivad sind druiidide valvekiskjad, enne kui pimedusse kaovad.",
    ],
    "kagu": [
        "Õhk lõhkeb kuumusest ja leegist sööstab välja väiksem tuleolend.",
        "Kõrbenud kivide vahelt tõuseb tulevari, kes tahab kõike enda ümber süüdata.",
    ],
    "edel": [
        "Kõrgel pilvede all möödub sinust tuulevorm, mida silm näeb alles liiga hilja.",
        "Õhusilla serval keerleb õhuvaim, kes ei salli võõraid oma taevas.",
    ],
    "loe": [
        "Katakombi kivides liigub pikk kriipiv heli, nagu veaks keegi metallküüsi mööda seina.",
        "Pimedast käigust tõuseb hauavaht, kes arvab, et sina kuulud samuti maa alla.",
    ],
}

KOHTUMIS_VAENLASED = {
    "pohhi": ("Marutõbine Hunt", 36, 9),
    "louna": ("Luust Rändur", 34, 8),
    "ida": ("Rannaröövel", 40, 10),
    "laas": ("Taskuvari", 32, 9),
    "kirre": ("Mudane Valvur", 46, 11),
    "kagu": ("Väike Tuleolend", 44, 12),
    "edel": ("Õhuvaim", 42, 11),
    "loe": ("Hauavaht", 50, 13),
}


PEATUKK2_FLAGID = {
    "chapter2_intro_seen": False,
    "chapter2_met_vunts": False,
    "chapter2_met_witch": False,
    "chapter2_met_druids": False,
    "chapter2_asked_farlands": False,
    "chapter2_has_farlands_pass": False,
    "chapter2_soul_contract_found": False,
    "chapter2_soul_contract_made": False,
    "chapter2_shadow_met": False,
    "chapter2_earth_trust": False,
    "chapter2_fire_trust": False,
    "chapter2_air_trust": False,
    "chapter2_water_trust": False,
    "chapter2_leaders_alerted": False,
    "chapter2_power_scaled": False,
    "chapter2_original_joukus": 0,
    "chapter2_days_spent": 0,
    "chapter2_energia": None,
    "chapter2_mana": None,
    "chapter2_council_summoned": False,
    "chapter2_council_proven": False,
    "chapter2_has_aethor_mark": False,
    "chapter2_armor": None,
    "chapter2_refused_aethor_mark": False,
    "chapter2_black_market_heat": 0,
    "chapter2_blacksmith_quest_done": False,
    "chapter2_blacksmith_quest_seen": False,
    "chapter2_tension_warning_seen": 0,
    "chapter2_unlocked_recipes": [],
    "chapter2_completed_sidequests": [],
    "chapter2_final_battle_won": False,
    "chapter2_ending_type": None,
    "chapter2_ending_seen": False,
    "chapter2_gateway_ch3": False,
    "chapter2_debug_overlay": False,
    "chapter3_origin": None,
    "chapter3_shadow_rank": 0,
    "chapter3_world_tone": None,
}

AETHORI_VANDEMARK = "Aethori Vandemärk"
AETHORI_TOENDITE_ARV = 3
AJASTUTE_MOOK = "Ajastute Mõõk"

ARMOR_SETID = {
    "Aetherraud Set": {
        "nimi": "Aetherraud Set",
        "hind": 42,
        "kaitse": 4,
        "max_durability": 45,
        "energia_regen": 1,
        "mana_regen": 0,
        "dodge_bonus": 0,
        "trust_penalty": 0,
        "allikas": "blacksmith",
        "eriefekt": "Iga lahingukäik taastab lisaks energiat.",
    },
    "Troonteras Set": {
        "nimi": "Troonteras Set",
        "hind": 86,
        "kaitse": 7,
        "max_durability": 60,
        "energia_regen": 2,
        "mana_regen": 0,
        "dodge_bonus": 0,
        "trust_penalty": 1,
        "allikas": "blacksmith",
        "vajab_mark": True,
        "eriefekt": "Kaitseasend vähendab vastase kahju tugevamalt.",
    },
    "Kroonisulami Set": {
        "nimi": "Kroonisulami Set",
        "hind": 140,
        "kaitse": 10,
        "max_durability": 75,
        "energia_regen": 3,
        "mana_regen": 0,
        "dodge_bonus": -2,
        "trust_penalty": 1,
        "allikas": "blacksmith",
        "vajab_mark": True,
        "eriefekt": "Kui HP langeb madalale, tekib üks kord kriisikaitse.",
    },
    "Varjuhõbe Set": {
        "nimi": "Varjuhõbe Set",
        "hind": 72,
        "kaitse": 5,
        "max_durability": 45,
        "energia_regen": 0,
        "mana_regen": 1,
        "dodge_bonus": 6,
        "trust_penalty": 0,
        "allikas": "must_turg",
        "eriefekt": "Shadow abi maksab vähem manat.",
    },
    "Öömalm Set": {
        "nimi": "Öömalm Set",
        "hind": 105,
        "kaitse": 8,
        "max_durability": 55,
        "energia_regen": 0,
        "mana_regen": 2,
        "dodge_bonus": 0,
        "trust_penalty": 0,
        "allikas": "must_turg",
        "eriefekt": "Mana taastub hästi, energia taastub aeglasemalt.",
    },
    "Katakombiteras Set": {
        "nimi": "Katakombiteras Set",
        "hind": 125,
        "kaitse": 9,
        "max_durability": 50,
        "energia_regen": 1,
        "mana_regen": 1,
        "dodge_bonus": 3,
        "trust_penalty": 0,
        "allikas": "must_turg",
        "eriefekt": "Shadow abi teeb rohkem kahju.",
    },
    "Maavande Set": {
        "nimi": "Maavande Set",
        "hind": 95,
        "kaitse": 8,
        "max_durability": 80,
        "energia_regen": 1,
        "mana_regen": 0,
        "dodge_bonus": -1,
        "trust_penalty": 0,
        "allikas": "elementaal",
        "vajab_flag": "chapter2_earth_trust",
        "eriefekt": "Armor kulub aeglasemalt.",
    },
    "Leegisüda Set": {
        "nimi": "Leegisüda Set",
        "hind": 95,
        "kaitse": 6,
        "max_durability": 55,
        "energia_regen": 1,
        "mana_regen": 1,
        "dodge_bonus": 1,
        "trust_penalty": 0,
        "allikas": "elementaal",
        "vajab_flag": "chapter2_fire_trust",
        "tule_bonus": 4,
        "eriefekt": "Tulerünnak jätab vastase põlema.",
    },
    "Pilvetantsija Set": {
        "nimi": "Pilvetantsija Set",
        "hind": 95,
        "kaitse": 4,
        "max_durability": 45,
        "energia_regen": 0,
        "mana_regen": 1,
        "dodge_bonus": 12,
        "trust_penalty": 0,
        "allikas": "elementaal",
        "vajab_flag": "chapter2_air_trust",
        "eriefekt": "Põiklemine maksab vähem energiat.",
    },
    "Sügavvee Set": {
        "nimi": "Sügavvee Set",
        "hind": 95,
        "kaitse": 5,
        "max_durability": 55,
        "energia_regen": 0,
        "mana_regen": 3,
        "dodge_bonus": 4,
        "trust_penalty": 0,
        "allikas": "elementaal",
        "vajab_flag": "chapter2_water_trust",
        "eriefekt": "Vesi taastab rohkem manat ja natuke elu.",
    },
}

ARMOR_SETID.update({
    "Adamantite Set": {
        "nimi": "Adamantite Set",
        "hind": 155,
        "kaitse": 11,
        "max_durability": 85,
        "energia_regen": 2,
        "mana_regen": 0,
        "dodge_bonus": -1,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Adamantite Set",
        "materjalid": ["Adamantite Ore", "Aether Ore"],
        "eriefekt": "Väga vastupidav set, mis sobib pikaks lahinguks.",
    },
    "Aquarium Set": {
        "nimi": "Aquarium Set",
        "hind": 130,
        "kaitse": 6,
        "max_durability": 62,
        "energia_regen": 0,
        "mana_regen": 3,
        "dodge_bonus": 5,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Aquarium Set",
        "materjalid": ["Aquarium Pearl", "Soolakivi"],
        "eriefekt": "Vee rünnakud taastavad rohkem ressursse.",
    },
    "Banglum Set": {
        "nimi": "Banglum Set",
        "hind": 118,
        "kaitse": 7,
        "max_durability": 58,
        "energia_regen": 1,
        "mana_regen": 0,
        "dodge_bonus": 2,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Banglum Set",
        "materjalid": ["Banglum Chunk", "Tuleraud"],
        "eriefekt": "Tugev löök teeb rohkem kahju.",
    },
    "Carmot Set": {
        "nimi": "Carmot Set",
        "hind": 145,
        "kaitse": 7,
        "max_durability": 65,
        "energia_regen": 1,
        "mana_regen": 2,
        "dodge_bonus": 3,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Carmot Set",
        "materjalid": ["Carmot Dust", "Metsajuur"],
        "eriefekt": "Puhkus ja meditatsioon annavad rohkem tagasi.",
    },
    "Kyber Set": {
        "nimi": "Kyber Set",
        "hind": 150,
        "kaitse": 8,
        "max_durability": 64,
        "energia_regen": 0,
        "mana_regen": 3,
        "dodge_bonus": 1,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Kyber Set",
        "materjalid": ["Kyber Crystal", "Varjulapp"],
        "eriefekt": "Combo rünnakud maksavad vähem manat.",
    },
    "Mythril Set": {
        "nimi": "Mythril Set",
        "hind": 175,
        "kaitse": 9,
        "max_durability": 70,
        "energia_regen": 2,
        "mana_regen": 2,
        "dodge_bonus": 4,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Mythril Set",
        "materjalid": ["Mythril Ore", "Tuleraud"],
        "eriefekt": "Tasakaalustatud legendaarne metall.",
    },
    "Orichalcum Set": {
        "nimi": "Orichalcum Set",
        "hind": 185,
        "kaitse": 10,
        "max_durability": 72,
        "energia_regen": 2,
        "mana_regen": 1,
        "dodge_bonus": 6,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Orichalcum Set",
        "materjalid": ["Orichalcum Ore", "Õhukas Kristall"],
        "eriefekt": "Põiklemine ja kaitse töötavad koos paremini.",
    },
    "Stormyx Set": {
        "nimi": "Stormyx Set",
        "hind": 210,
        "kaitse": 9,
        "max_durability": 68,
        "energia_regen": 3,
        "mana_regen": 2,
        "dodge_bonus": 8,
        "trust_penalty": 0,
        "allikas": "recipe",
        "vajab_recipe": "Stormyx Set",
        "materjalid": ["Stormyx Shard", "Katakombi Kild"],
        "eriefekt": "Õhu rünnakud ja dodge muutuvad tugevamaks.",
    },
    "Metallurgium Set": {
        "nimi": "Metallurgium Set",
        "hind": 320,
        "kaitse": 13,
        "max_durability": 95,
        "energia_regen": 2,
        "mana_regen": 2,
        "dodge_bonus": 5,
        "trust_penalty": 1,
        "allikas": "must_turg",
        "vajab_flag": "chapter2_soul_contract_made",
        "materjalid": ["Stormyx Set", "Mythril Set", "Orichalcum Set"],
        "eriefekt": "Musta turu maag sulatab kolm legendaarset setti üheks keelatud Metallurgiumiks.",
    },
})

MINE_MATERJALID = [
    ("Aether Ore", 12),
    ("Adamantite Ore", 38),
    ("Aquarium Pearl", 32),
    ("Banglum Chunk", 28),
    ("Carmot Dust", 34),
    ("Kyber Crystal", 36),
    ("Mythril Ore", 48),
    ("Orichalcum Ore", 54),
    ("Stormyx Shard", 70),
]

ASPEKTID = {
    "maa": "Maa Aspekt",
    "tuli": "Tule Aspekt",
    "vesi": "Vee Aspekt",
    "ohk": "Õhu Aspekt",
}

ALKEEMIA_MATERJALID = {
    "Alkeemiline Sool": 18,
    "Varjutint": 24,
}

CH2_DROPID = {
    "pohhi": [("Hundi Karv", 0.60), ("Metsajuur", 0.38), ("Pruun Vaigukild", 0.16)],
    "louna": [("Luumärk", 0.50), ("Kuivanud Ruunipael", 0.28), ("Tolmune Talisman", 0.12)],
    "ida": [("Märg Kest", 0.55), ("Soolakivi", 0.35), ("Kai Nael", 0.18)],
    "laas": [("Varjulapp", 0.52), ("Varjuline Taskukell", 0.18), ("Taskuvõti", 0.20)],
    "kirre": [("Soomuda Süda", 0.48), ("Maa Ruunikild", 0.38), ("Rabajuur", 0.22)],
    "kagu": [("Leegituhk", 0.50), ("Põlenud Südamik", 0.24), ("Tuleraud", 0.20)],
    "edel": [("Tuule Sulg", 0.50), ("Õhukas Kristall", 0.24), ("Pilvekiud", 0.18)],
    "loe": [("Katakombi Kild", 0.52), ("Hauapitseri Tolm", 0.30), ("Varioks", 0.16)],
}

CH2_MUUGI_HINNAD = {
    "Hundi Karv": 6,
    "Metsajuur": 4,
    "Pruun Vaigukild": 9,
    "Luumärk": 7,
    "Kuivanud Ruunipael": 10,
    "Tolmune Talisman": 13,
    "Märg Kest": 7,
    "Soolakivi": 5,
    "Kai Nael": 8,
    "Varjuline Taskukell": 16,
    "Varjulapp": 6,
    "Taskuvõti": 9,
    "Soomuda Süda": 12,
    "Maa Ruunikild": 14,
    "Rabajuur": 10,
    "Leegituhk": 11,
    "Põlenud Südamik": 17,
    "Tuleraud": 12,
    "Tuule Sulg": 11,
    "Õhukas Kristall": 17,
    "Pilvekiud": 12,
    "Katakombi Kild": 12,
    "Hauapitseri Tolm": 14,
    "Varioks": 15,
    "Alkeemiline Sool": 8,
    "Varjutint": 11,
    "Energia Tõmmis": 9,
    "Mana Kristall": 10,
    "Selge Vesi": 8,
    "Suur Energia Potion": 16,
    "Suur Mana Potion": 17,
    "Tormisegu": 13,
    "Varjutilk": 14,
}
for _armor_nimi, _armor in ARMOR_SETID.items():
    CH2_MUUGI_HINNAD[_armor_nimi] = max(1, _armor["hind"] // 2)
for _materjal_nimi, _materjal_hind in MINE_MATERJALID:
    CH2_MUUGI_HINNAD[_materjal_nimi] = max(1, _materjal_hind // 2)

CH2_OSTUD = [
    {"nimi": "Ribaside", "hind": 7, "item": {"nimi": "Ribaside", "hp_restore": 30}},
    {"nimi": "Kuivtoit", "hind": 9, "item": {"nimi": "Kuivtoit", "hp_restore": 35}},
    {"nimi": "Väike Elu Potion", "hind": 16, "item": {"nimi": "Väike Elu Potion", "hp_restore": 70}},
    {"nimi": "Ränduri Tõrvik", "hind": 12, "item": {"nimi": "Ränduri Tõrvik"}},
    {"nimi": "Soolaringi Kriit", "hind": 14, "item": {"nimi": "Soolaringi Kriit"}},
    {"nimi": "Alkeemiline Sool", "hind": 18, "item": {"nimi": "Alkeemiline Sool"}},
    {"nimi": "Tugev Elu Potion", "hind": 29, "item": {"nimi": "Tugev Elu Potion", "hp_restore": 120}},
    {"nimi": "Energia Tõmmis", "hind": 18, "item": {"nimi": "Energia Tõmmis", "energia_restore": 20}},
    {"nimi": "Mana Kristall", "hind": 20, "item": {"nimi": "Mana Kristall", "mana_restore": 18}},
    {"nimi": "Selge Vesi", "hind": 16, "item": {"nimi": "Selge Vesi", "energia_restore": 10, "mana_restore": 10}},
    {"nimi": "Suur Energia Potion", "hind": 32, "item": {"nimi": "Suur Energia Potion", "energia_restore": 38}},
    {"nimi": "Suur Mana Potion", "hind": 34, "item": {"nimi": "Suur Mana Potion", "mana_restore": 36}},
]

MUSTA_TURU_OSTUD = [
    {"nimi": "Varjutint", "hind": 22, "item": {"nimi": "Varjutint"}},
    {"nimi": "Alkeemiline Sool", "hind": 20, "item": {"nimi": "Alkeemiline Sool"}},
    {"nimi": "Suitsukapsel", "hind": 14, "item": {"nimi": "Suitsukapsel", "hp_restore": 20}},
    {"nimi": "Keelatud Segu", "hind": 26, "item": {"nimi": "Keelatud Segu", "hp_restore": 90}},
    {"nimi": "Varjukangas", "hind": 17, "item": {"nimi": "Varjukangas"}},
    {"nimi": "Musta Soola Kotike", "hind": 19, "item": {"nimi": "Musta Soola Kotike"}},
    {"nimi": "Tormisegu", "hind": 25, "item": {"nimi": "Tormisegu", "energia_restore": 34, "self_damage": 8}},
    {"nimi": "Varjutilk", "hind": 27, "item": {"nimi": "Varjutilk", "mana_restore": 34, "self_damage": 6}},
]

CH2_VASK_TASU = {
    "pohhi": (4, 10),
    "louna": (4, 10),
    "ida": (5, 12),
    "laas": (5, 11),
    "kirre": (7, 15),
    "kagu": (8, 16),
    "edel": (8, 16),
    "loe": (9, 18),
}

MITTE_MUUDAVAD = {
    "Ajastute Mõõk",
    "Kadunud Ajastu Kroon",
    "Kadunud Riikide Foliant",
    "Unustatud päevik",
    "Maagiline lamp",
    "Tormikompass",
    "Farlandsi läbisõiduluba",
    "Maa Aspekt",
    "Tule Aspekt",
    "Vee Aspekt",
    "Õhu Aspekt",
}


def chapter2_flags(mangija):
    flags = mangija.setdefault("special_flags", {})
    for key, value in PEATUKK2_FLAGID.items():
        flags.setdefault(key, value)
    flags.setdefault("chapter2_current_location", "Aethor")
    if not isinstance(flags.get("chapter2_unlocked_recipes"), list):
        flags["chapter2_unlocked_recipes"] = []
    if not isinstance(flags.get("chapter2_completed_sidequests"), list):
        flags["chapter2_completed_sidequests"] = []
    uuenda_ressursid(mangija)
    return flags


def arvuta_max_energia(mangija):
    stats = mangija["stats"]
    return 30 + stats["fuusiline_level"] * 2


def arvuta_max_mana(mangija):
    levelid = mangija["stats"]["elementaalne_level"]
    keskmine = sum(levelid.get(el, 1) for el in peatukk1.ELEMENDID) // 4
    return 25 + keskmine * 3


def uuenda_ressursid(mangija):
    flags = mangija.setdefault("special_flags", {})
    max_energia = arvuta_max_energia(mangija)
    max_mana = arvuta_max_mana(mangija)

    if flags.get("chapter2_energia") is None:
        flags["chapter2_energia"] = max_energia
    if flags.get("chapter2_mana") is None:
        flags["chapter2_mana"] = max_mana

    flags["chapter2_energia"] = max(0, min(int(flags["chapter2_energia"]), max_energia))
    flags["chapter2_mana"] = max(0, min(int(flags["chapter2_mana"]), max_mana))
    return flags


def kuva_ressursid(mangija):
    flags = uuenda_ressursid(mangija)
    print(f"Energia: {flags['chapter2_energia']}/{arvuta_max_energia(mangija)}")
    print(f"Mana   : {flags['chapter2_mana']}/{arvuta_max_mana(mangija)}")


def aethori_pinge(flags):
    paevad = int(flags.get("chapter2_days_spent", 0))
    heat = int(flags.get("chapter2_black_market_heat", 0))
    if flags.get("chapter2_has_aethor_mark", False):
        paevad += 4
        heat += 2
    if paevad >= 10 or heat >= 5:
        return "ohtlik"
    if paevad >= 6 or heat >= 3 or flags.get("chapter2_leaders_alerted", False):
        return "kasvav"
    return "madal"


def kuva_aethori_pinge(mangija):
    flags = chapter2_flags(mangija)
    print(f"Aethori pinge: {aethori_pinge(flags)}")


def uuenda_pinge_sundmus(mangija):
    flags = chapter2_flags(mangija)
    paevad = int(flags.get("chapter2_days_spent", 0))
    viimane = int(flags.get("chapter2_tension_warning_seen", 0))
    if paevad >= 10 and viimane < 10:
        flags["chapter2_tension_warning_seen"] = 10
        peatukk1.clear()
        peatukk1.section_title("AETHOR PRAGUNEB", peatukk1.ANSI_RED)
        print("Linnas räägitakse vaiksemalt kui varem.")
        print("Valvurid seisavad kauem samadel nurkadel ja inimesed väldivad vanu nimesid.")
        peatukk1.pause()
    elif paevad >= 6 and viimane < 6:
        flags["chapter2_tension_warning_seen"] = 6
        peatukk1.clear()
        peatukk1.section_title("AETHORI PINGE", peatukk1.ANSI_YELLOW)
        print("Aethor ei ole enam nii rahulik kui saabudes.")
        print("Iga päev enne langust kannab rohkem raskust.")
        peatukk1.pause()


def lisa_musta_turu_heat(mangija, kogus=1):
    flags = chapter2_flags(mangija)
    flags["chapter2_black_market_heat"] += kogus
    if flags["chapter2_black_market_heat"] in (3, 5):
        print("Musta turu liikumine jätab jälgi. Lossi kõrvad liiguvad lähemale.")


def ava_retsept(mangija, retsept):
    flags = chapter2_flags(mangija)
    if retsept not in flags["chapter2_unlocked_recipes"]:
        flags["chapter2_unlocked_recipes"].append(retsept)
        print(f"Uus armor retsept avatud: {retsept}")


def retsept_avatud(mangija, retsept):
    return retsept in chapter2_flags(mangija)["chapter2_unlocked_recipes"]


def on_ajastute_mook(leitud_artefaktid):
    return AJASTUTE_MOOK in leitud_artefaktid or "Kadunud Ajastu Kroon" in leitud_artefaktid


def ajastute_mooga_hind(mangija):
    return 12, 16


def piirkonna_xp_kordaja(koht, element=None):
    if koht == "Vuntsi maja":
        return 1.5
    if element == "maa" and koht == "Soomaa":
        return 1.25
    if element == "tuli" and koht == "Inferno":
        return 1.25
    if element == "õhk" and koht == "Õhuriik":
        return 1.25
    if element == "Ćµhk" and koht == "Ć•huriik":
        return 1.25
    if element == "vesi" and koht == "Farlands":
        return 1.25
    return 1.0


def taasta_ressursse(mangija, energia=0, mana=0):
    flags = uuenda_ressursid(mangija)
    flags["chapter2_energia"] = min(arvuta_max_energia(mangija), flags["chapter2_energia"] + energia)
    flags["chapter2_mana"] = min(arvuta_max_mana(mangija), flags["chapter2_mana"] + mana)


def kuluta_ressursse(mangija, energia=0, mana=0):
    flags = uuenda_ressursid(mangija)
    if flags["chapter2_energia"] < energia or flags["chapter2_mana"] < mana:
        print("Sul pole selleks piisavalt energiat või manat.")
        return False
    flags["chapter2_energia"] -= energia
    flags["chapter2_mana"] -= mana
    return True


def moodu_paev(mangija, mitu=1):
    flags = chapter2_flags(mangija)
    flags["chapter2_days_spent"] += mitu
    uuenda_pinge_sundmus(mangija)


def loo_armor(nimi):
    andmed = ARMOR_SETID[nimi]
    armor = dict(andmed)
    armor["durability"] = armor["max_durability"]
    return armor


def aktiivne_armor(mangija):
    flags = mangija.setdefault("special_flags", {})
    armor = flags.get("chapter2_armor")
    if not isinstance(armor, dict):
        return None
    nimi = armor.get("nimi")
    if nimi not in ARMOR_SETID:
        return None
    vaikimisi = loo_armor(nimi)
    vaikimisi.update(armor)
    vaikimisi["durability"] = max(0, min(int(vaikimisi.get("durability", 0)), vaikimisi["max_durability"]))
    flags["chapter2_armor"] = vaikimisi
    return vaikimisi


def armor_kaitse(mangija):
    armor = aktiivne_armor(mangija)
    if not armor:
        return 0
    if armor["durability"] <= 0:
        return max(0, armor["kaitse"] // 2)
    return armor["kaitse"]


def armor_bonus(mangija, key):
    armor = aktiivne_armor(mangija)
    if not armor:
        return 0
    return int(armor.get(key, 0))


def kannab_armorit(mangija, nimi):
    armor = aktiivne_armor(mangija)
    return bool(armor and armor.get("nimi") == nimi)


def kuluta_armorit(mangija, kogus=1):
    armor = aktiivne_armor(mangija)
    if not armor:
        return
    if armor["nimi"] == "Maavande Set":
        kogus = max(0, kogus - 1)
    armor["durability"] = max(0, armor["durability"] - kogus)
    if armor["durability"] == 0:
        print(f"{armor['nimi']} on täiesti mõranenud. Kaitse töötab ainult poole jõuga.")


def varusta_armor(mangija, nimi):
    flags = chapter2_flags(mangija)
    vana = aktiivne_armor(mangija)
    if vana:
        lisa_inventari_koopia(mangija, vana)
        print(f"Vana armor läks inventari: {vana['nimi']}")
    flags["chapter2_armor"] = loo_armor(nimi)
    print(f"Varustasid: {nimi}")


def armor_lubatud(mangija, nimi):
    armor = ARMOR_SETID[nimi]
    if armor.get("vajab_mark") and not chapter2_flags(mangija).get("chapter2_has_aethor_mark", False):
        return False
    if armor.get("vajab_recipe") and not retsept_avatud(mangija, armor["vajab_recipe"]):
        return False
    vajab = armor.get("vajab_flag")
    if not vajab:
        return True
    return bool(chapter2_flags(mangija).get(vajab, False))


def kuva_armor(mangija):
    armor = aktiivne_armor(mangija)
    if not armor:
        print("Armor: puudub")
        return
    print(f"Armor: {armor['nimi']} ({armor['durability']}/{armor['max_durability']} durability)")
    print(f"Kaitse: {armor['kaitse']} | energia regen +{armor.get('energia_regen', 0)} | mana regen +{armor.get('mana_regen', 0)} | dodge +{armor.get('dodge_bonus', 0)}")


def armor_poemenyy(mangija, allikas, pealkiri):
    while True:
        peatukk1.clear()
        peatukk1.section_title(pealkiri, peatukk1.ANSI_YELLOW)
        kuva_saldo(mangija)
        kuva_armor(mangija)
        print()
        valikud = [
            armor for armor in ARMOR_SETID.values()
            if armor["allikas"] == allikas and armor_lubatud(mangija, armor["nimi"])
        ]
        if not valikud:
            print("Praegu pole siin sulle sobivat setti.")
        for i, armor in enumerate(valikud, start=1):
            print(f"{i} - {armor['nimi']} - {armor['hind']} vaskdablooni")
            print(f"    kaitse {armor['kaitse']}, durability {armor['max_durability']}, energia +{armor.get('energia_regen', 0)}, mana +{armor.get('mana_regen', 0)}, dodge +{armor.get('dodge_bonus', 0)}")
            if armor.get("materjalid"):
                print(f"    materjalid: {', '.join(armor['materjalid'])}")
            if armor.get("trust_penalty"):
                print("    Aethori ametlik metall: elementaalide usaldus muutub raskemaks.")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "0":
            return
        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale valik.")
            peatukk1.pause()
            continue
        if not (0 <= idx < len(valikud)):
            print("Vale valik.")
            peatukk1.pause()
            continue
        armor = valikud[idx]
        puuduvad = [nimi for nimi in armor.get("materjalid", []) if not peatukk1.has_inventar(mangija, nimi)]
        if puuduvad:
            print("Sul puuduvad materjalid:")
            for nimi in puuduvad:
                print(f"  - {nimi}")
            peatukk1.pause()
            continue
        if mangija.get("kaart") is None or not peatukk1.kaart_eemalda_vask(mangija["kaart"], armor["hind"]):
            print("Sul pole piisavalt raha.")
            peatukk1.pause()
            continue
        for nimi in armor.get("materjalid", []):
            for ese in list(mangija["inventar"]):
                if ese["nimi"] == nimi:
                    mangija["inventar"].remove(ese)
                    break
        varusta_armor(mangija, armor["nimi"])
        if allikas == "must_turg":
            lisa_musta_turu_heat(mangija, 2)
        print(f"Uus saldo: {peatukk1.kaart_saldo_str(mangija['kaart'])}")
        peatukk1.pause()


def paranda_armorit(mangija):
    armor = aktiivne_armor(mangija)
    if not armor:
        print("Sul pole armorit, mida parandada.")
        peatukk1.pause()
        return
    puudu = armor["max_durability"] - armor["durability"]
    if puudu <= 0:
        print("Armor on juba täiskorras.")
        peatukk1.pause()
        return
    hind = max(2, puudu * 2)
    print(f"Parandamine maksab {hind} vaskdablooni.")
    if mangija.get("kaart") is None or not peatukk1.kaart_eemalda_vask(mangija["kaart"], hind):
        print("Sul pole piisavalt raha.")
        peatukk1.pause()
        return
    armor["durability"] = armor["max_durability"]
    print(f"{armor['nimi']} on jälle täiskorras.")
    print(f"Uus saldo: {peatukk1.kaart_saldo_str(mangija['kaart'])}")
    peatukk1.pause()


def myy_aktiivne_armor(mangija):
    flags = chapter2_flags(mangija)
    armor = aktiivne_armor(mangija)
    if not armor:
        print("Sul pole aktiivset armorit müüa.")
        peatukk1.pause()
        return
    baas = armor["hind"] // 2
    hind = max(1, int(baas * armor["durability"] / max(1, armor["max_durability"])))
    flags["chapter2_armor"] = None
    lisa_vask_tasu(mangija, hind)
    print(f"Müüsid aktiivse armori: {armor['nimi']}")
    peatukk1.pause()


def vota_armor_seljast(mangija):
    flags = chapter2_flags(mangija)
    armor = aktiivne_armor(mangija)
    if not armor:
        print("Sul pole aktiivset armorit seljas.")
        peatukk1.pause()
        return
    lisa_inventari_koopia(mangija, armor)
    flags["chapter2_armor"] = None
    print(f"Võtsid seljast: {armor['nimi']}")
    peatukk1.pause()


def varusta_inventarist_armor(mangija):
    armorid = [ese for ese in mangija["inventar"] if ese.get("nimi") in ARMOR_SETID]
    if not armorid:
        print("Inventaris pole armor setti.")
        peatukk1.pause()
        return

    while True:
        peatukk1.clear()
        peatukk1.section_title("VARUSTA ARMOR", peatukk1.ANSI_YELLOW)
        for i, armor in enumerate(armorid, start=1):
            dur = armor.get("durability", ARMOR_SETID[armor["nimi"]]["max_durability"])
            max_dur = armor.get("max_durability", ARMOR_SETID[armor["nimi"]]["max_durability"])
            print(f"{i} - {armor['nimi']} ({dur}/{max_dur})")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()
        if valik == "0":
            return
        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale valik.")
            peatukk1.pause()
            continue
        if not (0 <= idx < len(armorid)):
            print("Vale valik.")
            peatukk1.pause()
            continue
        armor = armorid[idx]
        mangija["inventar"].remove(armor)
        vana = aktiivne_armor(mangija)
        if vana:
            lisa_inventari_koopia(mangija, vana)
        flags = chapter2_flags(mangija)
        uus = loo_armor(armor["nimi"])
        uus.update(armor)
        flags["chapter2_armor"] = uus
        print(f"Varustasid: {armor['nimi']}")
        peatukk1.pause()
        return


def blacksmithi_quest(mangija):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("SEPA VÕLG", peatukk1.ANSI_YELLOW)
    if flags["chapter2_blacksmith_quest_done"]:
        print("Sepp noogutab sulle. Tema võlg on tasutud ja sinu nimi seisab tema paremal riiulil.")
        peatukk1.pause()
        return

    flags["chapter2_blacksmith_quest_seen"] = True
    vajalikud = ["Tuleraud", "Maa Ruunikild", "Katakombi Kild", "Varjukangas"]
    print("Sepp tahab teha midagi, mida Aethori ametlikud tellimused enam ei luba.")
    print("Too talle need materjalid:")
    for nimi in vajalikud:
        print(f"  - {nimi}: {jah_ei(peatukk1.has_inventar(mangija, nimi))}")
    print()
    if not all(peatukk1.has_inventar(mangija, nimi) for nimi in vajalikud):
        print("Kõik pole veel koos.")
        peatukk1.pause()
        return

    valik = input("Annad materjalid sepale? (j/e): ").strip().lower()
    if valik != "j":
        print("Sepp ei kiirusta. Sellist metalli ei lööda rutuga.")
        peatukk1.pause()
        return

    for nimi in vajalikud:
        for ese in list(mangija["inventar"]):
            if ese["nimi"] == nimi:
                mangija["inventar"].remove(ese)
                break
    flags["chapter2_blacksmith_quest_done"] = True
    varusta_armor(mangija, "Aetherraud Set")
    armor = aktiivne_armor(mangija)
    if armor:
        armor["max_durability"] += 15
        armor["durability"] = armor["max_durability"]
        armor["kaitse"] += 2
    print("Sepp sepistab sulle tugevdatud Aetherraud Seti.")
    print("See ei ole kõige uhkem metall, aga see ei murene kergesti.")
    peatukk1.pause()


def puhka(mangija, koht="Aethor", turvaline=True):
    flags = uuenda_ressursid(mangija)
    energia_taastus = max(1, int(arvuta_max_energia(mangija) * (0.9 if turvaline else 0.55)))
    mana_taastus = max(1, int(arvuta_max_mana(mangija) * (0.9 if turvaline else 0.55)))
    hp_taastus = 45 if turvaline else 25

    peatukk1.clear()
    peatukk1.section_title("PUHKUS", peatukk1.ANSI_CYAN)
    print(f"Puhkad kohas: {koht}.")
    taasta_ressursse(mangija, energia_taastus, mana_taastus)
    mangija["elud"] += hp_taastus
    moodu_paev(mangija)
    print(f"Taastad {hp_taastus} elu.")
    print(f"Energia taastub {flags['chapter2_energia']}/{arvuta_max_energia(mangija)} peale.")
    print(f"Mana taastub {flags['chapter2_mana']}/{arvuta_max_mana(mangija)} peale.")
    print(f"Vanas maailmas veedetud päevi: {flags['chapter2_days_spent']}")
    kuva_aethori_pinge(mangija)
    peatukk1.pause()


def rahulik_meditatsioon(mangija, koht="Aethor"):
    peatukk1.clear()
    peatukk1.section_title("MEDITATSIOON", peatukk1.ANSI_BLUE)
    print(f"Istud maha ja lased {koht} müral aeglaselt kaugemaks vajuda.")
    mana_taastus = max(8, int(arvuta_max_mana(mangija) * 0.45))
    energia_taastus = max(4, int(arvuta_max_energia(mangija) * 0.2))
    taasta_ressursse(mangija, energia=energia_taastus, mana=mana_taastus)
    moodu_paev(mangija)
    print(f"Taastad {energia_taastus} energiat ja {mana_taastus} manat.")
    kuva_ressursid(mangija)
    print(f"Vanas maailmas veedetud päevi: {chapter2_flags(mangija)['chapter2_days_spent']}")
    kuva_aethori_pinge(mangija)
    peatukk1.pause()


def treeni_peatukk2(mangija, aktiveeritud_altarid, tasuta=False, xp_kordaja=1.0, koht="Aethor"):
    while True:
        peatukk1.clear()
        stats = mangija["stats"]
        peatukk1.print_status_card(mangija, "TREENIMINE")
        kuva_ressursid(mangija)
        print()
        if tasuta:
            print("Vuntsi juures treenimine ei kuluta energiat ega manat.")
            print(f"XP kordaja: x{xp_kordaja}")
        else:
            print("Füüsiline treening kulutab 12 energiat.")
            print("Elementaalne meditatsioon kulutab 10 manat.")
            print(f"XP kordaja: x{xp_kordaja}")
        print()
        print("1 - Füüsiline treening")
        print(peatukk1.colorize("--- Elementaalne meditatsioon ---", peatukk1.ANSI_BLUE, bold=True))
        for i, el in enumerate(peatukk1.ELEMENDID, start=2):
            lv = stats["elementaalne_level"][el]
            xp = stats["elementaalne_xp"][el]
            vajab = peatukk1.xp_vajadus_leveliks(lv)
            saadav = peatukk1.colorize("jah", peatukk1.ANSI_GREEN, bold=True) if el in aktiveeritud_altarid else peatukk1.colorize("altar aktiveerimata", peatukk1.ANSI_RED)
            print(f"{i} - {el.capitalize()} meditatsioon [{saadav}] Level {lv} ({xp}/{vajab} XP)")
        print("6 - Rahulik meditatsioon")
        print("7 - Puhka")
        print("8 - Tagasi")

        valik = input("\nVali: ").strip()

        if valik == "1":
            if not tasuta and not kuluta_ressursse(mangija, energia=12):
                peatukk1.pause()
                continue
            lv = stats["fuusiline_level"]
            print(f"\n{peatukk1._vali_kirjeldus(peatukk1.FUUSILINE_KIRJELDUSED, lv)}")
            oli_level = lv
            tegelik_kordaja = xp_kordaja
            xp = int(peatukk1.FUUSILINE_XP * tegelik_kordaja)
            print(f"XP kordaja selles kohas: x{tegelik_kordaja}")
            tuli_levelup = peatukk1.lisa_xp(stats, "fuusiline", xp)
            if tuli_levelup and stats["fuusiline_level"] > oli_level:
                peatukk1.fuusiline_levelup_efekt(mangija, stats["fuusiline_level"])
            moodu_paev(mangija)
            peatukk1.pause()

        elif valik in ("2", "3", "4", "5"):
            el = peatukk1.ELEMENDID[int(valik) - 2]
            if el not in aktiveeritud_altarid:
                print(f"\n{el.capitalize()} altar pole veel aktiveeritud.")
                peatukk1.pause()
                continue
            if not tasuta and not kuluta_ressursse(mangija, mana=10):
                peatukk1.pause()
                continue
            lv = stats["elementaalne_level"][el]
            print(f"\n{peatukk1._vali_kirjeldus(peatukk1.ELEMENTAALNE_KIRJELDUSED[el], lv)}")
            oli_level = lv
            tegelik_kordaja = xp_kordaja * piirkonna_xp_kordaja(koht, el)
            xp = int(peatukk1.ELEMENTAALNE_XP * tegelik_kordaja)
            print(f"XP kordaja selles kohas: x{tegelik_kordaja}")
            tuli_levelup = peatukk1.lisa_xp(stats, el, xp, aktiveeritud_altarid)
            if tuli_levelup and stats["elementaalne_level"][el] > oli_level:
                peatukk1.elementaalne_levelup_efekt(mangija, el, stats["elementaalne_level"][el])
            taasta_ressursse(mangija, mana=4 if tasuta else 2)
            moodu_paev(mangija)
            peatukk1.pause()

        elif valik == "6":
            rahulik_meditatsioon(mangija, koht=koht)

        elif valik == "7":
            puhka(mangija, koht=koht, turvaline=True)

        elif valik == "8":
            return mangija

        else:
            print("Vale valik.")
            peatukk1.pause()


def maara_asukoht(mangija, nimi):
    chapter2_flags(mangija)["chapter2_current_location"] = nimi


def leia_asukoht(mangija):
    return chapter2_flags(mangija).get("chapter2_current_location", "Aethor")


def lisa_inventari_koopia(mangija, ese):
    mangija["inventar"].append(dict(ese))


def lisa_drop(mangija, nimi):
    lisa_inventari_koopia(mangija, {"nimi": nimi})


def lisa_vask_tasu(mangija, kogus):
    if mangija.get("kaart") is None:
        print(f"Leiad {kogus} vaskdablooni väärtuses saaki, aga ilma kaardita seda arvele ei kanta.")
        return
    peatukk1.kaart_lisa_vask(mangija["kaart"], kogus)
    print(f"Saad tasuks {kogus} vaskdablooni. Uus saldo: {peatukk1.kaart_saldo_str(mangija['kaart'])}")


def anna_lahingu_dropid(mangija, piirkond):
    vaikimisi = (5, 12)
    miinimum, maksimum = CH2_VASK_TASU.get(piirkond, vaikimisi)
    vask = random.randint(miinimum, maksimum)
    lisa_vask_tasu(mangija, vask)

    leitud_drop = False
    for nimi, voimalus in CH2_DROPID.get(piirkond, []):
        if random.random() <= voimalus:
            lisa_drop(mangija, nimi)
            print(f"Leidsid pärast võitlust eseme: {nimi}")
            leitud_drop = True
            if random.random() > 0.22:
                break
    if not leitud_drop:
        print("Seekord erilist eset ei langenud.")


def myygiks_sobivad_esemed(mangija):
    esemed = []
    for ese in mangija["inventar"]:
        nimi = ese["nimi"]
        if nimi in MITTE_MUUDAVAD:
            continue
        if nimi in ("Kuldne Dabloon", "Hõbedane Dabloon", "Vask Dabloon"):
            continue
        esemed.append(ese)
    return esemed


def ese_muugihind(nimi):
    return CH2_MUUGI_HINNAD.get(nimi, peatukk1.ESEMETE_HINNAD.get(nimi, 3))


def kuva_saldo(mangija):
    if mangija.get("kaart") is None:
        print("Saldo: puudub pangakaart")
        return
    print(f"Saldo: {peatukk1.kaart_saldo_str(mangija['kaart'])}")


def osta_poe_nimekirjast(mangija, ostud, pealkiri):
    while True:
        peatukk1.clear()
        peatukk1.section_title(pealkiri, peatukk1.ANSI_YELLOW)
        kuva_saldo(mangija)
        print()
        print("Mida sügavamale Aethori varjatud kihtidesse lähed, seda olulisemaks muutuvad varud.")
        print()
        for i, kaup in enumerate(ostud, start=1):
            lisa = []
            if "hp_restore" in kaup["item"]:
                lisa.append(f"+{kaup['item']['hp_restore']} HP")
            if "energia_restore" in kaup["item"]:
                lisa.append(f"+{kaup['item']['energia_restore']} energia")
            if "mana_restore" in kaup["item"]:
                lisa.append(f"+{kaup['item']['mana_restore']} mana")
            if "self_damage" in kaup["item"]:
                lisa.append(f"-{kaup['item']['self_damage']} HP risk")
            kirjeldus = f" ({', '.join(lisa)})" if lisa else ""
            print(f"{i} - {kaup['nimi']}{kirjeldus} - {kaup['hind']} vaskdablooni")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "0":
            return

        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale valik.")
            peatukk1.pause()
            continue

        if not (0 <= idx < len(ostud)):
            print("Vale valik.")
            peatukk1.pause()
            continue

        kaup = ostud[idx]
        if mangija.get("kaart") is None:
            print("Sul pole pangakaarti.")
            peatukk1.pause()
            continue
        if not peatukk1.kaart_eemalda_vask(mangija["kaart"], kaup["hind"]):
            print("Sul pole piisavalt raha.")
            peatukk1.pause()
            continue

        lisa_inventari_koopia(mangija, kaup["item"])
        print(f"Ostsid: {kaup['nimi']}")
        if "MUST TURG" in pealkiri:
            lisa_musta_turu_heat(mangija)
        print(f"Uus saldo: {peatukk1.kaart_saldo_str(mangija['kaart'])}")
        peatukk1.pause()


def muugi_menuu(mangija, pealkiri="MÜÜ ESE"):
    while True:
        myydavad = myygiks_sobivad_esemed(mangija)
        peatukk1.clear()
        peatukk1.section_title(pealkiri, peatukk1.ANSI_GREEN)
        kuva_saldo(mangija)
        print()

        if not myydavad:
            print("Sul pole praegu midagi müüa.")
            peatukk1.pause()
            return

        loendur = {}
        for ese in myydavad:
            nimi = ese["nimi"]
            loendur[nimi] = loendur.get(nimi, 0) + 1

        nimed = list(loendur.keys())
        for i, nimi in enumerate(nimed, start=1):
            print(f"{i} - {nimi} x{loendur[nimi]} - {ese_muugihind(nimi)} vaskdablooni")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "0":
            return

        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale valik.")
            peatukk1.pause()
            continue

        if not (0 <= idx < len(nimed)):
            print("Vale valik.")
            peatukk1.pause()
            continue

        nimi = nimed[idx]
        for ese in mangija["inventar"]:
            if ese["nimi"] == nimi:
                mangija["inventar"].remove(ese)
                break

        hind = ese_muugihind(nimi)
        lisa_vask_tasu(mangija, hind)
        print(f"Müüsid eseme: {nimi}")
        peatukk1.pause()


def lae_teise_peatuki_mang():
    peatukk1._paranda_world_state()
    print("=== VANA KOMPASSI SALADUS: PEATÜKK 2 ===\n")

    if peatukk1._vali_profiil("lae") is None:
        print("Save faili ei valitud.")
        return None, [], set()

    mangija, leitud_artefaktid, aktiveeritud_altarid = peatukk1.lae_mang()
    if mangija is None:
        print("Mängu laadimine ebaõnnestus.")
        return None, [], set()

    chapter2_flags(mangija)
    rakenda_aethori_norvendus(mangija)
    return mangija, leitud_artefaktid, aktiveeritud_altarid


def kontrolli_jatku_tingimus():
    if not peatukk1.WORLD_STATE.get("tempel_labitutud", False):
        print("See save ei sobi veel peatüki 2 jaoks.")
        print("Lõpeta enne peatükk 1 ja läbi Ajalohe tempel.")
        peatukk1.pause()
        return False
    return True


def ch2_rynnaku_nimi(tyyp):
    nimed = {
        "fuusiline": "Füüsiline löök",
        "tuli": "Tulelöök",
        "vesi": "Veelöök",
        "maa": "Maalöök",
        "ohk": "Õhulöök",
    }
    return nimed.get(tyyp, tyyp.capitalize())


def ch2_combo_nimi(tyyp1, tyyp2):
    return f"{ch2_rynnaku_nimi(tyyp1)} + {ch2_rynnaku_nimi(tyyp2)}"


def ch2_elemendid(mangija):
    elemendid = []
    for tyyp in ("tuli", "vesi", "maa", "ohk"):
        if elemendi_tase(mangija, tyyp) >= 1:
            elemendid.append(tyyp)
    return elemendid


def ch2_arvuta_dmg(mangija, tyyp="fuusiline"):
    baas = max(1, int(mangija["joukus"]))
    if tyyp == "fuusiline":
        return max(1, baas + random.randint(1, 6))
    dmg = max(1, int(baas * 0.8) + elemendi_tase(mangija, tyyp) * 3 + random.randint(1, 5))
    if tyyp == "tuli":
        dmg += armor_bonus(mangija, "tule_bonus")
    return dmg


def ch2_combod(mangija):
    tyybid = ["fuusiline"] + ch2_elemendid(mangija)
    combod = []
    for i, tyyp1 in enumerate(tyybid):
        for tyyp2 in tyybid[i + 1:]:
            if tyyp1 == "fuusiline":
                if elemendi_tase(mangija, tyyp2) >= 3:
                    combod.append((tyyp1, tyyp2))
            elif elemendi_tase(mangija, tyyp1) >= 3 and elemendi_tase(mangija, tyyp2) >= 3:
                combod.append((tyyp1, tyyp2))
    return combod


def ch2_combo_dmg(mangija, tyyp1, tyyp2):
    return int((ch2_arvuta_dmg(mangija, tyyp1) + ch2_arvuta_dmg(mangija, tyyp2)) * 1.25)


def lahingu_regen(mangija):
    energia = 3 + armor_bonus(mangija, "energia_regen")
    mana = 2 + armor_bonus(mangija, "mana_regen")
    if kannab_armorit(mangija, "Öömalm Set"):
        energia = max(1, energia - 1)
    taasta_ressursse(mangija, energia=energia, mana=mana)
    return energia, mana


def dodge_voimalus(mangija, lisa=0):
    fuus = mangija["stats"]["fuusiline_level"]
    ohk = elemendi_tase(mangija, "ohk")
    return max(0, min(60, 5 + fuus // 2 + ohk * 2 + armor_bonus(mangija, "dodge_bonus") + lisa))


def shadow_mana_hind(mangija):
    return 10 if kannab_armorit(mangija, "Varjuhõbe Set") or kannab_armorit(mangija, "VarjuhĆµbe Set") else 15


def dodge_energia_hind(mangija):
    return 3 if kannab_armorit(mangija, "Pilvetantsija Set") else 6


def kuva_lahingu_abi():
    peatukk1.clear()
    peatukk1.section_title("LAHINGU ABI", peatukk1.ANSI_CYAN)
    print("Kiire löök: tasuta füüsiline rünnak.")
    print("Tugev löök: kulutab energiat ja teeb rohkem kahju.")
    print("Kaitse: taastab natuke ressursse, vähendab vastase kahju ja kulutab armorit.")
    print("Põikle: kulutab energiat ja tõstab selle käigu dodge võimalust.")
    print("Keskendu: ei tee kahju, taastab energiat ja manat.")
    print("Elementrünnak: kulutab manat ja annab elemendi eriefekti.")
    print("Combo: kulutab energiat ja manat, teeb suuremat kahju.")
    print("Shadow abi: kulutab manat, pärast Hingelepingut teeb lisakahju.")
    print("Ajastulõige: vajab Ajastute Mõõka, kulutab energiat ja manat, lõikab läbi vastase käigu.")
    print()
    print("Elemendid:")
    print("Tuli: põletab vastast mitu käiku.")
    print("Vesi: taastab manat ja Sügavvee Setiga ka elu.")
    print("Maa: annab kaitseasendi.")
    print("Õhk: tõstab dodge võimalust.")
    print()
    print("Armor:")
    print("Durability kulub lööke vastu võttes. Blacksmith parandab selle.")
    peatukk1.pause()


def kasuta_ch2_eset_lahingus(mangija):
    kasutatavad = []
    for ese in mangija["inventar"]:
        if any(k in ese for k in ("hp_restore", "energia_restore", "mana_restore")):
            kasutatavad.append(ese)
    if not kasutatavad:
        print("Sul pole kasutatavaid esemeid.")
        peatukk1.pause()
        return False

    while True:
        peatukk1.clear()
        peatukk1.section_title("KASUTA ESET", peatukk1.ANSI_GREEN)
        for i, ese in enumerate(kasutatavad, start=1):
            lisa = []
            if "hp_restore" in ese:
                lisa.append(f"+{ese['hp_restore']} HP")
            if "energia_restore" in ese:
                lisa.append(f"+{ese['energia_restore']} energia")
            if "mana_restore" in ese:
                lisa.append(f"+{ese['mana_restore']} mana")
            if "self_damage" in ese:
                lisa.append(f"-{ese['self_damage']} HP")
            print(f"{i} - {ese['nimi']} ({', '.join(lisa)})")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()
        if valik == "0":
            return False
        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale valik.")
            peatukk1.pause()
            continue
        if not (0 <= idx < len(kasutatavad)):
            print("Vale valik.")
            peatukk1.pause()
            continue

        ese = kasutatavad[idx]
        if "hp_restore" in ese:
            mangija["elud"] += ese["hp_restore"]
            print(f"Taastad {ese['hp_restore']} elu.")
        if "energia_restore" in ese:
            taasta_ressursse(mangija, energia=ese["energia_restore"])
            print(f"Taastad {ese['energia_restore']} energiat.")
        if "mana_restore" in ese:
            taasta_ressursse(mangija, mana=ese["mana_restore"])
            print(f"Taastad {ese['mana_restore']} manat.")
        if "self_damage" in ese:
            mangija["elud"] = max(1, mangija["elud"] - ese["self_damage"])
            print(f"Segu tagasilöök võtab {ese['self_damage']} elu.")
        mangija["inventar"].remove(ese)
        peatukk1.pause()
        return True


def lihtne_lahing(mangija, vastane, lubatud_element=None, piirkond=None, leitud_artefaktid=None):
    efektid = {"burn": 0, "burn_dmg": 0}
    kriisikaitse_kasutatud = False
    while mangija["elud"] > 0 and vastane["elud"] > 0:
        regen_e, regen_m = lahingu_regen(mangija)
        kaitses = False
        dodge_lisa = 0
        dmg = 0

        if efektid["burn"] > 0:
            vastane["elud"] -= efektid["burn_dmg"]
            efektid["burn"] -= 1
            print(f"{vastane['nimi']} põleb ja kaotab {efektid['burn_dmg']} elu.")
            if vastane["elud"] <= 0:
                print(f"{vastane['nimi']} langeb tagasi.")
                if piirkond is not None:
                    anna_lahingu_dropid(mangija, piirkond)
                peatukk1.pause()
                return True

        peatukk1.clear()
        peatukk1.section_title(f"LAHING - {vastane['nimi']}", peatukk1.ANSI_RED)
        print(f"Sinu elud: {mangija['elud']}")
        print(f"{vastane['nimi']} elud: {vastane['elud']}")
        kuva_ressursid(mangija)
        kuva_armor(mangija)
        print(f"Taastus sel käigul: +{regen_e} energia, +{regen_m} mana")
        print()
        menu = []
        idx = 1

        print("-- Tegevused --")
        print(f"{idx} - Kiire löök (0 energia, {ch2_arvuta_dmg(mangija, 'fuusiline')} dmg)")
        menu.append(("quick", "fuusiline"))
        idx += 1
        print(f"{idx} - Tugev löök (8 energia, {int(ch2_arvuta_dmg(mangija, 'fuusiline') * 1.45)} dmg)")
        menu.append(("heavy", "fuusiline"))
        idx += 1
        print(f"{idx} - Kaitse (+6 energia, +2 mana, armor vähendab kahju)")
        menu.append(("defend", None))
        idx += 1
        print(f"{idx} - Põikle ({dodge_energia_hind(mangija)} energia, dodge {dodge_voimalus(mangija, 25)}%)")
        menu.append(("dodge", None))
        idx += 1
        print(f"{idx} - Keskendu (+8 energia, +10 mana)")
        menu.append(("focus", None))
        idx += 1

        elemendid = ch2_elemendid(mangija)
        if elemendid:
            print("-- Elemendid --")
            for tyyp in elemendid:
                nimi = ch2_rynnaku_nimi(tyyp)
                if lubatud_element == tyyp:
                    nimi += " [soovitus]"
                print(f"{idx} - {nimi} (10 mana, {ch2_arvuta_dmg(mangija, tyyp)} dmg)")
                menu.append(("element", tyyp))
                idx += 1

        combod = ch2_combod(mangija)
        if combod:
            print("-- Combod --")
            for tyyp1, tyyp2 in combod:
                print(f"{idx} - {ch2_combo_nimi(tyyp1, tyyp2)} (6 energia, 18 mana, {ch2_combo_dmg(mangija, tyyp1, tyyp2)} dmg)")
                menu.append(("combo", (tyyp1, tyyp2)))
                idx += 1

        shadow_index = None
        if chapter2_flags(mangija)["chapter2_soul_contract_made"]:
            print(f"{idx} - Shadow abi ({shadow_mana_hind(mangija)} mana)")
            shadow_index = idx
            idx += 1

        mook_index = None
        if leitud_artefaktid is not None and on_ajastute_mook(leitud_artefaktid):
            e_hind, m_hind = ajastute_mooga_hind(mangija)
            print(f"{idx} - Ajastulõige ({e_hind} energia, {m_hind} mana)")
            mook_index = idx
            idx += 1

        ravim_index = idx
        print(f"{idx} - Kasuta ravimit")
        print("? - Selgita lahinguvalikuid")
        print("0 - Põgene")
        valik = input("Vali: ").strip()

        if valik == "?":
            kuva_lahingu_abi()
            continue

        if shadow_index is not None and valik == str(shadow_index):
            if not kuluta_ressursse(mangija, mana=shadow_mana_hind(mangija)):
                peatukk1.pause()
                continue
            dmg = random.randint(8, 16)
            if kannab_armorit(mangija, "Katakombiteras Set"):
                dmg += 8
            print(f"Shadow rebib vastase varju viltu. Kahju: {dmg}.")
        elif mook_index is not None and valik == str(mook_index):
            e_hind, m_hind = ajastute_mooga_hind(mangija)
            if not kuluta_ressursse(mangija, energia=e_hind, mana=m_hind):
                peatukk1.pause()
                continue
            dmg = 18 + mangija["stats"]["fuusiline_level"] + sum(mangija["stats"]["elementaalne_level"].values()) // 4
            vastane["jou"] = max(1, vastane["jou"] - 2)
            dodge_lisa += 20
            print(f"Ajastute Mõõk lõikab hetke lahti. Kahju: {dmg}.")
            print(f"{vastane['nimi']} kaotab rütmi ja tema jõud langeb.")
        elif valik == str(ravim_index):
            kasuta_ch2_eset_lahingus(mangija)
            continue
        elif valik == "0":
            print("Taganed enne, kui olukord läheb hullemaks.")
            peatukk1.pause()
            return False
        else:
            try:
                chosen = int(valik) - 1
            except ValueError:
                print("Vale valik.")
                peatukk1.pause()
                continue
            if not (0 <= chosen < len(menu)):
                print("Vale valik.")
                peatukk1.pause()
                continue
            tegevus, payload = menu[chosen]
            if tegevus == "quick":
                dmg = ch2_arvuta_dmg(mangija, "fuusiline")
                print(f"Kasutad kiiret lööki ja teed {dmg} kahju.")
            elif tegevus == "heavy":
                if not kuluta_ressursse(mangija, energia=8):
                    peatukk1.pause()
                    continue
                dmg = int(ch2_arvuta_dmg(mangija, "fuusiline") * 1.45)
                print(f"Kasutad tugevat lööki ja teed {dmg} kahju.")
            elif tegevus == "defend":
                kaitses = True
                taasta_ressursse(mangija, energia=6, mana=2)
                print("Tõstad kaitse. Armor võtab järgmise löögi paremini vastu.")
            elif tegevus == "dodge":
                if not kuluta_ressursse(mangija, energia=dodge_energia_hind(mangija)):
                    peatukk1.pause()
                    continue
                dodge_lisa = 25
                print("Liigud kergemalt ja otsid vastase rütmist tühja kohta.")
            elif tegevus == "focus":
                taasta_ressursse(mangija, energia=8, mana=10)
                print("Keskendud hingamisele. Energia ja mana taastuvad.")
            elif tegevus == "element":
                tyyp = payload
                if not kuluta_ressursse(mangija, mana=10):
                    peatukk1.pause()
                    continue
                dmg = ch2_arvuta_dmg(mangija, tyyp)
                print(f"Kasutad {ch2_rynnaku_nimi(tyyp)} ja teed {dmg} kahju.")
                if tyyp == "vesi":
                    taasta_ressursse(mangija, mana=7 if kannab_armorit(mangija, "Sügavvee Set") else 4)
                    print("Vesi toob osa manast tagasi.")
                    if kannab_armorit(mangija, "Sügavvee Set"):
                        mangija["elud"] += 8
                        print("Sügavvee Set taastab ka 8 elu.")
                elif tyyp == "maa":
                    kaitses = True
                    print("Maa tõstab su ümber lühikese kaitsekihi.")
                elif tyyp == "ohk":
                    dodge_lisa += 12
                    print("Õhk teeb su sammu kergemaks.")
                elif tyyp == "tuli":
                    efektid["burn"] = 3
                    efektid["burn_dmg"] = 4 + elemendi_tase(mangija, "tuli") // 2
                    if kannab_armorit(mangija, "Leegisüda Set"):
                        efektid["burn_dmg"] += 3
                    print(f"Leek jääb vastase külge. Põletus: {efektid['burn_dmg']} kahju 3 käiku.")
            elif tegevus == "combo":
                if not kuluta_ressursse(mangija, energia=6, mana=18):
                    peatukk1.pause()
                    continue
                tyyp1, tyyp2 = payload
                dmg = ch2_combo_dmg(mangija, tyyp1, tyyp2)
                print(f"Kasutad combot {ch2_combo_nimi(tyyp1, tyyp2)} ja teed {dmg} kahju.")

        if dmg > 0:
            vastane["elud"] -= dmg
            if vastane["elud"] <= 0:
                print(f"{vastane['nimi']} langeb tagasi.")
                if piirkond is not None:
                    anna_lahingu_dropid(mangija, piirkond)
                peatukk1.pause()
                return True

        vastase_dmg = max(3, vastane["jou"] + random.randint(-2, 4))
        dodge = dodge_voimalus(mangija, dodge_lisa)
        if random.randint(1, 100) <= dodge:
            print(f"{vastane['nimi']} lööb mööda. Dodge õnnestus ({dodge}%).")
            peatukk1.pause()
            continue

        if kaitses:
            kordaja = 0.4 if kannab_armorit(mangija, "Troonteras Set") else 0.5
            vastase_dmg = int(vastase_dmg * kordaja)
            kuluta_armorit(mangija, 2)
        else:
            kuluta_armorit(mangija, 1)
        if kannab_armorit(mangija, "Kroonisulami Set") and not kriisikaitse_kasutatud and mangija["elud"] <= 30:
            vastase_dmg = int(vastase_dmg * 0.5)
            kriisikaitse_kasutatud = True
            print("Kroonisulami Set sulgeb korraks praod sinu ümber.")
        kaitse = armor_kaitse(mangija)
        saadud = max(1, vastase_dmg - kaitse)
        mangija["elud"] = max(0, mangija["elud"] - saadud)
        if kaitse:
            print(f"Armor vähendab kahju {kaitse} võrra.")
        print(f"{vastane['nimi']} vastab ja teeb {saadud} kahju.")
        peatukk1.pause()

    return mangija["elud"] > 0


def juhuslik_kohtumine(mangija, piirkond):
    if random.random() >= 0.20:
        return

    tekstid = JUHUSLIKUD_KOHTUMISED.get(piirkond, [])
    if not tekstid:
        return

    peatukk1.clear()
    peatukk1.section_title("JUHUSLIK KOHTUMINE", peatukk1.ANSI_RED)
    print(random.choice(tekstid))
    print()
    flags = chapter2_flags(mangija)
    if flags["chapter2_soul_contract_made"] and random.random() < 0.45:
        print("Shadow liigub su ette enne, kui löök päriselt kohale jõuab.")
        print("Tema kohalolu rebib kohtumise teravuse väiksemaks.")
        kahju = random.randint(2, 8)
        mangija["elud"] = max(1, mangija["elud"] - kahju)
        print(f"Shadow pehmendab lööki. Kaotad {kahju} elupunkti.")
        peatukk1.pause()
        return
    nimi, hp, jou = KOHTUMIS_VAENLASED.get(piirkond, ("Vari", 30, 8))
    vastane = {"nimi": nimi, "elud": hp, "jou": jou}
    element_map = {
        "kirre": "maa",
        "kagu": "tuli",
        "edel": "ohk",
        "ida": "vesi",
    }
    lihtne_lahing(mangija, vastane, element_map.get(piirkond), piirkond)


def rakenda_aethori_norvendus(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_power_scaled"]:
        return
    algne_jou = int(mangija.get("joukus", 0))
    flags["chapter2_original_joukus"] = algne_jou
    mangija["joukus"] = max(3, int(algne_jou * 0.35))
    flags["chapter2_power_scaled"] = True


def elemendi_tase(mangija, element):
    levelid = mangija["stats"]["elementaalne_level"]
    if element == "ohk":
        for key in ("õhk", "Ćµhk"):
            if key in levelid:
                return levelid[key]
        return 1
    return levelid.get(element, 1)


def usalduse_lavend(mangija, baas=6):
    flags = chapter2_flags(mangija)
    lavend = baas
    if flags["chapter2_shadow_met"]:
        lavend -= 1
    if flags.get("chapter2_has_aethor_mark") or peatukk1.has_inventar(mangija, AETHORI_VANDEMARK):
        lavend += 1
    lavend += armor_bonus(mangija, "trust_penalty")
    return max(1, lavend)


def aethori_mark_blokeerib_usaldust(mangija):
    flags = chapter2_flags(mangija)
    if flags.get("chapter2_has_aethor_mark", False) or peatukk1.has_inventar(mangija, AETHORI_VANDEMARK):
        print("Elementaalid tunnevad Aethori Vandemärki sinu küljes.")
        print("See märk ütleb neile, et seisad ikka veel Aethori käsu all.")
        print("Selle märgiga ei saa uut elementaalset usaldust võita.")
        peatukk1.pause()
        return True
    return False


def anna_aspekt(mangija, element):
    nimi = ASPEKTID[element]
    if not peatukk1.has_inventar(mangija, nimi):
        peatukk1.add_inventar(mangija, nimi)


def lepingu_koostisosad_koos(mangija):
    vajalikud = [
        ASPEKTID["maa"],
        ASPEKTID["tuli"],
        ASPEKTID["vesi"],
        ASPEKTID["ohk"],
        "Alkeemiline Sool",
        "Varjutint",
    ]
    return all(peatukk1.has_inventar(mangija, ese) for ese in vajalikud)


def osta_materjal(mangija, nimi, hind):
    if peatukk1.has_inventar(mangija, nimi):
        print(f"{nimi} on sul juba olemas.")
        peatukk1.pause()
        return
    if mangija.get("kaart") is None:
        print("Sul pole pangakaarti.")
        peatukk1.pause()
        return
    if not peatukk1.kaart_eemalda_vask(mangija["kaart"], hind):
        print("Sul pole piisavalt raha.")
        peatukk1.pause()
        return
    peatukk1.add_inventar(mangija, nimi)
    print(f"Ostsid: {nimi}")
    peatukk1.pause()


def must_turg(mangija):
    while True:
        peatukk1.clear()
        peatukk1.section_title("MUST TURG", peatukk1.ANSI_RED)
        print("Tagatänavas liigub kaup, mida ametlikult olemas ei ole.")
        kuva_saldo(mangija)
        print()
        print("1 - Vaata musta turu kaupa")
        print("2 - Müü mustale turule")
        print("3 - Keelatud armor setid")
        print("4 - Kuula kuulujutte")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "1":
            osta_poe_nimekirjast(mangija, MUSTA_TURU_OSTUD, "MUST TURG - KAUP")
        elif valik == "2":
            muugi_menuu(mangija, "MUST TURG - MÜÜK")
        elif valik == "3":
            armor_poemenyy(mangija, "must_turg", "MUST TURG - ARMOR")
        elif valik == "4":
            print("\"Kui vari käib sul järel, märkavad vanad jõud seda enne inimesi,\" sosistab kaupmees.")
            print("\"Mõni kardab rohkem. Mõni usaldab kiiremini.\"")
            print("\"Kui tood mulle midagi, mida loss ametlikult ei tunnista, liigub ka vask kiiremini,\" lisab ta muiates.")
            print("\"Musta maagi infusioon seob Stormyxi, Mythrili ja Orichalcumi üheks Metallurgiumiks,\" lisab kõrval seisev maag.")
            peatukk1.pause()
        elif valik == "0":
            return
        else:
            print("Vale valik.")
            peatukk1.pause()


def kaevandus(mangija):
    while True:
        peatukk1.clear()
        peatukk1.section_title("AETHORI KAEVANDUS", peatukk1.ANSI_YELLOW)
        print("Siit ostetakse armori jaoks metalle ja kristalle. Haruldasem materjal maksab rohkem.")
        kuva_saldo(mangija)
        print()
        for i, (nimi, hind) in enumerate(MINE_MATERJALID, start=1):
            print(f"{i} - {nimi} - {hind} vaskdablooni")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()
        if valik == "0":
            return
        try:
            idx = int(valik) - 1
        except ValueError:
            print("Vale valik.")
            peatukk1.pause()
            continue
        if not (0 <= idx < len(MINE_MATERJALID)):
            print("Vale valik.")
            peatukk1.pause()
            continue
        nimi, hind = MINE_MATERJALID[idx]
        if mangija.get("kaart") is None or not peatukk1.kaart_eemalda_vask(mangija["kaart"], hind):
            print("Sul pole piisavalt raha.")
            peatukk1.pause()
            continue
        peatukk1.add_inventar(mangija, nimi)
        print(f"Ostsid materjali: {nimi}")
        peatukk1.pause()


def hingelepingu_rituaal(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_soul_contract_made"]:
        print("Hingeleping on juba sõlmitud.")
        peatukk1.pause()
        return
    if not flags["chapter2_soul_contract_found"]:
        print("Sul puudub veel lepingu jälg.")
        peatukk1.pause()
        return
    if not lepingu_koostisosad_koos(mangija):
        print("Sul pole veel kõiki aspekte ega alkeemilisi materjale.")
        print("Vajad maa, tule, vee ja õhu aspekte ning Alkeemilist Soola ja Varjutinti.")
        peatukk1.pause()
        return

    peatukk1.clear()
    peatukk1.section_title("HINGELEPING", peatukk1.ANSI_MAGENTA)
    print("Neli aspekti asetuvad pitseriringi nagu nad oleksid seda kohta alati teadnud.")
    print("Maa hoiab ringi koos. Tuli annab sellele kuju. Vesi seob. Õhk laseb hingata.")
    input("(edasi...)\n")
    print("Varjutint jookseb mööda tahvlit ise.")
    print("Alkeemiline sool sulab kivisse ja avab joone, mida palja jõuga ei saaks tõmmata.")
    input("(edasi...)\n")
    print("Shadow astub sulle vastu, mitte enam külje pealt.")
    print("\"Kui sa teed seda käsuna, siis ma murdun,\" ütleb ta.")
    input("(edasi...)\n")
    print("Sa ei seo teda käsuga.")
    print("Sa seod ta tõotusega, et katkist lepingut ei korrata enam vana moodi.")
    input("(edasi...)\n")
    print("Ring sulgub vaikselt.")
    print("Shadow jääb alles.")
    flags["chapter2_soul_contract_made"] = True
    print("Shadow on nüüd sinu seotud kaaslane.")
    peatukk1.pause()


def kuva_peatuki_lore():
    peatukk1.clear()
    peatukk1.section_title("AETHORI LORE", peatukk1.ANSI_MAGENTA)
    print("Aethor ehitati nelja elemendi tasakaalu peale.")
    print("Hiljem ei austatud elemente enam, vaid neid hakati siduma, juhtima ja kasutama.")
    print()
    print("Keelatud katakombidesse maeti katkised lepingud, varjud ja tõendid riigi vana vea kohta.")
    print("Elementaalid on hostile, sest sinu nägu on nende jaoks aethoorlase nägu.")
    print("Sa pead tõestama, et tulid parandama, mitte allutama.")
    input("(edasi...)\n")
    print("Vana kroonik ütleb, et Aethor ei langenud esimesena kivide pärast.")
    print("Ta langes siis, kui juhid otsustasid, et leping elementidega peab alluma troonile, mitte maailmale.")
    input("(edasi...)\n")
    print("Maa seoti ruunidega, tuli aheldati sepikodade ja sõja külge,")
    print("vesi sunniti kandma laevu, mida ta ei õnnistanud,")
    print("ja õhule anti tornid, kust jälgida kõike allpool olevat.")
    input("(edasi...)\n")
    print("Kui lepingud hakkasid katkema, ei maetud katakombidesse ainult esemeid.")
    print("Sinna maeti nimed, tõotused, varjud ja terve osa Aethori ajaloost.")
    peatukk1.pause()


def juhtide_vastusamm(mangija):
    flags = chapter2_flags(mangija)
    if not flags["chapter2_leaders_alerted"]:
        return
    if flags.get("chapter2_leader_warning_seen", False):
        return

    peatukk1.clear()
    peatukk1.section_title("LOSSI PILK", peatukk1.ANSI_RED)
    print("Tagasiteel linna peatab sind kaks vaikset lossivahti.")
    print("Nad ei tõmba relva. See teeb olukorra hullemaks.")
    input("(edasi...)\n")
    print("\"Tema Kõrgus kuuleb, et sa küsid liiga vanu küsimusi,\" ütleb üks neist.")
    print("\"Katakombid, druiidid, nõid... need ei ole rajad, mida heatahtlik inimene pikalt käib.\"")
    input("(edasi...)\n")
    print("Teine vahimees vaatab su mõõka liiga kaua.")
    print("\"Aethor ei vaja päästjat, kes kisub lahti selle, mis on juba kord suletud.\"")
    flags["chapter2_leader_warning_seen"] = True
    peatukk1.pause()


def aethori_toendid(mangija):
    flags = chapter2_flags(mangija)
    return [
        ("Vunts kinnitas, et sa ei tulnud tühjast kohast", flags["chapter2_met_vunts"]),
        ("Põhja nõid kuulis sinu varju ja ei saatnud sind minema", flags["chapter2_met_witch"]),
        ("Druiidid tulid sinu ees udust välja", flags["chapter2_met_druids"]),
        ("Druiidid nägid, et sa ei murra maad jõuga", flags["chapter2_earth_trust"]),
        ("Sa leidsid katakombidest Hingelepingu jälje", flags["chapter2_soul_contract_found"]),
        ("Inferno leegid tunnistasid, et sa ei tulnud neid aheldama", flags["chapter2_fire_trust"]),
    ]


def aethori_noukogu(mangija):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("AETHORI PEALIKUD", peatukk1.ANSI_RED)

    if flags["chapter2_council_proven"]:
        print("Pealikud tunnevad su Vandemärgi ära.")
        print("See ei tee sinust nende oma, aga see seob su nime Aethori otsustega.")
        peatukk1.pause()
        return

    if not flags["chapter2_council_summoned"]:
        print("Sind viiakse saali, kus istuvad Aethori pealikud ja vanemad nõunikud.")
        print("Nende jaoks oled sa tundmatu mees valede teadmiste ja vale mõõgaga.")
        input("(edasi...)\n")
        print("\"Üks tegu võib olla õnn,\" ütleb vanim.")
        print("\"Me ei seo võõrast Aethoriga enne, kui mitu märki ütlevad sama asja.\"")
        flags["chapter2_council_summoned"] = True
        input("(edasi...)\n")

    toendid = aethori_toendid(mangija)
    tehtud = [nimi for nimi, olemas in toendid if olemas]
    puuduvad = [nimi for nimi, olemas in toendid if not olemas]

    print(f"Tõendeid: {len(tehtud)}/{AETHORI_TOENDITE_ARV}")
    for nimi in tehtud:
        print(f"  - {nimi}")

    if len(tehtud) < AETHORI_TOENDITE_ARV:
        print()
        print("Sellest ei piisa veel.")
        print("Võimalikud teed, mis võiksid sind kinnitada:")
        for nimi in puuduvad[:3]:
            print(f"  - {nimi}")
        peatukk1.pause()
        return

    print()
    print("Pealikud ei naerata, aga nad ei vaata sind enam kui juhuslikku ohtu.")
    print("Vanim asetab lauale märgi, mille metall on külm ja liiga raske.")
    print(f"See on {AETHORI_VANDEMARK}.")
    print()
    print("1 - Võta Vandemärk vastu")
    print("2 - Keeldu märgist")
    valik = input("Vali: ").strip()

    flags["chapter2_council_proven"] = True
    if valik == "1":
        flags["chapter2_has_aethor_mark"] = True
        peatukk1.add_inventar(mangija, AETHORI_VANDEMARK)
        print("Elementaalid tunnevad seda märki. Mõni usaldab sind selle pärast raskemini.")
        print("Ametlikud tugevamad armorid avanevad blacksmithi juures.")
    else:
        flags["chapter2_refused_aethor_mark"] = True
        print("Pealikud jätavad su nime meelde, aga mitte omana.")
        print("Elementaalid ei näe sinu küljes Aethori pitserit.")
    peatukk1.pause()


def druiidide_katse(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_earth_trust"]:
        print("Druiidid on juba näinud, kuidas sa maad ilma murdmata juhid.")
        peatukk1.pause()
        return
    if aethori_mark_blokeerib_usaldust(mangija):
        return

    peatukk1.clear()
    peatukk1.section_title("DRUIIDIDE KATSE", peatukk1.ANSI_GREEN)
    print("Soo vajub korraga su jalge all läbi.")
    print("Mudast tõusevad juured, mis ei taha sind edasi lasta.")
    input("(edasi...)\n")
    print("Udu seest kostab hääl:")
    print("\"Aethoorlased võtavad maa käest. Sina näed välja nagu nemad.\"")
    input("(edasi...)\n")
    print("Kuidas vastad?")
    print("1 - Surud juured jõuga tagasi")
    print("2 - Lõhud ruuni mõõgaga")
    print("3 - Kasutad maa-jõudu, et soo tasakaalustada")
    valik = input("Vali: ").strip()

    if valik != "3":
        print("Maa tõmbub sinu alt eemale.")
        print("Druiidid ei ründa sind lõpuni, aga nad ei usu sind veel.")
        mangija["elud"] = max(1, mangija["elud"] - 10)
        peatukk1.pause()
        return

    maa_level = elemendi_tase(mangija, "maa")
    if maa_level < usalduse_lavend(mangija, 6):
        print("Sa tunned maad, aga su side pole veel piisavalt kindel.")
        print("Druiidid vaikivad. Nad nägid tahet, kuid mitte meisterlikkust.")
        if chapter2_flags(mangija)["chapter2_shadow_met"]:
            print("Ometi märkavad nad varju su taga ja kõhklevad kauem kui enne.")
        peatukk1.pause()
        return

    print("Sa ei murra juuri. Sa kuulad, kuhu need liikuda tahavad.")
    print("Maa vajub tagasi paika nagu haav, millele ei suruta enam kätt peale.")
    input("(edasi...)\n")
    print("Druiidid astuvad lõpuks udust välja.")
    print("\"Sina ei käsi maad. Sa palud ja maa vastab,\" ütleb vanim neist.")
    print("\"See erinevus võib veel midagi päästa.\"")
    flags["chapter2_earth_trust"] = True
    flags["chapter2_met_druids"] = True
    anna_aspekt(mangija, "maa")
    peatukk1.pause()


def uuenda_juhtide_kahtlust(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_met_witch"] and flags["chapter2_earth_trust"]:
        flags["chapter2_leaders_alerted"] = True


def proovi_farlandsi_luba(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    print("Mainid Tormikompassi ja Farlandsi nime.")
    print("Valveohvitseri pilk muutub kohe külmaks.")
    flags["chapter2_asked_farlands"] = True

    if "Tormikompass" not in leitud_artefaktid:
        print("\"Sul pole isegi Tormikompassi. Farlands ei ava end niisama.\"")
        peatukk1.pause()
        return

    if flags["chapter2_has_farlands_pass"]:
        print("\"Sul on meie luba juba olemas. Ära raiska seda.\"")
        peatukk1.pause()
        return

    if flags["chapter2_earth_trust"] and flags["chapter2_met_witch"]:
        print("\"Druiidid ei löönud sind tagasi ja põhja nõid pani su nime oma vaikusesse kirja,\" ütleb ohvitser.")
        print("\"See on rohkem, kui enamik aethoorlasi iial saab.\"")
        print("Ta ulatab sulle märgistatud pääseloa.")
        print("Saad: Farlandsi läbisõiduluba")
        flags["chapter2_has_farlands_pass"] = True
        peatukk1.add_item(leitud_artefaktid, "Farlandsi läbisõiduluba")
        peatukk1.pause()
        return

    print("\"Farlands ei ole koht, kuhu me saadame igaühe, kes oskab kompassi käes hoida,\" ütleb ta.")
    print("\"Kui tahad itta kaugemale minna, pead kõigepealt tõestama, et Aethor võib sind usaldada.\"")
    peatukk1.pause()


def katakombi_avastus(mangija):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("PITSERISAAL", peatukk1.ANSI_YELLOW)
    print("Ukse siseküljel on samad märgid, millest nõid rääkis: hing, käsk ja side.")
    input("(edasi...)\n")
    print("Seinte vahele on raiutud hoiatus:")
    print("\"Ära seo varju käsuga, kui sa ei taha esmalt teda nimega kuulda.\"")
    input("(edasi...)\n")
    print("Põrandal lebab katkine lepingutahvel.")
    print("Shadow liigub korraks sinu kõrval selgemalt kui kunagi varem.")
    input("(edasi...)\n")
    print("Ta ei ründa.")
    print("Ta sirutab käe katkise tahvli poole nagu mäletaks seda kohta paremini kui sina.")
    input("(edasi...)\n")
    print("\"Mitte veel,\" kostab hääl, mis ei tule päris ruumist ega päris sinu seest.")
    print("See on esimene kord, kui vari vastab sõnadega.")
    input("(edasi...)\n")
    print("Tahvli tagaküljele on kraabitud poolik ülestähendus:")
    print("\"Projekt Varileping katkestati. Subjekt ei kuuletu käsule, kui talle antakse nimi enne ahelat.\"")
    flags["chapter2_soul_contract_found"] = True
    flags["chapter2_shadow_met"] = True
    peatukk1.pause()


def ajastute_mooga_pragu(mangija, leitud_artefaktid):
    peatukk1.clear()
    peatukk1.section_title("AJASTUTE MÕÕK", peatukk1.ANSI_MAGENTA)
    if not on_ajastute_mook(leitud_artefaktid):
        print("Siin on pragu ajas, aga sul puudub tera, mis oskaks seda puudutada.")
        peatukk1.pause()
        return
    flags = chapter2_flags(mangija)
    print("Katakombi seinal on juuspeen valgusjoon.")
    print("Ajastute Mõõk muutub su käes raskeks, nagu tunneks ta vana lõiget ära.")
    input("(edasi...)\n")
    print("Sa ei raiu seina. Sa raiud hetke, mil see sein kunagi suleti.")
    input("(edasi...)\n")
    print("Pragu avaneb ja sealt langeb välja metall, mis ei kuulu päriselt sellesse aega.")
    peatukk1.add_inventar(mangija, "Stormyx Shard")
    ava_retsept(mangija, "Stormyx Set")
    flags["chapter2_sword_rift_opened"] = True
    peatukk1.pause()


def inferno_katse(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_fire_trust"]:
        print("Inferno leegid on juba tunnistanud, et sa ei tulnud neid aheldama.")
        peatukk1.pause()
        return
    if aethori_mark_blokeerib_usaldust(mangija):
        return

    peatukk1.clear()
    peatukk1.section_title("INFERNO KATSE", peatukk1.ANSI_RED)
    print("Leegid keeravad su ümber ringi nagu kiskjad.")
    print("Tuleolendite jaoks oled sa järjekordne aethoorlane, kes tuli tuld omaks nimetama.")
    input("(edasi...)\n")
    print("Kuidas vastad?")
    print("1 - Paiskad tule laiali jõuga")
    print("2 - Lased mõõgal leegi läbi lõigata")
    print("3 - Tõmbad leegi tagasi kindlasse ringi, ilma seda lämmatamata")
    valik = input("Vali: ").strip()

    if valik != "3":
        print("Leek vihastub. Kuumus lööb sulle vastu rinda.")
        mangija["elud"] = max(1, mangija["elud"] - 12)
        peatukk1.pause()
        return

    tuli_level = elemendi_tase(mangija, "tuli")
    if tuli_level < usalduse_lavend(mangija, 6):
        print("Sa tunned tuld, aga su kontroll hajub liiga kiiresti.")
        print("Inferno ei hävita sind, kuid ta ei usu sind veel.")
        if chapter2_flags(mangija)["chapter2_shadow_met"]:
            print("Leegid ei lõika sind päris maha. Miski sinu taga muudab nad ettevaatlikuks.")
        peatukk1.pause()
        return

    print("Sa ei käsi leeki. Sa annad talle piiri, mida ta ise valib hoida.")
    print("Kuumus langeb niipalju, et saad jälle hingata.")
    input("(edasi...)\n")
    print("Leegis avaneb hetkeks nägu, mis ei ole inimlik.")
    print("\"Sina ei tulnud meid sepikotta tagasi viima,\" sosistab tuli.")
    flags["chapter2_fire_trust"] = True
    anna_aspekt(mangija, "tuli")
    peatukk1.pause()


def ohuriigi_katse(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_air_trust"]:
        print("Taevarahvas on juba näinud, et su samm ei lõhu nende kõrgust.")
        peatukk1.pause()
        return
    if aethori_mark_blokeerib_usaldust(mangija):
        return

    peatukk1.clear()
    peatukk1.section_title("ÕHURIIKI KATSE", peatukk1.ANSI_CYAN)
    print("Õhusild ei püsi paigal.")
    print("Tuul otsib su raskemat sammu ja lükkab selle kõrvale.")
    input("(edasi...)\n")
    print("Ülevalt kostab hääl:")
    print("\"Aethor ehitas torne, et õhku valvata. Miks peaks taevas sind kandma?\"")
    input("(edasi...)\n")
    print("Kuidas vastad?")
    print("1 - Hüppad jõuga sillale")
    print("2 - Torkad mõõga kivisse ja hoiad kinni")
    print("3 - Lased õhul end kergemaks teha ja astud tuule rütmis")
    valik = input("Vali: ").strip()

    if valik != "3":
        print("Tuul rebib su sammu lahti ja paiskab sind tagasi kivile.")
        mangija["elud"] = max(1, mangija["elud"] - 9)
        peatukk1.pause()
        return

    ohk_level = elemendi_tase(mangija, "ohk")
    if ohk_level < usalduse_lavend(mangija, 6):
        print("Sa kuuled tuult, aga sa ei oska veel temaga kaasa liikuda.")
        if chapter2_flags(mangija)["chapter2_shadow_met"]:
            print("Taevarahvas märkab siiski, et isegi vari sinu taga ei jaksa sammu raskeks teha.")
        peatukk1.pause()
        return

    print("Sa ei sunni õhku kandma. Sa teed end korraks piisavalt kergeks, et ta ise sind tõstaks.")
    print("Sild püsib paigal just nii kaua, et saaksid teisele poole vaadata.")
    input("(edasi...)\n")
    print("Kõrgel serval seisja kummardab vaevumärgatavalt.")
    print("\"Võib-olla ei kanna sa kaasas ainult Aethori vana raskust,\" ütleb ta.")
    flags["chapter2_air_trust"] = True
    anna_aspekt(mangija, "ohk")
    peatukk1.pause()


def farlands(mangija, leitud_artefaktid, aktiveeritud_altarid):
    flags = chapter2_flags(mangija)
    maara_asukoht(mangija, "Farlands")
    while True:
        peatukk1.clear()
        peatukk1.section_title("FARLANDS", peatukk1.ANSI_BLUE)
        print("Tormikompass tõmbab paadi läbi vee nagu teaks ta teed paremini kui ükski meremees.")
        print("Farlands ei võta sind vastu vaikusega, vaid jälgiva merega.")
        print()
        print("1 - Astu mustale rannale")
        print("2 - Uuri veepiiri")
        print("3 - Kuula, mida meri ütleb")
        print("0 - Tagasi Aethorisse")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "ida")
            print("Rannaliiv on tume ja märg, nagu oleks meri seda liiga kaua millestki varjanud.")
            print("Kaugemal seisavad veeolendid poolringis ega ründa kohe, aga relvad on neil käes.")
            if not flags["chapter2_water_trust"]:
                print("\"Aethoorlane,\" sosistab üks neist. Selles sõnas on rohkem süüdistust kui nimi.")
            peatukk1.pause()
        elif valik == "2":
            juhuslik_kohtumine(mangija, "ida")
            print("Veepiiril on vanad märgid, mille Aethori meremehed on kunagi kivisse lõiganud.")
            print("Keegi on need hiljem läbi kraapinud, nagu oleks tõotus tagasi võetud.")
            peatukk1.pause()
        elif valik == "3":
            juhuslik_kohtumine(mangija, "ida")
            vesi_level = elemendi_tase(mangija, "vesi")
            if not flags["chapter2_water_trust"] and aethori_mark_blokeerib_usaldust(mangija):
                continue
            if vesi_level >= usalduse_lavend(mangija, 8):
                print("Sa lased veel hetkeks ümber sõrmede keerelda ilma seda sundimata.")
                print("Meri ei rahune täielikult, aga ta lõpetab sinu peale karjumise.")
                print("Farlands märgib su ära kui kellegi, kes võib veel kuulata.")
                flags["chapter2_water_trust"] = True
                anna_aspekt(mangija, "vesi")
            else:
                print("Sa tunned voolu, aga meri ei tunnista sind veel omaks.")
                print("Farlandsi usaldus ei tule ainult kohale jõudmise eest.")
                if flags["chapter2_shadow_met"]:
                    print("Veeolendid ei ründa sind kohe. Nad tahavad enne mõista, miks vari sind saadab.")
            peatukk1.pause()
        elif valik == "0":
            maara_asukoht(mangija, "Rand")
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def intro(mangija):
    flags = chapter2_flags(mangija)
    if flags["chapter2_intro_seen"]:
        return
    maara_asukoht(mangija, "Aethor")
    peatukk1.clear()
    peatukk1.section_title("PEATÜKK 2", peatukk1.ANSI_CYAN)
    print("Sa ei kuku edasi.")
    print("Maailm liigub sinu ümber.")
    input("(edasi...)\n")
    print("Kivi krigin kaob.")
    print("Tolm ei kõrbe enam kurgus.")
    print("Õhk on korraga liiga puhas, nagu oleks keegi selle äsja loonud.")
    input("(edasi...)\n")
    print("Sa seisad tänaval, mida oled juba näinud.")
    print("Aga mitte sellisena.")
    input("(edasi...)\n")
    print("Linn on terve.")
    print("Tuli ei ole veel taevast söönud.")
    print("Kivid ei ole veel murdunud.")
    input("(edasi...)\n")
    print("Ei ole varemeid.")
    print("Ei ole vaikust, mis tuleb liiga hilja.")
    print("On hääled. Sammud. Kaugelt kostev turg.")
    input("(edasi...)\n")
    print("Sa oled enne langust.")
    print("Seekord jõudsid enne varemeid.")
    input("(edasi...)\n")
    print("Ajastute Mõõk on endiselt sinuga kaasas.")
    print("Kadunud Ajastu Kroon ei kadunud, vaid muutus templis selleks mõõgaks.")
    print("See sama artefakt tuli sinuga läbi aja kaasa.")
    input("(edasi...)\n")
    if peatukk1.has_inventar(mangija, "Kadunud Riikide Foliant"):
        print("Ka Kadunud Riikide Foliant jäi sinuga.")
        print("Vanad lehed näivad Aethoris raskemad, nagu tunneks raamat seda maad ära.")
        input("(edasi...)\n")
    if peatukk1.has_inventar(mangija, "Unustatud päevik"):
        print("Unustatud päevik on samuti alles.")
        print("Mõned read tunduvad nüüd selgemad kui varemete maailmas.")
        input("(edasi...)\n")
    if peatukk1.has_inventar(mangija, "Maagiline lamp"):
        print("Isegi Maagiline lamp tuli kaasa.")
        print("Selle valgus ei näita veel vastuseid, aga ta ei ole siin juhuslikult.")
        input("(edasi...)\n")
    print("Su elemendid on samuti alles.")
    print("Tuli, vesi, maa ja õhk vastavad sulle endiselt nagu peatükk 1 lõpus.")
    input("(edasi...)\n")
    print("Selle raskus on su käes kadunud,")
    print("aga tunne ei ole.")
    print("Aga Aethor surub su jõu madalamaks kui see oli varemete maailmas.")
    print("Su side elementidega püsib, kuid toores tugevus on siin palju nõrgem.")
    print("Sa tead, et midagi hakkab siin murduma.")
    input("(edasi...)\n")
    print("Ja nüüd oled sina siin enne seda hetke.")
    flags["chapter2_intro_seen"] = True
    peatukk1.pause()


def kuva_templi_parand(mangija, leitud_artefaktid):
    print("Templist kaasa toodud jõud:")
    if "Ajastute Mõõk" in leitud_artefaktid:
        print("  - Ajastute Mõõk (Kadunud Ajastu Krooni uus kuju)")
    elif "Kadunud Ajastu Kroon" in leitud_artefaktid:
        print("  - Kadunud Ajastu Kroon")
    if "Tormikompass" in leitud_artefaktid:
        print("  - Tormikompass")
    if on_ajastute_mook(leitud_artefaktid):
        print("  - Ajastute Mõõk: avab ajapragusid ja annab lahingus Ajastulõike")
    if "Ajastute Mõõk" not in leitud_artefaktid and "Kadunud Ajastu Kroon" not in leitud_artefaktid:
        print("  - Midagi templist kaasa ei tuvastatud")
    print("Peatükk 1 elementide tasemed tulid sinuga kaasa.")
    print(f"  - Tuli Lv {mangija['stats']['elementaalne_level']['tuli']}")
    print(f"  - Vesi Lv {mangija['stats']['elementaalne_level']['vesi']}")
    print(f"  - Maa Lv {mangija['stats']['elementaalne_level']['maa']}")
    ohk_level = mangija["stats"]["elementaalne_level"].get("õhk", mangija["stats"]["elementaalne_level"].get("Ćµhk", 1))
    print(f"  - Õhk Lv {ohk_level}")
    print()
    print("Peatükk 1 tähtsad esemed:")
    olulised = [
        "Kadunud Riikide Foliant",
        "Unustatud päevik",
        "Maagiline lamp",
    ]
    leitud = False
    for ese in olulised:
        if peatukk1.has_inventar(mangija, ese):
            print(f"  - {ese}")
            leitud = True
    for artefakt in ("Iidne Tee", "House deed"):
        if artefakt in leitud_artefaktid:
            print(f"  - {artefakt}")
            leitud = True
    if not leitud:
        print("  - Midagi erilist peatükist 1 pole kaasas")
    print()


def jah_ei(tekst):
    return "jah" if tekst else "ei"


def kuva_questid(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("QUESTID", peatukk1.ANSI_YELLOW)
    print("Põhiquest: peata Aethori langus enne, kui varemed sünnivad.")
    print()
    print("Põhisammud:")
    print(f"  - Kohtu Vuntsiga: {jah_ei(flags['chapter2_met_vunts'])}")
    print(f"  - Räägi põhja nõiaga: {jah_ei(flags['chapter2_met_witch'])}")
    print(f"  - Leia Hingelepingu jälg: {jah_ei(flags['chapter2_soul_contract_found'])}")
    print(f"  - Sõlmi Hingeleping: {jah_ei(flags['chapter2_soul_contract_made'])}")
    print()
    print("Usaldused:")
    print(f"  - Maa: {jah_ei(flags['chapter2_earth_trust'])}")
    print(f"  - Tuli: {jah_ei(flags['chapter2_fire_trust'])}")
    print(f"  - Õhk: {jah_ei(flags['chapter2_air_trust'])}")
    print(f"  - Vesi: {jah_ei(flags['chapter2_water_trust'])}")
    print()
    tehtud = [nimi for nimi, olemas in aethori_toendid(mangija) if olemas]
    print(f"Aethori pealike tõendid: {len(tehtud)}/{AETHORI_TOENDITE_ARV}")
    print(f"  - Vandemärk: {jah_ei(flags['chapter2_has_aethor_mark'])}")
    print(f"  - Vandemärgist keeldutud: {jah_ei(flags['chapter2_refused_aethor_mark'])}")
    print()
    print("Süsteemid:")
    print(f"  - Farlandsi luba: {jah_ei(flags['chapter2_has_farlands_pass'])}")
    print(f"  - Tormikompass: {jah_ei('Tormikompass' in leitud_artefaktid)}")
    print(f"  - Ajastute Mõõk: {jah_ei(on_ajastute_mook(leitud_artefaktid))}")
    print(f"  - Blacksmithi erisoov: {jah_ei(flags['chapter2_blacksmith_quest_done'])}")
    print(f"  - Musta turu heat: {flags['chapter2_black_market_heat']}")
    print(f"  - Aethori pinge: {aethori_pinge(flags)}")
    print(f"  - Päevi vanas maailmas: {flags['chapter2_days_spent']}")
    print(f"  - Avatud armor retseptid: {', '.join(flags['chapter2_unlocked_recipes']) or 'puuduvad'}")
    print(f"  - Tehtud kõrvalquestid: {len(flags['chapter2_completed_sidequests'])}/{len(SIDEQUESTID)}")
    print()
    print(f"Järgmine vihje: {_questi_vihje(mangija, leitud_artefaktid)}")
    peatukk1.pause()


SIDEQUESTID = {
    "pohhi": {
        "nimi": "Juure all sosistav metall",
        "tekst": "Aitad põhjametsas juurte vahele kinni jäänud maagilise soone vabaks.",
        "raha": 18,
        "materjalid": ["Metsajuur", "Carmot Dust"],
        "retsept": "Carmot Set",
    },
    "louna": {
        "nimi": "Vuntsi katkised kellad",
        "tekst": "Parandad Vuntsi kaitsekellad, et maja ümbrus vaiksemaks jääks.",
        "raha": 14,
        "materjalid": ["Kuivanud Ruunipael", "Banglum Chunk"],
        "retsept": "Banglum Set",
    },
    "ida": {
        "nimi": "Kai alla kadunud kast",
        "tekst": "Tõmbad veest välja kasti, mida sõdurid ametlikult ei tunnista.",
        "raha": 22,
        "materjalid": ["Soolakivi", "Aquarium Pearl"],
        "retsept": "Aquarium Set",
    },
    "laas": {
        "nimi": "Turu kristallivõlg",
        "tekst": "Aitad kaupmehel tagasi saada kristallid, mida loss ei taha arvele võtta.",
        "raha": 26,
        "materjalid": ["Kyber Crystal"],
        "retsept": "Kyber Set",
    },
    "kirre": {
        "nimi": "Soo all vaikiv südamik",
        "tekst": "Tood druiididele tagasi metallisüdamiku, mida maa ei tahtnud enam hoida.",
        "raha": 20,
        "materjalid": ["Maa Ruunikild", "Adamantite Ore"],
        "retsept": "Adamantite Set",
    },
    "kagu": {
        "nimi": "Leegisepise katse",
        "tekst": "Kannad tulest läbi metallitüki, mis ei tohi jahtuda.",
        "raha": 24,
        "materjalid": ["Tuleraud", "Mythril Ore"],
        "retsept": "Mythril Set",
    },
    "edel": {
        "nimi": "Õhusilla ankur",
        "tekst": "Seod ühe õhusilla ankrukivi uuesti tuule rütmi külge.",
        "raha": 24,
        "materjalid": ["Õhukas Kristall", "Orichalcum Ore"],
        "retsept": "Orichalcum Set",
    },
    "loe": {
        "nimi": "Tormi lukustatud pitser",
        "tekst": "Avad katakombis vana pitseri, mille taga oli tormist must metall.",
        "raha": 30,
        "materjalid": ["Katakombi Kild", "Stormyx Shard"],
        "retsept": "Stormyx Set",
    },
}


def sidequest(mangija, piirkond):
    flags = chapter2_flags(mangija)
    quest = SIDEQUESTID[piirkond]
    tehtud = flags["chapter2_completed_sidequests"]
    peatukk1.clear()
    peatukk1.section_title("KÕRVALQUEST", peatukk1.ANSI_GREEN)
    print(quest["nimi"])
    print()
    if piirkond in tehtud:
        print("See kõrvalquest on juba tehtud.")
        peatukk1.pause()
        return
    print(quest["tekst"])
    print()
    valik = input("Teed selle ära? (j/e): ").strip().lower()
    if valik != "j":
        print("Jätad selle hilisemaks.")
        peatukk1.pause()
        return
    tehtud.append(piirkond)
    lisa_vask_tasu(mangija, quest["raha"])
    for materjal in quest["materjalid"]:
        peatukk1.add_inventar(mangija, materjal)
    ava_retsept(mangija, quest["retsept"])
    moodu_paev(mangija)
    peatukk1.pause()


def aethori_pood(mangija):
    flags = chapter2_flags(mangija)
    while True:
        peatukk1.clear()
        peatukk1.section_title("AETHORI POOD", peatukk1.ANSI_YELLOW)
        print("Pood on täis hoolikalt sildistatud pudeleid, terasid ja matkavarustust.")
        print("Trader on nüüd päriselt siin, mitte lihtsalt juhuslik rändmüüja.")
        kuva_saldo(mangija)
        print()
        print("1 - Vaata ja osta kaupa")
        print("2 - Räägi traderiga")
        print("3 - Müü saaki")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "1":
            osta_poe_nimekirjast(mangija, CH2_OSTUD, "AETHORI POOD - KAUP")
        elif valik == "2":
            print("\"Aethoris liigub viimasel ajal imelikke tellimusi,\" pomiseb trader.")
            print("\"Tõrvikuid, soola, hauapitserite kriiti... keegi valmistub sügavaks retkeks.\"")
            print("\"Kui tood mulle soost, tulest või katakombidest midagi tervena tagasi, maksan ausat hinda,\" lisab ta.")
            if flags["chapter2_leaders_alerted"]:
                print("\"Ja nüüd küsivad lossi inimesed, kes sind näinud on,\" lisab ta vaiksemalt.")
                print("\"Kui liigud tõele lähemale, liiguvad nemad samuti.\"")
            peatukk1.pause()
        elif valik == "3":
            muugi_menuu(mangija, "AETHORI POOD - MÜÜK")
        elif valik == "0":
            return
        else:
            print("Vale valik.")
            peatukk1.pause()


def blacksmith(mangija):
    while True:
        peatukk1.clear()
        peatukk1.section_title("AETHORI BLACKSMITH", peatukk1.ANSI_YELLOW)
        print("Sepikojas helisevad metallid, mille nimed on vanemad kui praegune kuningas.")
        kuva_saldo(mangija)
        kuva_armor(mangija)
        print()
        print("1 - Osta ametlikke armor set'e")
        print("2 - Osta elementaalseid armor set'e")
        print("3 - Sepista avatud retseptidest")
        print("4 - Paranda aktiivset armorit")
        print("5 - Varusta armor inventarist")
        print("6 - Võta armor seljast (inventari)")
        print("7 - Müü aktiivne armor")
        print("8 - Sepa võlg")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "1":
            armor_poemenyy(mangija, "blacksmith", "BLACKSMITH - AETHORI METALLID")
        elif valik == "2":
            armor_poemenyy(mangija, "elementaal", "BLACKSMITH - ELEMENTAALSED SETID")
        elif valik == "3":
            armor_poemenyy(mangija, "recipe", "BLACKSMITH - AVATUD RETSEPTID")
        elif valik == "4":
            paranda_armorit(mangija)
        elif valik == "5":
            varusta_inventarist_armor(mangija)
        elif valik == "6":
            vota_armor_seljast(mangija)
        elif valik == "7":
            myy_aktiivne_armor(mangija)
        elif valik == "8":
            blacksmithi_quest(mangija)
        elif valik == "0":
            return
        else:
            print("Vale valik.")
            peatukk1.pause()


def adventurerite_gild(mangija):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("ADVENTURERITE GILD", peatukk1.ANSI_GREEN)
    print("Gildimajas lõhnavad õhk, nahk ja märjad mantlid.")
    print("Seinal ripuvad töökuulutused, kadunute lehed ja koletiste pearahad.")
    print()
    print("Vanem seikleja mõõdab sind pilguga.")
    print("\"Kui otsid ausat tööd, siis tööd siin jagub,\" ütleb ta.")
    print("\"Kui otsid tõde Aethori all, siis see töö ei jää ausaks kuigi kauaks.\"")
    if flags["chapter2_leaders_alerted"]:
        print("\"Linnavahid küsivad juba, miks sa nii palju valesid kohti külastad,\" lisab ta.")
    print()
    print("Siia saame hiljem lisada kõrvalülesanded ja bounty'd.")
    peatukk1.pause()


def lossi_eeskoda(mangija):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("AETHORI LOSS", peatukk1.ANSI_RED)
    print("Lossi eeskojas on vaikust rohkem kui peaks.")
    print("See ei ole pühalik vaikus. See on vaikus, kus liiga paljud inimesed kuulavad.")
    input("(edasi...)\n")
    if not flags["chapter2_leaders_alerted"]:
        print("Valvurid ei lase sind siseringi poole.")
        print("\"Lossil on hetkel muud mured kui rändurite küsimused,\" öeldakse sulle.")
        peatukk1.pause()
        return
    if not flags["chapter2_council_proven"]:
        aethori_noukogu(mangija)
        return
    print("Seekord ei saadeta sind kohe minema.")
    print("Selle asemel juhatatakse sind saali, kus ootab kuninga nõunik Arvel.")
    input("(edasi...)\n")
    print("\"Sa puudutad kohti, mis ei kuulu rahvale,\" ütleb Arvel.")
    print("\"Katakombid, druiidid, nõid, Farlands. Need ei ole rajad, mis hoiavad riiki koos.\"")
    input("(edasi...)\n")
    print("\"Kui tahad Aethorit päästa, lõpeta mineviku lahtikiskumine,\" lisab ta.")
    print("Tema toonist on aru saada, et ta ei usu isegi ise päriselt oma sõnu.")
    flags["chapter2_met_advisor"] = True
    peatukk1.pause()


def lossi_arhiiv(mangija):
    peatukk1.clear()
    peatukk1.section_title("LOSSI ARHIIV", peatukk1.ANSI_YELLOW)
    print("Arhiiviruum lõhnab tolmu, vaha ja peidetud hirmu järele.")
    print("Enamik riiuleid on korras. Just see teeb ühe puuduva koha liiga nähtavaks.")
    input("(edasi...)\n")
    print("Leiad katkise registrilehe:")
    print("\"Projekt Varileping viidi lossist välja pärast kuningliku käsu muudatust.\"")
    input("(edasi...)\n")
    print("\"Avalik versioon: hävitatud. Tegelik versioon: pitseeritud all-ladudes.\"")
    print("Keegi Aethori juhtidest teadis täpselt, mida katakombid endas hoiavad.")
    chapter2_flags(mangija)["chapter2_archive_found"] = True
    peatukk1.pause()


def lossi_kapteni_duell(mangija, leitud_artefaktid=None):
    flags = chapter2_flags(mangija)
    if flags.get("chapter2_captain_defeated", False):
        print("Lossikapten ei astu sulle enam ette.")
        peatukk1.pause()
        return

    peatukk1.clear()
    peatukk1.section_title("LOSSIKAPTEN", peatukk1.ANSI_RED)
    print("Lossi sisehoovis ootab sind kapten Raud.")
    print("\"Kui sa ei peatu, peatatakse sind jõuga,\" ütleb ta ilma vihata.")
    input("(edasi...)\n")
    vastane = {"nimi": "Kapten Raud", "elud": 85, "jou": 15}
    voidetud = lihtne_lahing(mangija, vastane, leitud_artefaktid=leitud_artefaktid)
    if voidetud:
        print("Kapten langeb ühele põlvele, aga ei palu armu.")
        print("\"Siis on tõesti hilja,\" ütleb ta vaikselt. \"Kui isegi sina jõudsid siia.\"")
        flags["chapter2_captain_defeated"] = True
    peatukk1.pause()


def laas(mangija, leitud_artefaktid, aktiveeritud_altarid):
    flags = chapter2_flags(mangija)
    maara_asukoht(mangija, "Aethor")
    while True:
        peatukk1.clear()
        peatukk1.section_title("LÄÄS - AETHOR", peatukk1.ANSI_CYAN)
        print("Aethor elab.")
        print("Turuplats sumiseb, kiviteed on terved ja inimeste nägudel pole veel varemete varje.")
        print("Kui teaksid vähem, tunduks kõik siin rahulik.")
        print()
        print("1 - Mine kuningriigi poodi")
        print("2 - Mine adventurerite gildi")
        print("3 - Jaluta turuplatsil")
        print("4 - Otsi musta turgu")
        print("5 - Mine lossi ette")
        print("6 - Mine blacksmithi juurde")
        print("9 - Kõrvalquest")
        print("10 - Mine kaevandusse")
        if flags.get("chapter2_met_advisor", False):
            print("7 - Otsi lossi arhiivi")
        if flags.get("chapter2_archive_found", False):
            print("8 - Astu vastu lossikaptenile")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "laas")
            aethori_pood(mangija)
        elif valik == "2":
            juhuslik_kohtumine(mangija, "laas")
            adventurerite_gild(mangija)
        elif valik == "3":
            juhuslik_kohtumine(mangija, "laas")
            print("Müüjad hüüavad, lapsed jooksevad läbi rahva ja kuskil mängib vilepill.")
            print("Ometi käib läbi rahvahulga närviline sosin: viimastel nädalatel kaovad inimesed maa alla.")
            if chapter2_flags(mangija)["chapter2_leaders_alerted"]:
                print("Veel vaiksem sosin käib ka sellest, et loss ei salli enam liigseid küsimusi.")
            peatukk1.pause()
        elif valik == "4":
            juhuslik_kohtumine(mangija, "laas")
            must_turg(mangija)
        elif valik == "5":
            juhuslik_kohtumine(mangija, "laas")
            lossi_eeskoda(mangija)
        elif valik == "6":
            juhuslik_kohtumine(mangija, "laas")
            blacksmith(mangija)
        elif valik == "7" and flags.get("chapter2_met_advisor", False):
            juhuslik_kohtumine(mangija, "laas")
            lossi_arhiiv(mangija)
        elif valik == "8" and flags.get("chapter2_archive_found", False):
            juhuslik_kohtumine(mangija, "laas")
            lossi_kapteni_duell(mangija, leitud_artefaktid)
        elif valik == "9":
            sidequest(mangija, "laas")
        elif valik == "10":
            kaevandus(mangija)
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def vuntsi_tugi(mangija, aktiveeritud_altarid):
    while True:
        peatukk1.clear()
        peatukk1.section_title("VUNTSI MAJA", peatukk1.ANSI_MAGENTA)
        print("Vunts on jätnud põrandale kriidiringid, raskused ja kummaliselt täpsed hingamisharjutused.")
        print("Siin saad treenida ilma energiat või manat kulutamata.")
        print()
        kuva_ressursid(mangija)
        print()
        print("1 - Tasuta treening ja meditatsioon (XP x1.5)")
        print("2 - Puhka Vuntsi juures")
        print("3 - Küsi nõu")
        print("0 - Lahku")
        valik = input("\nVali: ").strip()

        if valik == "1":
            treeni_peatukk2(mangija, aktiveeritud_altarid, tasuta=True, xp_kordaja=1.5, koht="Vuntsi maja")
        elif valik == "2":
            puhka(mangija, koht="Vuntsi maja", turvaline=True)
        elif valik == "3":
            print("\"Kui loss annab sulle märgi, ära arva, et mets seda samamoodi loeb,\" ütleb Vunts.")
            print("\"Märk võib avada ukse inimeste juures ja sulgeda pool sammu elementaalide ees.\"")
            peatukk1.pause()
        elif valik == "0":
            return
        else:
            print("Vale valik.")
            peatukk1.pause()


def vuntsi_maja(mangija, aktiveeritud_altarid):
    flags = chapter2_flags(mangija)
    if flags["chapter2_met_vunts"]:
        vuntsi_tugi(mangija, aktiveeritud_altarid)
        return

    peatukk1.clear()
    peatukk1.section_title("VUNTSI MAJA", peatukk1.ANSI_MAGENTA)
    print("Lõuna serval seisab üksik maja, mille aknad on seestpoolt kinni seotud nööride ja kellukestega.")
    print("Uks avaneb enne, kui jõuad koputada.")
    input("(edasi...)\n")
    print("Vunts istub laua taga, ümberringi lahtised märkmed, vanad kaardid ja liiga palju teesid.")
    print("\"Sa oled hiljaks jäänud,\" ütleb ta. \"Ja samas jõudsid täpselt õigel ajal.\"")
    input("(edasi...)\n")
    print("\"Aethor on terve ainult pealtvaates. Midagi on siin juba nihkes.\"")
    print("\"Teised tunnevad hirmu alles siis, kui müürid kukuvad. Mina tunnen seda enne pragusid.\"")
    input("(edasi...)\n")
    print("Ta ei ela linnas enam ammu.")
    print("Mitte sellepärast, et vihkaks inimesi, vaid sellepärast, et ta kuuleb liiga hästi, kui maailm valetab.")
    input("(edasi...)\n")
    print("\"Kui otsid vastuseid, siis mine põhja.\"")
    print("\"Vana puu juures elab keegi, kes räägib varjude ja hingede keelt paremini kui mina.\"")
    input("(edasi...)\n")
    print("\"Ja pea meeles,\" lisab Vunts.")
    print("\"Elementaalid ei näe sinus päästjat. Nad näevad sinus aethoorlast.\"")
    print("\"Sa pead neile näitama, et kasutad jõudu teisiti kui meie juhid seda tegid.\"")
    flags["chapter2_met_vunts"] = True
    peatukk1.pause()
    vuntsi_tugi(mangija, aktiveeritud_altarid)


def louna(mangija, leitud_artefaktid, aktiveeritud_altarid):
    maara_asukoht(mangija, "Vuntsi maja")
    while True:
        peatukk1.clear()
        peatukk1.section_title("LÕUNA - ERALDATUD MAJA", peatukk1.ANSI_MAGENTA)
        print("Linn jääb seljataha. Tuul on siin vaiksem ja rohi kasvab hooldamata radadel.")
        print("Ainsana seisab siin üks maja, liiga teadlikult teistest eemal.")
        print()
        print("1 - Mine majja")
        print("2 - Uuri ümbrust")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "louna")
            vuntsi_maja(mangija, aktiveeritud_altarid)
        elif valik == "2":
            juhuslik_kohtumine(mangija, "louna")
            print("Aia ümber on riputatud väikesed kellad ja luust tehtud märgid.")
            print("Need ei peleta loomi. Need on pandud millegi muu jaoks.")
            peatukk1.pause()
        elif valik == "9":
            sidequest(mangija, "louna")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def ida_sadam():
    peatukk1.clear()
    peatukk1.section_title("IDA - RANNAVÄGI", peatukk1.ANSI_BLUE)
    print("Rannas kõlavad käsud, saapad löövad vastu kaid ja odad välguvad merevalguses.")
    print("Paatide väe sõdurid valmistuvad justkui millekski, millest tavarahvas veel ei tea.")
    input("(edasi...)\n")
    print("Üks ohvitser peatab su.")
    print("\"Idameri ei anna viimasel ajal tagasi kõike, mis sinna läheb,\" ütleb ta.")
    print("\"Laevad jõuavad sadamasse tühjalt. Mõni jõuab tagasi ühe mehe võrra rohkem.\"")
    input("(edasi...)\n")
    print("Kai servas seisavad valmis paadid, aga ükski neist ei lähe praegu vabatahtlikult välja.")
    print("See ala sobib hiljem hästi nii mereretkedeks kui sõduritega seotud questideks.")
    peatukk1.pause()


def ida(mangija, leitud_artefaktid, aktiveeritud_altarid):
    flags = chapter2_flags(mangija)
    maara_asukoht(mangija, "Rand")
    while True:
        peatukk1.clear()
        peatukk1.section_title("IDA - RAND", peatukk1.ANSI_BLUE)
        print("Soolane tuul toob merelt kaasa rohkem rahutust kui värskust.")
        print("Kai ääres liiguvad Aethori paatide väe sõdurid pinges, nagu ootaksid nad halbu uudiseid.")
        print()
        print("1 - Mine sadamakaile")
        print("2 - Räägi sõduritega")
        print("3 - Küsi luba Farlandsi sõiduks")
        if flags["chapter2_has_farlands_pass"]:
            print("4 - Sõida Farlandsi")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "ida")
            ida_sadam()
        elif valik == "2":
            juhuslik_kohtumine(mangija, "ida")
            print("Sõdurid räägivad kadunud patrullidest, kummalisest udust ja sellest, et meri peegeldab vahel valet taevast.")
            peatukk1.pause()
        elif valik == "3":
            juhuslik_kohtumine(mangija, "ida")
            proovi_farlandsi_luba(mangija, leitud_artefaktid)
        elif valik == "4" and flags["chapter2_has_farlands_pass"]:
            juhuslik_kohtumine(mangija, "ida")
            maara_asukoht(mangija, "Farlands")
            mangija = farlands(mangija, leitud_artefaktid, aktiveeritud_altarid)
            maara_asukoht(mangija, "Rand")
        elif valik == "9":
            sidequest(mangija, "ida")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def pohja_noud(mangija):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("PÕHI - VANA PUU", peatukk1.ANSI_GREEN)
    print("Mets vaikib teistmoodi kui tavaline mets.")
    print("See ei ole tühi vaikus, vaid kuulav vaikus.")
    input("(edasi...)\n")
    print("Vana puu juured tõusevad maast nagu kivistunud lained.")
    print("Nende vahel seisab naine tumedas rüüs, nagu oleks ta puu varjust välja lõigatud.")
    input("(edasi...)\n")
    print("\"Sa tood endaga kaasa midagi, mis ei käi sinust sammu kaugusel,\" ütleb nõid.")
    print("\"Vari ei taha sind veel tappa. Ta tahab jääda.\"")
    input("(edasi...)\n")
    print("\"Kui otsid viisi, et ta sind kuulaks, pead sa enne õppima, mis seob hinge ja käsu.\"")
    print("\"Seda ei leita turult ega paleest. Seda maetakse.\"")
    input("(edasi...)\n")
    print("Nõid ei ütle veel nime, aga on selge, et ta mõtleb katakombe.")
    input("(edasi...)\n")
    print("\"Aethori juhid ei karda varje,\" ütleb ta lõpuks.")
    print("\"Nad kardavad seda hetke, kui keegi seob vana vea päris nimedega.\"")
    flags["chapter2_met_witch"] = True
    uuenda_juhtide_kahtlust(mangija)
    peatukk1.pause()


def pohhi(mangija, leitud_artefaktid, aktiveeritud_altarid):
    maara_asukoht(mangija, "Põhjamets")
    while True:
        peatukk1.clear()
        peatukk1.section_title("PÕHI - METS", peatukk1.ANSI_GREEN)
        print("Aethori põhjamets on vana ja liiga elus.")
        print("Tee keerab sammude all, nagu otsustaks mets alles nüüd, kas lasta sul edasi minna.")
        print()
        print("1 - Mine vana puu juurde")
        print("2 - Kuula metsa")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "pohhi")
            pohja_noud(mangija)
        elif valik == "2":
            juhuslik_kohtumine(mangija, "pohhi")
            print("Lehtede sahinas on hetkeks tunne, nagu keegi liiguks sinuga samas rütmis, aga mitte päris sinu kõrval.")
            print("Kui Shadow siia esimest korda päriselt sisse tuleb, on see koht selleks ideaalne.")
            peatukk1.pause()
        elif valik == "9":
            sidequest(mangija, "pohhi")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def kirre(mangija, leitud_artefaktid, aktiveeritud_altarid):
    flags = chapter2_flags(mangija)
    maara_asukoht(mangija, "Soomaa")
    while True:
        peatukk1.clear()
        peatukk1.section_title("KIRRE - SOOMAA", peatukk1.ANSI_GREEN)
        print("Kirde suunas vajub maa vette ja uttu.")
        print("Soo ei ole tühi. Ta on jälgiv, vana ja täis maasse lõigatud ruune.")
        print()
        print("1 - Otsi druiide")
        print("2 - Uuri ruunikive")
        print("3 - Proovi võita maa usaldus")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "kirre")
            print("Druiidid ei tule sinu juurde kohe välja.")
            print("Kõigepealt liigub udu, siis kostab puukeppide kolks ja alles siis kuuled häält.")
            print("\"Kui maa sind veel kannab, siis tal on põhjus,\" ütleb keegi nähtamatult.")
            print("\"Aga põhjus võib muutuda, kui su käed käituvad nagu teiste aethoorlaste omad.\"")
            flags["chapter2_met_druids"] = True
            peatukk1.pause()
        elif valik == "2":
            juhuslik_kohtumine(mangija, "kirre")
            print("Ruunid on sügavad ja kulunud, aga elavad veel.")
            print("Need räägivad maa tasakaalust, sidemetest ja sellest, kuidas üks katkine element võib tirida teised kaasa.")
            peatukk1.pause()
        elif valik == "3":
            juhuslik_kohtumine(mangija, "kirre")
            druiidide_katse(mangija)
            uuenda_juhtide_kahtlust(mangija)
        elif valik == "9":
            sidequest(mangija, "kirre")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def kagu(mangija, leitud_artefaktid, aktiveeritud_altarid):
    maara_asukoht(mangija, "Inferno")
    while True:
        peatukk1.clear()
        peatukk1.section_title("KAGU - INFERNO", peatukk1.ANSI_RED)
        print("Kagu suunas muutub maa mustaks ja õhk virvendab kuumusest.")
        print("See koht ei põle juhuslikult. Siin on tuli endale pesa teinud.")
        print()
        print("1 - Mine kõrbenud servale")
        print("2 - Uuri tulejälgi")
        print("3 - Proovi võita tule usaldus")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "kagu")
            print("Leegid ei tõuse siin ainult üles, vaid keeravad vahel nagu elusad asjad sinu poole.")
            print("Inferno südamik on veel kaugemal ja ootab, et keegi sinna liiga julgelt astuks.")
            print("Tuleolendid ei näe sinus külalist. Nad näevad sinus selle rahva nägu, kes tahtis tuld kamandada.")
            peatukk1.pause()
        elif valik == "2":
            juhuslik_kohtumine(mangija, "kagu")
            print("Tulejäljed ei käitu nagu tavaline põleng.")
            print("Mõni leek on põletanud kivi, aga jätnud kuivanud rohu puutumata.")
            peatukk1.pause()
        elif valik == "3":
            juhuslik_kohtumine(mangija, "kagu")
            inferno_katse(mangija)
        elif valik == "9":
            sidequest(mangija, "kagu")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def edel(mangija, leitud_artefaktid, aktiveeritud_altarid):
    maara_asukoht(mangija, "Õhuriik")
    while True:
        peatukk1.clear()
        peatukk1.section_title("EDEL - ÕHURIIK", peatukk1.ANSI_CYAN)
        print("Edela taevas ripuvad kiviplatvormid, sillad ja heledad tornid, mida maapind ei kanna.")
        print("Õhuriik ei alga väravast, vaid kõrgusest.")
        print()
        print("1 - Vaata õhusildu alt")
        print("2 - Kuula taevarahva kohta")
        print("3 - Proovi võita õhu usaldus")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "edel")
            print("Mõni sild liigub tuules nagu oleks ta elus.")
            print("Ilma loata või õige abita sa sinna veel ei tõuse.")
            print("Õhuvaimud hoiavad kõrgustest eemal kõik, kes lõhnavad Aethori vana käsu järele.")
            peatukk1.pause()
        elif valik == "2":
            juhuslik_kohtumine(mangija, "edel")
            print("Räägitakse, et taevarahvas ei lase maapealseid enda sekka enne, kui nood on tõestanud kerget sammu ja puhast kavatsust.")
            peatukk1.pause()
        elif valik == "3":
            juhuslik_kohtumine(mangija, "edel")
            ohuriigi_katse(mangija)
        elif valik == "9":
            sidequest(mangija, "edel")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def loe(mangija, leitud_artefaktid, aktiveeritud_altarid):
    maara_asukoht(mangija, "Keelatud katakombid")
    while True:
        peatukk1.clear()
        peatukk1.section_title("LOE - KEELATUD KATAKOMBID", peatukk1.ANSI_YELLOW)
        print("Loode servas vajub maa järk-järgult alla kivist treppideks ja pitseeritud käikudeks.")
        print("Siin algavad Keelatud katakombid, kuhu Aethor mattis selle, mida ta ei tahtnud enam mäletada.")
        print()
        print("1 - Mine ülemisse käiku")
        print("2 - Uuri pitserisaali ust")
        print("3 - Uuri katakombide ajalugu")
        print("4 - Proovi sõlmida Hingeleping")
        print("5 - Kasuta Ajastute Mõõka ajapraol")
        print("9 - Kõrvalquest")
        print("0 - Tagasi kaardile")
        valik = input("\nVali: ").strip()

        if valik == "1":
            juhuslik_kohtumine(mangija, "loe")
            print("Esimesed käigud on veel avarad, aga sügavamal kisub lagi madalaks ja õhk seisvaks.")
            print("See on selgelt peatüki üks suuremaid alasid.")
            peatukk1.pause()
        elif valik == "2":
            juhuslik_kohtumine(mangija, "loe")
            if chapter2_flags(mangija)["chapter2_met_witch"]:
                katakombi_avastus(mangija)
            else:
                print("Pitserisaali uksel on võõrad märgid.")
                print("Ilma nõia sõnadeta ei oska sa veel neid õigesse järjekorda mõelda.")
                peatukk1.pause()
        elif valik == "3":
            juhuslik_kohtumine(mangija, "loe")
            kuva_peatuki_lore()
        elif valik == "4":
            juhuslik_kohtumine(mangija, "loe")
            hingelepingu_rituaal(mangija)
        elif valik == "5":
            ajastute_mooga_pragu(mangija, leitud_artefaktid)
        elif valik == "9":
            sidequest(mangija, "loe")
        elif valik == "0":
            return mangija
        else:
            print("Vale valik.")
            peatukk1.pause()


def shadow_menu(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    if not flags["chapter2_soul_contract_made"]:
        print("Shadow ei kuula sind veel. Hingeleping peab enne sündima.")
        peatukk1.pause()
        return

    while True:
        peatukk1.clear()
        peatukk1.section_title("SHADOW", peatukk1.ANSI_MAGENTA)
        print("Vari ei seisa enam sinust eemal. Ta ootab, et sa küsiksid õigesti.")
        print()
        print("1 - Küsi vihjet")
        print("2 - Palu varjukaitset")
        print("3 - Kuula, mida ta mäletab")
        print("0 - Tagasi")
        valik = input("\nVali: ").strip()

        if valik == "1":
            print(f"Shadow ütleb: \"{_questi_vihje(mangija, leitud_artefaktid)}\"")
            peatukk1.pause()
        elif valik == "2":
            taastamine = min(18, max(6, flags.get("chapter2_original_joukus", 0) // 12))
            mangija["elud"] += taastamine
            print(f"Shadow tõmbab su ümbert osa survest endasse. Taastad {taastamine} elupunkti.")
            peatukk1.pause()
        elif valik == "3":
            print("\"Katakombid ei hoidnud ainult surnuid,\" ütleb Shadow.")
            print("\"Need hoidsid alles käske, mida Aethor kartis iseenda nimega nimetada.\"")
            peatukk1.pause()
        elif valik == "0":
            return
        else:
            print("Vale valik.")
            peatukk1.pause()


def _mapi_silt(mangija, nimi, silt):
    return f">{silt}<" if leia_asukoht(mangija) == nimi else silt


def kuva_maailmakaart(mangija):
    varv = peatukk1.ANSI_GREEN
    pohhi = _mapi_silt(mangija, "Põhjamets", "[1] PÕHI")
    loe = _mapi_silt(mangija, "Keelatud katakombid", "[8] LOE")
    kirre = _mapi_silt(mangija, "Soomaa", "[5] KIRRE")
    laas = _mapi_silt(mangija, "Aethor", "[4] LÄÄS")
    ida = _mapi_silt(mangija, "Rand", "[3] IDA")
    edel = _mapi_silt(mangija, "Õhuriik", "[7] EDEL")
    kagu = _mapi_silt(mangija, "Inferno", "[6] KAGU")
    louna = _mapi_silt(mangija, "Vuntsi maja", "[2] LÕUNA")
    farlands = ">Farlands<" if leia_asukoht(mangija) == "Farlands" else "Farlands"
    print(peatukk1.colorize("╔══════════════════════════════════════╗", varv, bold=True))
    print(peatukk1.colorize("║         AETHORI MAAILMAKAART         ║", varv, bold=True))
    print(peatukk1.colorize("╠══════════════════════════════════════╣", varv, bold=True))
    print(peatukk1.colorize(f"║            {pohhi:^26}              ║", varv))
    print(peatukk1.colorize(f"║       {loe:<12} │ {kirre:<12}       ║", varv))
    print(peatukk1.colorize("║                 ╲  │  ╱              ║", varv))
    print(peatukk1.colorize(f"║      {laas:<10} ── AETHOR ── {ida:<10}║", varv, bold=True))
    print(peatukk1.colorize("║                 ╱  │  ╲              ║", varv))
    print(peatukk1.colorize(f"║      {edel:<11}│ {kagu:<12}         ║", varv))
    print(peatukk1.colorize(f"║               {louna:^18}           ║", varv))
    print(peatukk1.colorize(f"║  Ida meri viib edasi: {farlands:<15}║", varv))
    print(peatukk1.colorize("╚══════════════════════════════════════╝", varv, bold=True))
    print()


def _questi_vihje(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    if not flags["chapter2_met_vunts"]:
        return "Külasta lõunas Vuntsi maja."
    if not flags["chapter2_met_witch"]:
        return "Mine põhja vana puu juurde ja otsi nõida."
    if not flags["chapter2_earth_trust"]:
        return "Tõesta druiididele, et kasutad maa-jõudu õigesti."
    if flags["chapter2_leaders_alerted"] and not flags["chapter2_council_proven"]:
        return "Aethori pealikud tahavad mitut tõendit, enne kui sind seotakse nende nimega."
    if not flags["chapter2_fire_trust"]:
        return "Infernos pead näitama, et sa ei tulnud tuld aheldama."
    if not flags["chapter2_air_trust"]:
        return "Õhuriik ootab, et astuksid tuulega, mitte tema vastu."
    if not flags["chapter2_asked_farlands"] and "Tormikompass" in leitud_artefaktid:
        return "Uuri Aethorit, et saada luba Farlandsi minekuks."
    if flags["chapter2_asked_farlands"] and not flags["chapter2_has_farlands_pass"]:
        return "Võida rohkem usaldust. Rannavalve ei vii veel Farlandsi."
    if flags["chapter2_met_witch"] and not flags["chapter2_soul_contract_found"]:
        return "Otsi Keelatud katakombidest Hingelepingu jälgi."
    if flags["chapter2_soul_contract_found"] and not flags["chapter2_has_farlands_pass"]:
        return "Sul on lepingujälg käes. Otsi, kuidas juhid seda kardavad."
    if flags["chapter2_has_farlands_pass"] and not flags["chapter2_water_trust"]:
        return "Farlands on avatud. Tõesta merele, et sa ei tulnud vallutama."
    if not flags["chapter2_soul_contract_made"]:
        return "Kogu aspektid ja alkeemilised materjalid, et sõlmida Hingeleping."
    return "Kogu infot Aethori kohta ja otsi teed edasi."


def kuva_hud(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    varv = peatukk1.ANSI_YELLOW
    asukoht = leia_asukoht(mangija)
    tormikompass = "aktiivne" if "Tormikompass" in leitud_artefaktid else "puudub"
    ajastute_mook = "kaasas" if on_ajastute_mook(leitud_artefaktid) else "puudub"
    if flags["chapter2_soul_contract_made"]:
        shadow = "sinu kaaslane"
        hingeleping = "sõlmitud"
    elif flags["chapter2_soul_contract_found"]:
        shadow = "seotud lepinguga"
        hingeleping = "leitud"
    elif flags["chapter2_shadow_met"]:
        shadow = "rääkinud sinuga"
        hingeleping = "jäljed leitud"
    elif flags["chapter2_met_witch"]:
        shadow = "ootab sidumist"
        hingeleping = "jäljed leitud"
    else:
        shadow = "jälgib eemalt"
        hingeleping = "leidmata"
    if flags["chapter2_has_farlands_pass"]:
        farlands = "luba olemas"
    elif flags["chapter2_asked_farlands"]:
        farlands = "keelatud"
    else:
        farlands = "lukus"
    print(peatukk1.colorize("╔══════════════════════════════════════╗", varv, bold=True))
    print(peatukk1.colorize("║                HUD                   ║", varv, bold=True))
    print(peatukk1.colorize("╠══════════════════════════════════════╣", varv, bold=True))
    print(peatukk1.colorize(f"║ Asukoht: {asukoht:<28}║", varv))
    print(peatukk1.colorize(f"║ Shadow: {shadow:<29}║", varv))
    print(peatukk1.colorize(f"║ Tormikompass: {tormikompass:<24}║", varv))
    print(peatukk1.colorize(f"║ Ajastute Mõõk: {ajastute_mook:<21}║", varv))
    print(peatukk1.colorize(f"║ Hingeleping: {hingeleping:<23}║", varv))
    print(peatukk1.colorize(f"║ Farlands: {farlands:<27}║", varv))
    if mangija.get("kaart") is not None:
        saldo = peatukk1.kaart_saldo_str(mangija["kaart"])
        print(peatukk1.colorize(f"║ Rahakott: {saldo:<28}║", varv))
    energia_line = f"Energia: {flags['chapter2_energia']}/{arvuta_max_energia(mangija)}"
    mana_line = f"Mana: {flags['chapter2_mana']}/{arvuta_max_mana(mangija)}"
    paev_line = f"Päevad vanas maailmas: {flags['chapter2_days_spent']}"
    pinge_line = f"Aethori pinge: {aethori_pinge(flags)}"
    print(peatukk1.colorize(f"ā•‘ {energia_line:<36} ā•‘", varv))
    print(peatukk1.colorize(f"ā•‘ {mana_line:<36} ā•‘", varv))
    print(peatukk1.colorize(f"ā•‘ {paev_line:<36} ā•‘", varv))
    print(peatukk1.colorize(f"ā•‘ {pinge_line:<36} ā•‘", varv))
    armor = aktiivne_armor(mangija)
    if armor:
        armor_line = f"Armor: {armor['nimi']} {armor['durability']}/{armor['max_durability']}"
    else:
        armor_line = "Armor: puudub"
    print(peatukk1.colorize(f"ā•‘ {armor_line:<36} ā•‘", varv))
    if flags["chapter2_original_joukus"]:
        jou_line = f"Jõud: {mangija['joukus']} / varem {flags['chapter2_original_joukus']}"
        print(peatukk1.colorize(f"║ {jou_line:<36} ║", varv))
    vihje = _questi_vihje(mangija, leitud_artefaktid)
    print(peatukk1.colorize("╠══════════════════════════════════════╣", varv, bold=True))
    print(peatukk1.colorize("║ Järgmine vihje:                      ║", varv))
    for rida in _murra_hud_ridadeks(vihje):
        print(peatukk1.colorize(f"║ {rida:<36} ║", varv))
    print(peatukk1.colorize("╚══════════════════════════════════════╝", varv, bold=True))
    print()


def vaata_maailmakaarti(mangija):
    peatukk1.clear()
    peatukk1.section_title("MAAILMAKAART", peatukk1.ANSI_GREEN)
    print("Kaardil on noolega märgitud su viimane teadaolev asukoht.")
    print()
    kuva_maailmakaart(mangija)
    peatukk1.pause()


def kuva_hud(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    varv = peatukk1.ANSI_YELLOW
    asukoht = leia_asukoht(mangija)
    tormikompass = "aktiivne" if "Tormikompass" in leitud_artefaktid else "puudub"
    ajastute_mook = "kaasas" if on_ajastute_mook(leitud_artefaktid) else "puudub"

    if flags["chapter2_soul_contract_made"]:
        shadow = "sinu kaaslane"
        hingeleping = "sõlmitud"
    elif flags["chapter2_soul_contract_found"]:
        shadow = "seotud lepinguga"
        hingeleping = "leitud"
    elif flags["chapter2_shadow_met"]:
        shadow = "rääkinud sinuga"
        hingeleping = "jäljed leitud"
    elif flags["chapter2_met_witch"]:
        shadow = "ootab sidumist"
        hingeleping = "jäljed leitud"
    else:
        shadow = "jälgib eemalt"
        hingeleping = "leidmata"

    if flags["chapter2_has_farlands_pass"]:
        farlands = "luba olemas"
    elif flags["chapter2_asked_farlands"]:
        farlands = "keelatud"
    else:
        farlands = "lukus"

    laius = 58

    def hud_rida(silt, vaartus):
        sisu = f"{silt}: {vaartus}" if silt else str(vaartus)
        if len(sisu) > laius - 4:
            sisu = sisu[:laius - 7] + "..."
        print(peatukk1.colorize(f"| {sisu:<{laius - 4}} |", varv))

    print(peatukk1.colorize("+" + "-" * (laius - 2) + "+", varv, bold=True))
    print(peatukk1.colorize(f"| {'HUD':^{laius - 4}} |", varv, bold=True))
    print(peatukk1.colorize("+" + "-" * (laius - 2) + "+", varv, bold=True))
    hud_rida("Asukoht", asukoht)
    hud_rida("Shadow", shadow)
    hud_rida("Tormikompass", tormikompass)
    hud_rida("Ajastute Mõõk", ajastute_mook)
    hud_rida("Hingeleping", hingeleping)
    hud_rida("Farlands", farlands)
    if mangija.get("kaart") is not None:
        hud_rida("Rahakott", peatukk1.kaart_saldo_str(mangija["kaart"]))
    hud_rida("Energia", f"{flags['chapter2_energia']}/{arvuta_max_energia(mangija)}")
    hud_rida("Mana", f"{flags['chapter2_mana']}/{arvuta_max_mana(mangija)}")
    hud_rida("Päevad vanas maailmas", flags["chapter2_days_spent"])
    hud_rida("Aethori pinge", aethori_pinge(flags))

    armor = aktiivne_armor(mangija)
    if armor:
        armor_line = f"{armor['nimi']} {armor['durability']}/{armor['max_durability']}"
    else:
        armor_line = "puudub"
    hud_rida("Armor", armor_line)

    if flags["chapter2_original_joukus"]:
        hud_rida("Jõud", f"{mangija['joukus']} / varem {flags['chapter2_original_joukus']}")

    print(peatukk1.colorize("+" + "-" * (laius - 2) + "+", varv, bold=True))
    hud_rida("Järgmine vihje", "")
    for rida in _murra_hud_ridadeks(_questi_vihje(mangija, leitud_artefaktid), laius - 6):
        hud_rida("", rida)
    print(peatukk1.colorize("+" + "-" * (laius - 2) + "+", varv, bold=True))
    print()


def vaata_hud(mangija, leitud_artefaktid):
    peatukk1.clear()
    peatukk1.section_title("HUD", peatukk1.ANSI_YELLOW)
    kuva_hud(mangija, leitud_artefaktid)
    peatukk1.pause()


def _murra_hud_ridadeks(tekst, laius=36):
    sonad = tekst.split()
    read = []
    praegune = ""
    for sona in sonad:
        kandidaat = sona if not praegune else f"{praegune} {sona}"
        if len(kandidaat) <= laius:
            praegune = kandidaat
        else:
            read.append(praegune)
            praegune = sona
    if praegune:
        read.append(praegune)
    return read[:2]


def lae_teine_save():
    vana_save = peatukk1.SAVE_FILE
    vana_meta = dict(peatukk1.SAVE_META)

    if peatukk1._vali_profiil("lae") is None:
        peatukk1.SAVE_FILE = vana_save
        peatukk1.SAVE_META = vana_meta
        return None, None, None

    mangija, leitud_artefaktid, aktiveeritud_altarid = peatukk1.lae_mang()
    if mangija is None:
        peatukk1.SAVE_FILE = vana_save
        peatukk1.SAVE_META = vana_meta
        return None, None, None

    return mangija, leitud_artefaktid, aktiveeritud_altarid


def koik_elementaalid_usaldavad(flags):
    return (
        flags["chapter2_earth_trust"]
        and flags["chapter2_fire_trust"]
        and flags["chapter2_air_trust"]
        and flags["chapter2_water_trust"]
    )


def ukski_elementaal_ei_usalda(flags):
    return (
        not flags["chapter2_earth_trust"]
        and not flags["chapter2_fire_trust"]
        and not flags["chapter2_air_trust"]
        and not flags["chapter2_water_trust"]
    )


def world_trust_valmis(flags):
    return koik_elementaalid_usaldavad(flags)


def havingu_lopp_valmis(flags):
    return flags["chapter2_has_aethor_mark"] and ukski_elementaal_ei_usalda(flags)


def ohverduse_lopp_valmis(flags):
    return world_trust_valmis(flags) and flags["chapter2_refused_aethor_mark"]


def shadowlord_lopp_valmis(flags):
    return (
        flags["chapter2_soul_contract_made"]
        and flags["chapter2_has_aethor_mark"]
        and world_trust_valmis(flags)
    )


def valitseja_lopp_valmis(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    return (
        not flags["chapter2_has_aethor_mark"]
        and world_trust_valmis(flags)
        and on_ajastute_mook(leitud_artefaktid)
        and kannab_armorit(mangija, "Metallurgium Set")
    )


def finaali_debug_readout(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    print()
    print("[DEBUG] Finaali seis")
    print(f"- Häving valmis: {havingu_lopp_valmis(flags)}")
    print(f"- Shadowlord valmis: {shadowlord_lopp_valmis(flags)}")
    print(f"- Ohverdus valmis: {ohverduse_lopp_valmis(flags)}")
    print(f"- Valitseja valmis: {valitseja_lopp_valmis(mangija, leitud_artefaktid)}")
    print(f"- Kõik usaldused: {world_trust_valmis(flags)}")
    print(f"- Aethori märk: {flags['chapter2_has_aethor_mark']}")
    print(f"- Märgist keeldutud: {flags['chapter2_refused_aethor_mark']}")
    print(f"- Hingeleping: {flags['chapter2_soul_contract_made']}")
    print(f"- Metallurgium seljas: {kannab_armorit(mangija, 'Metallurgium Set')}")
    print(f"- Ajastute Mõõk olemas: {on_ajastute_mook(leitud_artefaktid)}")


def sea_chapter3_carryover(flags, ending_type):
    flags["chapter3_origin"] = ending_type
    if ending_type == "ohverdus_vari":
        flags["chapter2_gateway_ch3"] = True
        flags["chapter3_shadow_rank"] = 2
        flags["chapter3_world_tone"] = "darkening"
    elif ending_type == "shadowlord":
        flags["chapter2_gateway_ch3"] = True
        flags["chapter3_shadow_rank"] = 3
        flags["chapter3_world_tone"] = "dominated"
    elif ending_type == "valitseja":
        flags["chapter3_shadow_rank"] = 1
        flags["chapter3_world_tone"] = "controlled"
    elif ending_type == "ohverdus_enes":
        flags["chapter3_shadow_rank"] = 0
        flags["chapter3_world_tone"] = "saved"
    elif ending_type == "having":
        flags["chapter3_shadow_rank"] = 0
        flags["chapter3_world_tone"] = "collapsed"


def kuva_chapter3_hook(flags):
    if not flags.get("chapter2_gateway_ch3"):
        return
    print()
    print("PEATÜKK 3 HOOK:")
    print("Pimeduse värav avaneb.")
    print(f"Päritolu: {flags.get('chapter3_origin')}")
    print(f"Varju tase: {flags.get('chapter3_shadow_rank')}")
    print(f"Maailma toon: {flags.get('chapter3_world_tone')}")


def hea_lopp_valmis(mangija):
    flags = chapter2_flags(mangija)
    return (
        world_trust_valmis(flags)
        and flags["chapter2_refused_aethor_mark"]
        and not flags["chapter2_has_aethor_mark"]
    )


def loppu_puuduvad_sammud(mangija):
    flags = chapter2_flags(mangija)
    sammud = []
    if not world_trust_valmis(flags):
        sammud.append("Kogu koik 4 elementaali usaldust.")
    if not flags["chapter2_refused_aethor_mark"] and not flags["chapter2_has_aethor_mark"]:
        sammud.append("Tee valik Aethori vandemargi osas.")
    return sammud


def _vana_endingut(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("PEATÜKI LÕPP", peatukk1.ANSI_MAGENTA)

    if flags["chapter2_ending_seen"]:
        print("Selle peatüki lõpp on juba nähtud selles save'is.")
        peatukk1.pause()
        return True

    if flags["chapter2_has_aethor_mark"]:
        print("Aethori Vandemärk on sinu küljes.")
        print("Lossi pealikud nimetasid seda usalduseks, aga elementaalid kuulsid selles käsku.")
        input("(edasi...)\n")
        print("Mida rohkem sa nende nime all liigud, seda kiiremini maailm kokku tõmbub.")
        print("Maa vaikib. Tuli vihastub. Õhk eemaldub. Vesi ei vasta.")
        input("(edasi...)\n")
        print("Aethor püsib veel ühe päeva kauem püsti, aga valel põhjusel.")
        print("See ei ole päästmine. See on vana vea kordamine.")
        print()
        print("HALB ENDING: AETHORI PITSEeritud LANGUS")
        flags["chapter2_ending_seen"] = True
        peatukk1.pause()
        return True

    print("Peatükk ei ole veel lõpu jaoks valmis.")
    print()
    print("Praegu on valmis ainult halb lõpp.")
    print("Halb lõpp avaneb, kui seod end Aethori Vandemärgiga ja aeg liigub edasi.")
    peatukk1.pause()
    return False


def kaivita_finaali_sundmus(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    peatukk1.clear()
    peatukk1.section_title("AETHOR MURDUB", peatukk1.ANSI_MAGENTA)

    if flags["chapter2_ending_seen"]:
        print("Selle peatuki lopp on juba nahtud selles save'is.")
        peatukk1.pause()
        return True

    if havingu_lopp_valmis(flags):
        print("Aethori vandemärk surub ajajoone halvimasse seisu.")
        print("Elementaalid ei usalda sind ja maailmal puudub tasakaalu ankur.")
        input("(edasi...)\n")
        print("Varjud võtavad kontrolli. Ajalõhe tempel laguneb seestpoolt.")
        print("Aethor kaob koos maailmaga.")
        print()
        print("HÄVINGU ENDING: HÄVINGU LÕPP")
        flags["chapter2_ending_seen"] = True
        flags["chapter2_ending_type"] = "having"
        sea_chapter3_carryover(flags, "having")
        peatukk1.pause()
        return True

    if shadowlord_lopp_valmis(flags):
        print("Sul on hingeleping, vandemärk ja kõik elementaalide usaldused.")
        print("Need jõud ei tasakaalustu. Need rebivad su varju sisse.")
        input("(edasi...)\n")
        print("Vari neelab su nime, naha ja tahte.")
        print("Aethor ei lange, aga saab uue isanda.")
        print()
        print("SHADOW ENDING: SHADOWLORD")
        flags["chapter2_ending_seen"] = True
        flags["chapter2_ending_type"] = "shadowlord"
        sea_chapter3_carryover(flags, "shadowlord")
        kuva_chapter3_hook(flags)
        peatukk1.pause()
        return True

    if ohverduse_lopp_valmis(flags):
        while True:
            peatukk1.section_title("OHVERDUSE VALIK", peatukk1.ANSI_GREEN)
            print("Maailma saab päästa ainult ohverduse hinnaga.")
            print("Vali, kes kaob ajaloost.")
            print("1 - Ohverdan iseenda")
            print("2 - Ohverdan varju")
            valik = input("\nVali: ").strip()

            if valik == "1":
                print("Sa seod ajajoone oma olemasoluga ja lased sellel siis kustuda.")
                print("Maailm jääb püsima. Sinu nimi hajub vaikuseks.")
                print()
                print("OHVERDUSE ENDING: VIIMANE VALGUS")
                flags["chapter2_ending_seen"] = True
                flags["chapter2_ending_type"] = "ohverdus_enes"
                sea_chapter3_carryover(flags, "ohverdus_enes")
                peatukk1.pause()
                return True

            if valik == "2":
                print("Sa ohverdad varju, aga pimedus leiab tee sinu sisse.")
                print("Maailm pääseb, kuid langeb tasapisi pimedusse.")
                print("Sinust saab uus vari ning tee peatükki 3 avaneb.")
                print()
                print("VARJU ENDING: PIMEDUSE VÄRAV")
                flags["chapter2_ending_seen"] = True
                flags["chapter2_ending_type"] = "ohverdus_vari"
                sea_chapter3_carryover(flags, "ohverdus_vari")
                kuva_chapter3_hook(flags)
                peatukk1.pause()
                return True

            print("Vali 1 või 2.")

    if valitseja_lopp_valmis(mangija, leitud_artefaktid):
        print("Ajastute Mõõk vastab su käele. Metallurgium hoiab su keha koos.")
        print("Sul on kõik usaldused, aga sa ei vali tasakaalu.")
        input("(edasi...)\n")
        print("Sa kirjutad loo ümber nii, et Aethor ei murdu - ta allub.")
        print("Maailm jääb alles, kuid elab nüüd su kontrolli all.")
        print()
        print("VALITSEJA ENDING: AJASTUTE VALITSEJA")
        flags["chapter2_ending_seen"] = True
        flags["chapter2_ending_type"] = "valitseja"
        sea_chapter3_carryover(flags, "valitseja")
        peatukk1.pause()
        return True

    return False


def finaali_sundmus_valmis(mangija, leitud_artefaktid):
    flags = chapter2_flags(mangija)
    if flags["chapter2_ending_seen"]:
        return False
    if havingu_lopp_valmis(flags):
        return True
    if shadowlord_lopp_valmis(flags):
        return True
    if ohverduse_lopp_valmis(flags):
        return True
    if valitseja_lopp_valmis(mangija, leitud_artefaktid):
        return True
    return False


def pohikaart(mangija, leitud_artefaktid, aktiveeritud_altarid):
    while True:
        uuenda_juhtide_kahtlust(mangija)
        juhtide_vastusamm(mangija)
        if finaali_sundmus_valmis(mangija, leitud_artefaktid):
            if kaivita_finaali_sundmus(mangija, leitud_artefaktid):
                return
        peatukk1.clear()
        peatukk1.section_title("AETHOR", peatukk1.ANSI_CYAN)
        peatukk1.print_status_card(mangija)
        flags = chapter2_flags(mangija)
        print(f"Päevi vanas maailmas: {flags['chapter2_days_spent']}")
        kuva_ressursid(mangija)
        kuva_armor(mangija)
        kuva_aethori_pinge(mangija)
        if flags.get("chapter2_debug_overlay", False):
            finaali_debug_readout(mangija, leitud_artefaktid)
        print()
        print("Sa seisad maailmas, mis pole veel langenud.")
        print("Kaart on tuttav, aga Aethor ise ei ole enam vare.")
        print()
        print("Liikumine:")
        print("1 - Põhi    2 - Lõuna   3 - Ida    4 - Lääs")
        print("5 - Kirre   6 - Kagu    7 - Edel   8 - Loe")
        print()
        print("Menüü:")
        print("M - Maailmakaart")
        print("H - HUD")
        print("A - Artefaktid ja elemendid")
        print("Q - Questid")
        print("I - Inventar")
        print("E - Kasuta taastavat eset")
        print("T - Treeni")
        print("P - Puhka")
        print("K - Statistika")
        print("V - Vari")
        print("S - Salvesta mäng")
        print("L - Lae mäng")
        print("0 - Välju")
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
            mangija = kirre(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "6":
            mangija = kagu(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "7":
            mangija = edel(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik == "8":
            mangija = loe(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik.lower() == "m":
            vaata_maailmakaarti(mangija)
        elif valik.lower() == "h":
            vaata_hud(mangija, leitud_artefaktid)
        elif valik.lower() == "a":
            peatukk1.clear()
            peatukk1.section_title("ARTEFAKTID JA ELEMENDID", peatukk1.ANSI_MAGENTA)
            kuva_templi_parand(mangija, leitud_artefaktid)
            peatukk1.pause()
        elif valik.lower() == "q":
            kuva_questid(mangija, leitud_artefaktid)
        elif valik.lower() == "i":
            peatukk1.kuva_inventar_mangija(mangija, leitud_artefaktid, aktiveeritud_altarid)
        elif valik.lower() == "e":
            kasuta_ch2_eset_lahingus(mangija)
        elif valik.lower() == "t":
            treeni_peatukk2(mangija, aktiveeritud_altarid, tasuta=False, xp_kordaja=1.25, koht=leia_asukoht(mangija))
        elif valik.lower() == "p":
            puhka(mangija, koht=leia_asukoht(mangija), turvaline=leia_asukoht(mangija) in ("Aethor", "Vuntsi maja"))
        elif valik.lower() == "k":
            peatukk1.kuva_stats(mangija)
            peatukk1.pause()
        elif valik.lower() == "v":
            shadow_menu(mangija, leitud_artefaktid)
        elif valik.lower() == "debug":
            flags["chapter2_debug_overlay"] = not flags.get("chapter2_debug_overlay", False)
            print(f"Finaali debug riba: {'SEES' if flags['chapter2_debug_overlay'] else 'VÄLJAS'}")
            if flags["chapter2_debug_overlay"]:
                finaali_debug_readout(mangija, leitud_artefaktid)
            peatukk1.pause()
        elif valik.lower() == "s":
            peatukk1.salvesta_mang(mangija, leitud_artefaktid, aktiveeritud_altarid)
            peatukk1.pause()
        elif valik.lower() == "l":
            uus_mangija, uus_artefaktid, uus_altarid = lae_teine_save()
            if uus_mangija is not None:
                mangija = uus_mangija
                leitud_artefaktid = uus_artefaktid
                aktiveeritud_altarid = uus_altarid
                if not kontrolli_jatku_tingimus():
                    return
                print("Peatükk 2 save laetud.")
                peatukk1.pause()
        elif valik == "0":
            return
        else:
            peatukk1.hamster_teade()
            peatukk1.pause()


def main():
    mangija, leitud_artefaktid, aktiveeritud_altarid = lae_teise_peatuki_mang()
    if mangija is None:
        return

    if not kontrolli_jatku_tingimus():
        return

    intro(mangija)
    pohikaart(mangija, leitud_artefaktid, aktiveeritud_altarid)


if __name__ == "__main__":
    main()
