from testData import *


def NotSoNaive(pattern, pattern_len, string, string_len):
    j, k, ell, compare_time = 0, 0, 0, 0
    if pattern[0] == pattern[1]:
        k = 2
        ell = 1
    else:
        k = 1
        ell = 2
    while j < string_len - pattern_len:
        if pattern[1] != string[j + 1]:
            j += k
        else:
            if pattern[2:pattern_len] == string[j + 2: j + pattern_len] and pattern[0] == string[j]:
                print("Tìm thấy từ khóa " + string[j:j + pattern_len] + " tại vị trí:" + str(j))
            j += ell


Search_String = "ASSDJ1AVASSSDJAV"
Search_pattern = "SSDJ"
NotSoNaive(Search_pattern, len(Search_pattern), Search_String, len(Search_String))
