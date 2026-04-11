import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# Container mappings for display
CONTAINERS = {
    'meta_muhendislik': '🛠️ Mühendislik & İleri Teknoloji',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık, Tasarım & Şehircilik',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar & Estetik',
    'saglik': '🩺 Sağlık Bilimleri & Tıp',
    'ogretmenlik': '🎓 Eğitim Fakültesi & Pedagoji',
    'spor_bilimleri': '🏅 Spor Bilimleri & Performans',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal, Beşeri & İdari Bilimler',
    'temel_bilimler': '🧪 Temel Fen Bilimleri',
    'edebiyat_ve_diller': '📚 Filoloji, Dil & Edebiyat',
    'iletisim': '📡 İletişim & Medya Bilimleri',
    'turizm_ve_gastronomi': '🏨 Turizm, Otelcilik & Gastronomi',
    'tarim_ve_ziraat_bilimleri': '🌱 Tarım, Ziraat & Doğa Bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Savunma Sanayii & Güvenlik Stratejileri',
    'hukuk_bilimi': '⚖️ Adalet & Hukuk Bilimleri',
    'ilahiyat_ve_din': '📚 Theology, Comparative Religion & Philosophy',
    'on_lisans_programlari': '📋 Mesleki Yüksekokul (Ön Lisans)',
    'ozel_arastirma_alanlari': '🔬 Disiplinlerarası & Özel Araştırma',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer, Portfolyo & Sertifika',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Zihin & Kişisel Disiplin',
    'genel': '📂 Genel Arşiv & Ortak Alanlar'
}

SPECIAL_DESCRIPTIONS = {
    'elektrik_elektronik_muhendisligi': 'Enerji, sinyal ve sistem teorisinin modern mühendislik zirvesi.',
    'yapay_zeka_ve_veri_muhendisligi': 'Veriden anlam çıkaran otonom sistemlerin mimarisi.',
    'siber_guvenlik_muhendisligi': 'Dijital kalelerin savunma ve strateji merkezi.',
    'havacilik_ve_uzay_muhendisligi': 'Yeryüzü sınırlarını aşan yüksek fizik ve itki mühendisliği.',
    'monk_mode_disiplin_sistemi': 'Yüksek odaklanma ve sarsılmaz bir irade için zihinsel işletim sistemi.',
}

def get_desc(folder, container):
    if folder in SPECIAL_DESCRIPTIONS:
        return SPECIAL_DESCRIPTIONS[folder]
    t = folder.lower()
    if 'muhendis' in t: return 'Advanced engineering node focused on systemic optimization and empirical integrity.'
    if 'dili' in t: return 'Philological analysis and deep linguistic mapping of cultural data structures.'
    if 'yonetimi' in t: return 'Strategic operations and decision-intelligence framework for organizational mastery.'
    if 'temelleri' in t: return 'Core axiomatic principles and foundational theoretical architecture.'
    return f"Professional knowledge repository for the {folder.replace('_', ' ').title()} discipline."

