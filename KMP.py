def findPrefix(pattern, pattern_size, lsp):
    j = 0
    lsp[0]
    i = 1
    while i < pattern_size:
        print(lsp)
        if pattern[i] == pattern[j]:
            j += 1
            lsp[i] = j
            i += 1
        else:
            if j != 0:
                j = lsp[j-1]
            else:
                lsp[i] = 0
                i += 1

pattern = "aaaa"
lsp = [0] * len(pattern)
findPrefix(pattern, len(pattern), lsp)
# print(lsp)
