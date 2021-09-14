import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print('\nTest accuracy:', test_acc)

### 以下を追加 ##################################################
# モデルと重みの保存
import os
import shutil
import tarfile

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # ignore TensofFlow warnings

path = 'saved_model'
tarpath = '.'

if os.path.isdir(path):
    shutil.rmtree(path)
    
os.mkdir(path)
model.save(f'{path}/my_model')
if os.path.isfile(f'{path}/cnn'):
    os.remove(f'{path}/cnn')
    
with tarfile.open(f'{tarpath}/saved_model.tgz', 'w:gz') as tar:
    tar.add(path)
    