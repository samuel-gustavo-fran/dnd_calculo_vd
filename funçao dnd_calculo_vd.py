def dnd_calculo_vd(ldvida,lnivel,mcon):
    lista_de_calculode_vida = []
    for idx,(i,j) in enumerate(zip(ldvida,lnivel)):
        if idx == 1:
            lista_de_calculode_vida.append(((((i/2)+1)+mcon)*(j - 1))+(i+mcon))
        else:
            lista_de_calculode_vida.append((((i/2)+1)+mcon)*j)
    return sum(lista_de_calculode_vida)
    
