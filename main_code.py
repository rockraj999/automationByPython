import datetime
import os
import validation as v
import mailService as ms
import shutil
import csv


def main():
    try:

        #print(os.getcwd())
        today_date = datetime.date.today().strftime('%Y%m%d')
        subject = f'Validation for {today_date} files'
        incoming_file = f'../incomingFiles/{today_date}'
        success_path = f'../successFiles/{today_date}'
        rejected_path = f'../rejectedFiles/{today_date}'
        total_file = len(os.listdir(incoming_file))

        if total_file > 0:                                                     # cheking if no file for today then no need to run
            success_cnt = 0
            reject_cnt = 0

            for file in os.listdir(incoming_file):                             # iterating over files in todays foilder
                with open(f'{incoming_file}/{file}') as f:
                    line = f.readlines()[1:]
                    rows = []
                    con_t_list = []

                    if len(line) > 0:                                          # in file if no data then no nrrd to process the file
                        for i in line:
                            split_list = i.split(',')
                            split_list[5] = split_list[5][:-1]
                            split_list.append("")
                            con_t = 0                                          # it account true condition for each rows  

                            def addStr(s):
                                if split_list[6]:
                                    split_list[6] = split_list[6] + ';' + s
                                else:
                                    split_list[6] = s

                            val_pid = v.validate_product_id(split_list[2])             # calling these fun and in return getting T/F
                            val_od = v.validate_order_date(split_list[1])
                            val_city = v.validate_city(split_list[5])
                            val_empty = v.validate_emptiness(split_list)
                            val_sales = v.validate_sales(split_list[2], split_list[3], split_list[4])

                            if val_pid:                                                 # if validation gives True then increasing con_t 
                                con_t += 1                                               # else recording reason for wrong validation 
                            else:
                                addStr(f"Invalid product id {split_list[2]}")
                            if val_empty:
                                con_t += 1
                            else:
                                addStr('Columns are empty.')
                            if val_od:
                                con_t += 1
                            else:
                                addStr(f"Date {split_list[1]} is a future date.")
                            if val_city:
                                con_t += 1
                            else:
                                addStr(f"Invalid city {split_list[5]}.")
                            if val_sales:
                                con_t += 1
                            else:
                                addStr(f'Invalid Sales calculation.')

                            con_t_list.append(con_t)                              # con_t_list var, it helps to determine if fileis success or failed
                            if con_t < 5:
                                rows.append(split_list)

                        if all(ele == 5 for ele in con_t_list):
                            success_cnt += 1
                            if not os.path.exists(success_path):
                                os.mkdir(success_path)
                            shutil.copyfile(f'{incoming_file}/{file}', f'{success_path}/{file}')

                        else:
                            reject_cnt += 1
                            if not os.path.exists(rejected_path):
                                os.mkdir(rejected_path)
                            shutil.copyfile(f'{incoming_file}/{file}', f'{rejected_path}/{file}')

                            with open(f'{rejected_path}/error_{file}', 'w', newline='') as z:
                                write = csv.writer(z)
                                write.writerow(['order_id', 'order_date', 'product_id', 'quantity', 'sales', 'city', 'Reason' ])
                                write.writerows(rows)
                    else:
                        reject_cnt += 1
                        if not os.path.exists(rejected_path):
                            os.mkdir(rejected_path)
                        shutil.copyfile(f'{incoming_file}/{file}', f'{rejected_path}/{file}')

                        with open(f'{rejected_path}/error_{file}', 'w', newline='') as z:
                            z.write('Empty_file')

            else:
                body = f"""
                Total Files: {total_file} \n
                Successful Files: {success_cnt} \n
                Rejected Files: {reject_cnt}
                """
                ms.sendmail(subject, body)

        else:
            print("no files present")

    except Exception as e:
        print(str(e))


main()
