

def genererPion(platforme):
    
    a = platforme.create_rectangle(50,50,80,80,fill="red") 
    b = platforme.create_rectangle(50,90,110,120,fill="red")
    c = platforme.create_rectangle(50,130,140,160,fill="red")
    d = platforme.create_rectangle(50,170,80,230,fill="red")
    e = platforme.create_rectangle(50,250,80,340,fill="red")
    f = platforme.create_rectangle(50,370,80,490,fill="red")
    g = platforme.create_rectangle(50,500,170,530,fill="red")
    h = platforme.create_rectangle(250,50,310,110,fill="red")
    i = platforme.create_rectangle(250,140,310,260,fill="red")
    j = platforme.create_rectangle(250,300,340,390,fill="red")
    k = platforme.create_rectangle(250,460,340,520,fill="red")

    a_b = platforme.create_rectangle(900,50,930,80,fill="blue") 
    b_b = platforme.create_rectangle(900,90,960,120,fill="blue")
    c_b = platforme.create_rectangle(900,130,990,160,fill="blue")
    d_b= platforme.create_rectangle(900,170,930,230,fill="blue")
    e_b = platforme.create_rectangle(900,250,930,340,fill="blue")
    f_b = platforme.create_rectangle(900,370,930,490,fill="blue")
    g_b = platforme.create_rectangle(900,500,1020,530,fill="blue")
    h_b = platforme.create_rectangle(800,50,860,110,fill="blue")
    i_b = platforme.create_rectangle(800,140,860,230,fill="blue")
    j_b = platforme.create_rectangle(800,300,890,390,fill="blue")
    k_b = platforme.create_rectangle(800,460,890,520,fill="blue")
    


   

    return [[a,b,c,d,e,f,g,h,i,j,k],[a_b,b_b,c_b,d_b,e_b,f_b,g_b, h_b,i_b, j_b, k_b]]


