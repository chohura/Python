#!/usr/bin/env python

from pathlib import Path

def zlicz(path):
  p = Path(path)
  count = 0 
  if p.is_dir():
    for x in p.iterdir():
      if x.is_dir():
        count += zlicz(x)
      else:
        count += 1
  return count 
  
if __name__ == '__main__':
  main()
 
