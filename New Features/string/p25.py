# We Can also use Walrus Operator (:=) inside f-string
import math
half_radius = 10
print(f'The Area of Cirlce with radius {2*half_radius} is {math.pi*2*half_radius*2*half_radius}')
print(f'The Area of Cirlce with radius {(r:=2*half_radius)} is {math.pi*r*r}')
print(f'The Area of Cirlce with radius {(r:=2*half_radius)} is {math.pi*r*r:.2f}')

