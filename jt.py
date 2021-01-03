doc = """usage: simp <snowflake_1> ... <snowflake_n>
"""

# assumes mat is non-ragged
def fmt2d(mat):
    widths = []
    for i, _ in enumerate(mat[0]):
        widths.append(maxlencol(mat, i))
    
    fmtmat = []
    for i, row in enumerate(mat):
        fmtrow = []

        if i == 1:
            for width in widths:
                fmtrow.append("="*width)
            fmtmat.append(fmtrow)
            fmtrow = []

        for entry, width in zip(row, widths):
            fmtrow.append("{:>{}}".format(entry, width))
        fmtmat.append(fmtrow)
    
    return fmtmat


def maxlencol(mat, i):
    maxlen = 0
    for x in mat:
        if len(str(x[i])) > maxlen:
            maxlen = len(str(x[i]))
    return maxlen


def seconds(milliseconds):
    if milliseconds == 0:
        return " "
    return str(milliseconds / -1000) + " s"


def time(snowflake):
    return (snowflake >> 22)


def melt(flakes):
    table = [["", *flakes]]
    for flake1 in flakes:
        row = [flake1]
        for flake2 in flakes:
            row.append(seconds(time(flake1) - time(flake2)))
        table.append(row)
    return table


if __name__ == "__main__":
    x = [795213537164263425, 795213552872062986]
    print(melt(x))