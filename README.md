# Crop Rotation Planner 🌱

A seasonal crop rotation planner based on **botanical families** and **soil pathogen interruption cycles**.

## Overview

This tool provides a structured, season-by-season crop rotation plan that alternates different botanical families to:

- **Interrupt pathogen life cycles** specific to each plant family
- **Maintain soil health** through nitrogen fixation, biofumigation, and structural improvement
- **Maximize yield** by leveraging synergies between successive crops

## Seasonal Plan

| Season | Botanical Family | Key Crops | Primary Role |
|--------|-----------------|-----------|-------------|
| **Primavera** (Spring) | Fabaceae (Leguminose) | Fagiolo, Pisello, Fava, Ceci | Nitrogen fixation |
| **Estate** (Summer) | Solanaceae | Pomodoro, Peperone, Melanzana | Exploit fixed nitrogen |
| **Autunno** (Autumn) | Brassicaceae (Crucifere) | Cavolo, Cavolfiore, Ravanello, Rucola | Biofumigation (glucosinolates) |
| **Inverno** (Winter) | Poaceae (Cereali) | Grano invernale, Orzo, Segale | Soil structure & nematode suppression |

## How It Works

Each season rotates to a different botanical family, preventing the buildup of host-specific soil pathogens:

1. **Fabaceae** → interrupts *Fusarium*, *Verticillium*, *Ralstonia*
2. **Solanaceae** → interrupts *Plasmodiophora*, *Alternaria*, *Rhizoctonia* (Brassica strains)
3. **Brassicaceae** → interrupts *Fusarium* f.sp. *niveum*, *Meloidogyne*, *Pythium*
4. **Poaceae** → interrupts *Meloidogyne*, *Heterodera*, *Sclerotinia*

The complete 4-season cycle should be repeated for at least **3–4 years** for effective pathogen suppression.

## Usage

```bash
python crop_rotation_planner.py
```

## Scientific References

The following PubMed articles support the scientific basis of crop rotation for soil disease management:

1. Yu, Stiller, Conaty, Egan — *Fungal foe: exploring cotton's physiological responses to Verticillium wilt.* Frontiers in Plant Science, 2026. (PMID: 42211466)

2. Chen, Smagghe, Su, Liu, Tian, Xu, Yang, Ma, Zhang, Li, Zhong, Muhae-Ud-Din — *Alfalfa Rotation Enhances Soil Microbial Diversity and Reduces Tilletia foetida DNA Abundance in Common Bunt-Infected Wheat Fields.* The Plant Pathology Journal, 2026. (PMID: 42210638)

3. Kyselov, Kalenska, Kyselov, Chonka, Mazurenko — *Arbuscular Mycorrhiza and Antagonistic Microbial Consortia Reduce Phytopathogenic Pressure and Improve Rhizosphere Functioning of Sugar Beet Under Short-Rotation Cropping Systems.* Plants (Basel, Switzerland), 2026. (PMID: 42197663)

## License

MIT
