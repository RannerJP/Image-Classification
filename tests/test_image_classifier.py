import os
import unittest
from image_classifier import ImageClassifier
from PIL import Image
from keras.models import load_model


class TestImageClassifier(unittest.TestCase):
    def test_valid_model_and_image(self):
        model = load_model(os.path.join('models', 'DogClassification.h5'))
        classifier = ImageClassifier(model)
        image = Image.open("assets/Valid_Image.jpg")
        image = image.resize((256,256))
        predicdition = classifier.get_prediction()
        self.assertIn(predicdition, [-1] + list(range(1,11)))

        