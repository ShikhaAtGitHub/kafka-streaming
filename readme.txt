Please Note: publisher.py and subscriber.py are part of Google pub/sub and producer.py for Kafka. 
For Part 1 Solution refer assignment_vectorai.py file or refer to the colab url provided at the top of the file.

1) Train CNN based model and save the model to be used in real-time predictions.
2) Now to generate a fake streaming data we can either use Google pub/sub or Kafka.
3) Once the kafka server is up and running, we create a topic which is responsible for storing the data coming from producers/publishers.
4) Consumer/subscribers subscribes to the topic to pull the data that could be analyse by the model(in our case predict the class).

Solution:
producer.py: responsible for producing/faking the data(the same data which we have used to train our model), it basically loads the saved data and serialises it before sending
it to the topic.

consumer.py: responsible for sequentially retrieving the data from the topic, this wrapped function in turn deserialises(from bytes to its original format) the data.
Once the data is fetched from the topic, it loads the saved cnn model and predicts on test data.

