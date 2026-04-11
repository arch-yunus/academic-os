import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

EXCLUDE_DIRS = {'.git', '.vs', '.github', 'scripts', 'assets', 'templates'}

def final_sanity_check():
    errors = []
    dept_count = 0
    tier_count = 0
    
    for container in os.listdir(ROOT_DIR):
        c_path = os.path.join(ROOT_DIR, container)
        if not os.path.isdir(c_path) or container in EXCLUDE_DIRS:
            continue
            
        for dept in os.listdir(c_path):
            d_path = os.path.join(c_path, dept)
            if not os.path.isdir(d_path):
                continue
            
            dept_count += 1
            # Check main README
            if not os.path.exists(os.path.join(d_path, "README.md")):
                errors.append(f"Missing README: {container}/{dept}")
            
            # Check Tiers 00-06
            for i in range(7):
                tier_found = False
                for t_dir in os.listdir(d_path):
                    if t_dir.startswith(f"0{i}_"):
                        tier_found = True
                        tier_count += 1
                        # Check tier README
                        if not os.path.exists(os.path.join(d_path, t_dir, "README.md")):
                            errors.append(f"Missing Tier README: {container}/{dept}/{t_dir}")
                if not tier_found:
                    errors.append(f"Missing Tier Directory 0{i}: {container}/{dept}")

    print(f"Sanity Check Results:")
    print(f"Total Departments Verified: {dept_count}")
    print(f"Total Tiers Verified: {tier_count}")
    
    if not errors:
        print("ALL CLEAR: Every node is present and has a README.")
    else:
        print(f"FOUND {len(errors)} ANOMALIES.")
        for e in errors[:10]: # Print first 10
            print(f"- {e}")

if __name__ == "__main__":
    final_sanity_check()
