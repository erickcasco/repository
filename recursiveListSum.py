def main():
  list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
  print(total(list))
def total(list):
    if not list:
        return 0
    else:
        return list[0] + total(list[1:]) 
main()
