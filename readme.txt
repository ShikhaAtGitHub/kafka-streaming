For Part 1 Solution refer assignment_vectorai.py file or refer to the colab url provided at the top of the file.

1) Train CNN based model and save the model to be used in real-time predictions.
2) Now to generate a fake streaming data we can use Kafka.
3) Once the kafka server is up and running, we create a topic(in our case: 'my_kafka_topic') which is responsible for storing the data pushed from producer.
4) Consumer subscribes to the topic to pull the data that could be analyse by the model(in our case predict the class).

Solution:
producer.py: responsible for producing/faking the data(the same data which we have used to train our model), it basically loads the saved data and serialises it before sending it to the topic. In our case we are trying to stream the test_data to our topic.

consumer.py: responsible for sequentially retrieving the data from the topic, this wrapped function in turn deserialises(from bytes to its original format) the data.
Once the data is fetched from the topic, it loads the saved cnn model, converts the shape of the pulled data from the topic to its original format the feeds the data into our trained model to predicts the classes.

USAGE:
1) Dump the trained cnn model in joblib format.
2) Install Zookeeper and kafka into your system using docker.
3) Install kafka-python in your working directory.
4) Create a topic('my_kafka_topic') >>> kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic my_kafka_topic
5) Start zookeeper and kafka from Docker Desktop.
6) Start running producer.py file by executing >>> python3 producer.py
7) Start running consumer.py file by executing >>> python3 consumer.py
8) You will see the model real-time prediction.
