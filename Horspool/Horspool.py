def PreBmBc(pattern, pattern_len, BmBc):
    i = 0
    while i < 256:
        BmBc[i] = pattern_len
        i += 1
    i = 0
    while i < pattern_len-1:
        BmBc[ord(pattern[i])] = pattern_len - i - 1
        i += 1



def Horspool(pattern, pattern_len, string, string_len):
    BmBc = [0] * 256
    PreBmBc(pattern, pattern_len, BmBc)
    j = 0
    while j <= string_len - pattern_len:
        c = string[j + pattern_len - 1]
        if string[j:j + pattern_len] == pattern:
            print("Tìm thấy pattern "+string[j:j + pattern_len]+" tại vị trí:" + str(j))
        j += BmBc[ord(c)]


from testData import *

Horspool(Search_pattern, len(Search_pattern), Search_String, len(Search_String))
