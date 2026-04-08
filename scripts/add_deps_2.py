import os

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

missing_deps = [
    'jeofizik_muhendisligi',
    'deniz_ulastirma_isletme_muhendisligi',
    'gemi_makineleri_isletme_muhendisligi',
    'ergoterapi',
    'dil_ve_konusma_terapisi',
    'gerontoloji',
    'sosyal_hizmet',
    'acil_yardim_ve_afet_yonetimi',
    'lojistik_yonetimi',
    'havacilik_yonetimi',
    'uluslararasi_ticaret_ve_lojistik',
    'insan_kaynaklari_yonetimi',
    'sosyal_bilgiler_ogretmenligi',
    'turkce_ogretmenligi',
    'cizgi_film_ve_animasyon'
]

for dep in missing_deps:
    dep_path = os.path.join(root_dir, dep)
    if not os.path.exists(dep_path):
        os.makedirs(dep_path)
        readme_content = f"# {dep.replace('_', ' ').title()}\n\nBu klasör {dep.replace('_', ' ').title()} bölümüne ait akademik notlar, araştırmalar ve dökümanlar içindir.\n"
        with open(os.path.join(dep_path, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"Created {dep}")

print("Phase 2 missing departments added.")
