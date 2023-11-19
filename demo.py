# d = {1: 'a', 2: 'b', 3: 'c', 4: 'a'}

# key = d.values()
# l = list(key)
# l1 = []
# for i in range(len(l)):
# 	if l[i] not in l1:
# 		l1.append(l[i])
# print(l1)


# for i in l1:
# 	print(f'The count of {i}:{l.count(i)}')


# CREATE TABLE Department (
#     dept_id INT PRIMARY KEY,
#     dept_code VARCHAR(10),
#     dept_name VARCHAR(40)
# );

# CREATE TABLE Employee (
#     emp_id INT PRIMARY KEY,
#     emp_name VARCHAR(100),
#     uidai VARCHAR(10),
#     dept_id INT,
#     salary INT,
#     FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
# );
# # Average salary paid for each department

# # select e.avg(salary), e.department from Employee as e join department as d on e.dept_id = d.dept_id;


# from collections import Counter

# d = {1: 'a', 2: 'b', 3: 'c', 4: 'a'}

# # # Use Counter to count the occurrences of values in the dictionary
# value_counts = Counter(d.values())
# print(value_counts)
# print(type(value_counts))

# Print the value counts
# for value, count in value_counts.items():
#     print(f"'{value}' occurs {count} times")

# print(dir(Counter))
# print(Counter(d.keys()))


# Counte the number of duplicate values how many time come:


# lower = int(input('Enter Lower Number:'))
# upper = int(input('Enter Upper Number:'))
# print('The list of Prime Number:')
# for num in range(lower, upper+1):
# 	if num > 1:
# 		for i in range(2, num):
# 			if num%i == 0:
# 				break
# 		else:
# 			print(num, end=',')


# To check given number is prime number 

from functools import reduce

# num = int(input('Enter Number:'))
# if num > 0:
# 	l = [x for x in range(1,num+1)]
# 	fac = reduce(lambda a,b:a*b, l)
# 	print(fac)
# elif num ==0:
# 	print('factorial of Zero is 1')
# else:
# 	print('Number should be greate then 0')


# a = int(input('Enter a:'))
# b = int(input('Enter b:'))

# temp = a
# a = b
# b = temp


from math import factorial
def factorial(number):
	if number >=1:
		result = 1
		for i in range(number,0, -1):
			result = result * i
		print(result)
	elif number == 0:
		result = 1
		print(result)
# number = int(input('Enter Number:'))
# factorial(number)





from django.db import models

class Country(models.Model):
	country_name = models.CharField(max_length=64, unique=True)

class City(models.Model):
	city_name = models.CharField(max_length=64, unique=True)
	country = models.ForeignKey(Country, on_delete=models.CASECADE)
	population = models.PosetiveIntegerField()

# Find Avg of population from each country
data = Country.objects.values('name').annotate(Avg('city__population'))
data = City.objects.values('country__name').annotate(Avg('population'))

# Find Sum of population from Each county
data = City.objects.values('country__name').annotate(Sum('population'))
data = Country.objects.values('name').annotate(Sum('city__population'))

# find Min of popuation from each Country
data = City.objects.values('country__name').annotate(Min('population'))
data = Country.objects.values('name').annotate(Min('city__population'))

# find Max of population from each Country
data = City.objects.values('country__name').annotate(Max('population'))
data = Country.objects.values('name').annotate(Max('city__population'))

# find number of city from each country
data = City.objects.values('country__name').annotate(Count('name'))
data = Country.objects.values('name').annotate(Count('city__name'))


# find a city and their country which have min population 
data = City.objects.values('country__name','name', 'population').order_by('population')[0]

select city.name, country.name from city inner join
country on city.id = country.id group by country.name 
where city.population = (select min(city.population) from city);

# find a city and thir country which have max population 
data = City.objects.values('country__name','name', 'population').order_by('-population')[0]



# Find Average of City population
data = City.objects.all().aggregate(Avg('popuation'))