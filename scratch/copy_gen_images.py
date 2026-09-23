import shutil
import os

source_dir = r"C:\Users\Asus\.gemini\antigravity\brain\3ea7cb13-02c4-4efc-8866-11bbbad3b7ce"
dest_dir = r"c:\Users\Asus\Desktop\dm-site\img"

mapping = {
    "hero_bg_industrial": "hero_bg_industrial.jpg",
    "industries_aerospace": "industries_aerospace.jpg",
    "quality_lab": "quality_lab.jpg"
}

for root, dirs, files in os.walk(source_dir):
    for f in files:
        for prefix, target_name in mapping.items():
            if f.startswith(prefix) and f.endswith(".jpg"):
                src_path = os.path.join(root, f)
                dst_path = os.path.join(dest_dir, target_name)
                shutil.copy2(src_path, dst_path)
                print(f"Copied {f} -> {dst_path}")
