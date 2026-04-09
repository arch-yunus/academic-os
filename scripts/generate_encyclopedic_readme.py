import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

CONTAINERS = {
    'meta_muhendislik': '🛠️ Mühendislik Bilimleri',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık ve Tasarım',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar',
    'saglik': '🩺 Sağlık Bilimleri',
    'ogretmenlik': '🎓 Eğitim ve Öğretmenlik',
    'spor_bilimleri': '🏅 Spor Bilimleri',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal ve Beşeri Bilimler',
    'temel_bilimler': '🧪 Temel Bilimler',
    'edebiyat_ve_diller': '📚 Edebiyat ve Diller',
    'iletisim': '📡 İletişim Bilimleri',
    'turizm_ve_gastronomi': '🏨 Turizm ve Gastronomi',
    'tarim_ve_ziraat_bilimleri': '🌱 Tarım ve Ziraat Bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Askeri Bilimler ve Savunma',
    'hukuk_bilimi': '⚖️ Hukuk',
    'ilahiyat_ve_din': '🕌 İlahiyat ve Din',
    'on_lisans_programlari': '📋 Ön Lisans Programları',
    'ozel_arastirma_alanlari': '🔬 Özel Araştırma Alanları',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer ve Sertifikasyonlar',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Yetkinlikler ve Gelişim',
    'genel': '📂 Genel ve Ortak Alanlar'
}

SPECIAL_DESCRIPTIONS = {
    # Engineering
    'elektrik_elektronik_muhendisligi': 'Enerji üretimi, iletimi ve elektronik devre tasarımı üzerine odaklanan temel mühendislik branşı.',
    'beyin_bilgisayar_arayuzu_bci_muhendisligi': 'Nöral sinyallerin dijital sistemlere aktarımı ve insan-makine etkileşimi üzerine ileri araştırma.',
    'yapay_zeka_ve_verii_muhendisligi': 'Büyük veri analizi, makine öğrenmesi ve otonom sistemlerin algoritma tasarımı.',
    'siber_guvenlik_muhendisligi': 'Dijital varlıkların korunması, sızma testleri ve güvenli sistem mimarileri geliştirme.',
    'yuksek_guclu_yariiletken_bilimi_ve_muhendisligi': 'Yeni nesil enerji elektroniği ve yarı iletken komponent teknolojileri üretimi.',
    'dusuk_irtifa_teknolojisi_ve_iha': 'Dronelar ve alçak irtifa hava araçlarının aerodinamik ve sistem tasarımı.',
    
    # China Export Specials
    'geleneksel_cin_tibbi': 'Binlerce yıllık kadim Çin tıp öğretileri ve bitkisel tedavi metodolojileri.',
    'kahve_bilimi_ve_muhendisligi': 'Kahve bitkisinin üretiminden işleme teknolojilerine ve kimyasal analizine kadar tüm süreçler.',
    'futbol_bilimi': 'Futbolun teknik, taktik, biyomekanik ve yönetimsel boyutlarının akademik analizi.',
    'tutun_bilimi': 'Tütün bitkisinin yetiştirilmesi, endüstriyel işlenmesi ve kalite kontrol süreçleri.',
    'ipek_muhendisligi_ve_serikultur': 'İpek böcekçiliği ve tekstil mühendisliğinin ipek üretimi özelindeki kesişimi.',
    
    # Meta Skills
    'monk_mode_disiplin_sistemi': 'Yüksek odaklanma, dijital detoks ve kişisel hedeflere tam adanmışlık disiplini.',
    'sun_tzu_stratejik_dunce': 'Antik savaş stratejilerinin modern iş ve yaşam yönetimine uygulanması.',
    'stoisizm_ve_mental_dayaniklilik': 'Stoacı fıkırlerin modern stres yönetimi ve sarsılmaz bir zihin yapısı için uygulanması.',
    
    # Defense
    'komuta_kontrol_ve_strateji': 'Askeri operasyonların yönetimi, karar destek sistemleri ve stratejik planlama.',
    'siber_savunma_ve_elektronik_harp': 'Dijital cephede savunma ve radar/sinyal sistemlerinde üstünlük sağlama yöntemleri.',
}

def get_desc(folder, container):
    if folder in SPECIAL_DESCRIPTIONS:
        return SPECIAL_DESCRIPTIONS[folder]
    
    # Fallback logic
    t = folder.lower()
    if 'muhendis' in t or 'engineering' in t:
        return 'Modern mühendislik prensipleriyle ilgili sistemin tasarımı, analizi ve optimizasyonu.'
    if 'dili' in t or 'edebiyati' in t:
        return 'İlgili dilin dilbilgisi yapısı, edebiyat tarihi ve kültürel bağlamının akademik incelenmesi.'
    if 'onlisans' in t or container == 'on_lisans_programlari':
        return 'Belirli bir mesleğe yönelik uygulamalı teknik beceriler ve operasyonel yetkinlikler eğitimi.'
    if 'teknolojisi' in t:
        return 'Modern teknolojik araçların ve süreçlerin ilgili alan özelinde uygulanması ve yönetimi.'
    if 'yonetimi' in t:
        return 'Süreçlerin, kaynakların ve organizasyonların stratejik ve operasyonel olarak yönetilmesi.'
    
    return f"{folder.replace('_', ' ').capitalize()} alanında teorik ve pratik uzmanlık çalışmaları."

