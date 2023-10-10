import hashlib
import re

def hash_process(line):
    match = re.search(r'"(.*?)"', line)
    myText = match.group(1)
    parts = line.split(myText)[1].strip().split('-')
    input_HA256 = parts[1].strip()
    input_MD5 = parts[2].strip()
    
    print("Text:", myText)
    SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
    MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

    count_correct = 0

    if SHA256 == input_HA256:
        count_correct += 1
        print('SHA256 is correct')
    else:
        print('SHA256 is wrong, the correct is ' + SHA256)

    if MD5 == input_MD5:
        count_correct += 1
        print('MD5 is correct')
    else: 
        print('MD5 is wrong, the correct is ' + MD5)

    if count_correct == 2:
        print('TRUE')
    else:
        print('FALSE')

    print()

with open('./phrases.txt', 'r') as file:
    for line in file:
        if line == '\n': continue
        hash_process(line)



