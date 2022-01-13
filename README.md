#TODO some more refining the language and tone - should be a bit more formal

# (1) INTRODUCTION
	(1.1) PROJECT AIMS AND OBJECTIVES:
		The project aims and objectives that will be achieved after completion of this project are discussed in this subchapter.
		The aims and objectives are as follows:
			- Billing Interface
			- Drug Management
			- Report Analysis
			#TODO should be like "to create a billing interface for carrying out transanctions easily"
		
	(1.2) BACKGROUND OF THE PROJECT:
		Our pharmacy billing and inventory management system - SED Pharma is a system
		that can be used for keeping track of pharmaceutical items that we currently
		have in stock, manually update them, get reports periodically as well as a
		fully working command line interface for purchasing items by prescription or as
		a bulk order. We have built a beautiful tabular UI that makes it very easy to
		display large amounts of data systematically. There are modules which can be
		used for checking purchase history or any other logs. This system eliminates
		the need to use manual work such as manual logging, manually updating excel
		sheets etc. and implements an all in one solultion which is tightly
		incorporated into our billing system and works flawlessly with exceptionally
		good error handling.
	
# (2) SYSTEM ANALYSIS
	In this section, we would be discussing and analyzing about the developing
	process of Pharmacy Billing and Inventory Management System including
	software requirement specification (SRS) and comparison between existing
	and proposed system. The functional and nonfunctional requirements are
	included in SRS part to  provide  complete  description  and  overview  of
	system  requirement  before  the  developing process is carried out.
	Besides that, existing vs proposed provides a view of how the proposed
	system will be more efficient than the existing one.
	
	(2.1) SOFTWARE REQUIREMENT SPECIFICATION:
		Pharmacy billing and inventory management system is a computerized
		system which helps the user (Pharmacist) to manage the daily activities
		in the pharmacy in an electronic format. It reduces the risk of paper
		work such as loss of registers, damage of registers and other time
		consuming activities in the pharmacy. It can help user to manage the
		transaction or record more effectively and in a time saving manner. 
		#TODO ippozhum books aayit aanu kedakkane change it to drugs stuff
		
	(2.2) PROBLEM STATEMENT:
		The problem occurred before having computerized system includes:
			- Loss of registers:
				If computerized system is not implemented, records are always
				under the threat of mishandling. There is a high chance of
				human error which can cause loss of records.
			- Damaged records:
				If a computerized system is not in existence, there is high risk of
				losing the records due to spilling of water by some members
				accidentally. Also natural disasters are a high threat to hard copy
				of records.
			- Difficult to search record:
				When hard copy of records are stored for a very long time it would
				become very difficult to search some particular record.
			- Space Consuming:
				When number of records start increasing, hard copy of those records
				could be space consuming.
			- Cost Consuming:
				When records are stored as hard copy, the hard copy records/registers
				would be required every year. This will increase the cost
				for management of a Pharmacy.
		#TODO ippozhum books aayit aanu kedakkane change it to drugs stuff

	(2.3) EXISTING VS PROPOSED:
		Existing System:
			Early day pharmacies are managed manually. It was time consuming as
			it needs a lot of time to record or retrieve the details. The
			pharmacist had to take their jobs very seriously as a small mistake
			could create a lot of problems. Also security of information is
			very less. Maintenance of Pharmacy catalogue and arrangement of
			books to the catalogue is a very complex task. In addition to its
			maintenance of member details, issue dates and return dates etc.
			manually is a complex task.
			#TODO ippozhum books aayit aanu kedakkane change it to drugs stuff
		Proposed System: 
			To solve the inconveniences as mentioned in the existing system, a
			Digital Library is proposed. The proposed system contains the following features:
				- Get medicine information
				- Check total medicines available
				- Update medicine details
				- Produce medicine reports, etc..
			#TODO ippozhum books aayit aanu kedakkane change it to drugs stuff
	
	(2.4) HARDWARE & SOFTWARE SPECIFICATIONS:
		The following is the specification of the system on which the software has been developed:
		System Specification:
			- Operating System: Linux, MacOS, Windows 7/10/11
				The software has been developed in Linux as it is very
				versatile and provides a wide variety of tools for testing
				and developing software. The software runs on almost all
				Unix, Unix-like and Windows systems with minimal dependancies and overheads.
			- Machine: Pentium Dual Core Processor 2.6 GHz or above, 2 GB
				RAM or above ,500 GB Hard Disk or above. We used Intel core
				i5 2nd generation based system, it is fast than other
				processors and provide reliable and stable performance and we
				can run our pc for longtime. By using this processor, we can
				keep on developing our project without any worries. 4GB RAM
				is used as it will provide fast reading and writing
				capabilities and will support in processing.
		Software Specification: 
			- Frontend used: Python 3.8+
			- Backend used: Data Files(Binary,CSV,Text)

