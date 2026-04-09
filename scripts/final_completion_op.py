import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'edebiyat_ve_diller': [
        'cin_dili_ve_edebiyati',
        'japon_dili_ve_edebiyati',
        'kore_dili_ve_edebiyati',
        'ispanyol_dili_ve_edebiyati',
        'italyan_dili_ve_edebiyati',
        'fars_dili_ve_edebiyati',
        'hititoloji',
        'sumeroloji'
    ],
    'tarim_ve_ziraat_bilimleri': [
        'bahce_bitkileri',
        'tarla_bitkileri',
        'bitki_koruma',
        'zootekni',
        'toprak_bilimi_ve_bitki_besleme'
    ],
    'genel': [
        'erasmus_ve_global_degisim_programlari',
        'staj_ve_profesyonel_is_hayati_giris'
    ],
    'ozel_arastirma_alanlari': [
        'guvenlik_bilimleri_ve_strateji',
        'psikolojik_harp_ve_sosyal_muhendislik'
    ],
    'on_lisans_programlari': [
        'polis_meslek_yuksekokulu_dersleri'
    ]
}

def create_final():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        # README for container if missing
        readme = os.path.join(c_path, 'README.md')
        if not os.path.exists(readme):
             with open(readme, 'w', encoding='utf-8') as f:
                f.write(f"# {container.replace('_', ' ').title()}\n\nBu klasör {container} ile ilgili alanları barındırır.\n")

        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"Final Step Created: {container}/{d}")
    print(f"\nFinal Check Complete: {count} new areas added.")

if __name__ == "__main__":
    create_final()
