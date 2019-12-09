with open("txt_2_4_04.txt", "r") as f, open("out_2_4_04.txt", "w") as o:
    out = []
    for l in f:
        out.append(l.rstrip())
    out.reverse()
    content = "\n".join(out)
    o.write(content)