#!/usr/bin/env python3

from z3 import *

FACES=6
FACELETS=4

FACE_F, FACE_U, FACE_D, FACE_R, FACE_L, FACE_B = 0,1,2,3,4,5

def rotate_FCW(s):
    return [
        [ s[FACE_F][2], s[FACE_F][0], s[FACE_F][3], s[FACE_F][1] ],   # for F
        [ s[FACE_U][0], s[FACE_U][1], s[FACE_L][3], s[FACE_L][1] ],   # for U
        [ s[FACE_R][2], s[FACE_R][0], s[FACE_D][2], s[FACE_D][3] ],   # for D
        [ s[FACE_U][2], s[FACE_R][1], s[FACE_U][3], s[FACE_R][3] ],   # for R
        [ s[FACE_L][0], s[FACE_D][0], s[FACE_L][2], s[FACE_D][1] ],   # for L
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_B][2], s[FACE_B][3] ] ]  # for B

def rotate_FH(s):
    return [ 
        [ s[FACE_F][3], s[FACE_F][2], s[FACE_F][1], s[FACE_F][0] ],
        [ s[FACE_U][0], s[FACE_U][1], s[FACE_D][1], s[FACE_D][0] ],
        [ s[FACE_U][3], s[FACE_U][2], s[FACE_D][2], s[FACE_D][3] ],
        [ s[FACE_L][3], s[FACE_R][1], s[FACE_L][1], s[FACE_R][3] ],
        [ s[FACE_L][0], s[FACE_R][2], s[FACE_L][2], s[FACE_R][0] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_B][2], s[FACE_B][3] ] ]

def rotate_FCCW(s):
    return [ 
        [ s[FACE_F][1], s[FACE_F][3], s[FACE_F][0], s[FACE_F][2] ],
        [ s[FACE_U][0], s[FACE_U][1], s[FACE_R][0], s[FACE_R][2] ],
        [ s[FACE_L][1], s[FACE_L][3], s[FACE_D][2], s[FACE_D][3] ],
        [ s[FACE_D][1], s[FACE_R][1], s[FACE_D][0], s[FACE_R][3] ],
        [ s[FACE_L][0], s[FACE_U][3], s[FACE_L][2], s[FACE_U][2] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_B][2], s[FACE_B][3] ] ]

def rotate_UCW(s):
    return [ 
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_U][2], s[FACE_U][0], s[FACE_U][3], s[FACE_U][1] ],
        [ s[FACE_D][0], s[FACE_D][1], s[FACE_D][2], s[FACE_D][3] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_B][2], s[FACE_B][3] ] ]

def rotate_UH(s):
    return [ 
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_U][3], s[FACE_U][2], s[FACE_U][1], s[FACE_U][0] ],
        [ s[FACE_D][0], s[FACE_D][1], s[FACE_D][2], s[FACE_D][3] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_B][2], s[FACE_B][3] ] ]

def rotate_UCCW(s):
    return [ 
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_U][1], s[FACE_U][3], s[FACE_U][0], s[FACE_U][2] ],
        [ s[FACE_D][0], s[FACE_D][1], s[FACE_D][2], s[FACE_D][3] ],
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_B][2], s[FACE_B][3] ] ]

def rotate_DCW(s):
    return [ 
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_U][0], s[FACE_U][1], s[FACE_U][2], s[FACE_U][3] ],
        [ s[FACE_D][2], s[FACE_D][0], s[FACE_D][3], s[FACE_D][1] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_B][2], s[FACE_B][3] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_R][2], s[FACE_R][3] ] ]

def rotate_DH(s):
    return [ 
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_B][2], s[FACE_B][3] ],
        [ s[FACE_U][0], s[FACE_U][1], s[FACE_U][2], s[FACE_U][3] ],
        [ s[FACE_D][3], s[FACE_D][2], s[FACE_D][1], s[FACE_D][0] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_F][2], s[FACE_F][3] ] ]

def rotate_DCCW(s):
    return [ 
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_U][0], s[FACE_U][1], s[FACE_U][2], s[FACE_U][3] ],
        [ s[FACE_D][1], s[FACE_D][3], s[FACE_D][0], s[FACE_D][2] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_B][2], s[FACE_B][3] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_B][0], s[FACE_B][1], s[FACE_L][2], s[FACE_L][3] ] ]

def rotate_RCW(s):
    return [ 
        [ s[FACE_F][0], s[FACE_D][1], s[FACE_F][2], s[FACE_D][3] ],
        [ s[FACE_U][0], s[FACE_F][1], s[FACE_U][2], s[FACE_F][3] ],
        [ s[FACE_D][0], s[FACE_B][2], s[FACE_D][2], s[FACE_B][0] ],
        [ s[FACE_R][2], s[FACE_R][0], s[FACE_R][3], s[FACE_R][1] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_U][3], s[FACE_B][1], s[FACE_U][1], s[FACE_B][3] ] ]

