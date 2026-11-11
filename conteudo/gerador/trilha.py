"""Gera uma trilha instrumental original (sem direitos autorais) para os vídeos.

Lo-fi simples a 92 BPM: acordes em pad, arpejo suave, bumbo e chimbal leves.
uso: python3 trilha.py <saida.wav> [segundos]
"""
import sys, wave
import numpy as np

SR = 44100
BPM = 92
BEAT = 60 / BPM
dur = float(sys.argv[2]) if len(sys.argv) > 2 else 32.0
n = int(SR * dur)
t = np.arange(n) / SR
mix = np.zeros((n, 2))

def nota(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)

# progressão: Fmaj7 - Em7 - Dm7 - Cmaj7 (1 compasso cada = 4 tempos)
ACORDES = [[53, 57, 60, 64], [52, 55, 59, 62], [50, 53, 57, 60], [48, 52, 55, 59]]
BAIXO = [41, 40, 38, 36]
compasso = 4 * BEAT

def env(length, a, r):
    e = np.ones(length)
    ka, kr = int(a * SR), int(r * SR)
    e[:ka] = np.linspace(0, 1, ka)
    e[-kr:] *= np.linspace(1, 0, kr)
    return e

def add(sig, start, pan=0.0, gain=1.0):
    i = int(start * SR)
    if i >= n: return
    sig = sig[: n - i] * gain
    mix[i:i + len(sig), 0] += sig * (1 - pan) / 2 * 2 ** 0.5
    mix[i:i + len(sig), 1] += sig * (1 + pan) / 2 * 2 ** 0.5

k = 0
pos = 0.0
rng = np.random.default_rng(7)
while pos < dur:
    ac, bx = ACORDES[k % 4], BAIXO[k % 4]
    L = int(compasso * SR)
    tt = np.arange(L) / SR
    # pad: senoides levemente desafinadas
    pad = sum(np.sin(2 * np.pi * nota(m) * tt) + 0.5 * np.sin(2 * np.pi * nota(m) * 1.003 * tt) for m in ac)
    add(pad * env(L, 0.6, 0.6) * 0.05, pos)
    # baixo
    b = np.sin(2 * np.pi * nota(bx) * tt) * np.exp(-tt * 1.2)
    add(b * 0.22, pos)
    # arpejo em colcheias
    for j in range(8):
        m = ac[[0, 2, 1, 3, 2, 3, 1, 2][j]] + 12
        Ln = int(BEAT / 2 * SR * 1.6)
        tn = np.arange(Ln) / SR
        pl = (np.sin(2 * np.pi * nota(m) * tn) + 0.3 * np.sin(4 * np.pi * nota(m) * tn)) * np.exp(-tn * 6)
        add(pl * 0.07, pos + j * BEAT / 2, pan=0.4 if j % 2 else -0.4)
    # bateria
    for j in range(4):
        st = pos + j * BEAT
        if j in (0, 2):  # bumbo
            Lk = int(0.35 * SR); tk = np.arange(Lk) / SR
            f = 110 * np.exp(-tk * 18) + 45
            add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tk * 9) * 0.45, st)
        if j in (1, 3):  # caixa suave (ruído filtrado)
            Ls = int(0.2 * SR); ts = np.arange(Ls) / SR
            nz = np.convolve(rng.standard_normal(Ls), np.ones(6) / 6, 'same')
            add(nz * np.exp(-ts * 22) * 0.12, st)
        for h in (0, 0.5):  # chimbal
            Lh = int(0.05 * SR); th = np.arange(Lh) / SR
            nz = np.diff(rng.standard_normal(Lh + 1))
            add(nz * np.exp(-th * 70) * 0.035, st + h * BEAT, pan=0.3)
    pos += compasso
    k += 1

# fade in/out e normalização
fade = int(1.5 * SR)
mix[:int(0.3 * SR)] *= np.linspace(0, 1, int(0.3 * SR))[:, None]
mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
mix = np.tanh(mix * 1.2)
mix = mix / np.abs(mix).max() * 0.8
pcm = (mix * 32767).astype('<i2')
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('ok', sys.argv[1], dur, 's')
