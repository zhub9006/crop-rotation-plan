#!/usr/bin/env python3
"""
Piano di Rotazione delle Colture Stagionale
Basato su famiglie botaniche e cicli di interruzione dei patogeni del suolo
"""

CROP_ROTATION_PLAN = {
    "Primavera": {
        "Famiglia": "Fabaceae (Leguminose)",
        "Colture": ["Fagiolo", "Pisello", "Fava", "Ceci"],
        "Ruolo": "Fissazione dell'azoto nel suolo; interrompe il ciclo di patogeni che colpiscono Solanaceae e Brassicaceae.",
        "Patogeni interrotti": ["Fusarium oxysporum", "Verticillium dahliae", "Ralstonia solanacearum"]
    },
    "Estate": {
        "Famiglia": "Solanaceae",
        "Colture": ["Pomodoro", "Peperone", "Melanzana"],
        "Ruolo": "Sfrutta l'azoto fissato dalle leguminose; rotazione lontano da patogeni delle Brassicaceae.",
        "Patogeni interrotti": ["Plasmodiophora brassicae", "Alternaria brassicicola", "Rhizoctonia solani (ceppo Brassica)"]
    },
    "Autunno": {
        "Famiglia": "Brassicaceae (Crucifere)",
        "Colture": ["Cavolo", "Cavolfiore", "Ravanello", "Rucola"],
        "Ruolo": "Rilascio di glucosinolati con effetto biofumigante; interrompe i patogeni delle Cucurbitaceae e Solanaceae.",
        "Patogeni interrotti": ["Fusarium oxysporum f.sp. niveum", "Meloidogyne incognita", "Pythium spp."]
    },
    "Inverno": {
        "Famiglia": "Cereali / Poaceae",
        "Colture": ["Grano invernale", "Orzo", "Segale"],
        "Ruolo": "Struttura del suolo con radici fascicolate; interrompe i patogeni delle dicotiledoni e riduce la pressione dei nematodi.",
        "Patogeni interrotti": ["Meloidogyne spp.", "Heterodera spp.", "Sclerotinia sclerotiorum"]
    }
}


def print_rotation_plan():
    print("=" * 70)
    print("   PIANO DI ROTAZIONE DELLE COLTURE STAGIONALE")
    print("   Interruzione dei cicli dei patogeni del suolo")
    print("=" * 70)

    for stagione, info in CROP_ROTATION_PLAN.items():
        print(f"\n{'─' * 70}")
        print(f"  🌱 {stagione.upper()}")
        print(f"{'─' * 70}")
        print(f"  Famiglia botanica : {info['Famiglia']}")
        print(f"  Colture consigliate: {', '.join(info['Colture'])}")
        print(f"  Ruolo agronomico   : {info['Ruolo']}")
        print(f"  Patogeni interrotti: {', '.join(info['Patogeni interrotti'])}")

    print(f"\n{'=' * 70}")
    print("  PRINCIPIO: Ogni stagione alterna una famiglia botanica diversa")
    print("  per impedire l'accumulo di patogeni specifici nel suolo.")
    print("  Il ciclo completo (4 stagioni) va ripetuto per almeno 3-4 anni.")
    print("=" * 70)


if __name__ == "__main__":
    print_rotation_plan()
