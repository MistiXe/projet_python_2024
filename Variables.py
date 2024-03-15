

def genererPion(platforme):
    
    a = platforme.create_rectangle(50,50,80,80,fill="red") 
    b = platforme.create_rectangle(50,90,120,120,fill="red")
    c = platforme.create_rectangle(50,130,160,160,fill="red")
    d = platforme.create_rectangle(50,170,80,240,fill="red")
    e = platforme.create_rectangle(50,250,80,360,fill="red")
    f = platforme.create_rectangle(50,370,80,520,fill="red")
    g = platforme.create_rectangle(50,530,200,560,fill="red")

    a_b = platforme.create_rectangle(950,50,980,80,fill="blue") 
    b_b = platforme.create_rectangle(950,90,1020,120,fill="blue")
    c_b = platforme.create_rectangle(950,130,1060,160,fill="blue")
    d_b= platforme.create_rectangle(950,170,980,240,fill="blue")
    e_b = platforme.create_rectangle(950,250,980,360,fill="blue")
    f_b = platforme.create_rectangle(950,370,980,520,fill="blue")
    g_b = platforme.create_rectangle(950,530,1100,560,fill="blue")

    return [[a,b,c,d,e,f,g],[a_b,b_b,c_b,d_b,e_b,f_b,g_b]]