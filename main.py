from population import Population

def main():
    population = Population()
    for _ in range(20):
        population.play_population()
        print(population)
        population = Population(population)

    print(population)
    population.play_best()

if __name__ == "__main__":
    main()
