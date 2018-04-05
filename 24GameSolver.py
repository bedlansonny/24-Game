##solver for 24 Game
import itertools

opers = ['+','-','/','*']
oc = [p for p in itertools.product(opers, repeat=3)]

paraStrs = ['          ',' (  )     ','     (  ) ','   (  )   ',' (  )(  ) ','(      )  ','  (      )','((  )  )  ','(  (  ))  ','  ((  )  )','  (  (  ))']
pc = [[c.strip() for c in s] for s in paraStrs]

while True:
    nums = list(input().split(' '))
    nc = list(set(itertools.permutations(nums,4)))
    output = ""
    for n in range(len(nc)):
        for o in range(len(oc)):
            for p in range(len(pc)):
                s = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(pc[p][0],pc[p][1],nc[n][0],oc[o][0],pc[p][2],pc[p][3],nc[n][1],pc[p][4],oc[o][1],pc[p][5],nc[n][2],pc[p][6],pc[p][7],oc[o][2],nc[n][3],pc[p][8],pc[p][9])
                try:
                    if eval(s)==24:
                        output += "{} = 24\n".format(s)
                        break
                except ZeroDivisionError:
                    continue
    if output == "":
        print("No solutions found.\n")
    else:
        print(output)
