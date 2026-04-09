import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'on_lisans_programlari': [
        'agiz_ve_dis_sagligi',
        'diyaliz',
        'optisyenlik',
        'yasli_bakimi',
        'eczane_hizmetleri',
        'bankacilik_ve_sigortacilik',
        'muhasebe_ve_vergi_uygulamalari',
        'buro_yonetimi_ve_yonetici_asistanligi',
        'yerel_yonetimler',
        'halkla_iliskiler_ve_tanitim_onlisans',
        'turizm_ve_otel_isletmeciligi_onlisans',
        'sivil_savunma_ve_itfaiyecilik',
        'ozel_guvenlik_ve_koruma',
        'sosyal_hizmetler_onlisans',
        'laboratuvar_teknolojisi',
        'mekatronik_onlisans',
        'bilgisayar_destekli_tasarim_ve_animasyon',
        'elektronik_teknolojisi',
        'makine_resim_ve_konstruksiyon',
        'insaat_teknolojisi_onlisans',
        'harita_ve_kadastro',
        'tıbbi_ve_aromatik_bitkiler',
        'fidan_yetistiriciligi',
        'su_urunleri_isletme_teknolojisi'
    ],
    'meta_muhendislik': [
        'deri_muhendisligi',
        'tekstil_tasarimi',
        'modelleme_ve_simulasyon'
    ],
    'temel_bilimler': [
        'deniz_bilimleri_ve_teknolojisi',
        'yer_bilimleri'
    ],
    'sosyal_ve_beseri_bilimler': [
        'muze_yonetimi',
        'kutuphanecilik_ve_bilgi_yonetimi',
        'halk_bilimi',
        'yenilik_yonetimi'
    ],
    'ozel_arastirma_alanlari': [
        'neuro_design',
        'climate_tech_ve_karbon_yakalama',
        'cyber_physical_systems',
        'regenerative_medicine',
        'algorithmic_governance',
        'longevity_science_advanced',
        'osint_ileri_seviye',
        'prompt_engineering_pro'
    ]
}

def create_additions():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"Created: {container}/{d}")
    print(f"\nPhase 4: Created {count} new areas.")

if __name__ == "__main__":
    create_additions()
