nums = [1,2,2,3,4]



def remove_adjacent(any_list):
    shortenedlist = []
    
    for x in any_list:
        if x not in shortenedlist:
            shortenedlist.append(x)
    return(shortenedlist)
            

remove_adjacent(nums)