import os
import shutil

root = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# Mapping: old_path -> new_container_name
to_move = {
    'hukuk': 'hukuk_bilimi',
    'ilahiyat': 'ilahiyat_ve_din'
}

for old, container in to_move.items():
    old_path = os.path.join(root, old)
    container_path = os.path.join(root, container)
    new_dept_path = os.path.join(container_path, old)
    
    if not os.path.exists(container_path):
        os.makedirs(container_path)
        with open(os.path.join(container_path, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(f"# {container.replace('_', ' ').title()}\n\nBu klasör {old} ve ilgili alanları barındırır.\n")

    if os.path.exists(old_path) and not os.path.exists(new_dept_path):
        shutil.move(old_path, new_dept_path)
        print(f"Moved {old} to {container}/{old}")
    else:
        print(f"Skipped {old} (already moved or doesn't exist)")
