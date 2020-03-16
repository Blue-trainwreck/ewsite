import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--movie", choices=['melodrama', 'football', 'other'], type=str)
args = parser.parse_args()
cars = args.cars
barbie = args.barbie
if 0 > args.cars or args.cars > 100:
    cars = 50
if 0 > args.barbie or args.barbie > 100:
    barbie = 50
if args.movie == 'melodrama':
    delta = 0
elif args.movie == 'football':
    delta = 100
else:
    delta = 50
boys = int((100 - barbie + cars + delta) / 3)
girls = 100 - boys
print('boy:', boys)
print('girl:', girls)
