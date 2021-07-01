def preBmBc(pattern, pattern_len, BmBc):
    i = 0
    while i < 256:
        BmBc[i] = pattern_len
        i += 1
    i = 0
    while i < pattern_len - 1:
        BmBc[ord(pattern[i])] = pattern_len - i - 1
        i += 1


def TunedBoyerMoore(pattern, pattern_len, string, string_len):
    BmBc = [0] * 256
    preBmBc(pattern, pattern_len, BmBc)
    shift = BmBc[ord(pattern[pattern_len - 1])]
    BmBc[ord(pattern[pattern_len - 1])] = 0
    j = 0
    while j<pattern_len:
        string+=pattern[pattern_len-1]
        j+=1

    j = 0
    while j < string_len:
        string[j+pattern_len-1]
        k = BmBc[ord(string[j + pattern_len - 1])]
        while k != 0:
            j += k
            k = BmBc[ord(string[j + pattern_len - 1])]
            j += k
            k = BmBc[ord(string[j + pattern_len - 1])]
            j += k
            k = BmBc[ord(string[j + pattern_len - 1])]
        if string[j:j + pattern_len] == pattern and j<string_len:
            print("Tìm thấy từ khóa " + string[j:j + pattern_len] + " tại vị trí:" + str(j))
        j += shift


Search_pattern = "GCAGAGAG"
Search_String = "GCATCGCAGAGAGTATACAGTACG"
TunedBoyerMoore(Search_pattern, len(Search_pattern), Search_String, len(Search_String))
