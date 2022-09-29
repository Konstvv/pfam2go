from pfam2go import pfam2go

pfam_list = ['PF00032', 'PF00049', 'PF08463']
data = pfam2go(pfam_list)
print(data)