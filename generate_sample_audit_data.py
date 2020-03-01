import csv
import sys
import random
from datetime import date
import bisect 
#from collections import OrderedDict
import progressbar


def generate_unqiue_uid_set(number: int) -> list:
    uid_l = list(range(0, number))
    return uid_l


def final_record_options(selection: int) -> str:
    options_dict = {
        0: 'missing',
        1: 'different',
        2: 'thief',
        3: 'original',
        4: 'original',
        5: 'original',
        6: 'original',
        7: 'original',
        8: 'original',
        9: 'original',
        10: 'original',
    }
    if selection in options_dict:
        return options_dict[selection]
    else:
        return None


def generate_preused_numbers(int_set: set, total: int, interval_limit: int, min_number: int = 1) -> list:
    while min_number + interval_limit <= total:
        min_number = random.randint(min_number, min_number + interval_limit)
        int_set.add(min_number)
        min_number += 1
    return int_set


def find_int_gaps(int_set: list, position: int = 1) -> int:
    gap = False
    while gap == False:
        if position in int_set:
            position += 1
        else:
            return position
            gap == True
    return position + 1


def generate_id_records(number_of_users: int):
    number_list = generate_unqiue_uid_set(number_of_users)
    full_list = []
    audit_record_count = 1
    username_number = 1
    username_set = set()
    username_set = generate_preused_numbers(username_set, len(number_list * 2), 5)
    for uid in progressbar.progressbar(number_list):
        max_date = None
        # Setup randaom data
        number_of_records = random.randint(0, 4)
        number_of_records = list(range(0, number_of_records))
        final_record_determination = random.randint(0, 10)
        final_record_state = final_record_options(final_record_determination)
        for i in number_of_records:
            record_list = []
            username_number = find_int_gaps(username_set, username_number)
            username_set.add(username_number)
            username = 'username' + str(username_number)
            if final_record_state == 'original' and i == number_of_records[0]:
                username_original = username
            record_list.append(audit_record_count)
            record_list.append(uid)
            record_list.append(username)
            if max_date:
                min_date = max_date
            else:
                min_date = date(2019, 3, 15)
            record_list.append(min_date)
            max_day = random.randint(min_date.day + 1, int(min_date.day) + 4)
            max_date = date(2019, 3, max_day)
            username_number = find_int_gaps(username_set, username_number)
            if i == number_of_records[-1]:
                if final_record_state == 'different':
                    username_set.add(username_number)
                if final_record_state == 'theif':
                    username_set.add(username_number)
            else:
                username_set.add(username_number)
            username = 'username' + str(username_number)
            if i == number_of_records[-1]:
                if final_record_state == 'original':
                    username = username_original
                    record_list.append(username)                   
                elif final_record_state == 'missing':
                    username = None
                    record_list.append(username)
                elif final_record_state == 'thief':
                    record_list.append(username)
            else:
                record_list.append(username)
            record_list.append(max_date)
            full_list.append(record_list)
            audit_record_count += 1
    
    with open("generated_audit_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(full_list)

generate_id_records(1000000)

