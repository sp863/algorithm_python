import numpy as np


def solution(keymap, targets):
    # incorrect solution...
    answer = []

    for i in range(len(targets)):
        count = 0
        for letter in targets[i]:
            found = []

            for key in keymap:
                if letter in key:
                    found.append(key.index(letter) + 1)

            if len(found) > 0:
                count += min(found)

        if count > 0:
            answer.append(count)

    return [-1] if len(found) <= 0 else answer

# Solution


def solution(keymap, targets):
    answer = []

    for target in targets:
        tmp_num = 0
        for t in target:
            num_lst = []
            for k in keymap:
                try:
                    num_lst.append(k.index(t))
                except:
                    num_lst.append(np.inf)

            tmp_num += (min(num_lst)+1)

        if tmp_num == np.inf:
            answer.append(-1)
        else:
            answer.append(tmp_num)

    return answer


def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer

# most answers utilize a keymap dictionary to reduce time complexity when searching for a letter
# Also, my solution was incorrect because I didn't consider the case where a letter is not in the keymap ex) [-1, -1, -1]
