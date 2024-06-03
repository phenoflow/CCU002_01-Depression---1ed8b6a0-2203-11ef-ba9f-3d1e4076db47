# Rochelle Knight, Venexia Walker, et al., 2024.

import sys, csv, re

codes = [{"code":"F33","system":"icd10"},{"code":"18818009","system":"icd10"},{"code":"755331000000108","system":"icd10"},{"code":"40379007","system":"icd10"},{"code":"191613003","system":"icd10"},{"code":"191610000","system":"icd10"},{"code":"1089641000000100","system":"icd10"},{"code":"268621008","system":"icd10"},{"code":"36474008","system":"icd10"},{"code":"191616006","system":"icd10"},{"code":"16264901000119109","system":"icd10"},{"code":"16264621000119109","system":"icd10"},{"code":"764611000000100","system":"icd10"},{"code":"28475009","system":"icd10"},{"code":"274948002","system":"icd10"},{"code":"1086471000000103","system":"icd10"},{"code":"40568001","system":"icd10"},{"code":"1089631000000109","system":"icd10"},{"code":"1089511000000100","system":"icd10"},{"code":"764691000000109","system":"icd10"},{"code":"191611001","system":"icd10"},{"code":"Eu33y","system":"icd10"},{"code":"Eu333","system":"icd10"},{"code":"E1134","system":"icd10"},{"code":"Eu331","system":"icd10"},{"code":"E1135","system":"icd10"},{"code":"Eu33z","system":"icd10"},{"code":"Eu32A","system":"icd10"},{"code":"E113z","system":"icd10"},{"code":"E1137","system":"icd10"},{"code":"Eu330","system":"icd10"},{"code":"E1133","system":"icd10"},{"code":"Eu332","system":"icd10"},{"code":"E1131","system":"icd10"},{"code":"Eu334","system":"icd10"},{"code":"E1136","system":"icd10"},{"code":"E113.","system":"icd10"},{"code":"E1132","system":"icd10"},{"code":"E1130","system":"icd10"},{"code":"Eu33.","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_01-depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_01-depression-recurr---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_01-depression-recurr---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_01-depression-recurr---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
