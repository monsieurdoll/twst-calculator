# twsisted wonderland(Disney mobile game) gacha chance calculator 
# calculator that calculates the chances of getting a card based on the amount of gems/keys(game currency) a player has 
# as well as telling the player if its a good idea to pull for the card depending on if the chances are above or below 50%
banners = {"standard": "4.54545", "event":"60.0" ,"birthday": "100.0"} #chances out of 100

gems = input("how many gems do you have?")
gems = (int(gems) / 30) # 30 gems = 1 pull
print(str(gems) + " pulls") # tellsplayer how many pulls they have in gems

keys = input("how many keys do you have? (count the amount of individual keys + 10 keys)")

total = ( gems + int(keys))

print(str(total) + " pulls in total") # tells the player how many pulls they have in total



def calc ( total):

    for i in banners :
        pulling = input("are you pulling on the" + " " + i + " banner? (y/n)")  
        
        if pulling == "y":
            chance = banners[i]
            basicssr = ( (1-(1- (1.5 / 100 ))**int(total) )*100 )
            print(basicssr)
            ssr =  ( (1- (1- (float(chance) / 100) )**int(total) )*100 ) 
            if basicssr < 50.0 :
                
                print("for every pull there is a 1.5 chance of getting an ssr, meaning that if you did " + " " + str(total) + " " + " pulls then there would be a " + " " + str(basicssr) + "% chance of getting an ssr, you should not pull right now :/" )
        
            elif basicssr >= 50.0 :
               
                print("for every pull there is a 1.5 chance of getting an ssr, meaning that if you did " + str(total) + " pulls then there would be a " + str(basicssr) + "% chance of getting an ssr, you should pull right now!!!!" + " HOWEVER.... if you manage to pull an ssr theres a " + str(chance) + "% chance to get the ssr youre aiming for" + ", meaning that out of those pulls there would be a " + str(ssr) + "% chance of getting your target ssr.")
            break  

        elif pulling == "n" :
            continue
        else :
            print("please type the correct thing (y/n) and try again")
        return 

calc(total) #calling the function