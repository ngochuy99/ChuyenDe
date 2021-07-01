def preQsBc(x, m, qsBc):
    i = 0
    while i < 256:
        qsBc[i] = m + 1
        i += 1
    i = 0
    while i < m:
        qsBc[ord(x[i])] = m - i
        i += 1

def QuickSearch(pattern, pattern_len, string, string_len):
    j, qsBc = 0, [0] * 256
    preQsBc(pattern, pattern_len, qsBc)
    while j < string_len - pattern_len:
        if pattern == string[j:j + pattern_len]:
            print("Tìm thấy từ khóa "+string[j:j + pattern_len]+" tại vị trí:" + str(j))
        j += qsBc[ord(string[j + pattern_len])]

from testData import *
Search_pattern = "asddadasddd"
Search_String = "awasdakdhasddadasdddkalwd"
QuickSearch(Search_pattern, len(Search_pattern), Search_String, len(Search_String))
