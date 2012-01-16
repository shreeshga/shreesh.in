.. title:: SQLAlchemy  
.. author:: Shreesh
.. time:: 20:13
.. updated:: 2011-03-23 05:23
.. timezone:: UTC
.. feed:: all
.. copyright:: Creative Commons Attribution 3.0 Unported

Me no wants mySQL statements 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ORM simply put;lets you define classes which get mapped to tables(relations) in
[my]SQL. Thats perfect If you are used to working with classes in C++ as
I am. You just define class and add class members which correspond to
the attributes of a table. The Fun part is, you can use inheritance to
map related tables.

I use `Flask <http://flask.pocoo.org/>`_ as my Web Framework. Armin has
written a convenient wrapper FLask\_SQLAlchemy. It takes away many of
the headaches of using SQLAlchemy and gives a single class interface.

User Activity Table
-----------------------------

Say you want to create a table called 'useractivity' which every user
activity. But usually there can be more than one 'type' of user
activity, like user checking into a place OR user making a comment on a
checking. So, In OO methodology, We need a generic UserActivity class;
and two derived classes: PlaceActivity and ConversationActivity. You
would declare the following classes:


.. sourcecode:: python

    class UserActivity(db.Model):
        __tablename__ = 'useractivity'
        id = db.Column(db.Integer,primary_key=True)
        user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
        type = db.Column(db.String(100), nullable=False)
        date_time = db.Column(db.DateTime)
        message = db.Column(db.String(2000))
        lat = db.Column(db.Float)
        lng = db.Column(db.Float)
        __mapper_args__ = {'polymorphic_on': type}
    class PlaceActivity(UserActivity):
        __tablename__ = None
        __mapper_args__ = {'polymorphic_identity': 'place'}
        __public__ = ['id','user_id','type','type_id','date_time','points','message','lat','lng']
        place_type = db.Column(db.Integer,db.ForeignKey('placetype.id'))
        place_id = db.Column(db.Integer)
        place_points = db.Column(db.Integer)
        def __init__(self,user_id=None,place_id=None,date_time=None,lat=None,lng=None,message=None):
            UserActivity.__init__(self,user_id,date_time,lat,lng,message)
            self.place_id = place_id
            self.place_type = Place.query.filter_by(id=place_id).first().type_id
            self.place_points = PlaceType.query.filter_by(id=self.place_type).first().points
    class ConversationActivity(UserActivity):
        __tablename__ = None
        __mapper_args__ = {'polymorphic_identity': 'conversation'}
        __public__ = ['id','user_id','type','type_id','date_time','points','message','lat','lng']
        conv_type = db.Column(db.Integer,db.ForeignKey('convotypes.id'))
        conv_id = db.Column(db.Integer)
        conv_points = db.Column(db.Integer)
        conv_result = db.Column(db.Integer)
        def __init__(self,user_id=None,conv_id=None,result=None,date_time=None,lat=None,lng=None,message=None):
            UserActivity.__init__(self,user_id,date_time,lat,lng,message)
            self.conv_id = conv_id
            self.conv_result = result
            self.conv_type = Conversation.query.filter_by(id=conv_id).first().type_id
            self.conv_points  = ConversationType.query.filter_by(id=self.conv_type).first().points

(I have omitted unrelated classes like ConversationType and PlaceType).
The key lines here is:

.. sourcecode:: python

    __mapper_args__ = {'polymorphic_identity': 'conversation'}
    __mapper_args__ = {'polymorphic_identity': 'place'}

ORM works by 'mapping' user defined classes to the database tables. By
default, the class members are made table attributes with the variable
names as the attribute name. In the above table we are trying to make
the attribute 'type' polymorphic i.e the variable value will depend on
the class object its called from.

So, Now you can insert either a Conversation Or Place Activity

.. sourcecode:: python

    placeActivity = PlaceActivity(user.id,convert_int(place_id),date_time,convert_float(lat),convert_float(lng))
    convActivity = ConversationActivity(user.id,pickupline_id,result,date_time,None,None,None)

Neat.

