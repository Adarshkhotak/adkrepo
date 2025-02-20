def convert_moves(S):
    move_map={
        "snake":'s',
        "water":'w',
        "gun":'g'
    }
    converted=""
    i=0
    while i<=len(S):
        if S[i:i+5] in move_map:
            converted+=move_map[S[i:i+5]]
            i+=5
        elif S[i :i+4] in move_map:
            converted+=move_map[S[i:i+4]]
            i+=4
        elif S[i :i+3] in move_map:
            converted+=move_map[S[i:i+3]]
            i+=3
        else:
            i+=1
    return converted

def snake_water_gun(n,s):
    st=convert_moves(s)
    print(st)
    wins_for_A =0
    drwa=0
    wins_for_B=0
    for i in range(0,2*n,2):
        player_a_move= st[i]
        player_b_move=st[i+1]

        if (player_a_move=='s' and player_b_move=='w') or\
            (player_a_move=='w' and player_b_move=='g') or\
            (player_a_move=='g' and player_b_move=='s'):
            wins_for_A+=1
        
        elif (player_a_move=='s' and player_b_move=='s') or\
            (player_a_move=='w' and player_b_move=='w') or\
            (player_a_move=='g' and player_b_move=='g'):
            drwa+=1
        else:
            wins_for_B+=1
    
    return wins_for_A,drwa



S="snakewaterwatergungunsnakegungun"
res=snake_water_gun(4,S)
#converted_s=convert_moves(S)
print(res)

#To seprate in list format
import re

S = "snakewaterwatergungunsnakegungun"
# Define the pattern to match the words
pattern = r'(snake|water|gun)'

# Find all matches of the pattern in the string
result = re.findall(pattern, S)

print(result)

