class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def preSkipSearch(pattern, pattern_len, SST):
    i = 0
    while i < pattern_len:
        ptr = Node(i)
        ptr.next = SST[ord(pattern[i])]
        SST[ord(pattern[i])] = ptr
        i += 1


def SkipSearch(pattern, pattern_len, string, string_len):
    i = pattern_len - 1
    SST = [None] * 256
    preSkipSearch(pattern, len(pattern), SST)
    while i < string_len:
        j = SST[ord(string[i])]
        while j is not None:
            if string[i-j.data:pattern_len-j.data+i] == pattern:
                print("Tìm thấy từ khóa " + string[i-j.data:pattern_len-j.data+i] + " tại vị trí:" + str(
                    i-j.data))
            j = j.next
        i += pattern_len


pattern = "asddadasddd"
string = "awasdakdhasddadasdddkalwd"
SkipSearch(pattern, len(pattern), string, len(string))

