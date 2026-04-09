import os
import shutil

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
TEMPLATE_FILE = os.path.join(ROOT_DIR, 'templates', 'COURSE_TEMPLATE.md')

# These are the standard subdirectories (Expanded to 00-04)
SUBDIR_DEFS = {
    "00_Akademik_Hazirlik_ve_Dil": {
        "label": "00 — Akademik Hazırlık ve Dil",
        "desc": "Hazırlık sınıfı müfredatı, yabancı dil yeterlilik çalışmaları ve akademik oryantasyon.",
    },
    "01_Temel_Bilimler_ve_Giris": {
        "label": "01 — Temel Bilimler ve Giriş",
        "desc": "Bölüme giriş niteliğindeki temel ders notları, genel kavramlar ve başlangıç kaynakları.",
    },
    "02_Alan_Dersleri": {
        "label": "02 — Alan Dersleri",
        "desc": "Bölümün özgül ve zorunlu alan derslerine ait notlar, ödevler ve kaynaklar.",
    },
    "03_Secmeli_ve_Ileri_Uygulama": {
        "label": "03 — Seçmeli & İleri Uygulama",
        "desc": "Seçmeli dersler, derinlemesine uygulama projeleri ve uzmanlaşma çalışmaları.",
    },
    "04_Arastirma_ve_Bitirme": {
        "label": "04 — Araştırma ve Bitirme",
        "desc": "Bitirme projeleri, staj raporları, seminer çalışmaları ve akademik araştırma notları.",
    },
}

# All current container folders
CONTAINERS = [
    'edebiyat_ve_diller',
    'hukuk_bilimi',
    'ilahiyat_ve_din',
    'iletisim',
    'meta_muhendislik',
    'mimarlik_ve_tasarim',
    'ogretmenlik',
    'saglik',
    'sosyal_ve_beseri_bilimler',
    'temel_bilimler',
    'turizm_ve_gastronomi',
    'ozel_arastirma_alanlari',
    'guzel_sanatlar',
    'spor_bilimleri'
]

def get_dept_readme_content(dept_name):
    title = dept_name.replace('_', ' ').title()
    return f"""# {title}

Bu klasör **{title}** bölümüne ait akademik notlar, araştırmalar ve dökümanlar içindir.

---

## 📂 Çekirdek Ders Ağacı
Akademik sistem entegrasyonu kapsamında bu bölüm için önerilen ve standartlaştırılmış ders/çalışma klasörleri:

- [00 — Akademik Hazırlık ve Dil](00_Akademik_Hazirlik_ve_Dil/)
- [01 — Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 — Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 — Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 — Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)

> [!TIP]
> Yeni bir ders eklerken ana dizindeki `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koyabilir ve kolayca kendi not şablonunuzu oluşturabilirsiniz!
"""

def get_subdir_readme_content(dept_name, sub_key):
    dept_title = dept_name.replace('_', ' ').title()
    sub = SUBDIR_DEFS[sub_key]
    return f"""# 📂 {sub['label']} — {dept_title}

## 📖 Açıklama
{sub['desc']}

---

## 📝 Bu Klasöre Nasıl Katkı Yapılır?
1. `DERS_SABLONU.md` (üst dizindeki) dosyasını bu klasöre kopyala
2. Dosyayı `DERS_ADI.md` olarak yeniden adlandır
3. İçini ders notları, ödevler ve kaynaklarla doldur
4. Pull Request aç veya doğrudan push et

> [!NOTE]
> Bu klasör **{dept_title}** bölümünün **{sub['label']}** dönemine aittir.
"""

def scaffold_department(dept_path, dept_name):
    # 1. Ensure Department README (Overwrite if missing tree)
    readme_path = os.path.join(dept_path, 'README.md')
    needs_rewrite = False
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "00 — Akademik Hazırlık" not in content:
                needs_rewrite = True
    else:
        needs_rewrite = True
        
    if needs_rewrite:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(get_dept_readme_content(dept_name))
    
    # 2. Copy DERS_SABLONU.md if available
    if os.path.exists(TEMPLATE_FILE):
        dest_template = os.path.join(dept_path, 'DERS_SABLONU.md')
        if not os.path.exists(dest_template):
            shutil.copy2(TEMPLATE_FILE, dest_template)
    
    # 3. Create Subdirs and their READMEs
    for sub_key in SUBDIR_DEFS.keys():
        sub_path = os.path.join(dept_path, sub_key)
        os.makedirs(sub_path, exist_ok=True)
        sub_readme = os.path.join(sub_path, 'README.md')
        if not os.path.exists(sub_readme):
            with open(sub_readme, 'w', encoding='utf-8') as f:
                f.write(get_subdir_readme_content(dept_name, sub_key))

def main():
    count = 0
    for container in CONTAINERS:
        container_path = os.path.join(ROOT_DIR, container)
        if not os.path.exists(container_path):
            continue
            
        print(f"Processing container: {container}")
        for item in os.listdir(container_path):
            item_path = os.path.join(container_path, item)
            if os.path.isdir(item_path) and not item.startswith('.') and item != 'README.md':
                scaffold_department(item_path, item)
                count += 1
                if count % 10 == 0:
                    print(f"  Processed {count} departments...")
    
    print(f"\nDone! Scaffolded/Upgraded {count} departments in total with 00-04 structure.")

if __name__ == "__main__":
    main()
