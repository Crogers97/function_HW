# def greet():
#     print("Hey")

# greet()

# def greet():
#     print("Hey")

# greeting = greet()
# print(greeting) ""

# def greet(name):
#     return "Hey" + name

# greeting = greet("Calum")
# print(greeting)


# def greet(name, time_of_day):
#     return "Good" +  time_of_day + "," + name

# name_1 = "Calum"
# time_of_day_1 = "morning"
# greeting =greet(name_1, time_of_day_1)
# print(greeting)

# name_2 = "Jamie"
# time_of_day_2 = "afternoon"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)




# def greet():
#     words = "Hey"
#     return words

# def greet_two():
#     return words

# print(greet_two())



chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 4 },
  { "name": "Mabel", "age": 5, "eggs": 3},
]

def count_eggs(list):
    total_eggs = 0

    for chicken in list:
        total_eggs += chicken["eggs"]
        chicken["eggs"] = 0 

    return f"{total_eggs} eggs collected"

print( count_eggs(chickens))
