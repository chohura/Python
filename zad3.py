#!/usr/bin/env python

def main():
  kod = 1234
  wprowadzony_kod = int(input("Podaj kod: "))
  if wprowadzony_kod == kod:
    print("Koda jest prawidłowy")
  else:
    print("Koda nie jest prawidłowy")
    
if __name__ == '__main__':
  main()