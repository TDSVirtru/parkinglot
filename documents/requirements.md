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

Both cars and spaces may posess attributes used to determine whether parking is feasible. 

Three attributes are in the TLRs - COMPACT, ELECTRIC, and HANDICAPPED.  More attributes are possible (e.g., "Company X", "Employee of the month", "Expecting mothers") so the architecture ought to scale well with additional attributes. 

Attributes are implemented as subclasses of a base class "Attribute." This recruits the Python type system to impart a sort of permanance to the attribute.  In Python this does not gurantee type safe behavior, but it does make changing an attribute's type a bizzare and deliberate action that a normal programmer would not do. 

##### Adjudicator 

The Adjudicator class contains the business logic used to determine if a car can, and would like to, park in a space.  

The Adjudicator object implements a class method "can_park( Car, Space) and returns either None (null in Python), ALLOWED, or PREFERRED, where the latter two are symbolic values. There TLRs do not call out any interactions between attributes, however in general Attributes sometimes interact. By passing the entire Car and Space objects can handle these interacting cases.  

Adjudication could be done with a pure function, however this limits support for possible context-sensitive Attributes in the future. The Adjuticator instance(s) are natural places to cache the current context.  A pure function would require this context to come in as part of the argument list. 

The Adjudicator.can_park(Car, Space) method implements the following rules:

1. Spaces with HANDICAPPED only accept cars with HANDICAPPED. 
1. Cars with HANDICAPPED require spaces with HANDICAPPED. 
1. Spaces with ELECTRIC only accept cars with ELECTRIC.  
1. Cars with ELECTRIC prefer spaces with ELECTRIC. 
1. Spaces with COMPACT only accept cars with COMPACT.  
1. Cars with COMPACT do not prefer COMPACT spaces.

##### Cars

Cars may have one or more of the attributes. A car with no attributes is a full-sized, non-privileged car. 

Some of the attributes are immutable properties of the car.  For example, a full sized car cannot become compact to fit into a compact space. Other attributes are mutable. A handicapped car may be driven by a handicapped driver one day and by an able-bodied driver the next. In the former case the car carries the "Handicapped" attribute, in the latter case it does not.   

An OO novice might try to fully subclass all cars into types. This is a mistake as it is unlikely to scale with increasing attributes.  With only three attributes there are eight theoretical subclasses of the base class "Car" - regular, handicapped, electric, compact, handicapped-electric, handicapped-compact, compact-electric, and handicapped-compact-electric. Subclassing this way would be extreme overengineering. 

Since the handicapped status is a mutable property of the car it should be a property of the base class, not a subclass. This improves the situation sligtly as it results in only four car types - regular, electric, compact, and compact-electric - but it does not resolve the fundamental problem.  If and when another attribute is desired the combinatorial explosion in the number of classes is limiting.

Multiple inheritance offers hope of a clean subclassing approach, however the parking behaviors for the different attributes may interact. In a language like Scala, with traits, there would be a good case for using the type system with multiple inheritance.  With Python there is no such advantage, so multiple inheritance was rejected as a design pattern. 

The most pragmatic approach in Python is to have a single class that carries an array of attribute instances that each support an Attribute.can\_park(car, space) method.  By off-loading the logic to the Attribute itself this inversion of control pattern is very flexible. 

Attribute mutablity is handled by adding and deleting mutable attribute instances from the attribute array.  Immutable attributes may not be added or deleted. 

##### Park base class

Spaces, Rows, Levels, and Lots all share an "abstract" base class Park that parks cars. The following business logic is used by the park method:

1. Cars park in the first preferred space found. 

1. If no preferred space is found, the car parks in the first permissible space.   
	
1. If no permissible spaces are found then the park operation is aborted. (Note that this is likely to happen in non-full lots because ethical drivers obey the parking constraints.) 

1. "Full" means full - no empty spaces exist. 

1. "Empty" means empty - no cars are parked at all.  (While this is a trivial case it appears to be what the TLRs require.)

1. If a Park reports neither Full nor Empty then it has some parked cars and some free spaces. 

##### Lot

A lot is an immutable set of levels. 

##### Level

A level is an immutable set of rows. 

##### Row

A row is an immutable list of spaces. 

##### Space 

A Space may hold one Car. Like Cars, Spaces have Attributes.  

1. Spaces may carry more than one attribute. 

1. The set of Attributes on a Parking space is immutable. 

From experience, there are very, very few cases where a Space has more than one attribute.  Handicapped spots are usually full sized, electric car spaces are rarely compact, and so on. However, it is possible, so this option must be preserved. 

The Space class is not subclassed. The rationalle for this is similar to the reasoning for Cars.  In a strongly typed language with support for multiple inheritance it could make sense to use the type system to differentiate behaviors, however there would be few benefits and there is a significant combinatorics issue with scale. 

The Space class accepts a number of Attribute instances on construction. This inversion of control is a powerful design pattern that is easily extended to support future growth.  Even context-sensitive Space attributes like "reserved for company X between 0600 and 1800 on weekdays" are easily implemented as the attribute instances hold this logic. 

###Extensions

These extensions exceed the top level requirements, but they make the project more interesting and intuitive.  My solution will include them if they are not burdensom. (Given the 48 hours, I may revisit this decision.)  

1. Cars have ids, and can be "unparked" with a DELETE /unpark operation that provides the id. 
 