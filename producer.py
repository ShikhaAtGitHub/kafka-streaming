from tensorflow import keras
import base64
import time
import kafka
import msgpack
import msgpack_numpy as m

fashion_mnist = keras.datasets.fashion_mnist
(train_images_x, train_labels_y), (test_images_x, test_labels_y) = fashion_mnist.load_data()
print("test: ", (test_images_x.dtype))

producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'])

for (x, y) in zip(test_images_x, test_labels_y):
    x_enc = msgpack.packb(x, default=m.encode) # converting numpy array into bytes and sending it to topic(serialization)
    encoded_x = base64.encodebytes(x_enc) # encoding bytes into encoded string
    producer.send('my_kafka_topic', encoded_x)
    print('Sent to topic my_kafka_topic---------', encoded_x)
    time.sleep(2)