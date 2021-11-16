import math 
import pyttsx3
import morse_talk as mtalk
from translate import Translator

helpmenucredits = """                 Credits 
        Github: https://github.com/Axorax
        
        Made with ❤ by Axorax""" 

helpmenuop = """         Basic Calculator all operators list.
        + = addition
        - = subtraction
        / = division
        ÷ = division
        * = multiplication
        × = multiplication
        
        Results are returned in decimal value for more accuracy!"""
helpmenuerrors = """              Errors
        If you have gotten an error, make sure that you 
        have entered in the correct/accepted value or 
        number. Don't put words in places where numbers 
        are meant to be used. 
        
        If you find any bugs or errors in the code you
        can contact the owner:
        Discord: Aceward#0037
        Instagram: aceward1
        """
helpmenutext = """          Help Menu
    1 = All special commands list.
    2 = Basic Calculator all operators list.
    3 = I got an error.
    4 = Credits"""
helpmenuspecial = """         All special commands list.
        log10
        log2
        log1p
        isqrt
        isnan
        isfinite
        nan
        inf
        tau
        e
        pi
        ceil
        comb
        """
c = "https://www.youtube.com/channel/UCoIgEBRn2TeOnIAg46Y6log"

print("""What do you want to use?
Options:
1 = Normal Calculator (4 operators)
2 = Special (pi,e,nan & others)
3 = Morse Code
4 = Binary
5 = Translator
6 = Text To Speech (tts)
7 = other
""")
print("Tip: Type help if your stuck!")

wanttouse = input("Type here: ")

if wanttouse == "help":
    print(helpmenutext)
    helpmenu = input("Type here: ")
    if helpmenu == "1":
        print(helpmenuspecial)
    elif helpmenu == "2":
        print(helpmenuop)
    elif helpmenu == "3":
        print(helpmenuerrors)
    elif helpmenu == "4":
        print(helpmenucredits)

if wanttouse == "credits":
    print(helpmenucredits)

if wanttouse == "sl":
    print(helpmenuspecial)

if wanttouse == " ":
    exit
if wanttouse != "1" or "2" or "3" or "5" or "6":
    exit 

if wanttouse == "1":
    n1 = float(input("Enter your first number: "))
    o = input("Enter an operator: ")
    n2 = float(input("Enter your second number: "))
    creditssss = input("Do you want credits? y/n: ")
    if o == "+":
        print(n1 + n2)
    elif o == "-":
        print(n1 - n2)
    elif o == "/":
        print(n1 / n2)
    elif o == "÷":
        print(n1 / n2)
    elif o == "*":
        print(n1 * n2)
    elif o == "×":
        print(n1 * n2)
    else:
        print("Invalid. Try again...")   
    if creditssss == "y":
        print(c)

if wanttouse == "2":
    s = input("Enter a special: ")
    creditsss = input("Credits? y/n: ")
    if s == "pi":
        print(f"Pi = {math.pi}")
    elif s == "e":
        print(f"e = {math.e}")
    elif s == "tau":
        print(f"tau = {math.tau}")
    elif s == "inf":
        print(f"inf = {math.inf}")
    elif s == "nan":
        print(f"nan = {math.nan}")
    elif s == "isfinite":
        isfinitevalue = float(input("Enter a value: "))
        print(f"isfinite: {math.isfinite(isfinitevalue)}")
    elif s == "isnan":
        isnanvalue = float(input("Enter a value: "))
        print(f"isnan: {math.isnan(isnanvalue)}")
    elif s == "isqrt":
        isqrtvalue = float(input("Enter a vlue: "))
        print(f"isqrt: {math.isqrt(isqrtvalue)}")
    elif s == "log1p":
        log1 = float(input("Enter a value: "))
        print(f"log1p: {math.log1p(log1)}")
    elif s == "log2":
        log2 = float(input("Enter a value: "))
        print(f"log2: {math.log2(log2)}")
    elif s == "log10":
        log10 = float(input("Enter a value: "))
        print(f"log10: {math.log10(log10)}")
    elif s == "ceil":
        ceilvalue = float(input("Enter a value: "))
        print(f"ceil: {math.ceil(ceilvalue)}")
    elif s == "comb":
        combval1 = float(input("Enter value 1: "))
        combval2 = float(input("Enter value 2: "))
        print(f"comb: {math.comb(combval1, combval2)}")
    elif s == "q" or "quit" or "exit":
        exit 
    elif creditsss == "y":
        print(c)
    else:
        print("Function not found. Type sl to see all the available functions.") 

if wanttouse == "3":
    print("""Do you want to encode or decode?(Morse Code)
    1 = Encode
    2 = Decode """)
    enordecode = input("Type here: ")
    if enordecode == "1":
        encodetext = input("Encode; Type here: ")
        print(f"Encoded Message: {mtalk.encode(encodetext)}")
    elif enordecode == "2":
        decodetext = input("Decode; Type here: ")
        print(f"Decoded Message: {mtalk.decode(decodetext)}")
    else:
         print("Error. Pls try again.")

if wanttouse == "4":
    print("""Do you want to encode or decode?(Binary)
    1 = Encode
    2 = Decode """)
    bint = input("Type here: ")
    if bint == "1":
        binent = input("Encode; Type here: ")
        print(f"Encoded Message: {mtalk.encode(binent, encoding_type='binary')}")
    elif bint == "2":
        bindet = input("Decode; Type here: ")
        print(f"Decoded Message: {mtalk.decode(bindet, encoding_type='binary')}")
    else:
     print("Error. Pls try again.")

if wanttouse == "7":
    print("""Choose what you want to use:
    1 = lower
    2 = upper """)
    other_choose = input('Type here:')
    if other_choose == "1":
        if_1_chosen = input("Enter a value: ")
        print("Lower: " + if_1_chosen.lower())
    if other_choose == "2":
        if_2_chosen = input("Enter a value: ")
        print("Upper: " + if_2_chosen.upper())

if wanttouse == "5":
    trto = input("Translate to(example; en): ")
    trmsg = input("Message/text: ")
    trmsgto = Translator(to_lang=trto)
    trmsgoutput = trmsgto.translate(trmsg)
    print("Translating...")
    print(trmsgoutput)

if wanttouse == "6":
        tts = input("Tts message: ")
        engine = pyttsx3.init()
        engine.say(tts)
        engine.runAndWait()

if wanttouse or helpmenu == "quit" or "q" or "exit":
    exit 

engine = pyttsx3.init()
engine.say("Made with love by Axorax!")
engine.runAndWait()
