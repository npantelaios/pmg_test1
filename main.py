import os

import glob
from PIL import Image, ImageDraw, ImageFont
import random

input_filename = "responses_csv/" + "unova_week2" + ".csv"
output_filename = 'charts_database/' + "unova2_week2" + ".png"
line_length = 10

def main():
    # TODO: count spreadsheet by timestamp columns (or close Google Form after X time)
    trainers_dict = count_responses()
    numbers_dict = convert_trainer2number(trainers_dict)
    for k in numbers_dict.keys():
        if k == 0:
            numbers_dict[k] = remove_main_characters_if_zero(numbers_dict[k])
            break
    numbers_dict = create_fake_numbers_to_test()
    create_chart(numbers_dict)

def count_responses() -> dict:
    with open(input_filename, 'r') as fin:
        rows = fin.read().splitlines()
    trainers_dict = init_dict()
    for row in rows[1:]:
        num_commas = len(row.split(','))
        trainers = row.split(',')[num_commas-15:]
        hasDuplicates = check_if_duplicates(trainers)
        if hasDuplicates:
            continue
        for trainer in trainers:
            trainers_dict[trainer] = trainers_dict.get(trainer, 0) + 1
    return trainers_dict

def convert_trainer2number(in_dict: dict) -> dict:
    out_dict = {}
    for k,v in in_dict.items():
        if v in out_dict.keys():
            out_dict[v].append(k.strip('\"'))
        else:
            out_dict[v] = [k.strip('\"')]
    return out_dict

def remove_main_characters_if_zero(zero_list: list):
    new_zero_list = []
    for i in zero_list:
        if not "Main_Character" in i:
            new_zero_list.append(i)
    return new_zero_list

def create_chart(in_dict: dict) -> None:
    img_folder = "images_hd/"
    prepare_str_images(in_dict)
    dict_len = len(in_dict)
    total_img = Image.new('RGB', (1,1), (250,250,250))
    column = 0
    line = 0
    block_indexes = calculate_blocks(dict_len)
    for k,v in sorted(in_dict.items(), reverse=True):
        column = 0
        cnt_trainer = 0
        my_colour = get_colour(line, block_indexes)
        total_height = ((len(v)-1)//line_length)+1
        str2img(k, total_height, my_colour)
        img_line = Image.open("number_images_temp/img" + str(k) + ".png")
        for trainer in v:
            img_trainer = Image.open(img_folder + trainer + ".png")
            img_trainer = img_trainer.resize((255,255))
            height = cnt_trainer//line_length
            img_line = merge_img_horizontally(img_line, img_trainer, 255*height, 255*(column+1))
            column += 1
            column = column%line_length
            cnt_trainer += 1
        if line == 0:
            total_img = img_line
        else:
            total_img = merge_img_vertically(total_img, img_line)
        total_img = add_white_line_below(total_img)
        line += 1
    total_img.save(output_filename)

def prepare_str_images(in_dict: dict) -> None:
    clean_directory()

def clean_directory() -> None:
    files = glob.glob('number_images_temp/*')
    for f in files:
        os.remove(f)

def calculate_blocks(dict_len: int) -> list:
    num_different_colours = 12
    block_numbers = [0,0,0,0,0,0,0,0,0,0,0,0]
    if dict_len <= 0:
        print("ZERO TRAINERS FOUND!!")
        return block_numbers
    # initial blocks all equal (1)
    for i in range(num_different_colours):
        if dict_len > 0:
            block_numbers[i] += 1
            dict_len -= 1
        else:
            break
    index = 1
    while dict_len > 0:
        block_numbers[index] += 1    
        index += 1
        if index >= (num_different_colours-2):
            index = 1
        dict_len -= 1
    block_indexes = []
    for i, _ in enumerate(block_numbers):
        if i == 0:
            block_indexes.append(block_numbers[i] - 1)
            continue
        if block_numbers[i-1] > 0:
            block_indexes.append(block_indexes[i-1] + block_numbers[i-1])
    return block_indexes

def get_colour(block_num: int, b_indexes: list) -> str:
    for i in range(len(b_indexes)-1, -1, -1):
        if block_num >= b_indexes[i]:
            return colours[i]

def str2img(word: int, height: int, my_colour: str) -> None:
    line_width = 5
    W,H = (255, 255*height)
    shape = [(0+line_width,0), (255-line_width,255*height)]
    img = Image.new('RGB', (W, H), color = (255,255,255))
    d = ImageDraw.Draw(img)
    d.rectangle(shape, fill=my_colour, outline =(0,0,0), width=line_width)
    font = ImageFont.truetype("Arial.ttf", 48)
    w,h = d.textsize(str(word), font=font)
    d.text(((W-w)/2,(H-h)/2), str(word), fill=(0,0,0), font=font)
    img.save("number_images_temp/img" + str(word) + ".png")

def merge_img_horizontally(image1: Image, image2: Image, height: int, width: int) -> Image:
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(255*(line_length+1), max(image1_size[1], image2_size[1])), (0,0,0))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(width,height))
    return new_image

def merge_img_vertically(image1: Image, image2: Image) -> Image:
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', (max(image1_size[0], image2_size[0]), image1_size[1]+image2_size[1]), (0,0,0))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(0, image1_size[1]))
    return new_image

def add_white_line_below(img: Image) -> Image:
    white_line = create_white_line()
    img = merge_img_vertically(img, white_line)
    return img 

def create_white_line() -> Image:
    img = Image.new('RGB', (255*(line_length+1), 6), color = (255, 255, 255))
    return img

def init_dict() -> dict:
    out_dict = {}
    with open("trainers/trainers_full.csv", 'r') as fin:
        trainers = fin.read().splitlines()
    for trainer in trainers:
        out_dict[trainer] = 0
    return out_dict

def check_if_duplicates(my_list: list) -> bool:
    ''' Check if given list contains any duplicates '''
    if len(my_list) == len(set(my_list)):
        return False
    else:
        return True

def create_fake_numbers_to_test() -> None:
    out_dict = {}
    randomize_range = 20
    with open("trainers/trainers_full.csv", 'r') as fin:
        trainers = fin.read().splitlines()
    for trainer in trainers:
        rand = random.randrange(1, randomize_range+1)
        if rand in out_dict.keys():
            out_dict[rand].append(trainer)
        else:
            out_dict[rand] = [trainer]
    return out_dict

colours = [
        "#FFFFFF",
        "#FF4400",
        "#DAD322",
        "#FFF700",
        "#40A56C",
        "#08FD00",
        "#00FFE6",
        "#0022FF",
        "#7700FF",
        "#FF00FF",
        "#A811E9",
        "#837A82",
        ]

if __name__ == "__main__":
    main()