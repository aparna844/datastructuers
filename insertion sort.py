# insertion sort 
def insertion_sort(sequence):
   for i in range(1,len(sequence)):
        for j in range(i):
           if sequence[i]<sequence[j]:
                sequence[i],sequence[j]=sequence[j],sequence[i]
                
                
    return sequence
