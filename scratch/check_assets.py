import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

src_regex = re.compile(r'(?:src|href|url\()\s*=\s*["\']?([^"\' >\)\?#]+)|url\(["\']?([^"\'\)\?#]+)["\']?\)', re.IGNORECASE)

print("Checking assets across HTML files...")
for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    matches = src_regex.findall(content)
    missing = []
    for m in matches:
        path = m[0] or m[1]
        path = path.strip()
        if not path or path.startswith('http') or path.startswith('https') or path.startswith('tel:') or path.startswith('mailto:') or path.startswith('data:') or path.startswith('#') or path.startswith('javascript:'):
            continue
        
        # strip leading / if present
        local_path = path.lstrip('/')
        local_path = local_path.replace('%20', ' ')
        
        if not os.path.exists(local_path):
            missing.append((path, local_path))
            
    if missing:
        print(f"\nIn {hf}:")
        for orig, loc in set(missing):
            print(f"  - MISSING: {orig} (resolved to: {loc})")
    else:
        print(f"\nIn {hf}: All local assets exist!")
