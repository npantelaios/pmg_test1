import os

import glob
from PIL import Image, ImageDraw, ImageFont
import random

ct = "unova2_week2"
line_length = 10
randomize_range = 15

def main():
    # TODO: take latest file
    # TODO: count by timestamp (or close it after X time)
    # TODO: check each line for duplicates
    # TODO: if "main_character" + 0 uses -> throw it away
    # TODO: put colours in "number" images
    latest_file = "Unova_week2.csv"
    trainers_dict = count_responses(latest_file)
    numbers_dict = convert_trainer2number(trainers_dict)
    numbers_dict = create_fake_numbers_to_test()
    create_chart(numbers_dict)

def count_responses(infile: str) -> dict:
    in_dir = "responses_csv/"
    in_path = in_dir + infile
    with open(in_path, 'r') as fin:
        rows = fin.read().splitlines()
    trainers_dict = {}
    for row in rows[1:]:
        num_commas = len(row.split(','))
        trainers = row.split(',')[num_commas-15:]
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

def create_chart(in_dict: dict) -> None:
    img_folder = "images_hd/"
    prepare_str_images(in_dict)
    total_img = Image.new('RGB', (1,1), (250,250,250))
    line = 0
    column = 0
    for k,v in sorted(in_dict.items(), reverse=True):
        column = 0
        cnt_trainer = 0
        total_height = ((len(v)-1)//line_length)+1
        str2img(k, total_height)
        img_line = Image.open("number_images_temp/img" + str(k) + ".png")
        for trainer in v:
            img_trainer = Image.open(img_folder + trainer + ".png")
            img_trainer = img_trainer.resize((255,255))
            # if column >= line_length:
                # total_img = merge_img_vertically(total_img, img_line)
                # img_line = Image.open("number_images_temp/img" + str(k) + ".png")
                # column = 0
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
    total_img.save('charts_database/' + str(ct) + ".png")

def prepare_str_images(in_dict: dict) -> None:
    clean_directory()
    # for k in in_dict.keys():
    #     str2img(k)

def clean_directory() -> None:
    files = glob.glob('number_images_temp/*')
    for f in files:
        os.remove(f)

def str2img(word: int, height: int) -> None:
    img = Image.new('RGB', (255, 255*height), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial.ttf", 48)
    d.text((100,100*height), str(word), fill=(255,255,255), font=font)
    img.save("number_images_temp/img" + str(word) + ".png")

def merge_img_horizontally(image1: Image, image2: Image, height: int, width: int) -> Image:
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(image1_size[0]+image2_size[0], max(image1_size[1], image2_size[1])), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(width,height))
    return new_image


def merge_img_vertically(image1: Image, image2: Image) -> Image:
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', (max(image1_size[0], image2_size[0]), image1_size[1]+image2_size[1]), (250,250,250))
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

def create_fake_numbers_to_test() -> None:
    out_dict = {}
    with open("trainers_full.csv", 'r') as fin:
        trainers = fin.read().splitlines()
    for trainer in trainers:
        rand = random.randrange(1, randomize_range)
        if rand in out_dict.keys():
            out_dict[rand].append(trainer)
        else:
            out_dict[rand] = [trainer]
    for k,v in sorted(out_dict.items(), reverse=True):
        print(k)
        print(v)
    return out_dict

if __name__ == "__main__":
    main()