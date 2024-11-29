import re

def validateemail(email):
    if re.search(r"^\w+@\w+\.(ac.uk|gov.uk|nhs.net)$", email):
        if email.endswith("ac.uk"):
            print("Valid academic email.")
        elif email.endswith("gov.uk"):
            print("Valid government email.")
        else:
            print("Valid NHS email.")
        return True
    else:
        listofreasons = reasonforinvalidity(email)
        print("The lists of reasons that the email is invalid:")
        for i in listofreasons:
            print(f"-{i}")
        return False

def reasonforinvalidity(invalid):
    listofreasons = []
    numberofat = 0
    for i in invalid:
        if re.search(r"(\w|@|\.)", i) == None and "There is at least one invalid character in the email." not in listofreasons:
            listofreasons.append("There is at least one invalid character in the email.")
        elif i == "@" and numberofat > 0 and "There are too many @ symbols in the email." not in listofreasons:
            listofreasons.append("There are too many @ symbols in the email.")
            numberofat += 1
        elif i == "@":
            numberofat += 1
    if re.search(r"(ac.uk|gov.uk|nhs.net)$", invalid) == None:
        listofreasons.append("The ending of the email is invalid.")
    if len(invalid.split(".")) > 3:
        listofreasons.append("There are too many dots in the email.")
    elif len(invalid.split(".")) < 3:
        listofreasons.append("There are too few dots in the email.")
    return listofreasons
            
def main():
    email = input("Please enter an email:\n").strip()
    validateemail(email)

if __name__ == "__main__":
    main()