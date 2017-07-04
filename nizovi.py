import sys

def main():
    struct = sys.stdin.readline().strip()

    whole_txt = "{"+"\n"
    gap = "  "
    word = gap
    for ch in struct[1:]:
        if ch != " ":
            if ch == "{":
                whole_txt += gap + ch + "\n"
                gap += "  "
                word = gap

            elif ch == ",":
                if word.strip() == "":
                    whole_txt = whole_txt[:-1]+ch+"\n"
                else:
                    whole_txt += word+ch + "\n"
                word = gap

            elif ch == "}":
                gap = gap[:-2]
                if word.strip()!="":
                    whole_txt += word + "\n" + gap + ch + "\n"
                else:
                    whole_txt += gap+ch+"\n"
                word = gap
            else:
                word += ch
    print whole_txt.strip()

if __name__ == '__main__':
    main()
