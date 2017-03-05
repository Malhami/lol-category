from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import numpy as np

from dataset_io import read_csv
from transform_data import z_score
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
#data = z_score(data)
data = StandardScaler().fit_transform(data)

def db_scan(data, metric):
  dbscan = DBSCAN(eps=0.8, min_samples=14, metric=metric).fit(data)
  print 'DBSCAN'
  #print dbscan.labels_
  print metrics.silhouette_score(data, dbscan.labels_)
  print collections.Counter(dbscan.labels_)
  reduced_data = reduce_with_pca(data)
  plot_2d_data(reduced_data, dbscan.labels_)

db_scan(np.array(data), 'euclidean')
print 'Data shape'
print data.shape
