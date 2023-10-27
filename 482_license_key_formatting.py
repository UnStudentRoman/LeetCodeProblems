

def licenseKeyFormatting(s, k):
    s_split = s.upper().replace('-','')[::-1]
    if s_split == '':
        return ''
    answer = ''
    counter = 0
    while len(s_split) >= k:
        while counter < k:
            answer += s_split[counter]
            counter += 1
        answer += '-'
        counter = 0
        s_split = s_split[k:]
    if len(s_split) > 0:
        answer += s_split
    answer = answer[::-1]
    if answer[0] == "-":
        return answer[1:]
    return answer

if __name__ == '__main__':
    s = "2-4A0r7-4k"
    k = 3
    print(licenseKeyFormatting(s, k))