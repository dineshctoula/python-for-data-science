

type=["python", "java","c", "c+"]
print(type)



empty=[]
print(empty)

print(type[2]) 

type.append('dot')
print(type)


s=['a','b','c', 'd','e']
print(s[-3:-1])
# negative slicing concept 

type.insert(3,"dinesh")
print(type)

# extending list 

list1=['a','b','c','d','e']
list2=['d','e','f','g']
list1.extend(list2)
print("updated list:",list1)


# changing the list items 

list1=['apple','banana','cherry','tomato']
list1[1]="pearl"
print(list1)

# removing an element from the list 

list2=['d','e','f','g']
list2.remove('e')
print(list2)



# deleting from the list 

list1=['dhoni','kohli','rohit','sehwag','harbhajan','parash']
del list1[1]
print(list1)


del list1[1:2]
print(list1)

list1.sort()
print(list1)


list1.reverse()
print(list1)

list2=list1.copy()
print(list2)



# dictionary 

list_names={
    "name1":"harry",
    "name2":"tom",
    "name3":"rocky",
}
print(list_names)


# name change gareko yaha  
list_names["name4"]="justin"
print(list_names)


del list_names["name2"]
print(list_names)

