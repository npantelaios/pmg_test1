import csv

def main():
    trainers_convert()

def trainers_convert() -> None:
    trainers = []
    with open("trainers_raw.csv", newline='') as csvfile:
        csv_lines = csv.reader(csvfile, delimiter=',')
        prev_line = ''
        for i, row in enumerate(csv_lines):
            if i==0: # titles
                continue 
            skip_row = False
            if skip_row:
                continue
            num_pokemon = len(row[3].split('\n'))
            pokemon = row[3].split('\n')
            for j in range(num_pokemon):
                is_trash = check_name(pokemon[j])
                if is_trash:
                    continue
                trainer_name = row[0] + '_' + pokemon[j]
                trainer_name = beautify_name(trainer_name)
                if trainer_name not in trainers:
                    trainers.append(trainer_name)
    with open("trainers_full.csv", 'w') as outfile:
        for trainer in trainers:
            outfile.write(trainer)
            outfile.write('\n')
    
def check_name(pkmon: str) -> bool:
    for blockword in clean_list:
        if blockword in pkmon:
            return True
    return False

def beautify_name(pkmon: str) -> str:
    pkmon = pkmon.replace(" ", "_")
    pkmon = pkmon.replace("(", "_")
    pkmon = pkmon.replace(")", "")
    pkmon = pkmon.replace("-", "_")
    pkmon = pkmon.replace("\'", "_")
    pkmon = pkmon.replace(".", "_")
    pkmon = pkmon.replace("__", "_")
    return pkmon

# initial csv source: https://www.serebii.net/pokemonmasters/trainers.shtml
# 6 Extra pairs not available in game dex:
# bugsy_scyther
# lear_hoopa
# rachel_umbreon
# sawyer_honckrow
# gloria_inteleon
# marnie_grimmsnarl
clean_list = [
            "Mega ",
            "Busted",
            "Piplup",
            "Prinplup",
            "Ponyta",
            "Makuhita",
            "Treecko",
            "Grovyle",
            "Espurr",
            "Palpitoad",
            "Turtwig",
            "Grotle",
            "Popplio",
            "Brionne",
            "Cyndaquil",
            "Quilava",
            "Amaura",
            "Oshawott",
            "Dewott",
            "Tepig",
            "Pignite",
            "Totodile",
            "Croconaw",
            "Voltorb",
            "Hangry",
            "Meditite",
            "Dusclops",
            "Seel",
            "Weepinbell",
            "Snivy",
            "Servine",
            "Nosepass",
            "Whirlipede",
            "Rowlet",
            "Dartrix",
            "Fennekin",
            "Braixen",
            "Surskit",
            "Blade",
            "Mudkip",
            "Marshtomp",
            "Chikorita",
            "Bayleef",
            "Cranidos",
            "EMPTY",
            ]

if __name__ == "__main__":
    main()