def rotate_RH(s):
    return [ 
        [ s[FACE_F][0], s[FACE_B][2], s[FACE_F][2], s[FACE_B][0] ],
        [ s[FACE_U][0], s[FACE_D][1], s[FACE_U][2], s[FACE_D][3] ],
        [ s[FACE_D][0], s[FACE_U][1], s[FACE_D][2], s[FACE_U][3] ],
        [ s[FACE_R][3], s[FACE_R][2], s[FACE_R][1], s[FACE_R][0] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_F][3], s[FACE_B][1], s[FACE_F][1], s[FACE_B][3] ] ]

def rotate_RCCW(s):
    return [ 
        [ s[FACE_F][0], s[FACE_U][1], s[FACE_F][2], s[FACE_U][3] ],
        [ s[FACE_U][0], s[FACE_B][2], s[FACE_U][2], s[FACE_B][0] ],
        [ s[FACE_D][0], s[FACE_F][1], s[FACE_D][2], s[FACE_F][3] ],
        [ s[FACE_R][1], s[FACE_R][3], s[FACE_R][0], s[FACE_R][2] ],
        [ s[FACE_L][0], s[FACE_L][1], s[FACE_L][2], s[FACE_L][3] ],
        [ s[FACE_D][3], s[FACE_B][1], s[FACE_D][1], s[FACE_B][3] ] ]

def rotate_LCW(s):
    return [ 
        [ s[FACE_U][0], s[FACE_F][1], s[FACE_U][2], s[FACE_F][3] ],
        [ s[FACE_B][3], s[FACE_U][1], s[FACE_B][1], s[FACE_U][3] ],
        [ s[FACE_F][0], s[FACE_D][1], s[FACE_F][2], s[FACE_D][3] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_L][2], s[FACE_L][0], s[FACE_L][3], s[FACE_L][1] ],
        [ s[FACE_B][0], s[FACE_D][2], s[FACE_B][2], s[FACE_D][0] ] ]
def rotate_LH(s):
    return [ 
        [ s[FACE_B][3], s[FACE_F][1], s[FACE_B][1], s[FACE_F][3] ],
        [ s[FACE_D][0], s[FACE_U][1], s[FACE_D][2], s[FACE_U][3] ],
        [ s[FACE_U][0], s[FACE_D][1], s[FACE_U][2], s[FACE_D][3] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_L][3], s[FACE_L][2], s[FACE_L][1], s[FACE_L][0] ],
        [ s[FACE_B][0], s[FACE_F][2], s[FACE_B][2], s[FACE_F][0] ] ]

def rotate_LCCW(s):
    return [ 
        [ s[FACE_D][0], s[FACE_F][1], s[FACE_D][2], s[FACE_F][3] ],
        [ s[FACE_F][0], s[FACE_U][1], s[FACE_F][2], s[FACE_U][3] ],
        [ s[FACE_B][3], s[FACE_D][1], s[FACE_B][1], s[FACE_D][3] ],
        [ s[FACE_R][0], s[FACE_R][1], s[FACE_R][2], s[FACE_R][3] ],
        [ s[FACE_L][1], s[FACE_L][3], s[FACE_L][0], s[FACE_L][2] ],
        [ s[FACE_B][0], s[FACE_U][2], s[FACE_B][2], s[FACE_U][0] ] ]

def rotate_BCW(s):
    return [ 
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_R][1], s[FACE_R][3], s[FACE_U][2], s[FACE_U][3] ],
        [ s[FACE_D][0], s[FACE_D][1], s[FACE_L][0], s[FACE_L][2] ],
        [ s[FACE_R][0], s[FACE_D][3], s[FACE_R][2], s[FACE_D][2] ],
        [ s[FACE_U][1], s[FACE_L][1], s[FACE_U][0], s[FACE_L][3] ],
        [ s[FACE_B][2], s[FACE_B][0], s[FACE_B][3], s[FACE_B][1] ] ]

def rotate_BH(s):
    return [ 
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_D][3], s[FACE_D][2], s[FACE_U][2], s[FACE_U][3] ],
        [ s[FACE_D][0], s[FACE_D][1], s[FACE_U][1], s[FACE_U][0] ],
        [ s[FACE_R][0], s[FACE_L][2], s[FACE_R][2], s[FACE_L][0] ],
        [ s[FACE_R][3], s[FACE_L][1], s[FACE_R][1], s[FACE_L][3] ],
        [ s[FACE_B][3], s[FACE_B][2], s[FACE_B][1], s[FACE_B][0] ] ]

def rotate_BCCW(s):
    return [ 
        [ s[FACE_F][0], s[FACE_F][1], s[FACE_F][2], s[FACE_F][3] ],
        [ s[FACE_L][2], s[FACE_L][0], s[FACE_U][2], s[FACE_U][3] ],
        [ s[FACE_D][0], s[FACE_D][1], s[FACE_R][3], s[FACE_R][1] ],
        [ s[FACE_R][0], s[FACE_U][0], s[FACE_R][2], s[FACE_U][1] ],
        [ s[FACE_D][2], s[FACE_L][1], s[FACE_D][3], s[FACE_L][3] ],
        [ s[FACE_B][1], s[FACE_B][3], s[FACE_B][0], s[FACE_B][2] ] ]

