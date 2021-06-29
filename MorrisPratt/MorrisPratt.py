def preMP(pattern, pattern_len, nextMP):
    i = 0
    j = nextMP[0] = -1
    while i < pattern_len:
        # print("i = " + str(i) + "; j = " + str(j))
        # print(pattern[i] + " " + pattern[j])
        # print(nextMP)
        while j > -1 and pattern[i] != pattern[j]:
            # print("i = " + str(i) + "; j = " + str(j))
            # print(pattern[i] + " " + pattern[j])
            # print(nextMP)
            j = nextMP[j]
        i += 1
        j += 1
        nextMP[i] = j


def MorrisPratt(pattern, pattern_len, string, string_len):
    nextMP = [0] * (len(pattern) + 1)
    preMP(pattern, pattern_len, nextMP)
    print(nextMP)
    i = 0
    j = 0
    while i < string_len:
        print("i = "+str(i) +";j = "+str(j))
        print(string[i] +" "+ pattern[j])
        while j > -1 and pattern[j] != string[i]:
            j = nextMP[j]
            print("i = " + str(i) + ";j = " + str(j))
        j += 1
        i += 1
        if j >= pattern_len:
            print("Tìm thấy từ khóa " + string[i - j:i - j + pattern_len] + " tại vị trí:" + str(i - j))
            j = nextMP[j]


pattern = "asddadasddd"
string = "awasdakdhasddadasdddkalwd"
# pattern = "GCAGAGAG"
# string = "GCATCGCAGAGAGTATACAGTACG"
MorrisPratt(pattern, len(pattern), string, len(string))
