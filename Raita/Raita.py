from testData import *


def preBmBc(pattern, pattern_len, BmBc):
    i = 0
    while i < 256:
        BmBc[i] = pattern_len
        i += 1
    i = 0
    while i < pattern_len - 1:
        BmBc[ord(pattern[i])] = pattern_len - i - 1
        i += 1


def Raita(pattern, pattern_len, string, string_len):
    BmBc = [0] * 256
    preBmBc(pattern, pattern_len, BmBc)
    j = 0
    while j < string_len - pattern_len:
        if pattern[pattern_len-1] == string[j + pattern_len-1] and pattern[0] == string[j] and pattern[
            int(pattern_len / 2)] == string[int(j + pattern_len / 2)] and pattern[1:pattern_len - 1] == string[
                                                                                                        j + 1:j + pattern_len - 1]:
            print("Tìm thấy từ khóa " + string[j:j + pattern_len] + " tại vị trí:" + str(j))
        j += BmBc[ord(string[j + pattern_len - 1])]


# Search_pattern = "GCAGAGAG"
# Search_String = "GCATCGCAGAGAGTATACAGTACG"

Raita(Search_pattern, len(Search_pattern), Search_String, len(Search_String))
