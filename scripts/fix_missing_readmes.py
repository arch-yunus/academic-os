import os

ROOT = r"g:\\Diğer bilgisayarlar\\Dizüstü Bilgisayarım\\github repolarım\\engineering-courses"

# Departments missing README and subdirs
MISSING = [
    ("mimarlik_ve_tasarim", "gorsel_iletisim_tasarimi"),
    ("mimarlik_ve_tasarim", "mimarlik"),
    ("ozel_arastirma_alanlari", "guzel_sanatlar"),
    ("saglik", "dis_hekimligi"),
    ("saglik", "molekuler_biyoloji_ve_genetik"),
    ("temel_bilimler", "biyoloji"),
]

# Template for main README (similar to previous ones)
def make_main_readme(title, emoji, desc):
    return f"# {emoji} {title}\n\n## 🎯 Amaç\n{desc}\n\n---\n\n## 📚 Temel Dersler\n- *(Ders listesi ekleyiniz)*\n\n---\n\n## 🔧 Kullanılan Araçlar ve Veritabanları\n| Alan | Araçlar / Platformlar |\n|------|----------------------|\n| Mevzuat | Mevzuat.gov.tr, Resmi Gazete |\n| İçtihat | Kazancı Hukuk, Lexpera, Sinerji Mevzuat |\n| Akademik | DergiPark, JSTOR, HeinOnline |\n| Belge / Dilekçe | Avukatlık Otomasyon Sistemleri (UYAP) |\n\n---\n\n## 🚀 Kariyer Alanları\n- *(Kariyer listesi ekleyiniz)*\n\n---\n\n## 📊 Gelecek Trendler\n- *(Trendler ekleyiniz)*\n\n---\n\n## 📂 Ders Ağacı\n- [01 Temel Bilimler ve Giriş](01_Temel_Bilimler_ve_Giris/)\n- [02 Alan Dersleri](02_Alan_Dersleri/)\n- [03 Seçmeli & İleri Uygulama](03_Secmeli_ve_Ileri_Uygulama/)\n- [04 Araştırma ve Bitirme](04_Arastirma_ve_Bitirme/)\n\n> [!TIP]\n> Yeni bir ders eklerken `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koy!\n"

# Subdir definitions (same as earlier script)
SUBDIR_DEFS = {
    "01_Temel_Bilimler_ve_Giris": {
        "label": "01 — Temel Bilimler ve Giriş",
        "desc": "Bölüme giriş niteliğindeki temel ders notları, genel kavramlar ve başlangıç kaynakları.",
    },
    "02_Alan_Dersleri": {
        "label": "02 — Alan Dersleri",
        "desc": "Bölümün özgül ve zorunlu alan derslerine ait notlar, ödevler ve kaynaklar.",
    },
    "03_Secmeli_ve_Ileri_Uygulama": {
        "label": "03 — Seçmeli & İleri Uygulama",
        "desc": "Seçmeli dersler, derinlemesine uygulama projeleri ve uzmanlaşma çalışmaları.",
    },
    "04_Arastirma_ve_Bitirme": {
        "label": "04 — Araştırma ve Bitirme",
        "desc": "Bitirme projeleri, staj raporları, seminer çalışmaları ve akademik araştırma notları.",
    },
}

DERS_SABLONU = """# 📝 Ders Notu Şablonu

## Ders Bilgileri
| Alan | Bilgi |
|------|-------|
| Ders Adı | *(buraya yaz)* |
| Öğretim Görevlisi | *(buraya yaz)* |
| Dönem | 20xx-20xx / Güz veya Bahar |
| Kredi | *(buraya yaz)* |

## 🎯 Dersin Amacı
*(Kısa açıklama)*

## 📚 Kaynaklar
- *(Kitap / Makale 1)*
- *(Kitap / Makale 2)*

## 📝 Notlar

### Hafta 1
...

### Hafta 2
...

## ✅ Katkı
Bu dosya kişisel not amaçlıdır. Paylaşmak için repository'e PR açabilirsin.
"""

def make_subdir_readme(dept_title, sub_key):
    sub = SUBDIR_DEFS[sub_key]
    return f"# 📂 {sub['label']} — {dept_title}\n\n## 📖 Açıklama\n{sub['desc']}\n\n---\n\n## 📝 Bu Klasöre Nasıl Katkı Yapılır?\n1. `DERS_SABLONU.md` (üst dizindeki) dosyasını bu klasöre kopyala\n2. Dosyayı `DERS_ADI.md` olarak yeniden adlandır\n3. İçini ders notları, ödevler ve kaynaklarla doldur\n4. Pull Request aç veya doğrudan push et\n\n> [!NOTE]\n> Bu klasör **{dept_title}** bölümünün **{sub['label']}** dönemine aittir.\n"

# Simple emoji and description mapping (you can customize)
EMOJI_DESC = {
    "gorsel_iletisim_tasarimi": ("🎨", "Görsel iletişim tasarımı, grafik ve UI/UX odaklı.") ,
    "mimarlik": ("🏛️", "Mimarlık, kentsel tasarım ve yapı bilimleri.") ,
    "guzel_sanatlar": ("🖼️", "Güzel sanatlar, resim, heykel ve sanat tarihi.") ,
    "dis_hekimligi": ("🦷", "Diş hekimliği, ağız sağlığı ve klinik uygulamalar.") ,
    "molekuler_biyoloji_ve_genetik": ("🧬", "Moleküler biyoloji ve genetik araştırmaları.") ,
    "biyoloji": ("🔬", "Biyoloji, temel yaşam bilimleri.") ,
}

for group, dept in MISSING:
    dept_path = os.path.join(ROOT, group, dept)
    os.makedirs(dept_path, exist_ok=True)
    emoji, desc = EMOJI_DESC.get(dept, ("📚", ""))
    title = dept.replace('_', ' ').title()
    # Main README
    with open(os.path.join(dept_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(make_main_readme(title, emoji, desc))
    # Subdir READMEs
    for sub_key in SUBDIR_DEFS.keys():
        sub_path = os.path.join(dept_path, sub_key)
        os.makedirs(sub_path, exist_ok=True)
        with open(os.path.join(sub_path, "README.md"), "w", encoding="utf-8") as f:
            f.write(make_subdir_readme(title, sub_key))
    print(f"[OK] {group}/{dept} created with subdirs")

print("\n=== TAMAMLANDI ===")
"
