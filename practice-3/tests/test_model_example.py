import pytest

import model_example

class TestBirdClassifier:
    '''Test suite for bird classifier'''

    def test_result_range(self):
        assert model_example.pred_id < len(model_example.model.bird_classes)

    def test_result(self):
        assert model_example.my_bird_class == '153.Philadelphia_Vireo'
