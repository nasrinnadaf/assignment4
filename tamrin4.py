sentenses= input("write your sentenses:   ").strip()
num=0 
space=False
for i in sentenses:
  if i==" ":
     if space==False:
       num=num+1
       space=True
  else:
      space=False  
print(f"Word {num+1}")