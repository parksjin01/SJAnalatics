import tensorflow as tf
import numpy as np
import cPickle

with open('../Crawling/dataset', 'rb') as f:
    result, cont = cPickle.load(f)

# result = tf.one_hot(result, 2, dtype=np.float32)
tmp = result[::]
result = []
for i in tmp:
    result.append([i])
result = np.array(result)
content = []
for line in cont:
    tmp = []
    for num in line:
        num = num.replace(',', '')
        tmp.append(float(num))
    content.append(tmp+[0]*(199-len(tmp)))
content = np.array(content)

train_set = [result[100:], content[100:]]
test_set = [result[:100], content[:100]]

x_data = content[100:]
y_data = result[100:]
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([199, 199]))
b1 = tf.Variable(tf.random_normal([199]))
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W3 = tf.Variable(tf.random_normal([199, 199]))
b3 = tf.Variable(tf.random_normal([199]))
layer2 = tf.sigmoid(tf.matmul(layer1, W3)+b3)

W4 = tf.Variable(tf.random_normal([199, 199]))
b4 = tf.Variable(tf.random_normal([199]))
layer3 = tf.sigmoid(tf.matmul(layer2, W4)+b4)

# W5 = tf.Variable(tf.random_normal([199, 199]))
# b5 = tf.Variable(tf.random_normal([199]))
# layer4 = tf.sigmoid(tf.matmul(layer3, W5)+b5)
#
# W6 = tf.Variable(tf.random_normal([199, 199]))
# b6 = tf.Variable(tf.random_normal([199]))
# layer5 = tf.sigmoid(tf.matmul(layer4, W6)+b6)

W2 = tf.Variable(tf.random_normal([199, 1]), name='weight2')
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
                      feed_dict={X: content[:100], Y: result[:100]})
   print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)

# x = tf.placeholder(tf.float32, [None, 199])
# y_ = tf.placeholder(tf.float32, [None, 1])
#
# w = tf.Variable(tf.random_normal([199, 1]))
# b = tf.Variable(tf.random_normal([1]))
# y = tf.nn.relu(tf.matmul(x, w)+b)
#
# cost = -tf.reduce_mean(y_ * tf.log(y) + (1 - y_) * tf.log(1 - y))
# train = tf.train.GradientDescentOptimizer(0.1).minimize(cost)
#
# predicted = tf.cast(y > 0.5, dtype=tf.float32)
# accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y_), dtype=tf.float32))
#
# init = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init)
#     for i in range(10000):
#         batch_y, batch_x = train_set
#         if i%2000 == 0:
#             print i
#             print(sess.run((y[:10]), feed_dict={x:batch_x, y_:batch_y}))
#         # print batch_x.shape, batch_x.dtype
#         # print batch_y.eval()
#         # print batch_x
#         sess.run(train, feed_dict={x:batch_x, y_:batch_y})
#
#     # prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
#     # accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
#     print ('Accuracy:', sess.run((accuracy, y, y_), feed_dict={x:test_set[1], y_:test_set[0]}))