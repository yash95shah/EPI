def parity(n: int) -> int:
  parity = 0
  while n:
    parity ^= n&1
    n >>= 1
  return parity

def paritybetter(n: int) -> int:
  parity = 0 
  while n:
    parity ^= 1
    n &= (n-1)
  return parity

    # 12 == 1 1 0 0 // 1 1 0

print( parity(12) )
print( paritybetter(12) )


# print(12^(12&1))

# 1 1 0 0
# 1 1 0 0