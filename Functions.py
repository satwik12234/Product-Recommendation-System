def reclist(uid): # function definition
  uid = uids[uid] # Row id of User
  upids = prd_fq[uid, :]  # column id of the products
  plist = np.argsort(upids)[::-1][:len(upids)] #frequnecy based sorting for the products
  plist = [products[p] for p in plist] # to retrive items in the sorted order based on frequency
  print(plist) #display

def viewproduct(uid, pid): # function definition
  uid = uids[uid] # row id of user
  pid = pids[pid] # column id of the product
  prd_fq[uid, pid] = prd_fq[uid, pid] + 1  # frequency increment
  print(prd_fq) # display
uname = input("Enter user name:")
print(reclist(uname))
pname = input("Select one product:")
viewproduct(uname, pname)
