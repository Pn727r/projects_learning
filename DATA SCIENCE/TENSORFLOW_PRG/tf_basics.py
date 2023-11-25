#programming elements

# constant 
# variable
# placeholder
#sparse tensor

# constant : creates a constant tensor from a tensor-like object
# tf.constant() # can't be changable

#variable : variable allow us to add new trainable parameters to a graph
# tf.variable() # value + data type

# placeholder : placeholders allow us to feed data to a tensorflow model from outside a model
# tf.placeholder() 

#sparse tensor : enable efficient storage and processing of tensor that contain a lot of Zero values to optimize calculation
# tf.SparseTensor()


import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))
  