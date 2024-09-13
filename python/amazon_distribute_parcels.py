def parcel_distr(n,parcels,extra_parcels):

    # make all delivery agents have same load
    for i in range(len(parcels)):
        extra = max(parcels)-parcels[i]
        extra = min(extra,extra_parcels)
        parcels[i]+=extra
        extra_parcels-=extra
    
    # equally distribute extra packages
    distr = extra_parcels//n
    parcels = [i+distr for i in parcels]
    extra_parcels-=distr*n

    # add the rest of the remaining extra packages
    for i in range(extra_parcels): parcels[i]+=1

    return parcels

print(parcel_distr(5,[7,5,1,9,1],25))