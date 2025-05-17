import random
from Individual import Individual
from connect4 import Connect4
import time

class Population:
    def __init__(self, pop=None):
        # pop_size * survival_rate should be >= 1
        self.pop_size = 10
        self.survival_rate = 0.4
        if pop:
            # selection
            sorted_pop = sorted(pop.individuals, key=lambda x: x.fitness, reverse=True)
            survivors = sorted_pop[:int(self.pop_size * self.survival_rate)]
            # crossover
            self.individuals = self.crossover(survivors)

            
        else:
            self.individuals = [ Individual() for _ in range(self.pop_size) ]

    def play_population(self):
        for i in range(len(self.individuals)):
            for j in range(i):
                self.play_game(self.individuals[i], self.individuals[j])

    def play_best(self):
        player1 = self.getBest()
        player2 = self.getBest()
        game = Connect4()
        is_player_one = True

        while True:
            print(game)
            time.sleep(1)
            if (is_player_one):
                game = player1.make_move(game)
            else:
                game = player2.make_move(game)
            if game.has_player_won():
                print(game)

                if game.current_player == 'X':
                    print('O win')
                    player2.addFitness(5)
                    player1.addFitness(-1)
                else:
                    print('X win')
                    player1.addFitness(5)
                    player2.addFitness(-1)
                break
            elif game.is_terminal():
                print(game)
                print('draw')
                player1.addFitness(4)
                player2.addFitness(4)
                break

    def play_game(self, player1, player2):
        game = Connect4()
        is_player_one = True

        while True:
            if (is_player_one):
                game = player1.make_move(game)
            else:
                game = player2.make_move(game)
            if game.has_player_won():
                if game.current_player == 'X':
                    player2.addFitness(3)
                else:
                    player1.addFitness(3)
                break
            elif game.is_terminal():
                player1.addFitness(1)
                player2.addFitness(1)
                break


    def crossover(self, survivors):
        crossed = []
        for i in range(self.pop_size//2):
            # crossover totally random
            ind1 = survivors[random.randint(0,len(survivors)-1)]
            ind2 = survivors[random.randint(0,len(survivors)-1)]
            crossed.append(ind2.crossover(ind1))
            crossed.append(ind1.crossover(ind2))
        return crossed

    def getBest(self):
        return sorted(self.individuals, key=lambda x: x.fitness, reverse=True)[0]

    def printAll(self):
        for i in self.individuals:
            print(i)



    def __str__(self):
        return f"\nTotal fitness: {sum([ i.fitness for i in self.individuals ])}\n Best: {self.getBest()}"
