################################################################################
########################### WORKSHOP c-base BERLIN #############################
###########################       Fox and Beat     #############################
###########################           pit          #############################
################################################################################


Clock.bpm = 120  # set bpm / 120 default

# How to play samples? 'play' vs. 'loop'
# (depending on the duration: use loop for longer samples)

p1 >> play("x-o-", amp=.5)

l1 >> loop("foxdot", P[:16])

l1 >> loop("ian1", P[0:56])
# try to change P[0:56] --> P[13:16] # P[15:16] shaker # add 31, add 43 by creating a list [P[15:16], 31, 43]


################################################################################
#                                      samples                                 #
################################################################################

# 1. play the " " internal structure

# every letter/symbol refers to a folder of samples (that can be modified)
# (default sample=0)
# x -> kick / - -> h-hat / o -> snare

p1 >> play("x-o-")


# () play the first and then the second in a cycle so: x-o--xo-x-o ...
p1 >> play("(x-)(-x)o-")

# [] subdivide the beat (play multiple samples within the duration of one beat)
p1 >> play("x-[o-]-")

p1 >> play("[x-][-t][o][-]")

# Nested brackets
# random sound design: more hh = glitch (and melody!)
p1 >> play("x-o[--[--------]-------------------------]", amp=.3)
# !!!!!! --> lower volume or amp, just to be sure...
p1 >> play("x-o[--[--------------]-------------------]", amp=.3)
p1 >> play("x-o[--[--------------]------[--------]---]", amp=.3)

p1 >> play("x{-[ou]}-")  # {} random


# < >
# build more complex beats on the fly

p1 >> play("x.o.")
p2 >> play(".-.-", rate=6)

p1 >> play("x-o-", rate=2)

p1 >> play("<x-o->")
p2.stop()

p1 >> play("<x.o.><.-.->")

p1 >> play("<x.o.><->")
# add <-> to play simultaneously more than one sample, in this case: x and -, just -, o and -, just -


p1 >> play("<x.><.-o{-[oy]}>") #useful for drops: just remove <x.> part on the fly!



# 2. sample player attributes


p1 >> play("x", dur=PDur(3, 7))  # change dur 1, 1/2, 1/4, 1/3, 3/2

p1 >> play("<x.o.><.-.{-[oy]}>", sample=2)  # change sample

# change sample, but more fun
p1 >> play("<x.o.><.-.{-[oy]}>", sample=PRand(6))

# change dur PDur (3,8), (5,16), etc
p1 >> play("<x.o.><.-.{-[oy]}>", sample=2, dur=PDur(3, 8))

# change dur PDur (3,8), (5,16), etc
p1 >> play("<x>", sample=2, dur=PDur(3, 8))
p2 >> play("-", sample=PRange(8, 12), dur=PDur(5, 16))
# ...
p2 >> play("-", sample=PRange(8, 12), dur=PDur(5, 16), rate=PRand(7))
p3 >> play("-.", sample=PRange(8, 12), dur=PDur(14, 16), rate=-2)

print(PRhythm([1/2, (3, 8)]))
p1 >> play("x-o-", sample=2, dur=PRhythm([1/2, (3, 8)]))

print(PRhythm([1/2, (5, 8)]))
p1 >> play("x-o-", sample=2, dur=PRhythm([1/2, (5, 8)]))


print(Player.get_fxs())  # <- print effects

# adding some effects:

# e.g., reverb and delays

p1 >> play("x...", room=2, mix=.25, echo=1.3)


# Audio effects on certain samples only:

# reverb affects only high-hats
p1 >> play("x-x-", room=[0, 2], mix=.25, cut=1)

# reverb only on the last shot of hh:
p1 >> play("x-x-", room=[0, 0, 0, 2], mix=.25, cut=1)


###

p1 >> play("x-o-", dur=1/2).fadein()


p1 >> play("x-o-", dur=1/2).every(8, "palindrome")

p1 >> play("<x-o->", sample=2, dur=1/2).sometimes("amen")
p1 >> play("<x-o->", sample=2, dur=1/2).every(7, "amen")
p1 >> play("<x.oy><.-.{-[oy]}>", sample=2, dur=1/2).sometimes("palindrome")


k1 >> play("<.y-s.y-n.n-{*.}..-.>", sample=[8, PRand(6), 0, PRand(6)],
           rate=[1, PRand(6), PRand(6), PRand(6)], dur=PDur(8, 8), mix=0,
           room=1).sometimes("palindrome")

k2 >> play("<X.[.x].><.*>", sample=3, amp=1)

k1.mix = [0, .1, .3, .1]
k2.dur = PDur(5, 16)

k2 >> play("X.[.v].", sample=3, amp=1)

# bonus technique: PEuclid2 on amp

k1 >> play("<x {ii^}  x  ^>< rOrd td>", dur=1/4, sample=PRand(5), amp=PEuclid2(1,
           16, .5, 0)).rotate()  # the higher the first value, LESS sample will be reproduced

k1 >> play("xo.kjh.", room=10, mix=1, rate=linvar([0.8, -1]), amp=.7, cut=0.5)

p1 >> saw([0], oct=3).every(4, "shuffle")


Master().hpf = 0 #always remember that you can effect the whole Master with an attribute

# Polyrhythms

p1 >> play("x.", dur=PDur(3, 8))
p2 >> play("-.", dur=PDur(2, 8))

# PDur(3,8) PDur(4,8)
# PDur(5,8) PDur(4,8)
# PDur(7,8) PDur(4,8)


################################################################################
#                                        loops                                 #
################################################################################


e1 >> loop("loopz/noise4", P[:32])

e1 >> loop("loopz/noise4", P[28:32])

e1 >> loop("loopz/noise4", [P[28:32], 31, P[2:4], 5],
           dur=PDur(5, 16), amp=.5).spread()

e2 >> loop("loopz/maasai", P[8:16], room=1, mix=.5)

e2.stop()

print(Attributes)

# sorry M.I.A.
# por mi looping loco

Clock.bpm = 68


o1 >> loop("paper_v1", P[:16])

o1 >> loop("paper_v1", P[:16], coarse=2)  # coarse is nice on vocal loops

o2 >> loop("paper_v3", P[:16], rate=1)
o2 >> loop("paper_v4", P[:16], rate=1)


o1 >> loop("paper_v1", P[:16], rate=1, room=2, mix=.45, echo=1.2)


o3 >> loop("paper_v5", [P[:16], 5, P[12:16], 7], rate=- 1.125, room=2, mix=.25, cut=1, coarse=var([0, 2], 4))
# start a jam!

p1 >> play("x-[x].")

k1 >> play("<x {ii^}  x  ^>< rOrd td>", dur=1/4, sample=PRand(5), amp=PEuclid2(1,
           16, .5, 0)).rotate()  # remember :the higher the first value, LESS sample will be reproduced
