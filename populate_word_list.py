from DATA.datamanager import Datamanager
i=0
woord = "jawaddedadde"
dm=Datamanager()
with open ("woorden/wordlist.txt","r") as bestand :
    
    
    while woord :
        
        woord= bestand.readline()
        woord=woord[0:len(woord)-1]
        
        #if ("0" or "1" or "2" or "3" or "4"or "5" or "6" or "7" or "8" or "9" or "'" or "." or "-" or "/" or "+"or "&" or "@" or "€" or " " or "²" or "³" or"₂" or"…" or " " or "¤")  in woord:
         #   continue
        
        if len(woord)<4 or len(woord) >8 :
            continue          
        if "0" in woord :
            continue
        if "1" in woord :
            continue
        if "2" in woord :
            continue
        if "3" in woord :
            continue
        if "4" in woord :
            continue
        if "5" in woord :
            continue
        if "6" in woord :
            continue
        if "7" in woord :
            continue 
        if "8" in woord :
            continue
        if "9" in woord :
            continue
        if "'" in woord :
            continue
        if "." in woord :
            continue
        if "-" in woord :
            continue
        if "+" in woord :
            continue
        if "&" in woord :
            continue
        if "@" in woord :
            continue   
        if "€" in woord :
            continue    
        if "²" in woord :
            continue
        if "³" in woord :
            continue   
        if "₂" in woord :
            continue    
        if "…" in woord :
            continue 
        if " " in woord :
            continue

        toevoegsel=woord[0].upper()
        if toevoegsel in "Å Ä Â Ã" :
            toevoegsel= "A"
        if toevoegsel in "Ç" :
            toevoegsel= "C"    
        if toevoegsel in "Ñ" :
            toevoegsel= "N" 
        if toevoegsel in "Ë Ê " :
            toevoegsel= "E" 
        if toevoegsel in "Ï Î" :
            toevoegsel= "I"    
        if toevoegsel in "Ö Ô" :
            toevoegsel= "O"                    
        if toevoegsel in "Ü Û" :
            toevoegsel= "U"  
        dm.woord_toevoegen(woord, toevoegsel)
        i=i+1
        if i == 200:
            print (woord)
            i=0


    # - `0` t/m `9` en `²` `³` `₂`
    # - `'` `.` `-` `/` `+` `&` `@` `€` uit de woorden halen
    #if "0" in woord :
 
#dm.woord_toevoegen(woord)

##woord=dm.woord_by_id(10)
#print (woord)

#woord = dm.woord_by_zoekterm("word")
#print (woord)




