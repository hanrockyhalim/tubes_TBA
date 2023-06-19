def get_token(teks, j):
    k = len(teks)
    kata = ""

    while j < k and (teks[j] == ' ' or teks[j] == '\r' or teks[j] == '\n'):
        j += 1

    while j < k and teks[j] != ' ' and teks[j] != '\r' and teks[j] != '\n':
        if teks[j] == '>':
            if kata != "":
                return kata, j
            else:
                j += 1
                if j < k and teks[j] == '=':
                    j += 1
                    return ">=", j
                else:
                    return ">", j
        elif teks[j] == '<':
            if kata != "":
                return kata, j
            else:
                j += 1
                if j < k and teks[j] == '=':
                    j += 1
                    return "<=", j
                else:
                    return "<", j
        elif teks[j] == '=':
            if kata != "":
                return kata, j
            else:
                j += 1
                return "=", j
        elif teks[j] == '+':
            if kata != "":
                return kata, j
            else:
                j += 1
                return "+", j
        elif teks[j] == '-':
            if kata != "":
                return kata, j
            else:
                j += 1
                return "-", j
        kata += teks[j]
        j += 1

    return kata, j


def main():
    print("Enter the text input:")
    input_lines = []
    while True:
        line = input()
        if line == "":
            break
        input_lines.append(line)

    input_text = "\n".join(input_lines)
    i = 0
    hsl = ""
    k = len(input_text)

    while i < k:
        token, i = get_token(input_text, i)
        hsl += token.strip() + "\n"

    print("Hasil:")
    print(hsl)


if __name__ == "__main__":
    main()
