def vowels_replace(string):
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for chr in string:
        if chr.lower() in vowels:
            string = string.replace(chr,'')

    return string

def vowels_regex(string):
    import re
    string = re.sub('[aeiou]','',string, flags=re.IGNORECASE)
    return string

string = input(" Input your string : ")

s = vowels_replace(string)
print("\tstring was '{}' and now it is '{}' ".format(string,s))

s = vowels_regex(string)
print("\tstring was '{}' and now it is '{}' ".format(string,s))