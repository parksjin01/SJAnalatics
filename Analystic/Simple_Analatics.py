# -*- encoding:utf-8 -*-

# 수익률: 3%이상인 모델: 약 94%의 정확도
# 수익률: 2%이상인 모델: 약 90%의 정확도
# 수익률: 1%이상인 모델: 약 81%의 정확도
# 손해율: 1%이상인 모델: 약 64%의 정확도
# 손해율: 2%이상인 모델: 약 80%의 정확도
# 손해율: 3%이상인 모델: 약 88%의 정확도

import tensorflow as tf
import numpy as np
import cPickle

def preprocess_dataset(data):
    dataset = data[0]+data[1]+data[2]+data[3]
    result = []
    content = []
    for data in dataset:
        for idx in range(len(data)/60+1):
            try:
                tmp_period = data[idx*60+3:idx*60+60+3]
            except:
                continue
            period = []
            for num in tmp_period:
                period.append(float(num.replace(',', '')))
            if len(period) < 60:
                period += [0.0]*(60-len(period))
            if float(data[idx*60].replace(',', '')) < period[0]*0.97:
                result.append([1])
            else:
                result.append([0])
            content.append(period)
    return np.array(result), np.array(content)


with open('../Util/dataset', 'rb') as f:
    data = cPickle.load(f)

result, content = preprocess_dataset(data)
# print list(result).count([1])
# print len(result)
# exit(0)
train_set = [result[2000:], content[2000:]]
test_set = [result[:2000], content[:2000]]

x_data = train_set[1]
y_data = train_set[0]
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([60, 60]))
b1 = tf.Variable(tf.random_normal([60]))
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W3 = tf.Variable(tf.random_normal([60, 60]))
b3 = tf.Variable(tf.random_normal([60]))
layer2 = tf.sigmoid(tf.matmul(layer1, W3)+b3)

W4 = tf.Variable(tf.random_normal([60, 60]))
b4 = tf.Variable(tf.random_normal([60]))
layer3 = tf.sigmoid(tf.matmul(layer2, W4)+b4)

W2 = tf.Variable(tf.random_normal([60, 1]), name='weight2')
b2 = tf.Variable(tf.random_normal([1]), name='bias2')
hypothesis = tf.sigmoid(tf.matmul(layer3, W2) + b2)

# cost/loss function
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
# Accuracy computation
# True if hypothesis>0.5 else False
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
# Launch graph
with tf.Session() as sess:
   # Initialize TensorFlow variables
   sess.run(tf.global_variables_initializer())
   for step in range(10001):
       sess.run(train, feed_dict={X: x_data, Y: y_data})
       if step % 100 == 0:
           print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run([W2]))

   # Accuracy report
   h, c, a = sess.run([hypothesis, predicted, accuracy],
                      feed_dict={X: test_set[1], Y: test_set[0]})
   print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)

print list(test_set[0]).count([1])