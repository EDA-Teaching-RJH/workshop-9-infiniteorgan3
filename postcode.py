'''
Any letter = *
Any Number = +

Formats of first part of UK postcodes:
[**+*]- ie. EC1-EC4,NW1W,SE1P,SW1 with WC postcode area

[*+*]- for areas E1, N1, W1

#[*+] or [*++] - for areas with first letter B, E, G, L, M, N, S, W

[**+] or [**++]- for all other area codes
#all postcodes end with the format [+**]

#not used in first position: Q,V,X
#not used in second position: I,J,Z

#for second part of postcode [+**]- Letters C, I, K, M, O, V not used, looks too similar to numbers when hand-written
for postcode formats [*+*], the third letter only has: A, B, C, D, E, F,G,H,J,K,P,S,T,U
for postcode formats [**+*], the fourth letter can be: A, B, E, H, M, N, P, R, V, W, X, Y
'''
import re

def main():
    address = input("Please enter a UK address.\n").strip()
    postcodeattempt = address.split(",")[len(address.split(",")) - 1].upper().strip()
    
    postcode = validatingpostcode(postcodeattempt)
    
    if postcode == False:
        print("Postcode not found.")
    else:
        print(f"Postcode: {postcode}")

def validatingpostcode(postcode):
    # Validating second part of postcode:
    invalidsecondhalfletters = ["C","I","K","M","O","V"]
    if re.search(r"\s(\d[A-Z][A-Z])$", postcode):
        if postcode.split(" ")[1][1] in invalidsecondhalfletters or postcode.split(" ")[1][2] in invalidsecondhalfletters:
            return False
    else:
        return False
    # Validating first part of postcode:
    invalidsecondletters = ["I","J","Z"]
    invalidfirstletters = ["Q","V","X"]
    validthirdletters = ["A", "B","C", "D","E","F","G","H","J","K","P","S","T","U"]
    validfourthletters = ["A","B","E","H","M","N","P","R","V","W","X","Y"]
    if postcode[0] in invalidfirstletters:
        return False
    if postcode[1] in invalidsecondletters:
        return False
    if re.search(r"^([A-Z]\d[A-Z])", postcode):
        if postcode[2] not in validthirdletters:
            return False
        if postcode[0] not in ["E", "N", "W"]:
            return False
        if postcode[1] != "1":
            return False
    elif re.search(r"^([A-Z]\d|[A-Z]\d\d)", postcode):
        if postcode[0] not in ["B", "E", "G", "L", "M", "N", "S", "W"]:
            return False
    elif re.search(r"^([A-Z][A-Z]\d[A-Z])", postcode):
        if postcode[3] not in validfourthletters:
            return False
    elif re.search(r"^([A-Z][A-Z]\d|[A-Z][A-Z]\d\d)", postcode):
        pass
    else:
        return False
    return postcode

if __name__ == "__main__":
    main()