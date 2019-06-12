#!/usr/bin/python3

# argparse is one of the cool argument parser that I can pass in a commandline environment to my program
import argparse

parser = argparse.ArgumentParser(description="This is a description")
parser.add_argument("-i", type=str, help="Help for the argument i", required=True)
parser.add_argument("-o", type=str, help="Help for the argument o", required=False)

#this one requires an argument.
cmdargs = parser.parse_args()

ivar = cmdargs.i # this will parse i
print(ivar)

ovar=cmdargs.o
print(ovar)