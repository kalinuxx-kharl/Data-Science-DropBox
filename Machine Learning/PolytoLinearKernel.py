from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#Makes concentric circles
points, labels = make_circles(n_samples=300, factor=.2, noise=.05, random_state = 1)

#Makes training set and validation set.
training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)

classifier = SVC(kernel = "linear", random_state = 1)
classifier.fit(training_data, training_labels)
print(classifier.score(validation_data, validation_labels))

print(training_data[0])
new_training = []
new_validation = []
for point in training_data:
  new_training.append([2 ** 0.5 * point[0] * point[1], point[0] ** 2, point[1] ** 2])
  
for point in validation_data:
  new_validation.append([2 ** 0.5 * point[0] * point[1], point[0] ** 2, point[1] ** 2])
  
classifier.fit(new_training,training_labels)
print(classifier.score(new_validation,validation_labels))




