def firstDuplicate(a):

    aset = set()
    for i in a:
        if i in aset:
            return i
        else:
            aset.add(i)

    if len(aset) == len(a):
        return -1
