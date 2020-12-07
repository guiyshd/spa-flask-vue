import tensorflow as tf
from funmodel import gen_teste, proc_res


def load():
    try:
        model = tf.keras.models.load_model('pesos-5.tf')
        d = proc_res(model.predict(gen_teste('../uploads/image.png')))

        response = {'dic': d }
        
        print(response)
        return response

    except Exception as error:
        
        erro = { 'Error found' : error }
        print(erro)
        return erro


if __name__ == '__main__':
    load()