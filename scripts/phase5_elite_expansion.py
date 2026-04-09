import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

ADDITIONS = {
    'on_lisans_programlari': [
        'asansor_teknolojisi',
        'sualti_teknolojisi',
        'avcilik_ve_yaban_hayati',
        'atik_yonetimi',
        'buyukbas_hayvan_yetistiriciligi',
        'cay_tarimi_ve_isleme',
        'un_ve_unlu_mamuller_teknolojisi',
        'sut_ve_besi_hayvanciligi',
        'seracilik',
        'organik_tarim',
        'bagcilik',
        'aricilik',
        'tibbi_tanitim_ve_pazarlama',
        'optisyenlik',
        'ortopedik_protez_ve_ortez',
        'patoloji_laboratuvar_teknikleri',
        'perfuzyon_teknikleri',
        'radyoterapi',
        'yasli_bakimi',
        'evde_hasta_bakimi',
        'eczane_hizmetleri',
        'agiz_ve_dis_sagligi',
        'diyaliz',
        'elektronorofizyoloji',
        'is_ve_ugrasi_terapisi_onlisans',
        'podoloji',
        'nukleer_tip_teknikleri',
        'is_sagligi_ve_guvenligi_onlisans',
        'itfaiyecilik_ve_sivil_savunma',
        'ozel_guvenlik_ve_koruma',
        'yerel_yonetimler',
        'bankacilik_ve_sigortacilik_onlisans',
        'muhasebe_ve_vergi_uygulamalari',
        'buro_yonetimi_ve_yonetici_asistanligi',
        'halkla_iliskiler_ve_tanitim_onlisans',
        'turizm_ve_otel_isletmeciligi_onlisans',
        'turizm_ve_seyahat_hizmetleri',
        'rayli_sistemler_isletmeciligi',
        'rayli_sistemler_makine_teknolojisi',
        'rayli_sistemler_elektrik_elektronik_teknolojisi',
        'gemi_insaati_onlisans',
        'gemi_makineleri_isletme_onlisans',
        'deniz_ulastirma_ve_isletme_onlisans',
        'yat_isletme_ve_yonetimi',
        'sivil_havacilik_kabin_hizmetleri',
        'sivil_hava_ulastirma_isletmeciligi_onlisans',
        'ucak_teknolojisi'
    ],
    'kariyer_ve_sertifikasyonlar': [
        'cisco_ccna_ccnp',
        'comptia_a_plus_sec_plus',
        'aws_certified_architect',
        'google_cloud_professional',
        'microsoft_azure_solutions',
        'pmp_proje_yonetimi',
        'cfa_chartered_financial_analyst',
        'toefl_ielts_ingilizce',
        'goethe_zertifikat_almanca',
        'delf_dalf_fransizca',
        'itil_v4_foundation',
        'six_sigma_green_black_belt'
    ],
    'meta_yetkinlikler_ve_gelisim': [
        'monk_mode_disiplin_sistemi',
        'zaman_yonetimi_ve_u_u',
        'hizli_ogrenme_teknikleri',
        'müzakere_ve_ikna_sanati',
        'sun_tzu_stratejik_düşünce',
        'liderlik_ve_ekip_yonetimi',
        'finansal_okuryazarlik_ve_yatirim',
        'stoisizm_ve_mental_dayaniklılık'
    ]
}

def create_phase5():
    total_new = 0
    for container, depts in ADDITIONS.items():
        c_path = os.path.join(ROOT_DIR, container)
        os.makedirs(c_path, exist_ok=True)
        # Container README
        readme = os.path.join(c_path, 'README.md')
        if not os.path.exists(readme):
            with open(readme, 'w', encoding='utf-8') as f:
                f.write(f"# {container.replace('_', ' ').title()}\n\nBu klasör {container} kapsamındaki profesyonel ve akademik alanları barındırır.\n")
        
        for d in depts:
            d_path = os.path.join(c_path, d)
            if not os.path.exists(d_path):
                os.makedirs(d_path)
                total_new += 1
                print(f"Phase 5 Created: {container}/{d}")
    
    print(f"\nPhase 5 Addition Complete: {total_new} new folders created.")

if __name__ == "__main__":
    create_phase5()