# op is turn number
def rotate(op, state, face, facelet):
    return If(op==0,  rotate_FCW (state)[face][facelet],
           If(op==1,  rotate_FCCW(state)[face][facelet],
           If(op==2,  rotate_UCW (state)[face][facelet],
           If(op==3,  rotate_UCCW(state)[face][facelet],
           If(op==4,  rotate_DCW (state)[face][facelet],
           If(op==5,  rotate_DCCW(state)[face][facelet],
           If(op==6,  rotate_RCW (state)[face][facelet],
           If(op==7,  rotate_RCCW(state)[face][facelet],
           If(op==8,  rotate_LCW (state)[face][facelet],
           If(op==9,  rotate_LCCW(state)[face][facelet],
           If(op==10, rotate_BCW (state)[face][facelet],
           If(op==11, rotate_BCCW(state)[face][facelet],
           If(op==12, rotate_FH  (state)[face][facelet],
           If(op==13, rotate_UH  (state)[face][facelet],
           If(op==14, rotate_DH  (state)[face][facelet],
           If(op==15, rotate_RH  (state)[face][facelet],
           If(op==16, rotate_LH  (state)[face][facelet],
           If(op==17, rotate_BH  (state)[face][facelet],
                      0))))))))))))))))))

move_names=["FCW", "FCCW", "UCW", "UCCW", "DCW", "DCCW", "RCW", "RCCW", "LCW", "LCCW", "BCW", "BCCW", "FH", "UH", "DH", "RH", "LH", "BH"]

def colors_to_array_of_ints(s):
    return [{"W":0, "G":1, "B":2, "O":3, "R":4, "Y":5}[c] for c in s]

def set_current_state (d):
    F=colors_to_array_of_ints(d["FACE_F"])
    U=colors_to_array_of_ints(d["FACE_U"])
    D=colors_to_array_of_ints(d["FACE_D"])
    R=colors_to_array_of_ints(d["FACE_R"])
    L=colors_to_array_of_ints(d["FACE_L"])
    B=colors_to_array_of_ints(d["FACE_B"])
    return F,U,D,R,L,B # return tuple

# 4
#init_F, init_U, init_D, init_R, init_L, init_B=set_current_state({"FACE_F":"RYOG", "FACE_U":"YRGO", "FACE_D":"WRBO", "FACE_R":"GYWB", "FACE_L":"BYWG", "FACE_B":"BOWR"})

# 5, 6s
init_F, init_U, init_D, init_R, init_L, init_B=set_current_state({"FACE_F":"BROW", "FACE_U":"YWOB", "FACE_D":"WROY", "FACE_R":"YGBG", "FACE_L":"BWYG", "FACE_B":"RORG"})

# 6, 50s   
#init_F, init_U, init_D, init_R, init_L, init_B=set_current_state({"FACE_F":"RBGW", "FACE_U":"YRGW", "FACE_D":"YGWB", "FACE_R":"OBRO", "FACE_L":"RYOO", "FACE_B":"WBYG"})

# 7, 6m30s 
#init_F, init_U, init_D, init_R, init_L, init_B=set_current_state({"FACE_F":"BBWY", "FACE_U":"OGOR", "FACE_D":"ROYY", "FACE_R":"WYBO", "FACE_L":"WWBG", "FACE_B":"RGGR"})

# 8, 47m
#init_F, init_U, init_D, init_R, init_L, init_B=set_current_state({"FACE_F":"YRRO", "FACE_U":"WWBY", "FACE_D":"WYWB", "FACE_R":"GBGO", "FACE_L":"RROB", "FACE_B":"OGYG"})

for TURNS in range(1,12): # 1..11
    print ("turns=", TURNS)

    s=Solver()

    state=[[[Int('state%d_%d_%d' % (n, side, i)) for i in range(FACELETS)] for side in range(FACES)] for n in range(TURNS+1)]
    op=[Int('op%d' % n) for n in range(TURNS+1)]

    for i in range(FACELETS):
        s.add(state[0][FACE_F][i]==init_F[i])
        s.add(state[0][FACE_U][i]==init_U[i])
        s.add(state[0][FACE_D][i]==init_D[i])
        s.add(state[0][FACE_R][i]==init_R[i])
        s.add(state[0][FACE_L][i]==init_L[i])
        s.add(state[0][FACE_B][i]==init_B[i])

    # solved state
    for face in range(FACES):
        for facelet in range(FACELETS):
            s.add(state[TURNS][face][facelet]==face)

    # turns:
    for turn in range(TURNS):
        for face in range(FACES):
            for facelet in range(FACELETS):
                s.add(state[turn+1][face][facelet]==rotate(op[turn], state[turn], face, facelet))

    if s.check()==sat:
        print ("sat")
        m=s.model()
        for turn in range(TURNS):
            print (move_names[int(str(m[op[turn]]))])
        exit(0)
