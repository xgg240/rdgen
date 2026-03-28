import sys, zipfile

zip_path = sys.argv[1] if len(sys.argv) > 1 else 'secrets.zip'
# Use pyzipper to handle AES encrypted zip
try:
    import pyzipper
    with pyzipper.AESZipFile(zip_path, 'r') as zin:
        names = zin.namelist()
        print('Files in zip:', names)
        with zipfile.ZipFile('fixed.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for name in names:
                data = zin.read(name)
                new_name = 'secrets.json' if name == 'config.json' else name
                zout.writestr(new_name, data)
                print(f'  {name} -> {new_name}')
except ImportError:
    # Fallback if pyzipper not available
    with zipfile.ZipFile(zip_path, 'r') as zin:
        names = zin.namelist()
        print('Files in zip:', names)
        with zipfile.ZipFile('fixed.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for name in names:
                data = zin.read(name)
                new_name = 'secrets.json' if name == 'config.json' else name
                zout.writestr(new_name, data)
                print(f'  {name} -> {new_name}')

import os
os.replace('fixed.zip', zip_path)
print('Fixed zip created')
