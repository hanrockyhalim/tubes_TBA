class Stack:
    def __init__(self):
        self.n = 0
        self.isi = []

    def push(stack, x):
        stack.n += 1
        stack.isi.append(x)

    def pop(stack):
        x = stack.isi[stack.n-1]
        stack.n -= 1
        stack.isi = stack.isi[:stack.n]
        return x

    def is_empty(stack):
        return stack.n == 0

    def read_top(stack):
        return stack.isi[stack.n-1]

def input_handler(input_str):
    _for = "f"
    _kali = "x"
    _bagi = "v"
    _minus = "m"
    _gt = "s"
    _get = "t"
    _lt = "u"
    _let = "g"
    _bb = "y"
    _bt = "z"
    _et = "e"
    _eet = "h"
    _plus = "c"
    _sc = "q"
    _ic = "r"
    _ob = "k"
    _cb = "w"
    _dc = "d"
    

    words = input_str.split(" ")
    result = []

    for word in words:
        result.append([word])

    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == "for":
                result[i][j] = _for
            elif result[i][j] == "*":
                result[i][j] = _kali
            elif result[i][j] == "/":
                result[i][j] = _bagi
            elif result[i][j] == "-":
                result[i][j] = _minus
            elif result[i][j] == ">":
                result[i][j] = _gt
            elif result[i][j] == ">=":
                result[i][j] = _get
            elif result[i][j] == "<":
                result[i][j] = _lt
            elif result[i][j] == "<=":
                result[i][j] = _let
            elif result[i][j] == "{":
                result[i][j] = _bb
            elif result[i][j] == "}":
                result[i][j] = _bt
            elif result[i][j] == "(":
                result[i][j] = _ob
            elif result[i][j] == ")":
                result[i][j] = _cb
            elif result[i][j] == "==":
                result[i][j] = _eet
            elif result[i][j] == "=":
                result[i][j] = _et
            elif result[i][j] == ";":
                result[i][j] = _sc
            elif result[i][j] == "int":
                result[i][j] = _dc
            elif result[i][j] == "+":
                result[i][j] = _plus
            elif result[i][j] == "++":
                result[i][j] = _ic
            elif result[i][j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                result[i][j] = "a"

    return "".join([item[0] for item in result])

def main():
    stack = Stack()

    tabel_parsing = {
        "L": {
            "f": "fNDKCKVRMBAKT",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-",

        },
        "N": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "k",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "D": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "IVEV",
            "#": "-"
        },
        "K": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "q",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "R": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "_",
            "r": "r",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "M": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "_",
            "r": "-",
            "k": "-",
            "w": "w",
            "d": "-",
            "#": "-"
        },
        "A": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "VEVOV",
            "b": "VEVOV",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "VEVOV",
            "e": "-", 
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "V": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "a",
            "b": "b",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "i",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "C": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "VPV",
            "b": "VPV",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "VPV",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "O": {
            "f": "-",
            "x": "x",
            "v": "v",
            "m": "m",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "c",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "P": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "s",
            "t": "t",
            "u": "u",
            "g": "g",
            "y": "-",
            "z": "-",
            "h": "h",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "B": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "y",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "T": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "z",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        },
        "I": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "-",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "d",
            "#": "-"
        },
        "E": {
            "f": "-",
            "x": "-",
            "v": "-",
            "m": "-",
            "a": "-",
            "b": "-",
            "s": "-",
            "t": "-",
            "u": "-",
            "g": "-",
            "y": "-",
            "z": "-",
            "h": "-",
            "i": "-",
            "e": "e",
            "c": "-",
            "q": "-",
            "r": "-",
            "k": "-",
            "w": "-",
            "d": "-",
            "#": "-"
        }
    }
    simbol_awal = "L"

    print("Aturan Produksi :")
    print("LL(1) DENGAN NOTASI SEDERHANA")
    print("L -> fNDKCKRMBATK")
    print("A -> VEVOV")
    print("D -> IVEV")
    print("C -> VPV")
    print("V -> a | b | i") # variable
    print("P -> s | t | u | g | h") # comparison
    print("O -> x | v | m | c ") # operation
    print("I -> d") # declaration int
    print("K -> q") # semi colon
    print("N -> k") # open bracket
    print("M -> w") # close bracket
    print("B -> y") # open curly brackets
    print("T -> z") # close curly brackets
    print("E -> e") # Equal 
    print("R -> r") # Increment 
    print()

    print("Parse Table")
    print_table(tabel_parsing)
    print()

    input_str = input("Input: ")
    input_str = input_handler(input_str)

    print("Hasil:")

    stack = Stack()
    stack.push(simbol_awal)
    input_index = 0

    while not stack.is_empty():
        top = stack.read_top()
        simbol = ""
        if input_index < len(input_str):
            simbol = input_str[input_index]
        else:
            simbol = "#"

        if top >= "a":
            if top == simbol:
                stack.pop()
                input_index += 1
            else:
                print("Error/Ditolak")
                break
        elif top <= "Z":
            sel = tabel_parsing[top][simbol]
            if sel != "-":
                stack.pop()
                for i in range(len(sel) - 1, -1, -1):
                    stack.push(sel[i])
            else:
                print("Error/Ditolak")
                break

    if stack.is_empty() and input_index == len(input_str):
        print("DITERIMA")
    else:
        print("Error/Ditolak")


def print_table(tbl):
    print("  \tf\tx\tv\tm\ta\tb\ts\tt\tu\tg\ty\tz\th\ti\te\tc\tq\tr\tk\tw\td\t#")
    for jdlBaris, dt in tbl.items():
        print(jdlBaris + "\t", end="")
        for isi in dt.values():
            print(isi + "\t", end="")
        print()


if __name__ == "__main__":
    main()
