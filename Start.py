#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import sonnet as snt

#------------------
def main(unused_argv):
 # tf.logging.set_verbosity(3)  # Print INFO log messages.
    Start(unused_argv)

#------------------
def Start(args):
    count = len(args)
    if count ==  1: #Ex it on lack of args, (MInimum of two args from cmD line)         
        print("No arguments:, exiting " + str(count))
    else:     
        print("DNC starting Please wait...")
        return
#Against arguments create the data ty
def PrepareForDataFormat():    
    return

#Prep for setup of data feedback, this could be end point, GUI, file or console depending On args
def PrepareDisplayFeedback():
    return
#Prep for runtime type, invoke, train or update
def PrepareRunTime():
    return




##------------------
#Execute
if __name__ == "__main__":
  tf.app.run()