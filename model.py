# recreate final model
import tensorflow as tf
from tensorflow.keras import layers, applications, Model

def create_model():
    input_shape = (224, 224, 3)
    base_model = applications.EfficientNetB0(include_top=False)

    inputs = layers.Input(shape=input_shape)
    x = base_model(inputs)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(101, activation="softmax")(x)

    return Model(inputs, outputs, name="food_detector")


def compile_model(saved_model):
    saved_model.compile(
      optimizer=tf.optimizers.Adam(0.0001),
      loss='sparse_categorical_crossentropy',
      metrics=['accuracy'])
    saved_model.load_weights("model_checkpoints/checkpoint.ckpt")
    return saved_model


def load_saved_model():
    return tf.keras.models.load_model("models/food_detector")

