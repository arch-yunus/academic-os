import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'meta_muhendislik': [
        'yuksek_guclu_yariiletken_bilimi_ve_muhendisligi',
        'elektronik_bilgi_materyalleri',
        'akilli_deniz_ekipmanlari',
        'akilli_gorsel_muhendislik'
    ],
    'tarim_ve_ziraat_bilimleri': [
        'biyolojik_islah_teknolojisi'
    ],
    'saglik': [
        'saglik_bilimi_ve_teknolojisi',
        'medikal_cihaz_ve_ekipman_muhendisligi'
    ],
    'turizm_ve_gastronomi': [
        'kahve_bilimi_ve_muhendisligi'
    ],
    'spor_bilimleri': [
        'futbol_bilimi',
        'havacilik_sporlari'
    ],
    'guzel_sanatlar': [
        'dijital_tiyatro'
    ],
    'edebiyat_ve_diller': [
        'cin_klasik_calismalari'
    ]
}

def create_china_export_v2():
    count = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                count += 1
                print(f"Great Wall Export Created: {container}/{d}")
    print(f"\nGreat Wall Export Complete: {count} new strategic areas added.")

if __name__ == "__main__":
    create_china_export_v2()
