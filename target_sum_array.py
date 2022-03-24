# For array, return pair that sums to target [1,3,2,2] target = 4 => return (1 3) (2 2)



def return_pair(arr, target_sum):
  if len(arr)<2:
    return None
  desired_already_present = set() #To store the results of the target sum element for the pair 
  output = set() #This stores the actual results
  for elem in arr:
    desired = target_sum -elem
    if desired not in desired_already_present:
      desired_already_present.add(elem)
    else:
      output.add((elem, desired))  # can also be (min(elem, desired), max(elem, desired)) to make sure its ordered.
  return "\n".join(map(str,list(output))) 



print(return_pair([2,3,1,2,5,0,4,1,3], 4))