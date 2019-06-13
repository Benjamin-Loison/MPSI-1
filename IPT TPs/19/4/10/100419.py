for k in range(N - 1):
    i0 = detection_pivot(k)
    if i0 != k:echanger(i0, k)
    transvections(k) # créer les 0 sous Mkk
    
def detection_pivot(k):
    # idée: extraire la colonne n°k et recherche
    c = [M[i][k] for i in range(N)]
    i0 = pos_max(c, k)

