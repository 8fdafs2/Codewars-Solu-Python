def sc_01(apple):
    for row in apple:
        for col in row:
            if col == 'B':
                return [apple.index(row), row.index(col)]
                
                
def sc_02(apple):
    for x, row in enumerate(apple):
        for y, col in enumerate(row):
            if col == 'B':
                return [x, y]
                
def sc_03(apple):
    return [[x, row.index('B')] for x, row in enumerate(apple) if 'B' in row][0]