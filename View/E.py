import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '\\Quarto\\Controller\\UserDatabase.db')

print(dirname)
print(filename)

for root, dirs, files in os.walk("."):
    for d in dirs:
        print(os.path.relpath(os.path.join(root, d), "."))
    for f in files:
        print(os.path.relpath(os.path.join(root, f), "."))
