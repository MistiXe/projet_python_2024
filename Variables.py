

def genererPion(platforme):
    
    a = platforme.create_rectangle(50,50,80,80,fill="red") 
    b = platforme.create_rectangle(50,90,110,120,fill="red")
    c = platforme.create_rectangle(50,130,140,160,fill="red")
    d = platforme.create_rectangle(50,170,80,230,fill="red")
    e = platforme.create_rectangle(50,250,80,340,fill="red")
    f = platforme.create_rectangle(50,370,80,490,fill="red")
    g = platforme.create_rectangle(50,530,170,560,fill="red")
    h = platforme.create_rectangle(250,50,310,110,fill="red")
    i = platforme.create_rectangle(250,140,310,260,fill="red")
    j = platforme.create_rectangle(250,340,340,430,fill="red")

    a_b = platforme.create_rectangle(950,50,980,80,fill="blue") 
    b_b = platforme.create_rectangle(950,90,1010,120,fill="blue")
    c_b = platforme.create_rectangle(950,130,1040,160,fill="blue")
    d_b= platforme.create_rectangle(950,170,980,230,fill="blue")
    e_b = platforme.create_rectangle(950,250,980,340,fill="blue")
    f_b = platforme.create_rectangle(950,370,980,490,fill="blue")
    g_b = platforme.create_rectangle(950,530,1070,560,fill="blue")
    h_b = platforme.create_rectangle(850,50,910,110,fill="blue")
    i_b = platforme.create_rectangle(850,140,910,230,fill="blue")
    j_b = platforme.create_rectangle(850,340,940,430,fill="blue")
    


   

    return [[a,b,c,d,e,f,g,h,i,j],[a_b,b_b,c_b,d_b,e_b,f_b,g_b, h_b,i_b, j_b]]


