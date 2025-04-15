dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
result=[]
for i in dice1:
    for j in dice2:
        a=i,j
        result.append(a)
print(result)


di={}
for i in range(2,13):
    c=0
    for j in result:
        if i == j[0]+j[1]:
            c+=1
    di[str(i)] = c/len(result)
print(di)

R = int(input("Enter a row size"))

P1_wins = 0
P2_wins = 0
  
for _ in range(R):
    a, b, c, d = map(int, input().split())

P1_sum = a+b
P1_prob = di[str(P1_sum)]


P2_sum = c+d
P2_prob = di[str(P2_sum)]



if P1_prob < P2_prob:
    P1_wins += 1

elif P2_prob < P1_prob:
    P2_wins += 1

if P1_wins > P2_wins:
    print("P1 wins")
elif P2_wins > P1_wins:
    print("P2 wins")
else:
    print("Tie")








