from numSol import NumSol
def main():
	Ep = [-0.375, -0.25, -0.125, 0, 0.125, 0.25, 0.375]
	#Ep = [0.01]
	for e in Ep:
		NumSol(e, 5)

	#main function

if __name__ == '__main__':
	main()
