import subprocess

for folder in folders.iterdir():
    for fp in folder.glob('*.ipynb'):
        subprocess.call([
            'jupyter', 'nbconvert', '--clear-output', '--inplace',
            fp.name
        ])