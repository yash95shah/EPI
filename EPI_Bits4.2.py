def swap_bits(number, index1, index2):
  #First check if both bits are the same and if they are, just return original number
  if number >> index1 & 1 != number >> index2 & 1:
    #Let's select a bitmask that will help flip the number
    bit_mask = index1|index2 << 1
    number ^= bit_mask
  return number 



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