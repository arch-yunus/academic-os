import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'saglik': [
        'geleneksel_cin_tibbi',
        'akupunktur_ve_moxibustion'
    ],
    'meta_muhendislik': [
        'ipek_muhendisligi_ve_serikultur',
        'dusuk_irtifa_teknolojisi_ve_iha',
        'uzay_zaman_bilgi_muhendisligi',
        'karbon_notr_bilimi_ve_teknolojisi',
        'akilli_molekuler_muhendislik',
        'akilli_gorsel_isitsel_muhendislik'
    ],
    'tarim_ve_ziraat_bilimleri': [
        'cay_bilimi_ve_teknolojisi'
    ],
    'guzel_sanatlar': [
        'geleneksel_cin_operasi_ve_muzigi'
    ],
    'turizm_ve_gastronomi': [
        'uluslararasi_kruvaziyer_yonetimi'
    ],
    'askeri_bilimler_ve_savunma_teknolojileri': [
        'komuta_kontrol_ve_strateji',
        'askeri_istihbarat_analizi',
        'savunma_yonetimi_ve_lojistik',
        'siber_savunma_ve_elektronik_harp',
        'askeri_havacilik_ve_uzay',
        'deniz_harp_ve_su_alti_stratejileri'
    ]
}

def create_china_expansion():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        # README for container
        readme = os.path.join(c_path, 'README.md')
        if not os.path.exists(readme):
            with open(readme, 'w', encoding='utf-8') as f:
                f.write(f"# {container.replace('_', ' ').title()}\n\nBu klasör {container} ile ilgili akademik ve stratejik alanları barındırır.\n")

        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"China Silk Road Created: {container}/{d}")
    print(f"\nSilk Road Expansion Complete: {count} new areas added.")

if __name__ == "__main__":
    create_china_expansion()
