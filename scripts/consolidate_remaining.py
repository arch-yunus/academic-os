import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

groups = {
    'edebiyat_ve_diller': [
        'alman_dili_ve_edebiyati',
        'arap_dili_ve_edebiyati',
        'fransiz_dili_ve_edebiyati',
        'ingiliz_dili_ve_edebiyati',
        'mutercim_ve_tercumanlik',
        'rus_dili_ve_edebiyati',
        'turk_dili_ve_edebiyati'
    ],
    'iletisim': [
        'gazetecilik',
        'halkla_iliskiler_ve_reklamcilik',
        'radyo_televizyon_ve_sinema',
        'yeni_medya_ve_iletisim'
    ],
    'turizm_ve_gastronomi': [
        'gastronomi_ve_mutfak_sanatlari',
        'konaklama_isletmeciligi',
        'turizm_isletmeciligi',
        'turizm_rehberligi',
        'yiyecek_icecek_isletmeciligi'
    ],
    'ogretmenlik': [
        'rehberlik_ve_psikolojik_danismanlik'
    ]
}

READMEs = {
    'edebiyat_ve_diller': '# 📚 EDEBİYAT VE DİLLER\n\nBu klasör dil, edebiyat ve çeviribilim ile ilgili bölümleri barındırır.\n',
    'iletisim': '# 📡 İLETİŞİM\n\nBu klasör medya, gazetecilik, radyo, televizyon ve halkla ilişkiler bölümlerini barındırır.\n',
    'turizm_ve_gastronomi': '# 🏨 TURİZM VE GASTRONOMİ\n\nBu klasör turizm, mutfak sanatları ve konaklama bölümlerini barındırır.\n'
}

for target_dir_name, members in groups.items():
    target_path = os.path.join(root_dir, target_dir_name)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    if target_dir_name in READMEs:
        readme_path = os.path.join(target_path, 'README.md')
        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(READMEs[target_dir_name])
                
    for d in members:
        src = os.path.join(root_dir, d)
        dst = os.path.join(target_path, d)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)
            print(f'Moved: {d} -> {target_dir_name}/{d}')
