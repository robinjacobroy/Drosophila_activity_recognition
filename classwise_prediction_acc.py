import tensorflow as tf
import pathlib
import numpy as np
import os

#class_names can be explicitly given if test_ds.classnames has diffent order than train_ds.class_names
#class_names = ['attempt_copulate', 'following', 'licking', 'wing_song']
img_height = 80
img_width = 80

test_ds = tf.keras.utils.image_dataset_from_directory(
  pathlib.Path('./to_predict/'),
  seed=123,
  #class_names=class_names,
  image_size=(img_height, img_width),
  #batch_size=1,
  shuffle=False)

class_names = test_ds.class_names

model = tf.keras.models.load_model("./best_model.h5")
predictions = model.predict(test_ds)
# Generate arg maxes for predictions
scores = tf.nn.softmax(predictions)
classes = np.argmax(scores, axis = 1)
print(classes)

predicted_labels = [class_names[i] for i in classes]
true_labels = [x.partition('/')[-1] for x in test_ds.file_paths]

occurrence = {item: 0 for item in set(predicted_labels)}
ctr = 0
for num, i in enumerate(zip(true_labels,predicted_labels)):

    true_label, fln = i[0].split('/')
    if true_label == i[1]:
        ctr+=1
        occurrence[true_label]+=1
    print(fln, true_label, i[1])
print("total corrent predictions=", ctr/(num+1))

labels = [x.split('/')[1] for x in test_ds.file_paths]
for i in set(labels):
    print(i, occurrence[i]/labels.count(i))
