import random
try:
    def game():
        hp_of_player=100
        hp_of_dragon=100
        story1='Once upon a time, there was a Greek King, Midas.'
        story2='He was very rich and had lots of Gold.'
        story3="He had a daughter, who he loved a lot."
        story4='One day, Midas found an angel in need of help. He helped her and in return she agreed to grant a wish. '
        story5='Midas wished that everything he touched would turn into gold. His wish was granted'
        story6='On his way home, he touched rocks and plants and they turned into gold.'
        story7='As he reached home, in excitement he hugged his daughter, who turned into gold.'
        story8='Midas was devastated and he had learnt his lesson.'
        story9='Upon learning his lesson, Midas asked the angel to take his wish away.'
        list_story=[story1,story2,story3,story4,story5,story6,story7,story8,story9]
        while hp_of_player>0 and hp_of_dragon>0:
            damage_of_player=random.randint(0,20)
            hp_of_player=hp_of_player-damage_of_player
            damage_of_dragon=random.randint(0,20)
            hp_of_dragon=hp_of_dragon-damage_of_dragon
            print(random.choice(list_story))
            print('hp of Player is:',hp_of_player,'and hp of Dragon is:',hp_of_dragon)
            if hp_of_player>0 or hp_of_dragon>0:
                continue
            else:
                return
        return hp_of_player,hp_of_dragon
    result=game()
    if result[0]>result[1]:
        winner='Player'
        loser='Dragon'
    else:
        winner='Dragon' 
        loser='Player'                
    print(winner,'defeated',loser,'!!!!')

except Exception as e:
    print(e)    