

def readlines(path , strip=False):
    with open(path , "r") as file:
        lines = file.readlines()
        newLines = []
        for line in lines:
            if line == "\n":
                continue
            if strip:
                newLines.append(line.strip())
            else:
                newLines.append(line)    
        return newLines

def clean_txt_data(path):
    users =readlines(path , True)
    with open(path , 'w') as file:
        file.writelines(list(map(lambda a : a + "\n" , users)))