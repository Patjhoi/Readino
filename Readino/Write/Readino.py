f = open('Write.ino', 'r')
pos = (('int', 'float', 'byte', 'bool', 'constante'),
       '\t\t\t\t\t Se declara la funcion',
       '\t\t\t\t\t Se declara la funcion en loop en donde irá el programa',
       '\t Se pone un breve comentario',
       '\t\t\t\t Se declara el pin',
       '\t\t\t\t Se lee el pin',
       '\t\t\t\t\t\t Se cierra el corchete',
       '\t\t\t\t\t Se pone un delay',
       '\t\t\t\t\t\t Se realiza un salto de linea')
state=('como salida', 'como entrada', 'y se activa la resistencia de pull up',
       'en alto', 'en bajo', 'INDEFINIDO')
while(True):
    line=f.readline()
    if('int' in line):
        p = line.rstrip('\n')
        print(p,"\t\t\t\t Se declara una variable de tipo", pos[0][0], "con el nombre: ", end="")
        p = p.replace(" ","")
        p = p.replace('int', '')
        name = []
        for var in p:
            if (var.isalpha()) | (var == '_') | (var.isnumeric()):
                name.append(var)
            else:
                break
        name = str(name)
        transTable = name.maketrans("", "", "'[], ")
        name = name.translate(transTable)
        if name.isidentifier():
            print(name, end=" ->  ")
            dig = p.replace(name, '')
            transTable = dig.maketrans("", "", " =;")
            dig = dig.translate(transTable)
            print(dig)
        else:
            print("")

    elif('float' in line):
        p = line.rstrip('\n')
        print(p,"\t\t\t\t Se declara una variable de tipo", pos[0][1], "con el nombre: ", end="")
        p = p.replace(" ","")
        p = p.replace('float', '')
        name = []
        for var in p:
            if (var.isalpha()) | (var == '_') | (var.isnumeric()):
                name.append(var)
            else:
                break
        name = str(name)
        transTable = name.maketrans("", "", "'[], ")
        name = name.translate(transTable)
        if name.isidentifier():
            print(name, end=" -> ")
            dig = p.replace(name, '')
            transTable = dig.maketrans("", "", " =;")
            dig = dig.translate(transTable)
            print(dig)
        else:
            print("")

    elif('byte' in line):
        p = line.rstrip('\n')
        print(p,"\t\t\t\t Se declara una variable de tipo", pos[0][2], "con el nombre: ", end="")
        p = p.replace(" ","")
        p = p.replace('byte', '')
        name = []
        for var in p:
            if (var.isalpha()) | (var == '_') | (var.isnumeric()):
                name.append(var)
            else:
                break
        name = str(name)
        transTable = name.maketrans("", "", "'[], ")
        name = name.translate(transTable)
        if name.isidentifier():
            print(name, end=" -> ")
            dig = p.replace(name, '')
            transTable = dig.maketrans("", "", " =;")
            dig = dig.translate(transTable)
            print(dig)
        else:
            print("")

    elif('bool' in line):
        p = line.rstrip('\n')
        print(p,"\t\t\t\t Se declara una variable de tipo", pos[0][3], "con el nombre: ", end="")
        p = p.replace(" ","")
        p = p.replace('bool', '')
        name = []
        for var in p:
            if (var.isalpha()) | (var == '_') | (var.isnumeric()):
                name.append(var)
            else:
                break
        name = str(name)
        transTable = name.maketrans("", "", "'[], ")
        name = name.translate(transTable)
        if name.isidentifier():
            print(name, end=" -> ")
            dig = p.replace(name, '')
            transTable = dig.maketrans("", "", " =;")
            dig = dig.translate(transTable)
            print(dig)
        else:
            print("")

    elif('#DEFINE' in line):
        p = line.rstrip('\n')
        print(p,"\t\t\t\t Se declara una variable de tipo", pos[0][4], "con el nombre: ", end="")
        p = p.replace(" ","")
        p = p.replace('#DEFINE', '')
        name = []
        for var in p:
            if (var.isalpha()) | (var == '_') | (var.isnumeric()):
                name.append(var)
            else:
                break
        name = str(name)
        transTable = name.maketrans("", "", "'[], ")
        name = name.translate(transTable)
        if name.isidentifier():
            print(name, end=" -> ")
            dig = p.replace(name, '')
            transTable = dig.maketrans("", "", " =;")
            dig = dig.translate(transTable)
            print(dig)
        else:
            print("")
        
    elif('void setup' in line):
        print(line.rstrip('\n'), pos[1])
    elif('void loop' in line):
        print(line.rstrip('\n'), pos[2])
    elif('//' in line):
        print(line.rstrip('\n'), pos[3])
    elif('pinMode' in line):
        p=line.rstrip('\n')
        print(p, pos[4], end = " ")
        p=p.replace(' ', '')    
        print(p[8], end = "")
        print(p[9].replace(',', ' '), end = " ")
        s= p.split(sep = ',')
        if('INPUT' in s[1]):
            print(state[1], end = " ")
            if('INPUT_PULLUP' in s[1]):
                print(state[2])
            else:
                print('\n')
        elif('OUTPUT' in s[1]):
            print(state[0])
        else:
            print(state[5])
    elif('digitalWrite' in line):
        p=line.rstrip('\n')
        print(p, pos[4], end = " ")
        p=p.replace(' ', '')
        print(p[13], end = "")
        print(p[14].replace(',', ' '), end = " ")
        s= p.split(sep = ',')
        if('HIGH' in s[1]):
            print(state[3])
        elif('LOW' in s[1]):
            print(state[4])
        else:
            print(state[5])
    # elif('digitalRead' in line):
    #     p = line.rstrip('\n')
    #     print(p, pos[4], end=" ")
    #     p = p.replace(' ', '')
    #     print(p[13], end="")
    #     print(p[14].replace(',', ' '), end=" ")
    #     s = p.split(sep=',')
    #     if('HIGH' in s[1]):
    #         print(state[2])
    #     elif('LOW' in s[1]):
    #         print(state[3])
    #     else:
    #         print(state[4])
    elif('}' in line):
        print(line.rstrip('\n'), pos[6])
    elif('delay' in line):
        print(line.rstrip('\n'), pos[7])
    elif('\n' in line):
        print(line.rstrip('\n'), pos[8])
    if not line:
        break
f.close()
