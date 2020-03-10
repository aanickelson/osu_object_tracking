import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import mixture

mean = [0, 0]
cov = [[10,0.5], [0.5, 1]]

x, y = np.random.multivariate_normal(mean, cov, 5000).T
X_train = np.column_stack((x, y))
# print(X_train)

# generate zero centered stretched Gaussian data
# C = np.array([[0., -0.7], [3.5, .7]])
# stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)
# print(stretched_gaussian)
# concatenate the two datasets into the final training set
# X_train = np.vstack([shifted_gaussian, stretched_gaussian])

# fit a Gaussian Mixture Model with two components
clf = mixture.GaussianMixture(n_components=2, covariance_type='full')
clf.fit(X_train)

print(clf.covariances_)

# display predicted scores by the model as a contour plot
x = np.linspace(-20., 30.)
y = np.linspace(-20., 40.)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0),
                 levels=np.logspace(0, 3, 10))
CB = plt.colorbar(CS, shrink=0.8, extend='both')
plt.scatter(X_train[:, 0], X_train[:, 1], .8)

plt.title('Negative log-likelihood predicted by a GMM')
plt.axis('tight')
plt.show()