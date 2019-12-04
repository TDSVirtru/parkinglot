#Parking Lot

##Analysis

###Top Level Requirements

Design and write an OO program for a parking lot:

1. The program shall use OO techniques (be broken into logical classes and functions).

1. The program shall indicate to the user if the lot is full or empty. 

1. The program shall be able to handle regular, handicapped, electric and compact cars.

1. The program shall compile, run, and accept input sets (e.g. test vectors). 

1. The program may be written in Python.

1. Sample input sets shall be provided, with expected outputs, for evaluation purposes. 

###Assumptions and Analysis

These assumptions are derived from the top level requirements by analysis.  Others may make different assumptions, but these are the ones that make sense to me:

##### Atttributes

Attributes are implemented as subclasses of a base class "Attribute." This recruits the Python type system to impart a sort of permanance to the attribute.  In Python this does not guarantee type safe behavior, but it does make changing an attribute's type a bizzare and deliberate action that a normal programmer would not do. 

The Attributes embody the parking rules. Each Attribute supports two methods, Attribute.desires(Space) for attributes owned by cars, and Attribute.permits(Car) for attributes owned by spaces. For the three attributes in the TLRs - COMPACT, ELECTRIC, and HANDICAPPED - the current set of rules are:

1. For Space attribute use: Attribute.permits(Car) -> True, False
	1. Spaces with HANDICAPPED only accept cars with HANDICAPPED. 
	1. Spaces with ELECTRIC only accept cars with ELECTRIC.
	1. Spaces with COMPACT only accept cars with COMPACT.  
  
1. For Car attribute use: Attribute.desires(Space) -> PREFERS, ACCEPTS, REJECTS
	1. Cars with HANDICAPPED require spaces with HANDICAPPED. 
	1. Cars with ELECTRIC prefer spaces with ELECTRIC. 
	1. Cars with COMPACT do not prefer COMPACT spaces.

Embedding the rules for attributes in the attributes supports inversion of control, so this architecture ought to scale well with future growth of attributes (e.g., "Company X", "Employee of the month", "Expecting mothers"). 

Context is another area of possible growth.  For example, a Space attribute like "reserved for company X" might only be in effect during business hours, or a car attribute like "employee of the month for October" is only in effect when it is October.  Implementing this sort of context requires only a relatively trivial modification to the .permits and .desires methods. Injecting an optional "Context" object ought to do it. 

Although TLRs do not call out any interactions between attributes, in general this can happen with attribute based access control.  By passing the entire Car and Space object to the determination methods, whatever these future interactions might be, their solution can be handled internally and without external effects.  
  
##### Adjudicator 

The Adjudicator class encapsulates the business logic used to determine if a car can, and would like to, park in a space.  The Adjudicator object implements a single method, Adjudicator.is_match( car, space) that returns either None, ALLOWED, or PREFERRED.
 
Internally, the method is a generic runner of the Car and Space attribute methods that actually know the rules.  

This Adjudication process could be done with a pure function, however using an instance allows encapsulation of any future contexts required by the attribute methods.  A pure function would require this context to come in as part of the argument list, which pushes management of the context deeper into the code base. 

##### Cars

Cars may have one or more attributes. A car with no attributes is a full-sized, non-privileged car. 

Some of the attributes are immutable, e.g. COMPACT or ELECTRIC, while others may change during the lifetime of the Car instance. The HANDICAPPED attribute, for example, would apply if the car is driven by a handicapped person but not apply if the driver is able-bodied. 

An OO novice might try to fully subclass all cars as specific subtypes. This approach was not taken as it scales badly with increasing attributes.  Even with only three attributes there are eight theoretical subclasses - regular, handicapped, electric, compact, handicapped-electric, handicapped-compact, compact-electric, and handicapped-compact-electric.  Each requires code that must be maintained, so this approach is classic overengineering.

Also, since the HANDICAPPED attribute is a mutable property, the eight subclasses divide into four pairs. The mutable HANDICAPPED attribute ought to be handles as an optional property of the four types that embody the four pairs - regular, electric, compact, and compact-electric - but it does not resolve the fundamental problem of exponential growth in the number of classes. 

Another approach would be to use something like Scala traits to import the various attributes via multiple inheritance. This is not much better, as it does not resolve the basic problem of exponental growth in the code base. 

The most pragmatic approach is to have a single class that is passed a collection of attribute instances that contain the business logic. This inversion of control pattern is very flexible.

Attribute mutablity would be handled by adding and deleting mutable attribute instances from the attribute set.  For simplicity, and since mutablity is not in the requirements, the attribute sets for cars are implemented with immutable frozen sets. 

##### Park base class

Spaces, Rows, Levels, and Lots all share an "abstract" base class Park that parks cars. The following business logic is used by the park method:

1. Cars are parked in the first preferred space found. 

1. If no preferred space is found, the car is parked in the first permissible space found.   
	
1. If no permissible spaces was found then the park operation is aborted. (Note that this is likely to happen in non-full lots because ethical drivers obey the parking constraints.) 

1. "Full" means full - no empty spaces exist. 

1. "Empty" means empty - no cars are parked at all.  (While this is a trivial case it appears to be what the TLRs require.)

1. If a Park reports neither Full nor Empty then it has some parked cars and some free spaces. 

Lot, level, and row are nodes in a tree data structure with Spaces as the leaves. This offers an opportunity for implementing the parking operation in the base class and not the subclasses. They exist primarily to create the parking tree from a JSON manifest. 

##### Lot

A lot is an immutable set of levels.  It is also the root of the parking data structure that exposes the parking API. 

##### Level

A level is an immutable set of rows. 

##### Row

A row is an immutable list of spaces. 

##### Space 

A Space is a parking spot that may hold one Car. Spaces are either Empty or Full. Like Cars, Spaces have Attributes.  

The Space class is not subclassed. The rationalle for this is similar to the reasoning for Cars.  In a strongly typed language with support for multiple inheritance it could make sense to use the type system to differentiate behaviors, however there would be few benefits, and like Cars, there are significant combinatorics issues with growth in the number of attributes. 

From experience, there are very, very few cases where a Space has more than one attribute, however multiple attributes are possible so this option must be preserved. Spaces contain a set of attributes. 

The Space class accepts an array of Attribute instances on construction. This inversion of control is a powerful design pattern that is easily extended to support future growth. 

###Extensions

These extensions exceed the top level requirements, but they make the project more interesting and intuitive.  My solution will include them if they are not burdensom. (Given the 48 hours, I may revisit this decision.)  

1. Cars have ids, and can be "unparked" with a DELETE /unpark operation that provides the id. 
 