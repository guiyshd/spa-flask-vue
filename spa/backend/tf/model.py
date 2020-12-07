import tensorflow as tf
from .funmodel import gen_teste, proc_res
import json


def load():
    try:
        model = tf.keras.models.load_model('backend/tf/pesos-5.tf')
        l = proc_res(model.predict(gen_teste('backend/uploads/image.png')))
        
        json_string = json.dumps([ob.__dict__ for ob in l])
        
        print(json_string)
        
        return json_string

    except Exception as error:
        
        erro = { 'Error found' : error }
        print(erro)
        return erro


if __name__ == '__main__':
    load()