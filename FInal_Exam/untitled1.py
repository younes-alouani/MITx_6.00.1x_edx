class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        self.tents = [tent_loc]
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for tent in self.tents :
            if tent.dist_from(new_tent_loc) < 0.5 :
                return False
        self.tents.append(new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        try :
            self.tents.remove(tent_loc)
        except :
            raise ValueError
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        for i in range(len(self.tents) - 1):
            j=i+1
            while j < len(self.tents):
                if self.tents[i].getX() > self.tents[j].getX() :
                    temp = self.tents[i]
                    self.tents[i] = self.tents[j]
                    self.tents[j] = temp
                j += 1
            
        results = "["
        for index in range(len(self.tents)):
            if index == len(self.tents) - 1 :
                results += "'"+ self.tents[index].__str__()+"']"
            else :
                results += "'"+ self.tents[index].__str__() +"', "
        return results
