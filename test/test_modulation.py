from modulation import select_modulation

def test_modulation():
    assert select_modulation(300) == '16-QAM'
    assert select_modulation(700) == 'QPSK'
    assert select_modulation(1200) == 'BPSK'
