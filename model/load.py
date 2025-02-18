import numpy as np
from keras.models import model_from_json # type: ignore
# from scipy.misc import imread, imresize,imshow
import tensorflow as tf


def init():
    # Loading the model architecture
    json_file = open('model/model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    
    # load weights into new model
    loaded_model.load_weights("model/model.weights.h5")
    print("Loaded Model from disk")
    
    # compile and evaluate loaded model 
    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    
    # loss,accuracy = model.evaluate(X_test,y_test)
    # print('loss:', loss)
    # print('accuracy:', accuracy)
    # graph = tf.compat.v1.get_default_graph()
    
    return loaded_model #,graph