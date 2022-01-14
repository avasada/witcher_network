import pandas as pd
import string
from bs4 import BeautifulSoup
from urllib.request import urlopen

#web scraping list of characters from witcher wiki
#https://witcher.fandom.com/wiki/Category:Characters_in_the_stories
from bs4 import BeautifulSoup
from urllib.request import urlopen

characters = []

def get_characters(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    images = soup.find_all("img")

    for image in images:
        name = image["alt"]
        name = name.split(" ")[0]
        if name not in characters:
            characters.append(name)

#1
get_characters("https://witcher.fandom.com/wiki/Category:The_Last_Wish_characters")
#2
get_characters("https://witcher.fandom.com/wiki/Category:Sword_of_Destiny_characters")
#3
get_characters("https://witcher.fandom.com/wiki/Category:Blood_of_Elves_characters")
#4
get_characters("https://witcher.fandom.com/wiki/Category:Time_of_Contempt_characters")
#5
get_characters("https://witcher.fandom.com/wiki/Category:Baptism_of_Fire_characters")
#6
get_characters("https://witcher.fandom.com/wiki/Category:The_Tower_of_the_Swallow_characters")
#7
get_characters("https://witcher.fandom.com/wiki/Category:The_Lady_of_the_Lake_characters")
#8
get_characters("https://witcher.fandom.com/wiki/Category:Season_of_Storms_characters")

all_characters = characters[1:]
all_characters.remove("The")



#load text files
book_1 = open("The_Last_Wish.txt", "r")
book_2 = open("The_Sword_of_Destiny.txt", "r")
book_3 = open("Blood_of_Elves.txt", "r")
book_4 = open("Times_of_Contempt.txt", "r")
book_5 = open("Baptism_of_fire.txt", "r")
book_6 = open("The_Tower_of_the_Swallow.txt", "r")
book_7 = open("The_Lady_of_the_Lake.txt", "r")

#create and fill dataframe
sources = []
targets = []
weights = []
types = []
books = []


def create_network(book, number):
    book_characters = []
    lines = []
    for line in book:
        lines.append(line)

    table = str.maketrans('', '', string.punctuation)
    stripped = [l.translate(table) for l in lines]
    
    for line in stripped:
        characters = []
        for c in all_characters:
            if c in line:
                characters.append(c)
        book_characters.append(characters)
    
    source_and_targets = []
    
    for i in range(len(book_characters)):
        length = len(book_characters)
        if len(book_characters[i]) == 1:
            source = book_characters[i]
            #turn thsi into a fucntion soon
            if i + 1 < length:
                if (len(book_characters[i + 1]) == 1) and (book_characters[i + 1] != book_characters[i]):
                    target = book_characters[i +1]
                    source_target = []
                    source_target.append(source)
                    source_target.append(target)
                    source_and_targets.append(source_target)
            if i + 2 < length:
                if (len(book_characters[i + 2]) == 1) and (book_characters[i + 2] != book_characters[i]):
                    target = book_characters[i +2]
                    source_target = []
                    source_target.append(source)
                    source_target.append(target)
                    source_and_targets.append(source_target)
            if i + 3 < length:
                if (len(book_characters[i + 3]) == 1) and (book_characters[i + 3] != book_characters[i]):
                    target = book_characters[i +3]
                    source_target = []
                    source_target.append(source)
                    source_target.append(target)
                    source_and_targets.append(source_target)
            if i + 4 < length:
                if (len(book_characters[i + 4]) == 1) and (book_characters[i + 4] != book_characters[i]):
                    target = book_characters[i +4]
                    source_target = []
                    source_target.append(source)
                    source_target.append(target)
                    source_and_targets.append(source_target)
            if i + 5 < length:
                if (len(book_characters[i + 5]) == 1) and (book_characters[i + 5] != book_characters[i]):
                    target = book_characters[i +5]
                    source_target = []
                    source_target.append(source)
                    source_target.append(target)
                    source_and_targets.append(source_target)
            
            df = {}
            
            for pair in source_and_targets:
                pair = str(pair)
                if pair in df:
                    df[pair] += 1
                else:
                    df[pair] = 1
   

            for key in df:
                #weights
                weight = df[key]
                weight = int(weight)
                weights.append(weight)
                #sources
                key = key.split()
                source = key[0]
                source = source.replace("[", "")
                source = source.replace("]", "")
                source = source.replace("'", "")
                source = source.replace(",", "")
                sources.append(source)
                #targets
                target = key[1]
                target = target.replace("[", "")
                target = target.replace("]", "")
                target = target.replace("'", "")
                target = target.replace(",", "")
                targets.append(target)
                #type
                types.append('Undirected')
                #book
                number = int(number)
                books.append(number)

    

'''
    for line in stripped:
        characters = []
        for c in all_characters:
            if c in line:
                characters.append(c)
        book_characters.append(characters)
'''

       
    
    
    
    

create_network(book_1, 1)
create_network(book_2, 2)
create_network(book_3, 3)
create_network(book_4, 4)
create_network(book_5, 5)
create_network(book_6, 6)
create_network(book_7, 7)

data = {'Source':sources, 'Target':targets, 'Type':types, 'Weight':weights, 'book':books}
witcher_network = pd.DataFrame(data)
print(witcher_network)

witcher_network.to_csv('witcher_network.csv')