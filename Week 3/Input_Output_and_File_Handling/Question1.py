with open('number.txt','r') as number:
    for line in number:
        line=line.strip()
        try:
            line=float(line)
            if line.is_integer():
                line=int(line)
                if line%2==0:
                    with open('even.txt','a') as even_numbers:
                        even_numbers.write(f"{line} ")
                elif line%2!=0:
                    with open('odd.txt','a') as odd_numbers:
                        odd_numbers.write(f"{line} ")
            else:
                with open('float.txt','a') as float_point_numbers:
                    float_point_numbers.write(f"{line} ")
        except ValueError:
            print("Not Real Number")