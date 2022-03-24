def swap_bits(x, i, j):
  if x<<i&1 != x<<j&j:
    bit_mask = i|j<<1
    x ^= bit_mask
  return x





# def swap_bits(x, i, j):
#   bit_i = (x & (1 <<  i)) >> i 
#   print(bit_i)
#   bit_j = (x & (1 <<  j)) >> j
#   print(bit_j)
#   x ^= (bit_i<<j) & (bit_j<<i)
#   return x


print (swap_bits(14, 2, 3))
# # 12 0 1          1 1 0 & 0 0 1       get_0th bit == 0 get 1st=1   
# # 
# # 
# #   1 1 0 0 
# #   0 1 1 0
# #   1 0 1 0
# #   10 10


# #    1 1 0 0
# #    0 0 0 0
# #     
# # 
# # 
# # ###
# ######
# ######
# ######
# ######
# ######
# ######
# ######
# ######
# #####
# # #######
# ######