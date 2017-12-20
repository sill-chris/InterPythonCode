def find_rare():
    with open("challange2_data.html", mode='rt', encoding='utf-8') as data:
        # loop over file
        for rec in data:
            # loop over line
            for c in rec:
                c.isalpha()
                    # print(c)





