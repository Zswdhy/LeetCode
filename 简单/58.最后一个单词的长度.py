def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    last_word = s.split(' ')[-1]
    return len(last_word)


if __name__ == '__main__':
    s = "Hello World"
    res = lengthOfLastWord(s)
