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

###Assumptions

These assumptions are derived from the top level requirements by analysis.  Others may make different assumptions, but these are the ones that make sense to me:

1. Cars may have one or more attributes - "Handicapped", "Electric", and "Compact". A car with no attributes is a full-sized, regular car. 

1. Spaces come in four types - "Regular", "Handicapped", "Electric", and "Compact". There are no handicapped spaces for electric vehicles, and all handicapped spaces accept full sized vehicles.   

1. Cars "park themselves" randomly into spaces governed by the following rules:

	1. Only cars with the "Handicapped" attribute may park in Handicapped spots.  

	1. Only cars with the "Electric" attribute may park in Electric spots. 

	1. Only cars with the "Compact" attribute may park in Compact spots. 

	1. Cars with the "Handicapped" attributes will not park themselves in non-handicapped spaces. 

	1. Cars with the "Electric" attribute may park themselves in non-electric spaces.

	1. Cars with the "Compact" attribute may park themselves in non-compact spaces.

	1. Cars with the "Electric" attribute prefer to park in electric spaces.

	1. Cars with the "Compact" attribute have no preference for compact spaces.
 
1. If a car cannot park itself it does not park itself. The car leaves and the park operation is ignored. Note that this may be true even if the parking lot has free spaces.

1. The structure of a parking lot is fixed. The inventory of spaces does not change during the run time of the parking lot instance.  

1. "Full" means full - no empty spaces exist. 

1. "Empty" means empty - no cars are parked at all.  While this is a trivial case with no practical meaning for cars looking for spaces it appears to be what the TLRs require. This implies that a parking lot that reports neither Full or Empty has some cars and some spaces. 
  
###Extensions

These extensions exceed the top level requirements, but they make the project more interesting and intuitive.  My solution will include them if they are not burdensom. (Given the 48 hours, I may revisit this decision.) 

1. The parking lot program may be implemented as a microservice with endpoints. 

1. The parking lot is actually a parking garage with multiple levels. Bookkeeping is done for each level. (In a real system, multiple garages could be supported by a server instance for each garage so level is sufficient.)

1. Cars have ids, and can be "unparked" with a DELETE /unpark operation that provides the id. 

##Approach

The parking lot is implemented as a Flask application.  This does not scale, as Flask instances are single threaded and blocking, but it does satisfy the requirements for a coding assignment. 

###Startup 

1. On boot, the server reads an input file to determine the inventory of the lot's spaces by type and level. 

1. The initial parking lot is empty.

###Endpoints 

1. A POST /park operation is supported that takes a Json car representation as the body of the request. It returns true if the operation is successful (the car parked itself), and false if the car decided to leave. 

1. A GET /full query returns true if there are no spaces.

1. A GET /empty query return true if no cars are parked in the lot. 

1. A GET /status query returns an overview of the free and occupied parking spaces, by level and type.  It does not include the car ids or any other detailed assignment of cars to spaces. 


