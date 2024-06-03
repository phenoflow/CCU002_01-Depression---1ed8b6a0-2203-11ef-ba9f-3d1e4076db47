# Rochelle Knight, Venexia Walker, et al., 2024.

import sys, csv, re

codes = [{"code":"75084000","system":"icd10"},{"code":"397701000000102","system":"icd10"},{"code":"76441001","system":"icd10"},{"code":"397711000000100","system":"icd10"},{"code":"191604000","system":"icd10"},{"code":"73867007","system":"icd10"},{"code":"191676002","system":"icd10"},{"code":"Eu328","system":"icd10"},{"code":"E130.","system":"icd10"},{"code":"Eu322","system":"icd10"},{"code":"E1124","system":"icd10"},{"code":"Eu323","system":"icd10"},{"code":"E1123","system":"icd10"},{"code":"Eu327","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_01-depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_01-depression-psych---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_01-depression-psych---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_01-depression-psych---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
