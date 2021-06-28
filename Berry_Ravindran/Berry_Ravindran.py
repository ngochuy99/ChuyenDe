def preBrBc(pattern, pattern_len, BrBc):
    BrBc = [[pattern_len + 2] * 256, [pattern_len] * 256]
    print(BrBc)
    i = 0
    while i < 256:
        BrBc[i][ord(pattern[0])] = pattern_len + 1
        i += 1
    i = 0

    while i < pattern_len - 1:
        print(pattern_len - i)
        BrBc[ord(pattern[i])][ord(pattern[i + 1])] = pattern_len - i
        i += 1
    i = 0
    while i < 256:
        BrBc[ord(pattern[pattern_len - 1])][i] = 1
        i += 1
    print(BrBc)
    print("  ", end="")
    for x in "ACGT":
        print(x + " ", end="")
    print("")
    for x in "ACGT":
        print(x + " ", end="")
        for y in "ACGT":
            print(str(BrBc[ord(x)][ord(y)]) + " ", end="")
        print("")


Search_pattern = "GCAGAGAG"
Search_String = "GCATCGCAGAGAGTATACAGTACG"
BrBc = []
preBrBc(Search_pattern, len(Search_pattern), BrBc)
