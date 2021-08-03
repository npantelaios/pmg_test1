**------------------------------------------------------------------------------------------------------------**

**------------------------------------------------------------------------------------------------------------**

**NEW README START**

**------------------------------------------------------------------------------------------------------------**

HOW TO RUN:

1.Open file **PUT_YOUR_SPREADSHEET_HERE_2_COLUMNS/DONT_RENAME_CHANGE_NUMBERS_FROM_0.csv**

2.Add the correct number for each trainer (currently all are set to 0)

3.RUN: **python3 main.py OR python main.py** from project home directory

**RESULT** is produced at folder **OUTPUT_RESULT_HERE** with current timestamp

**------------------------------------------------------------------------------------------------------------**

**SOME TRAINERS MISSING?** -> The trainers were last updated in July 20, 2021, trainers released after that may be missing

**------------------------------------------------------------------------------------------------------------**

**HOW TO ADD MISSING TRAINERS:**

1. Add trainer name in file: "trainers/trainers_full.csv" as a new row, row order doesn't matter

2. Add trainer image in folder: **images_hd/**. Image name should be the same as trainer name added in step1. (eg. Trainer name = Accerola*Mimikyu and image name: Accerola_Mimikyu.png). Don't use special characters except underscore('*'). Trainer name also needs to be added in the file you add the **number of usages for each trainer**(See: How to RUN, step 1)

**------------------------------------------------------------------------------------------------------------**

**NEW README END**

**------------------------------------------------------------------------------------------------------------**

**------------------------------------------------------------------------------------------------------------**

**------------------------------------------------------------------------------------------------------------**

(**Please don't submit fake responses, if I waste too much time every week I will stop producing the chart**)

**------------------------------------------------------------------------------------------------------------**

**Description**

This is an automated attempt to produce the League chart, for every user that completed the Google Form successfully (proof of clearance is required while completing the form)

**------------------------------------------------------------------------------------------------------------**

**Instructions**

1. Complete the form (image proof in the form of /vp/ image is required in Question1)

(Form Example): **https://forms.gle/NmEZXPMBE8pBvvzz8**

**------------------------------------------------------------------------------------------------------------**

**Results**

Chart is produced in folder **charts_database/\*.png**, you can change this in the first line of **main.py**

**------------------------------------------------------------------------------------------------------------**

**Notes**

All responses need to be verified by matching the Google Form response with the image/link that is linked with each response

**Reproduction**

1. Download the Form responses in folder **responses_csv/\*.csv**, you can change this in the second line of **main.py**

**Form Source for downloading responses:** https://docs.google.com/forms/d/1FHNGyT0nfjWmr4CbF62tj8ar6e45Q9u8pnS-Esd7V14/edit?usp=sharing

2. Run command

```
python3 main.py
```

**------------------------------------------------------------------------------------------------------------**

**Repo**

https://github.com/npantelaios/pmg_test1

**------------------------------------------------------------------------------------------------------------**

**Examples**

Example1:

![Example1](charts_database/example1.png?raw=true "Example1")

Example2:

![Example2](charts_database/example2.png?raw=true "Example2")

**------------------------------------------------------------------------------------------------------------**

(**Please don't submit fake responses, if I waste too much time every week I will stop producing the chart**)
