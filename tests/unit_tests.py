import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_add_command(self):
        response = functions.get_chatbot_response("!! add 2 2")
        print(response)
        self.assertEquals(response, 4)
        
    def test_divide_command(self):
        response = functions.get_chatbot_response("!! divide 2 2")
        invalid_response = functions.get_chatbot_response("!! divide 5 0")
        print(response)
        self.assertEquals(response, 1)
        self.assertEquals(invalid_response, "Invalid number: 0 try another")
        
    def test_hey_command(self):
        response = functions.get_chatbot_response("!! Hey Deandra")
        print(response)
        self.assertEquals(response, "What's up!")
        
    def test_say_command(self):
        response = functions.get_chatbot_response("!! say Hey Hey ho ho")
        print(response, "Hey Hey ho ho")

if __name__ == '__main__':
    unittest.main()