def string_match(a, b):
  short=min(len(a),len(b))
  c=0
  for i in range(short-1):
    s1=a[i:i+2]
    s2=b[i:i+2]
    if s1==s2:
      c+=1
  return c
