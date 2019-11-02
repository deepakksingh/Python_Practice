'''Without adapter pattern if we have different api/method for each object then we can check their instance type
    and then call respective apis/method"

---Implementation given below---

Disadvantage:
    There is a hardcoding of calling the api/method.
    Adding a new object needs changes.
    There is no uniform interface to call api/method.
'''
class HindiSpeaker:
    def kaise_ho(self):
        print("mein sirf hindi baat karta hoon")

class TeluguSpeaker:
    def ella_unnaru(self):
        print("Nēnu telugu mātramē māṭlāḍutunnānu")

class KannadaSpeaker:
    def heg_idiya(self):
        print("Nanu kannada matra matanaduttene")


# if __name__ == "__main__":
#     speakers = [
#         HindiSpeaker(),
#         KannadaSpeaker(),
#         TeluguSpeaker()
#     ]
#     for speaker in speakers:
#         if isinstance(speaker, HindiSpeaker):
#             speaker.kaise_ho()
        
#         elif isinstance(speaker, TeluguSpeaker):
#             speaker.ella_unnaru()

#         elif isinstance(speaker, KannadaSpeaker):
#             speaker.heg_idiya()
        
'''
Adapter Pattern: 
Approach 1
'''
class HindiSpeaker:
    def kaise_ho(self):
        print("mein sirf hindi baat karta hoon")

class HindiSpeakerAdapter:
    def __init__(self, hindi_speaker):
        self.hindi_speaker = hindi_speaker
    
    def speak(self):
        self.hindi_speaker.kaise_ho()


class TeluguSpeaker:
    def ella_unnaru(self):
        print("Nēnu telugu mātramē māṭlāḍutunnānu")

class TeluguSpeakerAdapter:
    def __init__(self, telugu_speaker):
        self.telugu_speaker = telugu_speaker
    
    def speak(self):
        self.telugu_speaker.ella_unnaru()


class KannadaSpeaker:
    def heg_idiya(self):
        print("Nanu kannada matra matanaduttene")
    
class KannadaSpeakerAdapter:
    def __init__(self, kannada_speaker):
        self.kannada_speaker = kannada_speaker
    
    def speak(self):
        self.kannada_speaker.heg_idiya()

# if __name__ == "__main__":
#     speakers = [
#         HindiSpeakerAdapter(HindiSpeaker()),
#         KannadaSpeakerAdapter(KannadaSpeaker()),
#         TeluguSpeakerAdapter(TeluguSpeaker())
#     ]

#     for speaker in speakers:
#         speaker.speak()

'''
Disadvantage of the above solution:
    We have to create a new adapter for each type of speaker
    Solution: Create a general adapter which works for any object.

'''

class SpeakerAdapter:
    _initialized = False

    def __init__(self, speaker_obj, **adapter_methods):
        self.speaker = speaker_obj

        for key, value in adapter_methods.items():
            func = getattr(self.speaker, value)
            self.__setattr__(key, func)
