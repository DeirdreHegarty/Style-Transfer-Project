# Machine Learning 


---

### NAME 

To be decided.


---

### AUTHORS

* Sean Keegan
* Sean Rooney
* Deirdre Hegarty


---

### INTRODUCTION

Our proposed project hopes to achieve style transfer between one image and another. 

The application needs 2 images - one content image and one style image. The
application will produce a mixed image where the contour lines are taken from
the content image and the textures and colour from the style image. These are
then mixed together to create a new image.


---

### METHODS

Start with random noise for the mixed image, send the content image, style
image and mixed image through the neural network. We then calculate different
loss function at different layers, and then weigh those different loss
functions. Take the gradient of these different loss functions, and use a
gradient to update the mixed image. This will be repeated a number of times
until a desired mixed image is created.

Two types of loss functions: content loss and style loss. 

Content loss will be at higher level layers. There will be a need to minimize
the difference between the activation features from the content image and from
the mixed image. Calculate features of that layer & the mean squared error =
the loss function for the content layer. We will want to minimize this error so
features activations in this layer are similar to that of the content image and
the mixed image.  The feature activations from the content image will be cached because
it will be the same each time we calculate them (reduce computation time).

Similar idea for the style layers, but calculate a gram matrix because we want
similarity between style image and the mixed image regarding features that are
activated together. Create style loss functions that will minimize the
difference between the gram matrix for multiple layers when inputing the style
and mixed images.



---

### MATERIALS

One team member will build a web scraper using Python. This web scraper will be
used to obtain a database of style images. Need a pre trained neural network VGG-16 model and python using Tensorflow. 


---

### EXPECTED RESULTS

Hopefully by the end of this project we will have produced an application that
provides opportunities for users to stylize images in accordance with a
specific painting/image. We aim to provide the best quality output image possible with our limited processing power and hope the style transfers are clearly recognsiable to the user.

At the very least our team will have learned skills including managing data,
working with a neural network, dealing with Tensorflow, and learning python.


---

### RISK ASSESSMENT

Because we will be processing a lot of images there may be issues with hardware
performance (fast GPU - take long time on CPU), this may also reduce the quality of the output image.

In order to achieve the optimal output image there will need to a high amount
of iterations. This process will take a lot of time and management. High
resolution images may need to be converted to low resolution to reduce
computational time.

---

### ACKNOWLEDGEMENTS

To be stumbled upon.


---

### STATEMENT

*We will keep all our source code in git and commit and push often and arrange
for Barack to have access to the repository.*

---









