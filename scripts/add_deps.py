import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# 1. Fix Turkish characters in all existing folder names at the root (excluding hidden/special folders)
def replace_tr_chars(text):
    tr_map = {
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'İ': 'I',
        'ç': 'c', 'Ç': 'C',
        'ü': 'u', 'Ü': 'U',
        'ö': 'o', 'Ö': 'O',
        'ğ': 'g', 'Ğ': 'G'
    }
    for search, replace in tr_map.items():
        text = text.replace(search, replace)
    return text

for d in os.listdir(root_dir):
    full_path = os.path.join(root_dir, d)
    if os.path.isdir(full_path):
        if d in ['.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates']:
            continue
        new_name = replace_tr_chars(d)
        if new_name != d:
            new_path = os.path.join(root_dir, new_name)
            # if exists, we might need a merge but usually it's just pure rename
            if not os.path.exists(new_path):
                os.rename(full_path, new_path)
                print(f"Renamed {d} -> {new_name}")

# Also explicitly rename `mühendisligi` in any directory using os.rename to be doubly sure!
# Since replace_tr_chars covers ü -> u, and g was already g (mühendisligi), it will become muhendisligi.

# Let's ensure directories inside ozel_arastirma_alanlari are perfectly ASCII
special_path = os.path.join(root_dir, 'ozel_arastirma_alanlari')
if os.path.exists(special_path):
    for d in os.listdir(special_path):
        fpath = os.path.join(special_path, d)
        if os.path.isdir(fpath):
            new_name = replace_tr_chars(d)
            if new_name != d:
                new_fpath = os.path.join(special_path, new_name)
                if not os.path.exists(new_fpath):
                    os.rename(fpath, new_fpath)
                    print(f"Renamed {d} -> {new_name}")

# 2. Add Missing Departments
missing_deps = [
    'isletme_muhendisligi',
    'ucak_muhendisligi',
    'gemi_insaati_ve_gemi_makineleri_muhendisligi',
    'otomotiv_muhendisligi',
    'fizik_muhendisligi',
    'matematik_muhendisligi',
    'nukleer_enerji_muhendisligi',
    'yonetim_bilisim_sistemleri',
    'ekonometri',
    'calisma_ekonomisi_ve_endustri_iliskileri',
    'veterinerlik',
    'odyoloji',
    'ebelik',
    'turk_dili_ve_edebiyati',
    'ingiliz_dili_ve_edebiyati',
    'mutercim_ve_tercumanlik',
    'arkeoloji',
    'sanat_tarihi',
    'okul_oncesi_ogretmenligi',
    'ingilizce_ogretmenligi',
    'ozel_egitim_ogretmenligi'
]

for dep in missing_deps:
    dep_path = os.path.join(root_dir, dep)
    if not os.path.exists(dep_path):
        os.makedirs(dep_path)
        # Create a basic README.md
        readme_content = f"# {dep.replace('_', ' ').title()}\n\nBu klasör {dep.replace('_', ' ').title()} bölümüne ait akademik notlar, araştırmalar ve dökümanlar içindir.\n"
        with open(os.path.join(dep_path, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"Created {dep}")

print("Missing departments added and folders sanitized.")
