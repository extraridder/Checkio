def turn(z1):
    return ('{}{}{}{}'.format(z1[3][0],z1[2][0],z1[1][0],z1[0][0]),'{}{}{}{}'.format(z1[3][1],z1[2][1],z1[1][1],z1[0][1]),'{}{}{}{}'.format(z1[3][2],z1[2][2],z1[1][2],z1[0][2]),'{}{}{}{}'.format(z1[3][3],z1[2][3],z1[1][3],z1[0][3]))

def recall_password(cipher_grille, ciphered_password):
    output_string = ""
    a = cipher_grille
    for i in range(1,5):
        #print(i,a)
        for ii in range(0,4):
            for iii in range(0,4):
                if a[ii][iii] == "X":
                    output_string += ciphered_password[ii][iii]
        a = turn(a)

    #print(output_string)
    return output_string

recall_password(('X...','..X.','X..X','....'),('itdf','gdce','aton','qrdi'))
recall_password(('....','X..X','.X..','...X'),('xhwc','rsqx','xqzz','fyzr'))