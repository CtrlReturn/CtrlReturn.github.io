Clock.bpm = 93
Root.default = "G"
Scale.default = Scale.minor
var.chordOne = (0, 1, 2, [7, -3])
var.chordTwo = (0, 2, 3, 4, [6, 11/2])
var.chordThree = [(0, 2), (0, 2), (0, 2, 7)]
var.chordFour = Pvar([(0, 4), (3, 8), (0, PRand(Scale.default, seed=2)), (3, PRand(Scale.default, seed=6))])

d1 >> glass(var.chordOne, oct=4, dur=16, lpf=linvar([2400, 1200], 128), lpr=3/4, hpf=400, beat_dur=1, peak=4/5, level=6/5, room=linvar([1/2, 1], 128), mix=linvar([1/2, 2/3], 128), amplify=2/3, amp=0)
d1.amp=linvar([1/8, 2/3], 128)

p1 >> prayerbell(var.chordThree, oct=PRand([6, 7], 16), dur=16, echo=(0, 1/2, 2, 3, 4, 6), echotime=8, pong=1, pongtime=4, room=1, mix=3/4, amplify=1/3*var([PxRand([1/4, 1], seed=7), 0], PRand([16, 32, 64, 96, 48], seed=10)), amp=0)
p1.amp=3/4

b2 >> ssaw(0, oct=3, dur=16, sus=32, delay=PRand([4, 8, 16, 24, 12], seed=9), atk=2, shape=1, blur=3/2, lpf=200, lpr=1/2, room=2/3, mix=2/3, amplify=6/5*PRand([0, 1], [64, 128, 96, 160], seed=34), amp=0)
b2.amp=1

n1 >> brown(dur=1, sus=1, cut=4, hpf=[900, 1200, 500, 700], hpr=1/4, shape=3/4, room=3/4, mix=2/3, pan=PSine(64), amplify=1/8, amp=1)

b1 >> play("D", sdb=1, sample=1, dur=4, room=3/4, mix=1/2, amplify=4/5, amp=1)
b2 >> play("D", sdb=1, sample=PxRand([2, 4]), dur=4, delay=2, echo=[0, 1/2], echotime=4, room=3/4, mix=1/2, amplify=4/5, amp=1)
drums = Group(b1, b2)
drums.amp=1

k4 >> play("x", sdb=1, sample=6, dur=8, delay=[(0, 1/2), 0, 0, [0, (0, 3)]], blur=3/2, lpf=400, amplify=4/5*P[1, 0], amp=0)
k5 >> play("x", sdb=1, sample=4, dur=8, delay=[(0, 1/2), 0, 0, [0, (0, 3)]], blur=3/2, lpf=0, amplify=4/5*P[1, 0], amp=0)
k6 >> play("t", sdb=1, sample=3, dur=8, delay=7, room=2/3, mix=1/3, amplify=2/3, amp=0)
BK = Group(k4, k5, k6)
BK.amp=1

h1 >> play("S", sdb=1, sample=8, dur=PDur(3, 12)*8, echo=1/2, echotime=[2, 2, 4], room=2/3, mix=2/3, amplify=1/2, amp=1).sometimes("stutter", echo=[1/2, (1/3, 2/3)])

l1 >> bass(var.chordOne, oct=PRand([4,4,5,6,4]), dur=2, amp=1.2, lpf=100, drive=0.01, dist=0, chop = PRand([1,2,3,4])).often("stutter", PRand(1,5), oct=PRand([5,6,7,8]))
k1 >>klank(l1.pitch+[0,0,1,2], dur=4, hpf=var([10000, 8000, 15000]), amp=0.3, drive=0.1, room=2).stop()
k2 >> keys(k1.pitch,  dur=1/3, lpf=500, sus=0.1 * PRand(1,10), delay=(0,1/PRand([1,2,3])), pan=PRand([-1, 1]), chop=PRand(1,5), room=PRand(0,5)).often("stutter", PRand([1,5]), oct=PRand(5,9))

