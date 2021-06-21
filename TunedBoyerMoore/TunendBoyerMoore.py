def preBmBc(Pattern, Pattern_len, BmBc):
    i = 0
    while i < 256:
        BmBc[i] = Pattern_len
        i += 1
    i = 0
    while i < Pattern_len - 1:
        BmBc[ord(Pattern[i])] = Pattern_len - i - 1
        i += 1
    for x in Pattern:
        print(x + " : " + str(BmBc[ord(x)]))


Search_pattern = "GCAGAGAG"
Search_String = "GCATCGCAGAGAGTATACAGTACG"
BmBc = [0] * 256
preBmBc(Search_pattern, len(Search_pattern), BmBc)
