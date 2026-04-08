import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

SKIP = {'.git', '.github', '.vs', 'assets', 'genel', 'scripts', 'templates',
        'ozel_arastirma_alanlari', 'meta_muhendislik', 'ogretmenlik',
        'saglik', 'temel_bilimler', 'sosyal_ve_beseri_bilimler'}

# ── Mapping: folder_name -> group ────────────────────────────────────────────
groups = {
    'saglik': [
        'ameliyathane_hizmetleri', 'anestezi_ve_reanimasyon', 'beslenme_ve_diyetetik',
        'cocuk_gelisimi', 'dil_ve_konusma_terapisi', 'dis_hekimligi', 'ebelik',
        'eczacilik', 'ergoterapi', 'fizyoterapi_ve_rehabilitasyon', 'gerontoloji',
        'hemsirelik', 'molekuler_biyoloji_ve_genetik', 'odyoloji', 'ozurluluk_calismalari',
        'saglik_yonetimi', 'tibbi_goruntuleme_teknikleri', 'tibbi_laboratuvar_teknikleri',
        'tip', 'veterinerlik', 'acil_yardim_ve_afet_yonetimi',
    ],
    'temel_bilimler': [
        'astronomi_ve_uzay_bilimleri', 'biyoistatistik', 'biyoloji',
        'fizik', 'istatistik', 'jeoloji', 'kimya', 'matematik',
    ],
    'sosyal_ve_beseri_bilimler': [
        'antropoloji', 'arkeoloji', 'cografya', 'dilbilim', 'ekonomi', 'ekonometri',
        'felsefe', 'iktisat', 'isletme', 'maliye', 'muhasebe_ve_finans_yonetimi',
        'psikoloji', 'sanat_tarihi', 'siyaset_bilimi_ve_kamu_yonetimi',
        'sosyal_hizmet', 'sosyoloji', 'tarih', 'uluslararasi_iliskiler',
        'dis_ticaret', 'ekonometri', 'calisma_ekonomisi_ve_endustri_iliskileri',
        'sigortacilik_ve_risk_yonetimi', 'girisimcilik', 'insan_kaynaklari_yonetimi',
        'lojistik_yonetimi', 'enerji_yonetimi', 'yonetim_bilisim_sistemleri',
        'uluslararasi_ticaret_ve_lojistik', 'havacilik_yonetimi', 'spor_yoneticiligi',
        'rekreasyon', 'antrenorluk_egitimi', 'beden_egitimi_ve_spor_bilimleri',
    ],
}

readme_texts = {
    'saglik': "# 🏥 SAĞLIK BİLİMLERİ\n\nBu klasör tüm sağlık bilimleri bölümlerini barındırır. YÖK standartlarına göre adlandırılmıştır.\n",
    'temel_bilimler': "# 🔬 TEMEL BİLİMLER\n\nBu klasör temel fen ve doğa bilimleri bölümlerini barındırır.\n",
    'sosyal_ve_beseri_bilimler': "# 👥 SOSYAL ve BEŞERİ BİLİMLER\n\nBu klasör sosyal bilimler, beşeri bilimler, iktisat ve işletme bölümlerini barındırır.\n",
}

# Create group dirs and README
for group_name, readme_text in readme_texts.items():
    group_path = os.path.join(root_dir, group_name)
    if not os.path.exists(group_path):
        os.makedirs(group_path)
    readme_path = os.path.join(group_path, 'README.md')
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_text)

# Move departments
total = 0
for group_name, members in groups.items():
    group_path = os.path.join(root_dir, group_name)
    seen = set()
    for d in members:
        if d in seen:
            continue
        seen.add(d)
        src = os.path.join(root_dir, d)
        dst = os.path.join(group_path, d)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)
            print(f"[{group_name}] {d}")
            total += 1

print(f"\nToplam {total} bölüm taşındı.")
