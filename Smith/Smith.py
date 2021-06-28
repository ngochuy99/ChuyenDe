def preBmBc(pattern, pattern_len, BmBc):
    i = 0
    while i > 256:
        BmBc[i] = pattern_len
        i += 1
    i = 0
    while i < pattern_len - 1:
        BmBc[ord(pattern[i])] = pattern_len - i - 1
        i += 1


def preqsBc(pattern, pattern_len, qsBc):
    i = 0
    while i < 256:
        qsBc[i] = pattern_len + 1
        i += 1
    i = 0
    while i < pattern_len:
        qsBc[ord(pattern[i])] = pattern_len - i
        i += 1

def Smith(pattern, pattern_len, string, string_len):
    BmBc = [0] * 256
    qsBc = [0] * 256
    preBmBc(pattern, pattern_len, BmBc)
    preqsBc(pattern, pattern_len, qsBc)
    j = 0
    while j < string_len - pattern_len:
        if pattern == string[j:j + pattern_len]:
            print("Tìm thấy từ khóa " + string[j:j + pattern_len] + " tại vị trí:" + str(j))
        j += max(BmBc[ord(string[j + pattern_len-1])], qsBc[ord(string[j + pattern_len])])


from testData import *
# Search_pattern = "GCAGAGAG"
# Search_String = "GCATCGCAGAGAGTATACAGTACG"
Smith(Search_pattern, len(Search_pattern), Search_String, len(Search_String))
