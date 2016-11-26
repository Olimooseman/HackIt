
from colorama import Fore
from string import digits

def encrypt(string):
    remove_digits = str.maketrans("", "", digits)
    res = string.translate(remove_digits)
    return shifttext(res, len(string))

def shifttext(text, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    data = []
    for letter in text:
        if letter.strip() and letter in letters:
            data.append(letters[(letters.index(letter) + shift) % 26])
        else:
            data.append(letter)
    return "".join(data)

def run(prog, args, files):
    if openfile(files, prog) == "Programs cannot be opened.":
        if prog == "crack.prog":
            return encrypt(args[0].split(".")[0])
    return Fore.RED + prog + ":\t\tProgram not found"

def listfiles(files):
    toprint = ""
    for fil in files:
        toprint += fil[0] + "." + fil[1] + "\t\t"
    return toprint[:len(toprint) - 1]

def openfile(files, fil):
    for thing in files:
        if thing[0] == fil.split(".")[0]:
            toprint = ""
            for item in thing[2]:
                toprint += item + "\n"
            toprint = toprint[:len(toprint) - 1]
            return toprint
    return fil + ":\tNo such file in server."

def hlp(args):
    if len(args) == 0:
        return "This is HackNet port 59. Open welcome.txt, then proceed to connect to Tutorial server, \'tut.server\'."

def stringinate(lis):
    ret = ""
    for thing in lis:
        ret += "\n--------------------\nSubject: " + thing[0] + "\n"
        for content in thing[1]:
            ret += content + "\n"
    return ret

def findport(server, port):
    try:
        filetosort = open("./servers/" + server, "r")
    except:
        return ""
    for x in range(0, int(filetosort.readline())):
        for z in range(0, 2):
            filetosort.readline()
        for y in range(0, int(filetosort.readline())):
            filetosort.readline()

    for x in range(0, int(filetosort.readline())):
        toreturn = []
        curport = filetosort.readline()
        curport = curport[:len(curport)-1]

        for y in range(0, int(filetosort.readline())):
            toadd = []
            toadd.append(filetosort.readline())
            otheradd = []
            for z in range(0, int(filetosort.readline())):
                line = filetosort.readline()
                line = line[:len(line) - 1]
                otheradd.append(line)
            toadd.append(otheradd)
            if curport == port:
                toreturn.append(toadd)
        
        if curport == port:
            return stringinate(toreturn)
    return ""

def web(server):
    try:
        filetosort = open("./servers/" + server, "r")
    except:
        return ""
    for x in range(0, int(filetosort.readline())):
        for z in range(0, 2):
            filetosort.readline()
        for y in range(0, int(filetosort.readline())):
            filetosort.readline()

    for x in range(0, int(filetosort.readline())):
        toreturn = []
        curport = filetosort.readline()
        curport = curport[:len(curport)-1]

        for y in range(0, int(filetosort.readline())):
            toadd = []
            toadd.append(filetosort.readline())
            otheradd = []
            for z in range(0, int(filetosort.readline())):
                line = filetosort.readline()
    ret = ""
    for x in range(int(filetosort.readline())):
        ret += filetosort.readline()
    ret = ret[:len(ret) - 1]
    return ret



def connecttoserver(server):
    try:
        filetosort = open("./servers/" + server, "r")
    except:
        return []
    files = []
    for x in range(0, int(filetosort.readline())):
        toadd = []
        for z in range(0,2):
            line = filetosort.readline()
            line = line[:len(line) - 1]
            toadd.append(line)
        toaddtotoadd = []
        for y in range(0, int(filetosort.readline())):
            line = filetosort.readline()
            line = line[:len(line) - 1]
            toaddtotoadd.append(line)
        toadd.append(toaddtotoadd)
        files.append(toadd)
    return files

def register(userlis, server, curfiles):
    if not len(userlis) == 0:
        if userlis[0] in ["ls", "cd", "man"]:
            return ["This ain't bash."]
        elif userlis[0] == "help":
            return [hlp(userlis[1:])]
        elif userlis[0] == "connect":
            if userlis[1].split(".")[1] == "firewall":
                needed = encrypt(userlis[1].split(".")[0])
                pwrd = input(Fore.RED + "Password:\t\t")
                pwrd = pwrd[:len(pwrd) - 0]
                if not pwrd == needed:
                    return [Fore.RED + "Could not connect to server " + userlis[1], server, curfiles]
            files = connecttoserver(userlis[1])
            return ["Connected to server " + userlis[1] + " successfully.", userlis[1], files]
        elif userlis[0] == "files":
            return [listfiles(curfiles)]
        elif userlis[0] == "run":
            return [run(userlis[1], userlis[2:], curfiles)]
        elif userlis[0] == "port":
            return [findport(server, userlis[1])]
        elif userlis[0] == "open":
            return [openfile(curfiles, userlis[1])]
        elif userlis[0] == "web":
            return [web(userlis[1])]
        elif not userlis[0] == "q":
            return [Fore.RED + userlis[0] + ":\tNot a valid command"]
    return []

def main():
    for x in range(0,40):
        print(Fore.BLUE + "...")
    print(Fore.BLUE + "This game is powered by Moosie Shell.")
    print(Fore.BLUE + "Mosh powering up...")
    server = "home.server"
    curfiles = connecttoserver(server)
    userin = ""
    while not userin == "q":
        userin = input(Fore.GREEN + server + "\t>\t" + Fore.BLACK)
        try:
            thingy = register(userin.split(), server, curfiles)
        except:
            thingy = []
            print(Fore.RED + userin.split()[0] + ":\t used incorrectly")
        if not len(thingy) == 0 and not thingy[0] == "":
            print(Fore.BLACK + thingy[0])
        if len(thingy) == 3:
            server = thingy[1]
            curfiles = thingy[2]

main()
print(Fore.BLACK + "\n\n\n\nQuitting so soon? Coward.\n\n\n\n\nI'll be watching you.")
