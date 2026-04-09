import os
import shutil

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
MUH_DIR = os.path.join(ROOT_DIR, "meta_muhendislik")

# Super Merge Map: Source -> Target
SUPER_MERGE_MAP = {
    # Textile
    "tekstil_tasarimi": "tekstil_muhendisligi",
    
    # Materials
    "fonksiyonel_malzeme_bilimi": "metalurji_ve_malzeme_muhendisligi",
    "yumusak_madde_bilimi_ve_muhendisligi": "metalurji_ve_malzeme_muhendisligi",
    "akilli_malzemeler_ve_teknoloji": "metalurji_ve_malzeme_muhendisligi",
    
    # Aviation
    "sevk_ve_itki_muhendisligi": "havacilik_ve_uzay_muhendisligi",
    
    # Marine
    "akilli_deniz_ekipmanlari": "gemi_insaati_ve_gemi_makineleri_muhendisligi",
    
    # Electronics
    "elektronik_bilgi_materyalleri": "elektronik_ve_haberlesme_muhendisligi",
    
    # Nuclear
    "nukleer_kimya_muhendisligi": "nukleer_enerji_muhendisligi",
    
    # Micro-Nano
    "mikro_nano_sistemler_ve_cihazlar": "mikro_elektro_mekanik_sistemler_mems",
}

RENAME_MAP = {
    "mikro_elektro_mekanik_sistemler_mems": "mikro_nano_sistemler_ve_mems"
}

def super_consolidate():
    # 1. Merging
    for src, dst in SUPER_MERGE_MAP.items():
        src_path = os.path.join(MUH_DIR, src)
        dst_path = os.path.join(MUH_DIR, dst)
        
        if os.path.exists(src_path):
            print(f"Executing Super Merge: {src} -> {dst}")
            if not os.path.exists(dst_path):
                # If target doesn't exist, just rename (unlikely for targets like civil/textile)
                os.rename(src_path, dst_path)
            else:
                # Merge subfolders (00-06)
                for item in os.listdir(src_path):
                    s_item = os.path.join(src_path, item)
                    d_item = os.path.join(dst_path, item)
                    if os.path.isdir(s_item):
                        if not os.path.exists(d_item):
                            try:
                                shutil.move(s_item, dst_path)
                            except:
                                pass
                try:
                    shutil.rmtree(src_path)
                except:
                    pass

    # 2. Renaming
    for old, new in RENAME_MAP.items():
        old_path = os.path.join(MUH_DIR, old)
        new_path = os.path.join(MUH_DIR, new)
        if os.path.exists(old_path) and not os.path.exists(new_path):
            print(f"Renaming {old} -> {new}")
            os.rename(old_path, new_path)

def finalize_titles():
    # Fix titles for all consolidated folders
    for folder in os.listdir(MUH_DIR):
        folder_path = os.path.join(MUH_DIR, folder)
        if os.path.isdir(folder_path):
            readme_path = os.path.join(folder_path, "README.md")
            if os.path.exists(readme_path):
                title = folder.replace('_', ' ').title()
                # Turkish Fixes
                title = title.replace('Muhendisligi', 'Mühendisliği')
                title = title.replace('Insaat', 'İnşaat')
                title = title.replace('Ulasim', 'Ulaşım')
                title = title.replace('Isletme', 'İşletme')
                title = title.replace('Tekstil', 'Tekstil')
                title = title.replace('Mikro Nano Sistemler Ve Mems', 'Mikro-Nano Sistemler ve MEMS')
                title = title.replace('Havacilik Ve Uzay', 'Havacılık ve Uzay')
                title = title.replace('Nukleer', 'Nükleer')
                title = title.replace('Gemi Insaati', 'Gemi İnşaatı')
                title = title.replace('Siber Guvenlik', 'Siber Güvenlik')
                
                with open(readme_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                if lines and lines[0].startswith('#'):
                    lines[0] = f"# {title}\n"
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                print(f"Final Title Check: {folder} -> {title}")

if __name__ == "__main__":
    super_consolidate()
    finalize_titles()
