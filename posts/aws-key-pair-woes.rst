Getting locked out of AWS instance
------------------------------------

Each AWS instance is associated with a key pair. And if ever you decide to login from a different system,

Do this:

* create a new_volume.
* create a new_instance with a new_key pair.
* mount your original_volume (say /mnt/)
* Start your new_volume with new_instance.
* ssh into it with new_key pair and execute

.. sourcecode:: bash

    cat ~/.ssh/authorized_keys >> /mnt/home/<user>/.ssh/authorized_keys

* exit.
* stop your new_instace with new_volume
* start your original_instance with original_volume
* you are back in.

messy.
