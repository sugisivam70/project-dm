import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print("=== CHECKING ALL HTML AND CSS ASSETS & LINKS ===")

for hf in html_files:
    print(f"\n--- {hf} ---")
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all src="..." and href="..."
    attr_matches = re.findall(r'(src|href)=["\']([^"\']+)["\']', content)
    for attr, val in attr_matches:
        if val.startswith(('http://', 'https://', 'mailto:', 'tel:', 'wa.me', '#', 'javascript:')):
            continue
        # clean path
        clean_val = val.split('?')[0].split('#')[0]
        if clean_val.startswith('/'):
            clean_val = clean_val[1:]
        
        if not os.path.exists(clean_val):
            print(f"BROKEN {attr}: '{val}' -> resolved: '{clean_val}'")

    # Find inline style url(...)
    url_matches = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', content)
    for val in url_matches:
        if val.startswith(('http://', 'https://', 'data:')):
            continue
        clean_val = val.split('?')[0].split('#')[0].replace('\\', '')
        if clean_val.startswith('/'):
            clean_val = clean_val[1:]
        if not os.path.exists(clean_val):
            print(f"BROKEN style url: '{val}' -> resolved: '{clean_val}'")

# Check style.css
print("\n--- style.css ---")
with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    css_content = f.read()
url_matches = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', css_content)
for val in url_matches:
    if val.startswith(('http://', 'https://', 'data:')):
        continue
    clean_val = val.split('?')[0].split('#')[0].replace('\\', '')
    if clean_val.startswith('/'):
        clean_val = clean_val[1:]
    if clean_val and not os.path.exists(clean_val):
        print(f"BROKEN css url: '{val}' -> resolved: '{clean_val}'")