def generate_encyclopedic_readme():
    header = """<div align="center">

![MZ-OS Hero Banner](assets/aos_hero_banner.png)

# 🏛️ MEDRESETÜ’Z-ZEHRA İŞLETİM SİSTEMİ (MZ-İS)
### *Yapay Zeka Çağı İçin Kapsamlı ve Mültidisipliner Bilgi Ontolojisi* 🌐💎🚀

[![Versiyon](https://img.shields.io/badge/VERSİYON-v2025.Elite-00A9E0?style=for-the-badge&logo=target)](./)
[![Kapsam](https://img.shields.io/badge/KAPSAM-385_Benzersiz_Alan-D4AF37?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Standart](https://img.shields.io/badge/STANDART-7_Kademeli_Hiyerarşi-black?style=for-the-badge&logo=gitbook)](./)
[![Miras](https://img.shields.io/badge/MİRAS-Medresetü’z--Zehra-18453B?style=for-the-badge&logo=openai&logoColor=white)](./)

---

## 🏗️ Teknik Kapasite ve Metodoloji
**Medresetü’z-Zehra İşletim Sistemi (MZ-İS)**, farklı bilgi akışlarını tek bir standart çerçevede birleştirmek için tasarlanmış yüksek yoğunluklu bir akademik ekosistemdir. **Bilimsel Tarafsızlık** ve **Ampirik Titizlik** ilkesiyle hareket eden sistem, 385 benzersiz disiplini 7 kademeli bir mimari altında sınıflandırır.

> [!NOTE]
> **Metodoloji:** Bilim ve mühendisliği temel sorgulama yöntemi olarak kullanan, katı bir akademik yaklaşım benimsiyoruz. Tüm müfredat yapıları (YÖK ve Çin MoE) profesyonel bir nesnellikle entegre edilmiştir.

---

</div>

## ⚙️ Elit 7-Kademeli Mimari (00-06)
Bu ontolojideki her bir disiplin, endüstriyel standartlara uygun, katı bir hiyerarşi ile yapılandırılmıştır:

| Kademe | Kategori | Hedef |
| :--- | :--- | :--- |
| **`00`** | **Akademik Hazırlık** | Dil yeterliliği ve temel oryantasyon süreci. |
| **`01`** | **Temel Bilimler** | Alanın üzerine inşa edildiği teorik ve sayısal temel. |
| **`02`** | **Çekirdek Modüller** | Zorunlu ana branş dersleri ve teknik uzmanlık. |
| **`03`** | **İleri Uygulama** | Seçmeli uzmanlıklar ve usta seviyesi pratikler. |
| **`04`** | **Araştırma & Geliştirme** | Bitirme projeleri, tezler ve orijinal akademik çıktılar. |
| **`05`** | **Lisansüstü Yol** | Yüksek Lisans ve Doktora seviyesindeki akademik rotalar. |
| **`06`** | **Küresel Standartlar** | Sertifikasyonlar ve endüstriyel profesyonel kıstaslar. |

---

## 🕌 Felsefi Temeller: MZ-İS'in Ruhu
*"Vicdanın ziyası ulûm-u diniye, aklın nuru fünun-u medeniyedir."*

MZ-İS, modern bilimsel metodolojiyi bir **Yöntem** olarak kullanırken, **İlhamını** ve **Etik Ruhunu** Medresetü’z-Zehra vizyonundan —kalp ve aklın imtizacından— alır.

| ✍️ Düstur | 🏛️ MZ-İS Prensibi |
| :--- | :--- |
| **"Eyleme dökülmeyen ilim, yerinde sayan bir gölge gibidir."** | **Aktif Üretim ve Mühendislik** |
| **"Hakikat için Din ve Fen bir arada olmalıdır."** | **Mültidisipliner Bütünlük** |
| **"Varlığın büyük nizamını bilmek için çabala."** | **Ampirik Sorgulama ve Titizlik** |

---

## 📚 Ansiklopedik Dizin (385 Disiplin)

20 stratejik konteyner altında gruplanan her alan, uzmanlık için standart bir yol sunar.

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
        section += "| Bölüm / Alan | Akademik Odak / Misyon |\n"
        section += "| :--- | :--- |\n"
        
        for d in depts:
            dept_name = d.replace('_', ' ').title()
            link = f"[{dept_name}]({folder}/{d}/)"
            desc = get_desc(d, folder)
            section += f"| {link} | {desc} |\n"
            total_count += 1
            
        section += "\n"
        section += "</details>\n\n"
        body += section

    footer = f"""
---

## 🛠️ Profesyonel Enstrümantasyon (V.2025)
- **Çekirdek Zeka:** Gemini 2.0 / Claude 3.5 Sonnet / GPT-o1
- **Geliştirme & IDE:** Cursor / Windsurf
- **Araştırma Motoru:** Perplexity Pro
- **Mimari:** 7-Kademeli Standartlaştırılmış İskelet

## ⚖️ Lisans
Bu proje **MIT Lisansı** ile korunmaktadır.

<div align="center">

**Hazırlayan:** Bahattin Yunus Çetin  
*Mühendis ve MZ-İS Mimarı*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

---
*"İlim, müminin yitik malıdır; nerede bulursa alsın."*
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md updated in pure Turkish. Total: {total_count}")

if __name__ == "__main__":
    generate_encyclopedic_readme()
