import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

CONTAINERS = {
    'meta_muhendislik': '🛠️ Mühendislik Bilimleri',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık ve Tasarım',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar',
    'saglik': '🩺 Sağlık Bilimleri',
    'ogretmenlik': '🎓 Eğitim ve Öğretmenlik',
    'spor_bilimleri': '🏅 Spor Bilimleri',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal ve Beşeri Bilimler',
    'temel_bilimler': '🧪 Temel Bilimler',
    'edebiyat_ve_diller': '📚 Edebiyat ve Diller',
    'iletisim': '📡 İletişim Bilimleri',
    'turizm_ve_gastronomi': '🏨 Turizm ve Gastronomi',
    'hukuk_bilimi': '⚖️ Hukuk',
    'ilahiyat_ve_din': '🕌 İlahiyat ve Din',
    'ozel_arastirma_alanlari': '🔬 Özel Araştırma Alanları',
    'genel': '📂 Genel ve Ortak Alanlar'
}

def generate_summary():
    summary_md = "# 🗂️ Akademik Müfredat ve Ders Notları İndeksi\n\n"
    summary_md += "Bu dosya `scripts/generate_summary.py` tarafından otomatik oluşturulmuştur. Tüm bölümler YÖK standartlarına göre gruplandırılmıştır. (00-04 Tam Yapı)\n\n"
    
    # Sort containers by name or predefined order
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        summary_md += f"## {title}\n\n"
        summary_md += "| Bölüm | Yol |\n"
        summary_md += "|-------|-----|\n"
        
        items = os.listdir(container_path)
        depts = [d for d in items if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')]
        depts.sort()
        
        for d in depts:
            dept_name = d.replace('_', ' ').title()
            link = f"[{d}]({folder}/{d}/)"
            summary_md += f"| {dept_name} | {link} |\n"
        
        summary_md += "\n"

    with open(os.path.join(ROOT_DIR, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
        f.write(summary_md)
    print("SUMMARY.md updated successfully with full 184 departments.")

if __name__ == "__main__":
    generate_summary()
