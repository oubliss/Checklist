from utils import UI
import pickle


class Admin(UI):
    def __init__(self):
        self.step_index = -1
        self.to_do = ['choose_list']
        print("Welcome to the Admin menu! To return to the flight checklist, \n"
              "restart the program. If you make a mistake, just enter \"!\" \n"
              "to go back a step.")
        while(True):
            self.step()

    def step(self):
        self.step_index += 1
        self.__getattribute__(self.to_do[self.step_index])()

    def choose_list(self):
        options = {'Platforms (i.e. N###UA_Colloqiual_Name)': "platforms",
                   'General Locations (i.e. Colorado)': "groups",
                   'Specific Locations (i.e. ABC City Park)': "locations",
                   'Objectives (i.e. Photogrametry)': "objectives"}
        message = "What would you like to edit?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def platforms(self):
        options = {'Add': "platforms_add",
                   'Remove': "platforms_remove",
                   'Reorder': "platforms_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def platforms_add(self):
        old_dict = pickle.load(open("ndict.pkl", "rb"))
        print(list(old_dict.keys()))
        add = self.no_commas("Is your platform in this list? (y/n)")
        while add.lower() not in ["y", "n"]:
            add = self.no_commas("Enter y or n")
        if add not in "Yesyes":
            self.back()

        name = self.no_commas("Enter the name of your platform in the format "
                              "N###UA_Colloqiual_Name")
        scoop = self.no_commas("Does this platform have an interchangeable "
                               "scoop?")
        while scoop.lower() not in ["y", "n"]:
            scoop = self.no_commas("Enter y or n")

        if scoop in "Yesyes":
            scoop = True
        else:
            scoop = False

        old_dict[name] = scoop
        pickle.dump(old_dict, open("ndict.pkl", "wb"))
        print("Platform " + name + " has been added.")
        self.back()

    def platforms_remove(self):
        old_dict = pickle.load(open("ndict.pkl", "rb"))
        to_remove = self.get_index(list(old_dict.keys()),
                                   message="Which platform would you like to "
                                           "remove?", free_response=False)
        old_dict.pop(to_remove)
        pickle.dump(old_dict, open("ndict.pkl", "wb"))
        print("Platform " + to_remove + " has been removed.")
        self.back()

    def platforms_reorder(self):
        old_dict = pickle.load(open("ndict.pkl", "rb"))
        keys = list(old_dict.keys())
        print("Here is the current order of the platforms: ")
        for i in range(len(keys)):
            print(str(i+1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the platform you want listed first and ending with the "
              "one you want listed last.")
        new_dict = {}
        while len(old_dict.keys()) > 0:
            print("\tRemaining: " + str(list(old_dict.keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_dict[keys[next_elem-1]] = old_dict.pop(keys[next_elem-1])

        pickle.dump(new_dict, open('ndict.pkl', 'wb'))
        self.back()

    def groups(self):
        pass

    def locations(self):
        pass

    def objectives(self):
        pass
