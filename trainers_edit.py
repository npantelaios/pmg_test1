import csv


def main():
    add_new_trainers()
    # trainers_convert()


def add_new_trainers():
    with open("trainers/new_trainers_to_add.csv") as f:
        new_rows = f.read().splitlines()
    with open("trainers/trainers_full.csv") as f:
        current_rows = f.read().splitlines()
    all_rows = sorted(new_rows + current_rows)
    fout1 = open("trainers/trainers_full.csv", "w")
    fout2 = open(
        "PUT_YOUR_SPREADSHEET_HERE_2_COLUMNS/DONT_RENAME_CHANGE_NUMBERS_FROM_0.csv", "w"
    )
    all_rows = list(dict.fromkeys(all_rows))
    print(len(all_rows))
    for row in all_rows:
        fout1.write(row + "\n")
        fout2.write(row + ",0,\n")
    fout1.close()
    fout2.close()


def trainers_convert() -> None:
    trainers = []
    with open("trainers/trainers_raw.csv", newline="") as csvfile:
        csv_lines = csv.reader(csvfile, delimiter=",")
        prev_line = ""
        for i, row in enumerate(csv_lines):
            if i == 0:  # titles
                continue
            skip_row = False
            if skip_row:
                continue
            num_pokemon = len(row[3].split("\n"))
            pokemon = row[3].split("\n")
            for j in range(num_pokemon):
                is_trash = check_name(pokemon[j])
                if is_trash:
                    continue
                trainer_name = row[0] + "_" + pokemon[j]
                trainer_name = beautify_name(trainer_name)
                if trainer_name not in trainers:
                    trainers.append(trainer_name)
    with open("trainers/trainers_full.csv", "w") as outfile:
        for trainer in trainers:
            outfile.write(trainer)
            outfile.write("\n")


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
    pkmon = pkmon.replace("'", "_")
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
