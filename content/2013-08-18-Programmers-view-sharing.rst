:title: Programmer's View of Sharing  
:time: 21:30
:timezone: UTC
:author: shreesh
:updated: 2013-10-16 21:30
:category: tech,shorts

| Date: 2023-10-10
| State: Fix a bug in sharing module 
|

As i track down a bug in a legacy code, i am left wondering at the state of social sharing.  Somehow i feel this whole thing is broken.  Just have a look at the data strucuture:

.. code-block:: java
	
	public class Share {
		long 	lat,long;
		Ambience ambience;
		bytes[] odor;
		bytes[] view180;
		bytes[] audio;
	}

	public class Ambience {
		String temp;
		String chill;
		String humidity;
		String condition;
	}

No wonder experiecing a "share" from others is such a drain on senses.
Can't imagine people using this for a long time. 




