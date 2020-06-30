

import json
import sys
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

sys.path.append('..')  # persistent import directory for K9 secrets

from k9secrets import IAMAuthenticatorKey, assistant_service_URL, assistant_id

class State(object):
    '''
    State parent class to support standard Python functions
    '''

    def __init__(self):
        print('Entering state:', str(self))

    def on_event(self, event):
        '''
        Incoming events processing is delegated to the child State
        to define and enable the valid state transitions.
        '''
        pass

    def run(self):
        '''
        Enable the state to do something - this is usually delegated
        to the child States)
        '''
        print('Run event for ' + str(self) + ' state not implemented')

    def __repr__(self):
        '''
        Leverages the __str__ method to describe the State.
        '''
        return self.__str__()

    def __str__(self):
        '''
        Returns the name of the State.
        '''
        return self.__class__.__name__


# Start K9 assistant states

class Observe(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))

    def run(self):
        # Can transition to Hotword via listen
        # Listens for MQTT events to change status
        # Waits for command to go into announcement mode 'make_announcement'
        # Waits for command to go into listen mode 'listen_for_hotword'
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'listen_for_hotword':
            return Hotword()
        if event == 'make_announcement':
            return Announce()
        return self

class Announce(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))

    def run(self):
        # Pulls announcements from a queue
        # Announces them and then returns
        k9.on_event('done')
        pass

    def on_event(self, event):
        if event == 'done':
            return Observe()
        return self

class Hotword(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # open microphone etc

    def run(self):
        # Can transition to Hotword via listen
        # k9.on_event('heard_name')
        pass

    def on_event(self, event):
        if event == 'heard_name':
            # close microphone etc
            return Get_Command()
        return self

class Get_Command(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # open the STT capability

    def run(self):
        # Do speech to text        # 
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'command_received':
            closeSTT()
            return Understand()
        if event == 'timeout':
            closeSTT()
            return Observe()
        if event === 'listen_off':
            closeSTT()
            return Observe()
        return self
    
    def closeSTT(self):
        # close STT

class Understand(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # creates session

    def run(self):
        # Talks to conversation
        # Work out what the action/response should be
        # k9.on_event('response_received')
        pass

    def on_event(self, event):
        if event == 'response_received':
            return Respond()
        return self

class Respond(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))

    def run(self):
        # Make things happen and use TTS
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'chess':
            return Chess()
        if event == 'move':
            return Move()
        if event == 'response_complete':
            return Get_Command()
        return self

class Move(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))

    def run(self):
        # Can transition to Hotword via listen
        # Listens for MQTT heartbeats
        pass

    def on_event(self, event):
        if event == 'stop_moving':
            return Observe()
        if event == 'timeout':
            return Observe()
        return self

class Chess(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # set up board
        # create sub-state

    def run(self):
        # starts game
        # end game
        pass

    def on_event(self, event):
        if event == 'game_done':
            return Get_Command()
        return self

# End K9 assistant states

class K9_Assistant(object):
    '''
    An assistant finite state machine that starts in waiting state and
    will transition to a new state on when a transition event occurs.
    It also supports a run command to enable each state to have its
    own specific behaviours
    '''

    def __init__(self):
        ''' Initialise the K9 assistant in its Waiting state. '''

        # Start with a default state.
        self.state = Waiting()

    def run(self):
        ''' State behavior is delegated to the current state'''

        self.state.run()

    def on_event(self, event):
        '''
        Incoming events are delegated to the current state, which then
        returns the next valid state.
        '''

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

# States for the sub-state Chess Game

class Setup_Board(State):

    '''
    Set up the board
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # set up board
        # create sub-state

    def run(self):
        # Can transition to Hotword via listen
        # Listens for MQTT events to change status
        # Waits for command to go into announcement mode 'make_announcement'
        # Waits for command to go into listen mode 'listen_for_hotword'
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'game_done':
            return Get_Command()
        return self

class White_Move(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # set up board
        # create sub-state

    def run(self):
        # Can transition to Hotword via listen
        # Listens for MQTT events to change status
        # Waits for command to go into announcement mode 'make_announcement'
        # Waits for command to go into listen mode 'listen_for_hotword'
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'game_done':
            return Get_Command()
        return self

class Black_Move(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # set up board
        # create sub-state

    def run(self):
        # Can transition to Hotword via listen
        # Listens for MQTT events to change status
        # Waits for command to go into announcement mode 'make_announcement'
        # Waits for command to go into listen mode 'listen_for_hotword'
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'game_done':
            return Get_Command()
        return self

class Endgame(State):

    '''
    The child state where the Dalek is scanning for faces, but appears dormant
    '''
    def __init__(self):
        print('Entering state:', str(self))
        # set up board
        # create sub-state

    def run(self):
        # Can transition to Hotword via listen
        # Listens for MQTT events to change status
        # Waits for command to go into announcement mode 'make_announcement'
        # Waits for command to go into listen mode 'listen_for_hotword'
        # k9.on_event('listen for hotword')
        pass

    def on_event(self, event):
        if event == 'game_done':
            return Get_Command()
        return self


class ChessGame(object):
    '''
    An assistant finite state machine that starts in waiting state and
    will transition to a new state on when a transition event occurs.
    It also supports a run command to enable each state to have its
    own specific behaviours
    '''

    def __init__(self):
        ''' Initialise the K9 assistant in its Waiting state. '''

        # Start with a default state.
        self.state = Setup()

    def run(self):
        ''' State behavior is delegated to the current state'''

        self.state.run()

    def on_event(self, event):
        '''
        Incoming events are delegated to the current state, which then
        returns the next valid state.
        '''

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)


authenticator = IAMAuthenticator(IAMAuthenticatorKey)
assistant = AssistantV2(
    version='2020-04-01',
    authenticator=authenticator)
assistant.set_service_url(assistant_service_URL)

# Create session
session = assistant.create_session(assistant_id).get_result()
print("Session established")

# Send text message
message = assistant.message(
    assistant_id,
    session["session_id"],
    input={'text': 'What is your purpose?'},
    context={
        'metadata': {
            'deployment': 'myDeployment'
        }
    }).get_result()

text = message["output"]["generic"][0]["text"]

print(text)
#print(json.dumps(message, indent=2))

assistant.delete_session(assistant_id, session["session_id"]).get_result()