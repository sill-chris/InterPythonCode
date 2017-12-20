def translate_python(message, offset):
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = s1[offset:] + s1[:offset]
    print(s1)
    print(s2)
    t = str.maketrans(s1, s2)
    print(message.translate(t))



if __name__ == '__main__':
    s = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
        rfyrq ufyr amknsrcpq ypc dmp.
        bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
        sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
        lmu ynnjw ml rfc spj."""

    translate_python("map", 2)
