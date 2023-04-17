#!/usr/bin/env python3
""" study re module"""
import re

test_numbers = ["+1 223-456-7890",
"2-223-456-7890",
"+1 223 456-7890",
"(223) 456-7890",
"1 223 456 7890",
"223.456.7890",
"1-989-211-2222"]

def return_number(match_obj):
# validate number raise ValueError if not valid
    print(match_obj.groups())
    if not re.match(r"[2-9][0-8]\d", match_obj.group("area") ):
        raise ValueError("invalid phone number area code {}".format(match_obj.group("area")))
    
    if not re.match(r"[2-9]\d\d", match_obj.group("exch") ):
        raise ValueError("invalid phone number exchange {}".format(match_obj.group("exch")))
                                
    country = match_obj.group("country")
    if not country:
        country = "1"

    return("{}-{}-{}-{}".format(country, match_obj.group('area'), match_obj.group('exch'), match_obj.group('number')))

regexp = re.compile(r"\+?(?P<country>\d{1,3})?[- .]?\(?(?P<area>\d{3})\)?[- .]?(?P<exch>(\d{3}))[- .](?P<number>\d{4})")

# regexp = re.compile(r"+?(?P<country>\d{1,3})?[- .]?\(?(?P<area>\d{3})\)?[- .]?(?P<exch>(\d{3}))[- .](?P<number>\d{4})")
      
for number in test_numbers:
    # print(regexp.sub(return_number, number))
    # res=regexp.sub(return_number, number)
    res= re.sub(regexp,return_number, number)
    # print(f"original Numner: {number}" )
    print(f"New Numner: {res}")


