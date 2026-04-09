import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# Syllabus Mapping: Department Folder -> List of Core Courses
SYLLABUS_MAP = {
    # ENGINEERING
    'elektrik_elektronik_muhendisligi': [
        'Devre_Teorisi_I_ve_II',
        'Elektronik_Devreleri_I_ve_II',
        'Sinyaller_ve_Sistemler',
        'Elektromanyetik_Alan_Teorisi',
        'Enerji_Iletimi_ve_Dagitimi',
        'Haberlesme_Sistemlerine_Giris',
        'Guc_Elektronigi',
        'Kontrol_Sistemleri'
    ],
    'bilgisayar_muhendisligi': [
        'Veri_Yapilari_ve_Algoritmalar',
        'Isletim_Sistemleri',
        'Veritabanı_Yonetim_Sistemleri',
        'Bilgisayar_Organizasyonu_ve_Mimarisi',
        'Nesne_Yonelimli_Programlama',
        'Yazilim_Muhendisligi_Prensipleri',
        'Bilgisayar_Aglarina_Giris',
        'Otomat_Teorisi'
    ],
    'yapay_zeka_ve_veri_muhendisligi': [
        'Makine_Ogrenmesi',
        'Derin_Ogrenme',
        'Veri_Madenciligi',
        'Dogal_Dil_Isleme',
        'Bilgisayarla_Goru',
        'Istatistiksel_Veri_Analizi',
        'Yapay_Zeka_Etigi',
        'Otonom_Sistemler'
    ],
    'insaat_muhendisligi': [
        'Statik_ve_Mukavemet',
        'Akiskanlar_Mekanigi',
        'Yapi_Statigi',
        'Zemin_Mekanigi',
        'Betonarme_Tasarimi',
        'Celik_Yapilar',
        'Ulastirma_Muhendisligi',
        'Yapi_Isletmesi'
    ],
    # HEALTH
    'tip': [
        'Anatomi_ve_Diseksiyon',
        'Tibbi_Fizyoloji',
        'Tibbi_Biyokimya',
        'Histoloji_ve_Embriyoloji',
        'Tibbi_Farmakoloji',
        'Patoloji_ve_Patofizyoloji',
        'Tibbi_Mikrobiyoloji',
        'Klinik_Bilimlere_Giris'
    ],
    # LAW
    'hukuk': [
        'Anayasa_Hukuku',
        'Medeni_Hukuk',
        'Ceza_Hukuku_Genel_Hukumler',
        'Idare_Hukuku',
        'Borclar_Hukuku',
        'Ticaret_Hukuku',
        'Hukuk_Felsefesi_ve_Sosyolojisi',
        'Roma_Hukuku'
    ],
    # BASIC SCIENCES
    'fizik_muhendisligi': [
        'Klasik_Mekanik',
        'Elektromanyetik_Teori',
        'Kuantum_Mekaniğine_Giris',
        'Termodinamik_ve_Istatistiksel_Fizik',
        'Yariiletken_Fizigi',
        'Optik_ve_Fotonik',
        'Katıhal_Fiziği',
        'Nükleer_Fizik_Prensipleri'
    ]
}

BIBLIOGRAPHY_MAP = {
    'meta_muhendislik': 'Önerilen Bibliyografya: Boylestad, Sedra/Smith, Stallings, Knuth, Hibbeler.',
    'saglik': 'Önerilen Bibliyografya: Guyton & Hall, Sobotta, Robbins, Harrison.',
    'hukuk_bilimi': 'Önerilen Bibliyografya: Kemal Gözler, Türk Medeni Kanunu Şerhleri, Roma Hukuku Temelleri.',
}

def populate_depth():
    count_dirs = 0
    for container in os.listdir(ROOT_DIR):
        container_path = os.path.join(ROOT_DIR, container)
        if not os.path.isdir(container_path) or container.startswith('.'):
            continue
            
        for dept in os.listdir(container_path):
            dept_path = os.path.join(container_path, dept)
            if not os.path.isdir(dept_path):
                continue
                
            # 1. Inject course folders if mapping exists
            if dept in SYLLABUS_MAP:
                target_tier = os.path.join(dept_path, '02_Alan_Dersleri')
                if os.path.exists(target_tier):
                    for course in SYLLABUS_MAP[dept]:
                        course_dir = os.path.join(target_tier, course)
                        if not os.path.exists(course_dir):
                            os.makedirs(course_dir)
                            # Create placeholder README
                            with open(os.path.join(course_dir, 'README.md'), 'w', encoding='utf-8') as f:
                                f.write(f"# {course.replace('_', ' ')}\n\nBu klasör {dept.replace('_', ' ').title()} branşının çekirdek dersi olan {course.replace('_', ' ')} akademik notları içindir.\n")
                            count_dirs += 1

            # 2. Enrich department README with Bibliography
            readme_path = os.path.join(dept_path, 'README.md')
            if os.path.exists(readme_path) and container in BIBLIOGRAPHY_MAP:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if "## 📚 Kaynakça" not in content:
                    with open(readme_path, 'a', encoding='utf-8') as f:
                        f.write(f"\n\n--- \n\n## 📚 Kaynakça & Başvuru\n{BIBLIOGRAPHY_MAP[container]}\n")

    print(f"High-density population complete. Created {count_dirs} course nodes.")

if __name__ == "__main__":
    populate_depth()
