import random


def get_count_neighbourhood(field, x, y):
	count = 0
	neighbourhood = []
	
	for sub_y in range(y-1, y, y+1):
		for sub_x in range(x-1,x,x+1):
			if sub_x != x and sub_y != y:
				neighbourhood.append(0)

	print(len(neighbourhood))

	return

def main():

	field = [[0 for x in range(100)] for y in range(100)]

	for i in range(1000):
		x = random.randint(0,99)
		y = random.randint(0,99)
		field[y][x] = 1

	while(True):
		for y in range(len(field)):
			for x in range(len(field[0])):
				count_neighbourhood = get_count_neighbourhood(field, x, y)

	pass

if __name__ == "__main__":
	main()
	pass
			

