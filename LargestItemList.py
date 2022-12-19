def largest(List):
    if len(List) == 1:
        return List[0]
    else:
        return max(List[0], largest(List[1:]))
def main():
  List= [10, 20, 30, 40, 50, 60, 70, 80, 90]
  print(largest(List))
main()
