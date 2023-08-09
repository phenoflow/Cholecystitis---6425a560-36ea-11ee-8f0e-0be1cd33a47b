# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J651000","system":"readv2"},{"code":"J651z00","system":"readv2"},{"code":"101538.0","system":"med"},{"code":"107004.0","system":"med"},{"code":"15735.0","system":"med"},{"code":"1924.0","system":"med"},{"code":"26889.0","system":"med"},{"code":"31650.0","system":"med"},{"code":"34683.0","system":"med"},{"code":"38289.0","system":"med"},{"code":"39025.0","system":"med"},{"code":"41018.0","system":"med"},{"code":"44605.0","system":"med"},{"code":"44649.0","system":"med"},{"code":"44922.0","system":"med"},{"code":"45172.0","system":"med"},{"code":"46248.0","system":"med"},{"code":"505.0","system":"med"},{"code":"61298.0","system":"med"},{"code":"63258.0","system":"med"},{"code":"72904.0","system":"med"},{"code":"7459.0","system":"med"},{"code":"932.0","system":"med"},{"code":"96679.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cholecystitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cholecystitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cholecystitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cholecystitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