# (3) SYSTEM DESIGN
	(3.1) DATA FILE/TABLE DESIGN:
		#TODO represent all .DB files in tabular/somewhat readable form	
		
	(3.2) MENU STRUCTURE:
			├── Billing
			│   ├── Bill Generation
			│   ├── Bulk Order
			│   │   └── Local File Scanning
			│   ├── Customer Data Store
			│   ├── Drug Search
			│   │   ├── Item Add
			│   │   └── Quantity Modifier
			│   └── Order Modification Page
			├── Inventory
			│   ├── Bulk Add
			│   │   └── Local File Scanning
			│   ├── Expired
			│   │   ├── Get Expired
			│   │   └── Remove Expired
			│   ├── Search and Edit
			│   │   ├── Edit Name
			│   │   ├── Edit Price
			│   │   └── Edit Qty
			│   └── View Inventory
			├── Management
			│   ├── Password Editor
			│   └── Tax Value Editor
			├── Reports
			│   ├── Drug Sales Charts
			│   └── Sales Report
			└── User History
				├── Search by Date
				└── Search by User
				
	(3.3) DATA FLOW DIAGRAMS
		#TODO psycho artistic skill poratherakk
		
# (4) SYSTEM IMPLEMENTATION
	(4.1) SOURCE CODE AND MODULE DESCRIPTION
		#TODO first show modules like in 3.2 menu structure then give explanation and below that give source code snippet(split into small chunks)
	(4.2) SCREENSHOTS
		#TODO take screenshots in idle of working of the program
		
# (5) SYSTEM TESTING
	Software Testing is an empirical investigation conducted to provide
	stakeholders with information about the quality of the product, with
	respect to the context in which it is intended to operate. Software Testing
	also provides an objective, independent view of the software to allow the
	management to appreciate and understand the risks during the implementation
	of the software. The aim of the system testing process was to determine all
	defects in our project. The program was subjected to a series of trial
	operations with test inputs and various observations were made and based on
	these observations, changes were made and again tested for better results.
	Our Project went through two levels of testing Unit testing and Integration testing.

	(5.1) UNIT TESTING:
		Unit testing was undertaken when a module has been created and successfully
		reviewed. In order to test a single module, we need to provide a complete
		working environment.
	(5.2) INTEGRATION TESTING:
		After integrating the entire modules developed, we performed various checks by
		providing different set of test input. The primary objective is to test all the
		modules in order to ensure that no errors are occurring when one module invokes
		the other module.

# (6) CONCLUSION
	The software for Pharmacy is found to be working efficiently. The software
	appears very flexible since it is menu driven with user-friendly screens.
	No Formal programming knowledge is required for the user. Also, the user is
	not burdened with data storing and data retrieval procedures as both are
	done internally. The user is able to manipulate data easily.
	
# (7) REFERENCES
	Learning Computer Science by Sumita Arora
	sed by Neville Joseph Sabu
	Mainly referred MJ's Brain
	Psycho's Artistic skills
	John F Aradan and Akarsh's Silence
	Prxni's Motivation