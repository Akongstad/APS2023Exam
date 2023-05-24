ALPHABET_SIZE = 26

def mp(c):
    return ord(c) - ord('A')

class Node:
    def __init__(self):
        self.ch = [None] * ALPHABET_SIZE
        self.c = 0
        self.d = 0

    def insert(self, s, i = 0):
        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            self.c += 1
        else:
            self.c += 1
            v = mp(s[i])
            if self.ch[v] == None:
                self.ch[v] = Node()
                self.ch[v].d = self.d + 1

            self.ch[v].insert(s, i + 1)

    def cleanup(self):
        for i in range(ALPHABET_SIZE):
            if self.ch[i] != None:
                self.ch[i].cleanup()
                del self.ch[i]

    def count(self, count):
        count[self.d] = max(self.c, count[self.d])
        for i in range(ALPHABET_SIZE):
            if self.ch[i] != None:
                self.ch[i].count(count)

def main():
    while True:
        try:
            s = input().strip()
        except:
            break
        if len(s) == 0:
            break

        root = Node()
        for i in range(len(s)):
            if s[i] != ' ':
                root.insert(s, i)

        dpth = [0] * (len(s) + 3)
        root.count(dpth)
        for i in range(1, len(s) + 2):
            if dpth[i] > 1:
                print(dpth[i])
            else:
                print()
                break

if __name__ == "__main__":
    main()
