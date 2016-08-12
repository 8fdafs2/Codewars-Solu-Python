def autocorrect(input):

    text = ["u", "you", "Youuuuu", "your"]
    text1 = ["!", "?", ".", ","]
    s1 = input.strip().split()
    s2 = []
    for i in s1:
        flag = False
        if i[-1] in text1:
            flag = True
            word = i[-1]
            i = i[:-1]
            print(word)
        if i in text:

            a = ["your", "sister"]
            s2.extend(a)

        else:
            if i not in s2:
                s2.append(i)
            if flag:
                s2[s2.index(i)] = s2[s2.index(i)] + word
    print s2
    s3 = (' ').join(s2)
    return s3
