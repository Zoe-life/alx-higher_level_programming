#!/usr/bin/python3

for i in range(26):
    print(chr(ord('z') - i) if i % 2 == 0 else chr(ord('A') + i), end='')