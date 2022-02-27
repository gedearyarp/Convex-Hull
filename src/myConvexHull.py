def DivideAndConquerConvexHull(res, bucket, IdxLine1, IdxLine2, direction) :
    # PointLine1 dan PointLine2 merupakan titik koordinat yang jika disatukan akan membentuk garis awal
    PointLine1 = bucket[IdxLine1]
    PointLine2 = bucket[IdxLine2]
    
    # idx merupakan index titik/point yang memiliki jarak terjauh dan garis awal dan berada pada direction
    # yang sesuai dengan parameter
    idx = -1 
    
    # maxDist merupakan jarak terjauh dari semua kemungkinan titik/point dengan garis awal dan berada pada direction
    # direction yang sesuai dengan parameter
    maxDist = 0
    
    # Melakukan iterasi untuk mencari nilai idx dan maxDist
    for i in range(len(bucket)) :
        # Persamaan dibawah didapatkan dari rumus jarak titik dengan garis pada bidang koordinat
        curDist = ((bucket[i][1] - PointLine1[1]) * (PointLine2[0] - PointLine1[0]) 
                   - (PointLine2[1] - PointLine1[1]) * (bucket[i][0] - PointLine1[0]))
        if curDist * direction >= 0 and abs(curDist) > maxDist :
            idx = i
            maxDist = abs(curDist)
    
    # Jika idx tidak berubah maka tidak mendapatkan titik yang sesuai dengan direction dari garis
    # awal, artinya garis awal ini merupakan bagian dari Convex Hull
    if idx == -1 :
        newLineRes = [IdxLine1, IdxLine2]
        if newLineRes not in res :
            res.append(newLineRes)
        return res
    
    # Jika nilai idx tidak -1 lakukan kembali iterasi pada kedua garis baru hasil dari pasangan
    # titik awal pertama dengan titik terjauh dan titik terjauh dengan titik awal kedua
    res = DivideAndConquerConvexHull(res, bucket, IdxLine1, idx, direction)
    res = DivideAndConquerConvexHull(res, bucket, idx, IdxLine2, direction)
    
    # Mengembalikan array pasangan index Convex Hull
    return res

def ConvexHull(bucket) :
    # Deklarasi minX, maxX yang merupakan titik dengan nilai x paling minimum dan paling maksimum
    minX = 0
    maxX = 0
    
    # res merupakan array pasangan index yang merupakan solusi dari Convex Hull
    res = [] 
    
    # Mencari nilai minX dan maxX 
    for i in range(len(bucket)) :
        if bucket[i][0] < bucket[minX][0] :
            minX = i
        if bucket[i][0] > bucket[maxX][0] :
            maxX = i
    
    # Melakukan rekursi algoritma divide and conquer pada kedua sisi dari garis minX dan maxX
    res = DivideAndConquerConvexHull(res, bucket, minX, maxX, 1)
    res = DivideAndConquerConvexHull(res, bucket, minX, maxX, -1)
    
    # Mengembalikan array beranggotakan pasangan titik yang merupakan garis-garis Convex Hull
    return res


