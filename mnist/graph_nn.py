import numpy as np
import matplotlib.pyplot as plt

training_size, nn_random = np.load('nn_random.npy')
nn_max_entropy = np.load('nn_max_entropy.npy')
nn_max_meanvar = np.load('nn_max_meanvar.npy')
nn_max_bald = np.load('nn_max_bald.npy')
nn_max_layer_bald = np.load('nn_max_layer_bald.npy')

fig, ax = plt.subplots(1, 1, figsize=(12, 9))

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# plt.xticks(range(300, 1201, 100), fontsize=14)
plt.yticks(range(0, 101, 1), fontsize=14)

plt.plot(training_size, nn_random, lw=1., color='#ff7f0e', label='random')
plt.plot(training_size, nn_max_entropy, lw=1., color='#1f77b4', label='maximum entropy')
plt.plot(training_size, nn_max_meanvar, lw=1., color='#aec7e8', label='maximum mean variance')
plt.plot(training_size, nn_max_bald, lw=1., color='#008000', label='maximum bald')
plt.plot(training_size, nn_max_layer_bald, lw=1., color='#ff0000', label='maximum layer bald')

plt.legend(bbox_to_anchor=(0.7, 0.1), loc=2, borderaxespad=0.)

plt.show()