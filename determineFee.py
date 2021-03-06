import json

def selectFee():
    print('Select fee to be determined:\n')
    print('1. Exam fee\n2. Application fee\n')
    fee_type = int(input())
    return fee_type

def selectNationality(fee_type, data):
    print('Select nationality:\n')
    if fee_type == 1:
        i = 1
        for each in data['Exam Fee']:
            print('{}. {}'.format(i, each))
            i += 1
    else:
        i = 1
        for each in data['Application Fee']:
            print('{}. {}'.format(i, each))
            i += 1
    nationality = int(input())
    return nationality

def selectCourse():
    print('Select course:\n')
    print('1. Medical\n2. Dental\n3. Ayurveda\n')
    course = int(input())
    return course

def selectLevel():
    print('Select level:\n')
    print('1. UG\n2. PG\n3.DIPLOMA\n')
    level = int(input())
    return level

def determineFee(fee_type, nationality, course, level, data):
    if course not in [1, 2, 3] or level not in [1, 2, 3]:
        print('Invalid Course / Invalid Level')
        exit()
    if fee_type == 1:
        match nationality:
            case 1: resultant_fee = data['Exam Fee']['INDIAN']['ALL_COURSES']['ALL_LEVEL']['amount']
            case 2: resultant_fee = data['Exam Fee']['FOREIGN']['ALL_COURSES']['ALL_LEVEL']['amount']
            case 3: resultant_fee = data['Exam Fee']['NRI']['ALL_COURSES']['ALL_LEVEL']['amount']
            case 4: resultant_fee = data['Exam Fee']['SAARC']['ALL_COURSES']['ALL_LEVEL']['amount']
            case _: print('Invalid nationality'); exit()
    elif fee_type == 2:
        match nationality:
            case 1: 
                match level:
                    case 1: resultant_fee = data['Application Fee']['INDIAN']['ALL_COURSES']['UG']['amount']
                    case 2: resultant_fee = data['Application Fee']['INDIAN']['ALL_COURSES']['PG']['amount']
                    case 3: resultant_fee = data['Application Fee']['INDIAN']['ALL_COURSES']['UG-DIPLOMA']['amount']
                    case _: print('Invalid level'); exit()
            case 2: 
                match level:
                    case 1: resultant_fee = data['Application Fee']['FOREIGN']['ALL_COURSES']['UG']['amount']
                    case 2: resultant_fee = data['Application Fee']['FOREIGN']['ALL_COURSES']['PG']['amount']
                    case 3: resultant_fee = data['Application Fee']['FOREIGN']['ALL_COURSES']['UG-DIPLOMA']['amount']
                    case _: print('Invalid level'); exit()
            case _: print('Invalid nationality'); exit()
    else:
        print('Invalid fee type')
        exit()
    return resultant_fee



if __name__ == '__main__':
    file = open('data.json', 'r')
    data = json.load(file)
    fee_type = selectFee()
    nationality = selectNationality(fee_type, data)
    course = selectCourse()
    level = selectLevel()
    fee = determineFee(fee_type, nationality, course, level, data)
    print('Fee to be paid: {}'.format(fee))