import os
import shutil

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# 1. New Containers and moves
MOVES = {
    'spor_bilimleri': [
        'antrenorluk_egitimi',
        'beden_egitimi_ve_spor_bilimleri',
        'rekreasyon',
        'spor_yoneticiligi'
    ]
}

# 2. Additions
ADDITIONS = {
    'guzel_sanatlar': [
        'resim',
        'heykel',
        'geleneksel_turk_sanatlari',
        'fotograf',
        'el_sanatlari'
    ],
    'meta_muhendislik': [
        'rayli_sistemler_muhendisligi',
        'ulasim_muhendisligi'
    ],
    'ozel_arastirma_alanlari': [
        'prompt_muhendisligi',
        'blokzincir_ve_web3',
        'biyoinformatik',
        'ton_os_ekosistemi'
    ]
}

def move_depts():
    for container, depts in MOVES.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        # Create README for new container if missing
        readme = os.path.join(c_path, 'README.md')
        if not os.path.exists(readme):
            with open(readme, 'w', encoding='utf-8') as f:
                f.write(f"# 🏅 {container.replace('_', ' ').title()}\n\nBu klasör spor ve ilgili alanları barındırır.\n")
        
        # Look for these depts in sosyal_ve_beseri_bilimler
        src_container = os.path.join(ROOT_DIR, 'sosyal_ve_beseri_bilimler')
        for d in depts:
            src = os.path.join(src_container, d)
            dst = os.path.join(c_path, d)
            if os.path.exists(src) and not os.path.exists(dst):
                shutil.move(src, dst)
                print(f"Moved {d} to {container}/")

def create_additions():
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        for d in depts:
            d_path = os.path.join(c_path, d)
            os.makedirs(d_path, exist_ok=True)
            print(f"Created dept: {container}/{d}")

if __name__ == "__main__":
    move_depts()
    create_additions()
