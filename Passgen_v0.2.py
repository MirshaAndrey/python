	#!/usr/local/bin/python3
import random, string, os
print ('                                                                            ')
print ('                                                                            ')
print (' ========================================================================== ')
print ('|                                                                          |')
print ('|                              PassGen_v0.2                                |')
print ('| Generator of passwords of complexity of the specified length by the user |')
print ('|                                 MacOS                                    |')
print ('|                                                                          |')
print (' ========================================================================== ')
print ('                                                                            ')
print ('                                                                            ')
k=int(input('Enter a max lenght (no more than 80 characters): '))
print ('                                                                            ')
def generator_pw():
    pwd = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(pwd) for x in range(random.randint(k, k)))
print ('                                                                            ')
print ('         The generated password has been copied to the clipboard            ')
print ('                                                                            ')
os.system("echo '%s' | pbcopy" % generator_pw())
