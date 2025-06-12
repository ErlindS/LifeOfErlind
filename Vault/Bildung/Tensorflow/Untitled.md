Agenda:
P 18, 19 - What are Tensors -> Multidimensional Arrays -> Not Changable
		z = tf.constant(0)
P 20 Changable Tensor -> a = tf.Variable() -> can assign Content a.assign


P22 - 25 filling of data

P 22, 23 Random Tensors random = tf.random.Generator.from_seed(42)
		    t = random.normal([3])
		    t = random.normal([3,3], mean=4.0, stddev=0.01)
		    t = random.uniform([2], dtype=tf.int32, minval=42, maxval=1024)
P 24		    tf.random.set_seed(12)
		    a = tf.constant([1,2,3,4,5,6,7])
		    b = tf.random.shuffle(a, seed=4)
P 25		    tf.ones((1, 2, 3))

Sum: 9 Commands

P 25 - 35 Operations on Tensors

P 36 - 42 Basic Operations

P 42 - 50 Operations on Tensors


