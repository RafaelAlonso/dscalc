from dscalc.lib import sum, subtract

def test_sum():
    # escolhe inputs dessa funcao
    a, b = 2, 2

    # deve saber qual e o output
    esperado = 4

    # deve ver se o que a gente consegue eh o esperado
    conseguiu = sum(a,b)
    assert conseguiu == esperado

    # escolhe inputs dessa funcao
    c, d = 5, 0

    # deve saber qual e o output
    expected = 5

    # deve ver se o que a gente consegue eh o esperado
    got = sum(c,d)
    assert got == expected

def test_subtract():
    # escolhe inputs dessa funcao
    a, b = 2, 2

    # deve saber qual e o output
    esperado = 0

    # deve ver se o que a gente consegue eh o esperado
    conseguiu = subtract(a,b)
    assert conseguiu == esperado

    # escolhe inputs dessa funcao
    c, d = 0, 5

    # deve saber qual e o output
    expected = -5

    # deve ver se o que a gente consegue eh o esperado
    got = subtract(c,d)
    assert got == expected
