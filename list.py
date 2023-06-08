# Python Lists
#
# # List
# # Data structure
# # A way to organise and store data in Python
# # A collection of data


# # Syntax
# # square brackets []
# # comma separated values
# # ["a", "b", "c"]
countries = ["Cambodia", "Vietnam", "Thailand", "Laos", "Myanmar", "Malaysia", "Singapore", "Indonesia", "Philippines"]

print(countries[0]) # Cambodia

# # List indexing
# # Indexing starts at 0
# # Last index is -1

print(countries[-1]) # Philippines

# # List slicing
# # Syntax: list[start:end:step]
# # start: inclusive
# # end: exclusive

print(countries[0:5])
print(countries[:5]) # same as above

print(countries[5:]) # ['Malaysia', 'Singapore', 'Indonesia', 'Philippines']

# list length

print(len(countries)) # 9

#  sort list
countries.sort()
print(countries)

# reverse list
countries.reverse()
# or
countries.sort(reverse=True)
print(countries)

# # append to list
countries.append("Brunei")

# # insert into list
countries.insert(0, "Timor Leste") # insert at index 0
print(countries)

# # remove from list
countries.remove("Brunei")
print(countries)
# # remove from list by index
countries.pop(0) # remove at index 0
print(countries)

# # remove all items from list
countries.clear()
# or 
countries = []
print(countries)

cambodia_provinces = ["Phnom Penh", "Kandal", "Takeo", "Kampot", "Kep", "Koh Kong", "Preah Sihanouk", "Kampong Speu", "Kampong Chhnang", "Pursat", "Battambang", "Banteay Meanchey", "Siem Reap", "Oddar Meanchey", "Preah Vihear", "Stung Treng", "Ratanakiri", "Mondulkiri", "Kratie", "Kampong Thom", "Kampong Cham", "Tbong Khmum", "Prey Veng", "Svay Rieng", "Kandal", "Kep", "Koh Kong", "Preah Sihanouk", "Kampong Speu", "Kampong Chhnang", "Pursat", "Battambang", "Banteay Meanchey", "Siem Reap", "Oddar Meanchey", "Preah Vihear", "Stung Treng", "Ratanakiri", "Mondulkiri", "Kratie", "Kampong Thom", "Kampong Cham", "Tbong Khmum", "Prey Veng", "Svay Rieng"]
print(cambodia_provinces.count("Kandal"))
# remove duplicates
cambodia_provinces = list(dict.fromkeys(cambodia_provinces)) # convert to dictionary to remove duplicates, then convert back to list
print(cambodia_provinces)
print(len(cambodia_provinces))


# # nested lists
# # list inside a list


# # join lists
# # use + operator
# # or use extend() method
# # or use append() method

# # list methods
# # https://www.w3schools.com/python/python_ref_list.asp

# # list comprehension
# # https://www.w3schools.com/python/python_lists_comprehension.asp

# # list unpacking
# # https://www.w3schools.com/python/gloss_python_unpacking.asp