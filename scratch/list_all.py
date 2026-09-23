import os

def get_all_files(dir_path):
    all_files = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), dir_path).replace('\\', '/')
            all_files.append(rel)
    return all_files

print("=== ALL FILES IN DM-SITE ===")
for f in sorted(get_all_files('.')):
    if not f.startswith('.git') and not f.startswith('scratch'):
        print(f)
