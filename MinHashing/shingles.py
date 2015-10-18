def get_shingles(string, shingle_length):
    ret = set([])
    for i in range(0, len(string) - shingle_length + 1):
        ret.add(string[i:i + shingle_length])

    return sorted(list(ret))

def L(n, p1, p2):
    ret = 0
    for i in range(0, len(p1)):
        ret += abs((p1[i] - p2[i])**n)

    return ret**(1.0/n)


def L1L2():
    ps = []
    ps.append((63, 8))
    ps.append((51, 18))
    ps.append((58, 13))
    ps.append((56, 15))

    for p in ps:
        print L(1, p, (0, 0)),  L(1, p, (100, 40))

    for p in ps:
        print L(2, p, (0, 0)),  L(2, p, (100, 40))

def main():
    L1L2()
    return

    s1 = get_shingles('ABRACADABRA', 2)
    s2 = get_shingles('BRICABRAC', 2)

    print len(s1)
    print len(s2)

    print len(set(s1) & set(s2))

    s1_ = set(get_shingles('ABRACADABRA', 1))
    s2_ = set(get_shingles('BRICABRAC', 1))

    print len(s1_ & s2_)
    print len(s1_ | s2_)

if __name__ == '__main__':
    main()




    """How many 2-shingles does ABRACADABRA have?
How many 2-shingles does BRICABRAC have?
How many 2-shingles do they have in common?
What is the Jaccard similarity between the two documents"?"""