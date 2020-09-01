#pip3 install pikepdf tqdm
#Con banner personal
import pikepdf, sys, random, time
from tqdm import tqdm
from colorama import init, Fore

GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED
BLUE = Fore.BLUE
GRAY = Fore.LIGHTBLACK_EX

#Banner
def ClownLogo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                   ____  ____  ______   ______                __            
                  / __ \/ __ \/ ____/  / ____/________ ______/ /_____  _____
                 / /_/ / / / / /_     / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
                / ____/ /_/ / __/    / /___/ /  / /_/ / /__/ ,< /  __/ /    
               /_/   /_____/_/       \____/_/   \__,_/\___/_/|_|\___/_/     
                                                             

         Autor -#- AlfonzMx Script de cracking PDF 100% efectivo "Uso Personal"       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

def usage():
    print(f"         {RED}usage {BLUE}: {GREEN}pdf_cracker.py [example.pdf] [wordlist.txt]{RESET}")

ClownLogo()

try:
    #Wordlist file
    wordlist = sys.argv[2]
    # the pdf file you want to crack its password
    pdf_file = sys.argv[1]
except:
    usage()
    exit()
# load password list
passwords = [ line.strip() for line in open(wordlist) ]

# iterate over passwords
for password in tqdm(passwords, "  Crack PDF"):
    try:
        # open PDF file
        with pikepdf.open(pdf_file, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print(f"{GREEN}   [{RED}+{GREEN}] Password found:{RESET}", f"{BLUE}", " %s" % (password), f"{RESET}")
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
