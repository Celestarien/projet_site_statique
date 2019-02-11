import markdown
import os
import subprocess
from pathlib import Path

p = Path('.')

print('***********************************')
print('   Convertisseur Markdown - HTML   ')
print('***********************************')
print('1 - Convertir')
print('2 - Installer les packages (PIP)')
choice = int(input())


if choice == 1:
    print('***********************************')
    print('         Operating system          ')
    print('***********************************')
    print('1 - Windows')
    print('2 - Linux')
    choice2 = int(input())
    if choice2 == 1:        # Pour les OS Windows
        dossier = list(p.glob('**/*.md'))
        print("*************************************")
        print("Fichier que vous pouvez convertir: ")
        print(dossier)
        print("*************************************")
        while True:
            fichier = input("Quel est le nom de votre fichier markdown (sans l'extension) : ")
            os.system("python -m markdown " + fichier + ".md > " + fichier + ".html")
            print("Ok.")

    elif choice2 == 2:      # Pour les OS Linux
        dossier = list(p.glob('**/*.md'))
        print("*************************************")
        print("Fichier que vous pouvez convertir: ")
        print(dossier)
        print("*************************************")
        while True:
            fichier = input("Quel est le nom de votre fichier markdown (avec l'extension) : ")
            os.system("python3 -m markdown " + fichier + ".md > " + fichier + ".html")
            print("Ok.")
elif choice == 2:
    os.system("pip install markdown")


