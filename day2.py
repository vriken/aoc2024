import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

with open('C:\\Users\\vrike\\Downloads\\input.txt', 'r') as file:
    sequences = [[int(x) for x in line.strip().split()] for line in file.readlines()]

# create features
def create_features(sequence):
    diffs = np.diff(sequence)
    return np.array([
        np.all(diffs > 0) or np.all(diffs < 0),  # monotonic
        np.all(np.abs(diffs) >= 1) and np.all(np.abs(diffs) <= 3)  # check differences
    ]).astype(int)

# training data
diffs = [np.diff(seq) for seq in sequences]
X = np.array([
    [np.all(diff > 0) or np.all(diff < 0), np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3)]
    for diff in diffs
]).astype(int)

y = np.array([
    int(np.all(diff > 0) or np.all(diff < 0)) and int(np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3))
    for diff in diffs
])

# train model
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=100, batch_size=32, verbose=1)

# predict
predictions = model.predict(X)
safe_count = int(np.sum(predictions > 0.5))

print(safe_count)