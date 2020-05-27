spells = {"Frost Bolt":{'rank':[1,2,3,4,5,6,7,8,9,10],'level':[4,8,14,20,26,32,38,44,50,60], 'mana':[25,35,50,65,100,130,160,195,225,290], 'effect_low':[18,31,51,74,126,174,227,292,353,515],'effect_high':[21,36,58,83,139,191,248,317,384,556],'cast':3},   "Shadow Bolt":{'rank':[1,2,3,4,5,6,7,8,9],'level':[1,6,12,20,28,36,44,52,60], 'mana':[25,40,70,110,160,210,265,315,370], 'effect_low':[12,23,48,86,142,204,281,360,455],'effect_high':[17,30,57,99,163,231,316,403,508],'cast':3},"Flash of Light":{'rank':[1,2,3,4,5],'level':[20,26,34,42,50], 'mana':[35,50,70,90,115], 'effect_low':[67,102,153,206,278],'effect_high':[77,117,171,231,310],'cast':1.5}}
sp = int(input("What is your spell power?"))

def spell_calc():
    for spell in spells:
        print(f"\n\nCalculating: {spell}\n")
        for i in range(len(spells.get(spell).get("rank"))):
            try:
                dr = ((spells.get(spell).get("level")[i+1] - 1 + 5)) / 60 # downrank calculator
            except:
                dr = 1
            avg = (spells.get(spell).get("effect_low")[i] + spells.get(spell).get("effect_high")[i]) / 2 # average hit taken from the tooltip
            spc = dr * spells.get(spell).get("cast") / 3.5 # spell power coefficient
            esp = sp * spc # effective spell power
            raw_power = avg + (sp * spc) # power on hit
            hpm = raw_power / spells.get(spell).get("mana")[i]  # hp per mana healed
            print(f"Tooltip: {avg},\t Downrank coef: {round(dr,2)},\t SPC: {round(spc,2)},\t ESP: {round(esp,2)},\t Raw hit: {round(raw_power,2)},\t Hit per mana: {round(hpm,2)}")
spell_calc()