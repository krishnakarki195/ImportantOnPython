#!/usr/bin/python
# usage: market space
# pass : block filler and does nothings
# Logical operations : and/or

print "welcome to the market"
food_type = raw_input("what food type you need - mutton/chicken/fish/veg: ")

if food_type == 'fish':
  print "welcome to the fish market"
  fish_type = raw_input("what kind of fish do you need - solomon/fillets/rohu/tofu: ")
  if fish_type == 'solomon' or fish_type == 'Solomon':
    print "your fish type {} is available".format(fish_type)
    print "how much quantity of {} you need".format(fish_type)
  elif fish_type == 'fillets':
    print "your fish type {} is available".format(fish_type)
    print "how much quantity of {} you need".format(fish_type)
  elif fish_type == 'rohu':
    print "your fish type {} is available".format(fish_type)
    print "how much quantity of {} you need".format(fish_type)
  else:
    print "your fish type {} is not available".format(fish_type)
    print "how about mutton/chicken/veg"    
elif food_type == 'mutton':
  pass
elif food_type == 'chicken':
  pass
elif food_type == 'veg':
  pass
else:
  pass
