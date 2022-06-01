##
## Exercise 1: Largest Puddle
##


class Puddle(object):
    def __init__(self):
        #A list of sets of coordinates that are in the puddle
        self.puddle_map = []
    
    def increase_puddle(self, x,y):
        #Add the point to the puddle
        if not self.check_puddle(x, y):
            self.puddle_map.append((x,y))

    def check_puddle(self, x,y):
        #If the point is in the puddle, return True
        #If the point is not in the puddle, return False
        for i in self.puddle_map:
            if i == (x,y):
                return True

    def get_puddle_map_as_string(self):
        #Return the puddle map as a string
        return str(self.puddle_map)

    def is_valid_puddle(self, size):
        #Return False if puddle contains point in coordinate zero or size-1
        #Return True if puddle does not contain point in coordinate zero or size-1
        if (0,0) in self.puddle_map:
            return False
        if (size-1,size-1) in self.puddle_map:
            return False
        for i in range(size):
            if (0,i) in self.puddle_map:
                return False
            if (i,0) in self.puddle_map:
                return False
            if (i,size-1) in self.puddle_map:
                return False
        return True

        
                    
                
# 		(y-1,x)
# (y,x-1)	_y,x_	(y,x+1)
# 		(y+1,x)



# - Olhar ponto
# - Se o ponto é menor que 5:
# 	- Se o ponto é vizinho de uma poça existente:
# 		- Verificar se o valor do ponto é menor ou igual aos vizinhos:
# 			- Incluir o ponto na poça
# 	- Senão, criar uma nova poça


            

    
class PuddleFinder(object):
    puddle_candidates = []

    def __init__(self,field):
        # Check if field is list
        if type(field) != list:
            raise TypeError("field must be a list")
        # Check if field is square
        if len(field) != len(field[0]):
            raise ValueError("field must be a square")
        # Check if field is list of ints
        for row in field:
            for point in row:
                if type(point) != int:
                    raise TypeError("field must be a list of ints")
        self.field = field
        self.size = len(field)
        self.puddle_candidates = []

    def check_field_for_puddles(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.field[y][x] < 5:
                    self.check_point(x,y)


    def check_point(self, x,y):
        #Check for neighbor points if there is in a puddle in puddle_candidates
        #If there is a neighbor puddle, append it to the puddle if the point is less than or equal to the neighbor
        #If there is not a neighbor puddle, create a new puddle_candidate
        #If there is a neighbor puddle, check if the point is less than or equal to the neighbor
        added_neighbor = False
        if neighbor_puddles := self.get_neighbor_puddles(x, y):
            for puddle in neighbor_puddles:
                for point in puddle.puddle_map:
                    if self.field[y][x] <= self.field[point[1]][point[0]]:
                        puddle.increase_puddle(x,y)
                        added_neighbor = True
            if not added_neighbor:
                self.puddle_candidates.append(Puddle())
                self.puddle_candidates[-1].increase_puddle(x,y)

        else:
            self.puddle_candidates.append(Puddle())
            self.puddle_candidates[-1].increase_puddle(x,y)

    
    def get_neighbor_puddles(self, x, y):
        #Return a list of neighbor puddles
        #Check if there is a puddle in puddle_candidates
        #If there is, check if the point is less than or equal to the neighbor
        #If there is not, create a new puddle_candidate
        neighbor_puddles = []
        for puddle in self.puddle_candidates:
            for p_y in range(y-1,y+1):
                neighbor_puddles.extend(puddle for p_x in range(x - 1, x + 1) if puddle.check_puddle(p_x, p_y))

        return neighbor_puddles
   

                
                    

def main():
    field = [ 
        [5, 5, 5, 5, 5, 2, 2], 
        [5, 4, 3, 3, 5, 2, 2], 
        [5, 3, 5, 3, 5, 2, 2], 
        [5, 5, 5, 5, 5, 5, 2], 
        [5, 5, 5, 5, 2, 1, 5], 
        [5, 3, 2, 5, 1, 4, 5], 
        [5, 5, 2, 5, 5, 3, 5] 
    ]
    
    puddle_finder = PuddleFinder(field)
    puddle_finder.check_field_for_puddles()
    
    print_valid(puddle_finder)


    print_invalid(puddle_finder)

    print("---------------------")
    dist_puddles(puddle_finder)

    print("---------------------")
    valid_puddles(puddle_finder)

def valid_puddles(puddle_finder):
    print("Validity of puddles:")
    for y in range(puddle_finder.size):
        for x in range(puddle_finder.size):
            if puddle_finder.field[y][x] < 5:
                for n in range(len(puddle_finder.puddle_candidates)):
                    if puddle_finder.puddle_candidates[n].check_puddle(x,y):
                        if puddle_finder.puddle_candidates[n].is_valid_puddle(puddle_finder.size):
                            print("v", end="")
                        else:
                            print("i", end="")
            else:
                print("*", end="")
        print()

def dist_puddles(puddle_finder):
    print("Distribution of puddles:")
    for y in range(puddle_finder.size):
        for x in range(puddle_finder.size):
            if puddle_finder.field[y][x] < 5:
                for n in range(len(puddle_finder.puddle_candidates)):
                    if puddle_finder.puddle_candidates[n].check_puddle(x,y):
                        print(n,end="")
            else:
                print("*", end="")
        print()

def print_invalid(puddle_finder):
    print("Invalid puddles:")
    for puddle in puddle_finder.puddle_candidates:
        if not puddle.is_valid_puddle(puddle_finder.size):
            print(puddle.get_puddle_map_as_string())

def print_valid(puddle_finder):
    print("Valid puddles:")
    for puddle in puddle_finder.puddle_candidates:
        if puddle.is_valid_puddle(puddle_finder.size):
            print(puddle.get_puddle_map_as_string())

    
    


if __name__ == '__main__':
    main()