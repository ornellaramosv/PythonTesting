## 1. Overview ##

f = open("movie_metadata.csv",'r')
data = f.read()
list_elements = data.split("\n")
movie_data = []
for row in list_elements:
    movie_data.append(row.split(","))
print(movie_data[0:5])



## 3. Writing Our Own Functions ##

def get_movie_names(movie_list):
    list_movies = []
    for rows in movie_list:
        list_movies.append(rows[0])
    return list_movies
movie_names = get_movie_names(movie_data)
print(movie_names)

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
def is_usa(input_list):
    if input_list[6] == "USA":
        return True
    else:
        return False
wonder_woman_usa = is_usa(wonder_woman)
            
    
    

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def index_equals_str(input_lst,index,string):
    if input_lst[index] == string:
        return True
    else:
        return False

wonder_woman_in_color = index_equals_str(wonder_woman,2,"Color")

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst,index,input_str,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

num_of_us_movies = feature_counter(movie_data,6,"USA",True)
print(num_of_us_movies)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst):
    films_dc = {}
    films_dc["japan_films"] = feature_counter(input_lst,6,"Japan",True)
    films_dc["color_films"] = feature_counter(input_lst,2,"Color",True)
    films_dc["films_in_english"] = feature_counter(input_lst,5,"English",True)
    return films_dc

summary = summary_statistics(movie_data)