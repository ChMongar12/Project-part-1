import csv

def add_vote(id ,vote ):
    "first we if the csv file alreay has the the id in it, if not it will add the id and who everr they voted for."

    with open("votes.csv",mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, vote])


def check_id(id):
    "this one returns true if the voter has already voted.if it finds the id in the csv file then it will return true and false if not"
    checking_id = int(id)
    with open("votes.csv", mode='a', newline='') as file:
        with open("votes.csv",mode = 'r',newline = '') as file:

            v_reader = csv.reader(file)
            for row in v_reader:
                for value in row:
                    try:
                        if float(value) == checking_id:
                            return True
                    except ValueError:
                        continue
        return False
def id_is_pos(id):
    "checks if the id is posotive"
    id = int(id)
    if id<0:
        return True
    else:
        return False

def valid_write_in(writin):
    "checks if the name is valid"
    "learned is alpha from https://www.geeksforgeeks.org/python-string-isalpha-method/"
    if writin.replace(" ","").isalpha():
        return True
    else:
        return False















