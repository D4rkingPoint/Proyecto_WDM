# src/modulation.py

def select_modulation(distance):
    if distance < 500:
        return '16-QAM'
    elif distance < 1000:
        return 'QPSK'
    else:
        return 'BPSK'
