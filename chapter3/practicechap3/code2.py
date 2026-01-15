# write a program to fill a letter template given below with name and date

letter = """  Dear <|name|>,
            you are selected
              <|Date|>"""
print(letter.replace("<|name|>", "Ram").replace("<|Date|>","4 aug 2025"))