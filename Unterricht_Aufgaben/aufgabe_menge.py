M = {i+1 for i in range(15)}                 # M = {1,2,...,15}
A = {i+1 for i in range(15) if i % 2 == 0}   # A = {1,3,5,7,...,15}
B = {i+1 for i in range(15) if i % 2 == 1}   # B = {2, 4, 6, 8, 10, 12, 14}

# print(M)
# print(A)
# print(B)

C = {2,3,5,12,13}



print(A.union(B))# a) A vereinigt B
print(A.intersection(B)) # b) A geschnitten B
print((M-C).intersection(B)) # c) nicht C geschnitten B
print(M-(M-B)) # d) M\ nicht B # \ heißt ohne
print(C-A) # e) C\A #(C ohne A)
print((M-(M- C)).intersection(C)) # f) (M ohne nicht C) geschnitten C
print(B - (M - (A.union(C))))    # g) B ohne (nicht(A vereinigt C))

# def vereinigung(menge1, menge2):     
# return menge1.union(menge2) 

# def schnittmenge(menge1, menge2):         
# return menge1.intersection(menge2) 
# def differenz(menge1, menge2):     
# return menge1.difference(menge2)