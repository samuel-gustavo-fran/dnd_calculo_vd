def dnd_calculo_vd(ldvida,lnivel,mcon):
    lista_de_calculode_vida = [((((i/2)+1)+mcon)*(j - 1))+(i+mcon) if ldvida[0] == i else (((i/2)+1)+mcon)*j  for i , j in zip(ldvida,lnivel)]
    return lista_de_calculode_vida