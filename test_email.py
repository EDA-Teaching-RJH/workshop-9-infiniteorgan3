from email import validateemail


def test_validation():
    assert validateemail("qvahxzeueq@nhs.net") == False
    assert validateemail("rwvqhptft@nhs.net") == False
    assert validateemail("njvun@nhs.net") == False
    assert validateemail("omkueltb@gov.uk") == False
    assert validateemail("qpzyqnlaq@nhs.net") == False
    assert validateemail("dkf*ggnu@gov.uk") == False
    assert validateemail("mtnur@pnngov.uk") == False
    assert validateemail("wiq)jadaa@nhs.net") == False
    assert validateemail("fph@jp@ac.uk") == False
    assert validateemail("euktfrzm@gov.uk") == False
    assert validateemail("eee.eee@gov.uk") == False
    assert validateemail("ejam2@kent.ac.uk") == True
    assert validateemail("eeee@rrrr.ac.uk") == True
    assert validateemail("e@h.ac") == False
    assert validateemail("e@f.gov.uk") == True
    assert validateemail("ejam@*/**.gov.uk") == False
    
def main():
    test_validation()

if __name__ == "__main__":
    main()