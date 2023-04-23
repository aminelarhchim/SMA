from mesa import Model
from mesa.time import RandomActivation
from communication.preferences.Preferences import Preferences
from communication.agent.CommunicatingAgent import CommunicatingAgent
from communication.preferences.CriterionName import CriterionName
from communication.preferences.CriterionValue import CriterionValue
from communication.message.MessageService import MessageService
from communication.preferences.Value import Value
import random
from random import randint
list_criterion = [CriterionName.PRODUCTION_COST, CriterionName.ENVIRONMENT_IMPACT,
                  CriterionName.CONSUMPTION, CriterionName.DURABILITY,
                  CriterionName.NOISE]

class ArgumentAgent(CommunicatingAgent):
    """ ArgumentAgent which inherit from CommunicatingAgent .
    """
    def __init__(self , unique_id , model , name , preferences):
        super().__init__(unique_id , model , name , preferences)
        self.preference = preferences

    def step(self):
        super().step()

    def get_preference(self):
        return self.preference

    def generate_preferences(self , List_items,detail=False):
    # see question 3
        preferences = Preferences()
        # If the agent has not generated the preferences yet and if it is reading from a csv file

        preferences.set_criterion_name_list(list_criterion)
        for item in List_items:
            for criterion in list_criterion:
                random = randint(0, 4)
                preferences.add_criterion_value(CriterionValue(
                        item, criterion, Value.matchvalue(random)))
                if detail:
                    print(item, criterion, Value.matchvalue(random))

        self.preference = preferences

    
    

class ArgumentModel(Model):
    """ ArgumentModel which inherit from Model .
    """
    def __init__(self):
        self.schedule = RandomActivation(self)
        self.__messages_service = MessageService(self.schedule)

        # To be completed
        #
        # a = ArgumentAgent(id , " agent_name ")
        # a. generate_preferences(preferences)
        # self.schedule .add(a)
        # ...
        alice = ArgumentAgent(0, "Alice")
        alice.generate_preferences(self)
        self.schedule.add(alice)

        bob = ArgumentAgent(1, "Bob")
        bob.generate_preferences()
        self.schedule.add(bob)

    def step(self):
        self.__messages_service.dispatch_messages()
        self.schedule.step()


if __name__ == " __main__ ":
    argument_model = ArgumentModel()

# To be completed