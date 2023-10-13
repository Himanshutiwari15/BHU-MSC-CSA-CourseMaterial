def findMinCoins(coins, amount):
  
  coins.sort(reverse=True)
  
  minCoins = []
  for i in coins:
    while amount >= i:
      amount -= i
      minCoins.append(i)

  print(minCoins)

coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000] 
amount = 568

findMinCoins(coins, amount)