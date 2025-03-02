import file1
file1.show()

from importlib import reload
while True:
    file1.show()
    reload(file1)

