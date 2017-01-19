
def is_family(tree):
    #print(tree)
    a = enumerate(tree)
    for i,s in a:
        #print("START LOOP",i,s)
        if len(tree) == 1:
            #print("True len==1")
            print("True")
            return True
    for i in range(1,len(tree)):
        print(i, tree[i],tree[i][0],[tree[x][1] for x in range(0,i)])
        if tree[i][0] in [tree[x][1] for x in range(0,i)] or tree[i][0] in [tree[x][0] for x in range(0,i)] and tree[i][1] not in [tree[x][0] for x in range(0,i)]:
            print("True")
            continue
        else:
            print("False")
            return False
    print("True")
    return True

'''
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([['Logan', 'Mike']]) == True, 'One father, one son'
    assert is_family([['Logan', 'Mike'],['Logan', 'Jack']]) == True, 'Two sons'
    assert is_family([['Logan', 'Mike'],['Logan', 'Jack'],['Mike', 'Alexander']]) == True, 'Grandfather'
    assert is_family([['Logan', 'Mike'],['Logan', 'Jack'],['Mike', 'Logan']]) == False, 'Can you be a father for your father?'
    assert is_family([['Logan', 'Mike'],['Logan', 'Jack'],['Mike', 'Jack']]) == False, 'Can you be a father for your brather?'
    assert is_family([['Logan', 'William'],['Logan', 'Jack'],['Mike', 'Alexander']]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
'''

#is_family([['Logan', 'Mike']])
#is_family([['Logan', 'Mike'],['Logan', 'Jack']])
#is_family([['Logan', 'William'],['Logan', 'Jack'],['Mike', 'Alexander']])
is_family([["Logan","Mike"],["Logan","Jack"],["Mike","Logan"]])