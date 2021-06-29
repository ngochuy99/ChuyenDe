def preKMP(pattern, pattern_len, nextKMP):
    i = 0
    j = nextKMP[0] = -1
    pattern+="\0"
    while i < pattern_len:
        while j > -1 and pattern[i] != pattern[j]:
            j = nextKMP[j]
        i += 1
        j += 1
        if pattern[i] == pattern[j]:
            nextKMP[i] = nextKMP[j]
        else:
            nextKMP[i] = j



def KnuthMorrisPratt(pattern, pattern_len, string, string_len):
    nextKMP = [0] * (len(pattern) + 1)
    preKMP(pattern, pattern_len, nextKMP)
    i = 0
    j = 0
    print(nextKMP)
    while i < string_len:
        print("i = " + str(i) + ";j = " + str(j))
        print(string[i] + " " + pattern[j])
        while j > -1 and pattern[j] != string[i]:
            j = nextKMP[j]
            print("i = " + str(i) + ";j = " + str(j))
        j += 1
        i += 1
        if j >= pattern_len:
            print("Tìm thấy từ khóa " + string[i - j:i - j + pattern_len] + " tại vị trí:" + str(i - j))
            j = nextKMP[j]


pattern = "asddadasddd"
string = "awasdakdhasddadasdddkalwd"
KnuthMorrisPratt(pattern, len(pattern), string, len(string))
