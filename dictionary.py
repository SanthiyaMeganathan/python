monthvalue ={
    "jan":"january",
    "feb":"feburary",
    "mar":"march",
    "apr":"april",
    "may":"may",
    "jun":"june",
    "jul":"july",
    "aug":"august",
    "sep":"september",
    "oct":"october",
    "nov":"november",
    "dec":"december"
}

print(monthvalue["jan"])


print(monthvalue.get("feb"))
print(monthvalue.get("feb","mar"))
print(monthvalue.get("abc"))
print(monthvalue.get("abc","not found"))
#if we pass something that not present in 
# the dictory in get function then it will pass none
#  as answer and we can also pass 
# what to print when the key is not present in the  dictonary