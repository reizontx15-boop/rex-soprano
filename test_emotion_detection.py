import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Teste para Alegria (Joy)
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')
        
        # Teste para Raiva (Anger)
        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')
        
        # Teste para Nojo (Disgust)
        res_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')
        
        # Teste para Tristeza (Sadness)
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')
        
        # Teste para Medo (Fear)
        res_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