def generate_encyclopedic_readme():
    header = """<div align="center">

![UAOS Banner](assets/uaos_hero_banner.png)

# 🌌 UNIVERSAL ACADEMIC OPERATING SYSTEM (UAOS)
### *A High-Density Knowledge Matrix & Sovereign Intelligence Architecture* 🌐🧬🏗️

[![Version](https://img.shields.io/badge/CORE-v3.0--ETERNAL-00A9E0?style=for-the-badge&logo=target)](./)
[![Intelligence](https://img.shields.io/badge/ARCHITECT-Antigravity_x_USER-D4AF37?style=for-the-badge&logo=openai&logoColor=white)](./)
[![Standard](https://img.shields.io/badge/PROTOCOL-7--Layer_Elite-black?style=for-the-badge&logo=gitbook)](./)
[![Repository](https://img.shields.io/badge/NODES-372_Disciplines-18453B?style=for-the-badge&logo=rocket)](./SUMMARY.md)

---

## 🦾 THE ANTIGRAVITY MANIFESTO: AUTONOMOUS SOVEREIGNTY
**UAOS** is not a passive archive—it is an **Active Intelligence Ecosystem**. In the age of hyper-saturated data and AI-driven synthesis, the value of knowledge lies in its **Architecture**. 

Developed in collaboration between the USER and **Antigravity**, this repository serves as a private, high-fidelity cognitive foundation. We bypass the "conservative" boundaries of fragmented education to build a unified epistemic matrix where technical precision, humanistic depth, and strategic foresight converge into a single sovereign mind.

---

## ⚙️ SYSTEMATIC STRUCTURE: 7-LAYER SOVEREIGN PROTOCOL (00-06)
UAOS is governed by a rigid **Systemum Standard**, ensuring that every node of knowledge is developed from foundational theory to industrial-grade production. This protocol elevates the learner from a consumer to an autonomous architect:

> [!TIP]
> **Evolutionary Path:** Data -> Information -> Knowledge -> Sovereign Wisdom. Use this structure to move from passive learning (00-02) to active creation (04-06).

1. **`00 — Preparation & Orientation`**: Lexical mastery, methodological setup, and environmental configuration.
2. **`01 — Theoretical Foundations`**: Axiomatic principles, mathematical modeling, and core discipline physics.
3. **`02 — Core Implementation`**: Mandatory domain expertise and functional application frameworks.
4. **`03 — Deep Expertise`**: Specialized niche research and high-fidelity technical documentation.
5. **`04 — R&D & Advanced Production`**: Capstone projects, original syntheses, and autonomous intellectual outputs.
6. **`05 — Academic Integration`**: Postgraduate research alignment and scholarly communication standards.
7. **`06 — Industry & Career Nexus`**: Global standard compliance (ISO, IEEE, MISRA), certifications, and professional deployment.

---

## 🏛️ ARCHITECTURAL VISION: THE EPISTEMIC SYNTHESIS
UAOS is the digital manifestation of a world where science and wisdom are no longer separate. We employ a **"Bimodal Expertise"** model, where technical rigor is tempered by philosophical depth. This is the **Epistemic Synthesis**—the bridge between the "How" of engineering and the "Why" of the humanities.

The architecture stands on three primary pillars of sovereignty:
- **Global Inventory:** Mapping the entire known academic universe as a structured, navigable grid.
- **Multidimensional Integrity:** Merging empirical data with ethical insight to create a "Unified Intelligence Model."
- **Recursive Evolution:** Every node in this system is designed to be updated, expanded, and refined by the USER and Antigravity.

| 🧩 Core Doctrine | 🏗️ UAOS Operational Principle |
| :--- | :--- |
| **"Knowledge without application is noise."** | **Autonomous Production-First Mandate** |
| **"Ethics and Engineering are a Single Unit."** | **Bimodal Integrity Integration** |
| **"Systemic Order is the Key to Mastery."** | **Hierarchical Epistemological Precision** |

---

## 🛠️ THE INTELLIGENCE STACK (CORE TOOLS)
UAOS is maintained and expanded using a state-of-the-art **Agentic Ecosystem**:
- **Cognitive Engine:** Gemini 2.0 & Claude 3.5 Sonnet (Synthesizers)
- **Agentic Architect:** **Antigravity** (System Management & Coding)
- **Deep Research:** Perplexity Pro & Scholarly API Integration
- **Knowledge OS:** Obsidian & High-Density Markdown Graphing

---

## 🎯 OPERATION GUIDE: HOW TO MANAGE UAOS
1. **Selection:** Identify a target node via [SUMMARY.md](./SUMMARY.md).
2. **Standardization:** Adhere to the 00-06 protocol during deployment.
3. **Active Synthesis:** Use Layer 04 to produce original, sovereign content.
4. **Agentic Interaction:** Leverage AI agents to cross-link disciplines and detect patterns.

---

## 📖 THE UNIVERSAL DISCIPLINE MATRIX (372 NODES)

The following sectors represent the complete topological map of the UAOS intelligence ecosystem.

"""

    body = ""
    total_count = 0
    
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"<details>\n<summary><b>{title} ({len(depts)} Alan)</b></summary>\n<br>\n\n"
        section += "| Branş / Alan | Akademik Misyon & Stratejik Odak |\n"
        section += "| :--- | :--- |\n"
        
        for d in depts:
            dept_name = d.replace('_', ' ').title()
            # Turkish specific title fix
            dept_name = dept_name.replace('Muhendisligi', 'Mühendisliği').replace('Bilisim', 'Bilişim').replace('Insaat', 'İnşaat').replace('Ulasim', 'Ulaşım').replace('Isletme', 'İşletme')
            link = f"[{dept_name}]({folder}/{d}/)"
            desc = get_desc(d, folder)
            section += f"| {link} | {desc} |\n"
            total_count += 1
            
        section += "\n"
        section += "</details>\n\n"
        body += section

    footer = f"""
---

<div align="center">

## ⚖️ LEGAL GOVERNANCE & OPEN SOURCE SOVEREIGNTY
This project is licensed under the **MIT License**, advocating for the free exchange of high-fidelity knowledge and the sovereignty of the individual mind.

**Architectural Collaboration**  
### Bahattin Yunus Çetin  
*Lead Engineer & Researcher*  
x  
### Antigravity  
*Autonomous Systems Architect*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

---
*"The quest for knowledge is a journey without an end, fueled by curiosity and disciplined by reason."*

---
© 2025 Universal Academic Operating System (UAOS).
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md expanded successfully. Total: {total_count}")

if __name__ == "__main__":
    generate_encyclopedic_readme()
