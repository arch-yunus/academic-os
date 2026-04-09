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
    'ilahiyat_ve_din': '🕌 İlahiyat, Din & Felsefe',
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
    'tutun_bilimi': 'Tütün bitkisinin agronomik, endüstriyel ve kimyasal süreçlerinin akademik analizi.',
    'deniz_hukuku_ve_stratejisi': 'Mavi Vatan ve uluslararası sularda egemenlik haklarının hukuki temelleri.',
}

def get_desc(folder, container):
    if folder in SPECIAL_DESCRIPTIONS:
        return SPECIAL_DESCRIPTIONS[folder]
    t = folder.lower()
    if 'muhendis' in t: return 'Sistem tasarımı ve ampirik çözümleme odaklı ileri mühendislik alanı.'
    if 'dili' in t: return 'Filolojik yapı ve kültürel mirasın derinlemesine incelenmesi.'
    if 'yonetimi' in t: return 'Operasyonel ve stratejik karar destek mekanizmalarının yönetimi.'
    return f"{folder.replace('_', ' ').title()} disiplinine ait teorik ve pratik uzmanlık deposu."

def generate_encyclopedic_readme():
    header = """<div align="center">

![AOS Hero Banner](assets/aos_hero_banner.png)

# 🏛️ AKADEMİK İŞLETİM SİSTEMİ (AOS)
### *Yapay Zeka Çağı İçin Küresel Bilgi Nizamı ve Mültidisipliner Ontoloji* 🌐💎🚀

[![Versiyon](https://img.shields.io/badge/VERSION-2025.Elite-00A9E0?style=for-the-badge&logo=target)](./)
[![Kapsam](https://img.shields.io/badge/SCOPE-372_Disciplines-D4AF37?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Standard](https://img.shields.io/badge/STANDARD-7--Tier_Elite-black?style=for-the-badge&logo=gitbook)](./)
[![Philosophy](https://img.shields.io/badge/VISION-Double_Wing-18453B?style=for-the-badge&logo=openai&logoColor=white)](./)

---

## 📜 AOS ANA DÜSTURU VE MANİFESTO
**Akademik İşletim Sistemi (AOS)**, bilginin parçalandığı bu çağda, her disiplini tek bir rasyonel ve metodolojik çatı altında birleştiren "Zülcenahayn" (Çift Kanatlı) bir dökümantasyon ekosistemidir.

> [!IMPORTANT]
> **Bilim bir yöntem, merak ise motorumuzdur.** AOS; aklı fenle (bilimle), ruhu yüksek bir vizyonla donatan profesyonel bir akademik iskelettir. Burada bilim metodolojidir, hakikat ise nihai gayedir.

---

</div>

## ⚙️ ELİT 7-KADEMELİ HİYERARŞİ (Systemum 0-6)
AOS içindeki her branş, rastgele notlar yerine **7 katmanlı elit bir nizam** üzerine inşa edilmiştir:

| Kademe | Tanım | Akademik Hedef |
| :--- | :--- | :--- |
| **`00`** | **Hazırlık** | Dil yeterliliği ve temel metodolojik oryantasyon. |
| **`01`** | **Teori** | Alanın üzerine inşa edildiği sayısal ve kuramsal temel. |
| **`02`** | **Çekirdek** | En zorunlu ve temel branş yetkinliklerinin inşası. |
| **`03`** | **Uzmanlık** | Seçmeli ve ileri seviye branş derinleşmesi. |
| **`04`** | **Üretim** | Orijinal bitirme projeleri ve AR-GE çıktıları. |
| **`05`** | **Akademi** | Lisansüstü ve bilimsel araştırma metodolojileri. |
| **`06`** | **Dünya** | Sektörel sertifikasyonlar ve küresel standartlar. |

---

## 🏛️ VİZYONER MİRAS: "RUHUMUZUN DERİNLİĞİ"
AOS, modern bilimsel metodolojiyi rasyonel bir **Yöntem** olarak kullanır. Ancak bu devasa iskelete can veren ruh; kalbi ve aklı, fenle dinin imtizacını hedefleyen **Medresetü’z-Zehra** gibi kadim ve vizyoner miraslardan beslenir.

> [!TIP]
> **"Aklın nuru fünun-u medeniyedir, vicdanın ziyası ulûm-u diniyedir."**
> Bizim için bilim, "Varlığın Büyük Nizamı"nı anlama çabasıdır.

---

## 📚 ANSİKLOPEDİK BÖLÜM DİZİNİ (372 BRANŞ)

Aşağıdaki kategoriler, AOS ekosisteminin 372 benzersiz hücresini temsil eder.

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
        section += "| Branş / Alan | Akademik Misyon & Odak |\n"
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

## 🛠️ PROFESYONEL ARAÇLAR & MİMARİ
- **Çekirdek Akıl:** Gemini 2.0 / Claude 3.5 Sonnet
- **Ontoloji:** 7-Tier Standardize Scaffolding
- **Geliştirici:** Bahattin Yunus Çetin (*Mühendis & AOS Mimarı*)

---

<div align="center">

**[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)**

*"İlim, müminin yitik malıdır; nerede bulursa alsın."*

---
© 2025 AOS - Tüm Hakları Bilim ve Hikmete Aittir.
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md updated with 'The Ayar' (Ultimate Refinement). Total: {total_count}")

if __name__ == "__main__":
    generate_encyclopedic_readme()
