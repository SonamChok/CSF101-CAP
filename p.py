 #Read the input file
f=open('CSF101CAP1/input_2_cap1.txt','r')
data= f.readlines()
f.close()
    
def calculate_round_score(player_choice, opponent_choice, result):
    choice={'A':1,'B':2, 'C':3}
    result={'X':0, 'Y':3, 'Z':6}
    player_choice= choice[player_choice]+result[result]
total_score= 0 

for line in data:
    opponent_choice, result= line.strip().split()
    if opponent_choice =='A' and result=='X':
        player_choice='C'
    elif opponent_choice=='A' and result=='Y':
        player_choice='A'
    elif opponent_choice=='A' and result=='Z':
        player_choice='B'
    elif opponent_choice=='B' and result=='X':
        player_choice='A'
    elif opponent_choice=='B' and result=='Y':
        player_choice='B'
    elif opponent_choice=='B' and result=='Z':
        player_choice='C'
    elif opponent_choice=='C' and result=='X':
        player_choice='B'
    elif opponent_choice=='C' and result=='Y':
        player_choice='C'
    else:
        player_choice='A'
        
    round_score=calculate_round_score(player_choice, opponent_choice, result)
    
    total_score+=round_score
    
print('total score:', total_score)
    
    
    