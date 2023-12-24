def solution(s):
    words = s.split(" ")
    answer = []
    for word in words:
        new_word = ''
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                new_word += w.upper()
            else:
                new_word += w.lower()
        answer.append(new_word)
    return " ".join(answer)