## Exercise: Python Dict and Tuples

1. We have following information on countries and their population (population is in crores),

    |Country|Population|
    |-------|----------|
    |China|143|
    |India|136|
    |USA|32|
    |Pakistan|21|
    1. Using above create a dictionary of countries and its population
    2. Write a program that asks user for three type of inputs,
        1. print: if user enter print then it should print all countries with their population in this format,
            ```
            china==>143
            india==>136
            usa==>32
            pakistan==>21
            ```
            
        1. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
        2. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
        3. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
        4. population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

# to add a country 
collect = input("what fuction do you want to perform: ")
if collect == 'add':
    country = input('input the country here: ')
    if country in population:
        print("this country exist in our list")
    elif country:
        pop = input("what the population of the country; ")
        population[country] = float(pop)
        print(population)
# to print 
elif collect == 'print':
    print(population)

# to remove
elif collect == 'remove':
    country = input('country to remove: ')
    if country in population:
        population.pop(country)
        print(population)
    else:
        print("this country is not in our list")
#to query
elif collect == 'query':
    country = input('country to query: ')
    if country in population:
        print("the population is: ", population[country])

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_exercise_1_country_population.py)

2. You are given following list of stocks and their prices in last 3 days,

    |Stock|Prices|
    |-------|----------|
    |info|[600,630,620]|
    |ril|[1430,1490,1567]|
    |mtl|[234,180,160]|

    1. Write a program that asks user for operation. Value of operations could be,
        1. print: When user enters print it should print following,
            ```
            info ==> [600, 630, 620] ==> avg:  616.67
            ril ==> [1430, 1490, 1567] ==> avg:  1495.67
            mtl ==> [234, 180, 160] ==> avg:  191.33
            ```
        2. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

you = {'info':[600,630,620],
    'ril':[1430,1490,1567],
    'mtl':[234,180,160]}
user = input('input goes here: ')
if user == 'print':
    for i in you:
     deem = round(sum(you[i])/len(you[i]), 2)
     print(i, "==>", you[i], "==>" + "avg:", deem)
elif user == 'add':
    stock = input("stock: ")
    prices = input("prices: ")
    you[stock] = [int(prices)]
    print(you)
[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_exercise_2_stocks.py)

3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_exercise_3_circle.py)
