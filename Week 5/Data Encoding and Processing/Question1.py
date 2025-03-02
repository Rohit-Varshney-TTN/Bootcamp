import io 
file = io.StringIO()
file.write('Hello and Welcome to the TTN')
file.seek(0)
result = file.read()
print(result)