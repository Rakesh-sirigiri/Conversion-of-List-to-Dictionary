list = [['a', 'b', 1,2], ['c', 'd', 3, 4], ['e', 'f', 5, 6 ]]
print("The original list is : " + str(list))
res = {tuple(sub[:2]): tuple(sub[2:]) for sub in list}
print("The mapped Dictionary : " + str(res))
