#!/usr/bin/env python

from pathlib import Path

def main():
  p = Path('C:Windows')
  for x in p.iterdir():
    print(x)
    
  print(len(list(p.iterdir())))
  
if __name__ == '__main__':
  main()
