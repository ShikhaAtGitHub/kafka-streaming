import os
from kafka import KafkaConsumer
import msgpack
import msgpack_numpy as m
import numpy as np
import time
from joblib import load
import tensorflow as tf

model_path = os.path.abspath('./model/cnn_model.joblib')
clf = load(model_path)

# Kafka Consumer 
consumer = KafkaConsumer(
    'my_kafka_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

for message in consumer:
    x_return = np.frombuffer(message.value, dtype=np.uint8)
    print('x_return size', x_return.shape)
    # x_rec = msgpack.unpackb(message.value, object_hook=m.decode)
    x_shaped = np.array(x_return).reshape(1,28,28)
    prediction = np.argmax(clf.predict(x_shaped), axis=-1)  # it uses a softmax last-layer activation
    print('prediction-----', prediction)
    time.sleep(2)
