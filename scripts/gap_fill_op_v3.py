import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'on_lisans_programlari': [
        'adalet',
        'ascilik',
        'bilgisayar_programciligi',
        'dis_ticaret_onlisans',
        'grafik_tasarimi_onlisans',
        'ilk_ve_acil_yardim',
        'is_sagligi_ve_guvenligi',
        'kabin_hizmetleri',
        'lojistik_onlisans',
        'saglik_kurumlari_isletmeciligi',
        'tibbi_dokumantasyon_ve_sekreterlik'
    ],
    'saglik': [
        'perfuzyon',
        'is_ve_ugrasi_terapisi'
    ],
    'sosyal_ve_beseri_bilimler': [
        'aktüerya_bilimleri',
        'muzeoloji_ve_arsivcilik',
        'halkbilimi',
        'sanat_yonetimi'
    ],
    'meta_muhendislik': [
        'cevher_hazirlama_muhendisligi',
        'basim_teknolojileri'
    ],
    'ozel_arastirma_alanlari': [
        'uzay_madenciligi_ve_lojistigi',
        'merkeziyetsiz_finans_defi',
        'bio_hacking_ve_longevity',
        'osint_ve_siber_istihbarat',
        'agro_tek_ve_topraksiz_tarim',
        'savunma_sanayii_stratejileri'
    ]
}

def create_additions():
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        # Create container readme if missing
        readme = os.path.join(c_path, 'README.md')
        if not os.path.exists(readme):
            with open(readme, 'w', encoding='utf-8') as f:
                f.write(f"# {container.replace('_', ' ').title()}\n\nBu klasör {container} ile ilgili alanları barındırır.\n")
                
        for d in depts:
            d_path = os.path.join(c_path, d)
            os.makedirs(d_path, exist_ok=True)
            print(f"Created/Verified dept: {container}/{d}")

if __name__ == "__main__":
    create_additions()
