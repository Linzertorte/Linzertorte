
# auto split audio by silence detection
# ffmpeg -i "2.mp3" -af silencedetect=noise=-30dB:d=0.5 -f null - 2> vol.txt
# python audio_split.py vol.txt
def convert(t):
    i = int(t)
    s = int((t - i)*1000)
    h = i/3600
    i = i%3600
    m = i/60
    i = i%60
    return "%02d:%02d:%02d,%03d"%(h,m,i,s)

import sys
F = sys.argv[1]
INTERVAL = 5
cnt = 1
with open(F) as f:
    l,r = 0,0
    skipped = False
    for line in f.readlines():
        line = line.rstrip()
        if "silence_start" in line:
            t = float(line.split(':')[1])
            if t - l < INTERVAL:
                skipped = True
                continue
            r = t
            skipped = False
            print cnt
            print convert(l),'-->',convert(r)
            print cnt
            print
            cnt += 1
        elif "silence_end" in line:
            t = float(line.split('|')[0].split(':')[1])
            if not skipped:
                l = t
