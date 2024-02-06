rectangleX = coteCarre/7
    rectangleY = coteCarre/6
    R = 0.9*(rectangleX/2)
    deltaX = (rectangleX-2*R)/2
    deltaY = (rectangleY-2*R)/2
    for i in range(7):
        for j in range(6):
            xmin = xminSup + i*rectangleX + deltaX
            ymin = yminSup + j*rectangleY + deltaY
            xmax = xmin + 2*R
            ymax = ymin + 2*R
            A = xmin, ymin
            B = xmax, ymax
            cnv.create_oval(A,B, fill='ivory', outline='ivory')