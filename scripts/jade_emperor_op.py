import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'temel_bilimler': [
        'ekolojik_restorasyon',
        'sulak_alan_bilimi_ve_yonetimi'
    ],
    'meta_muhendislik': [
        'mikro_elektro_mekanik_sistemler_mems',
        'deniz_hukuku_ve_stratejisi'
    ],
    'sosyal_ve_beseri_bilimler': [
        'bolgesel_ve_ulke_arastirmalari',
        'stratejik_hammadde_ekonomisi'
    ],
    'saglik': [
        'saglik_ve_tibbi_guvenlik'
    ],
    'genel': [
        'afet_yonetimi_ve_acil_durum_teknolojileri'
    ]
}

def create_jade_emperor_expansion():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"Jade Emperor Export Created: {container}/{d}")
    print(f"\nJade Emperor Expansion Complete: {count} new areas added.")

if __name__ == "__main__":
    create_jade_emperor_expansion()
