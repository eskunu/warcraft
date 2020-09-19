import random

def curse_of_agony(spellpower):
    if spellpower == 0:
        spellpower = 1
    damage_per_tick = 1024 / 12
    spc = spellpower * 15 / 15 / 12
    tick = spc + damage_per_tick
    return tick

def shadowbolt(spellpower):
    if spellpower == 0:
        spellpower = 1
    damage = random.randint(455,507)
    spc = spellpower * 3.5 / 3
    cast = spc + damage
    return cast

def hit_or_miss(hit_chance, crit_chance):
    x = random.randint(0,100) / 100
    if x < hit_chance:
        #x = random.randint(0,100)
        if x < hit_chance * crit_chance:
            return 1.5
        else:
            return 1

def damage_per_second(ticks):
    hits = 0
    crits = 0
    damage = 0
    for i in range(0,ticks):
        x = hit_or_miss(.91, .10)
        if x == 1:
            curse = curse_of_agony(370) * x
            shadow = shadowbolt(480) * x
            hits += 1rrr
            damage += shadow
        if x == 1.5:
            curse = curse_of_agony(370) * x
            shadow = shadowbolt(480) * x
            hits += 1
            crits += 1
            damage += shadow
        elif x == None:
            pass
            #print("Miss")
    return hits / ticks * 100, crits / ticks * 100, damage, ticks

ticks = 100000
print(f"Damage per second: {damage_per_second(ticks)[2] / ticks / 2.5}, hit: {damage_per_second(ticks)[0]}% crits: {damage_per_second(ticks)[1]}% over {ticks} iterations")
#print(f"Hits: {hits / 100}, Crits: {crits / 100}, Damage per second: {damage / 100 / 2.5}")
    
