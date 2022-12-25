uids = {} #dict
for i in range(len(users)): # start=0, stop 3 step 1  i 0 i<stop 0<3 True
  uids[users[i]]=i # uids[users[0]]=0  user1: 0 user2:1 user3:2

pids = {} # dict
for i in range(len(products)):
  pids[products[i]]=i # pids[laoptop]=0 , mouse 1 monitor 2 pendrive 3 harddisk 4

print(uids, pids)

prd_fq = np.zeros((len(users),len(products)) ) # 3*5 
print(prd_fq)
