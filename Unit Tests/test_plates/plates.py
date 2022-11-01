def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
  cifs = ['0','1','2','3','4','5','6','7','8','9']
  ok0 = False
  must_be_cif = False
  if len(s) > 1 and len(s) < 7 and s[0] not in cifs and s[1] not in cifs:
    for l in s:
      if l in ['.',',','!','?','(',')','[',']','{','}',':',';','-','"',"'"]:
        return False
      if must_be_cif == False:
        if l == '0':
          return False
        else:
          if l in cifs:
            must_be_cif = True
      else:
        if l not in cifs:
          return False
  else:
    return False
  return True

if __name__ == "__main__":
    main()
