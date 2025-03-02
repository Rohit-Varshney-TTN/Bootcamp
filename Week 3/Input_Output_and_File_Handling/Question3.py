command=input("Enter the command: ")
delimiter= None
quotation= '"'
skip=0
head=0
tail=0
unique=set()
command=command.split()

if command[0]=="csvlook":
    file_path=command[-1]

    if "-d" in command:
        delimiter = command[command.index("-d")+1]
    if "-q" in command:
        quotation = command[command.index("-q")+1]
    if "-f" in command:
        numbers = command[command.index("-f")+1]
        for num in numbers.split(","):
            unique.add(int(num)-1)
    if "--skip-row" in command:
        skip = int(command[command.index("--skip-row")+1])
    if "--head" in command:
        head = int(command[command.index("--head")+1])
    if "--tail" in command:
        tail = int(command[command.index("--tail")+1])

    with open(file_path,"r") as file:
        lines=[]
        for line in file:
            lines.append(line)

    if delimiter is None:
        delimiter = "\t"
        
    data=[]
    for line in lines:
        data.append(line.split(","))

    if skip:
        data=data[skip:]
    if head:
        data=data[:head]
    if tail:
        data=data[-tail:]

    for row in data:
        if unique:
            print(delimiter.join(quotation+row[i]+quotation for i in unique if i<len(row)))
        else:
            print(delimiter.join(quotation+col+quotation for col in row))