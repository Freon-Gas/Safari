from animal import Animal, Manager, Zebra, Lion
import random
import os

def print_TODO(todo):
    print(f'<<<NOT IMPLEMENTED: {todo} >>>')

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.occupancy = [[False for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TODO('get random empty coordinates')
        self.num_zebras = num_zebras
        self.num_lions = num_lions
        self.world_size = world_size
        self.zebras = [Zebra(0,0,0) for _ in range(num_zebras)]
        self.lions = [Lion(0,0,0) for _ in range(num_lions)]
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')
        self.manager = Manager(world_size=self.world_size, num_zebras=self.num_zebras, num_lions=self.num_lions)
        self.grid = self.manager.generate_grid()

    def display(self):
        print(f'Clock: {self.timestep}')
        print(f'Zebras: {self.manager.num_zebras}')
        print(f'Lions: {self.manager.num_lions}')
        self.manager.display_grid(self.grid)
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def move_animals(self):
        for zebra in self.manager.zebras:
            zebra.move(self.grid)

        for lion in self.manager.lions:
            lion_position = lion.lion_move(self.grid)
            if lion_position is not None:
                lion_x, lion_y = lion_position
            # if eaten_zebra:
            #     will_be_gone_zebra = self.get_zebra_at_position(eaten_zebra[0], eaten_zebra[1])
                # if will_be_gone_zebra:
                #     self.manager.zebras.remove(will_be_gone_zebra)
                if lion.starving_counter >= 3: 
                    self.manager.lions.remove(lion)
                    self.manager.num_lions -= 1
                    self.grid[lion_x][lion_y] = ' '
                for zebra in self.manager.zebras:
                    if zebra.x == lion_x and zebra.y == lion_y:
                        self.manager.zebras.remove(zebra)
                        self.manager.num_zebras -= 1

                    
            
    def get_zebra_at_position(self, x, y):
        for zebra in self.manager.zebras:
            if zebra.x == x and zebra.y == y:
                return zebra

    

    def breed_animals(self):
        new_zebras = []
        new_lions = []
        for zebra in self.manager.zebras:
            new_zebra = zebra.zebra_breed(self.grid)
            if new_zebra:
                new_zebras.append(new_zebra)
                self.manager.num_zebras += 1
        self.manager.zebras.extend(new_zebras)

        for lion in self.manager.lions:
            new_lion = lion.lion_breed(self.grid)
            if new_lion:
                new_lions.append(new_lion)
                self.manager.num_lions += 1
        self.manager.lions.extend(new_lions)

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.move_animals()
            self.breed_animals()
            self.display()
            #os.system('cls')
 

if __name__ == '__main__':
    safari = CircleOfLife(5, 5, 2)
    safari.run(1000)