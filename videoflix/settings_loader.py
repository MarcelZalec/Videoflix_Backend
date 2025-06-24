import importlib.util
import os

def settings_module():
    base_dir = os.path.dirname(__file__)
    project_name = os.path.basename(base_dir)
    keyfile_path = os.path.join(base_dir, 'keyfile.py')

    if os.path.exists(keyfile_path):
        # Prüfen, ob das Modul local_settings auch wirklich importierbar ist
        home_settings_spec = importlib.util.find_spec(f'{project_name}.local_settings')
        if home_settings_spec is not None:
            print("Lokale Settings werden verwendet")
            return f'{project_name}.local_settings'

    print("Globale Settings werden verwendet")
    return f'{project_name}.settings'