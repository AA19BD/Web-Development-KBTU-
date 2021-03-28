def count_code(str):
  counts=0
  for i in range(97,123):
    counts+= str.count('co'+chr(i)+'e')
  return counts 