from DATA.datamanager import Datamanager

dm=Datamanager()
"""
woorden=dm.alle_woorden()
for woord in woorden :
    print (woord[1] )


woord = "abluties"
woord=dm.check_by_zoekterm(woord,woord[0])
print (woord)
"""
woord = "daar"
woord=dm.check_by_zoekterm_alle_woorden(woord)
print (woord)
"""a="test"
print (len(a))
print ("e" in a )
print (("0" or "e") not in a)
print (a[0].upper())
#AÃ¤ron
#¤
raarletters = "`å` `ç` `ñ``Å``ä` `ë` `ï` `ö` `ü` en `â`  `ê`  `î`  `ô`  `û`"
print (raarletters.upper())"""