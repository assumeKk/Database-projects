/* Insert Data into category*/
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (1,'Programming','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (2,'Maths','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (3,'Biology','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (4,'Chemisty','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (5,'Music','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (6,'Physics','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (7,'Art','Non-fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (8,'Manga','fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (9,'Adventure','fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (10,'Horror Story','fiction');
INSERT INTO assignment.Category (CategoryID, Name, CategoryType)VALUES (11,'English','Non-fiction');

/* Insert Data into SalesRep*/
INSERT INTO assignment.SalesRep (SalesRepID, Name)VALUES (567,'Ben');
INSERT INTO assignment.SalesRep (SalesRepID, Name)VALUES (568,'Sam');
INSERT INTO assignment.SalesRep (SalesRepID, Name)VALUES (569,'John');
INSERT INTO assignment.SalesRep (SalesRepID, Name)VALUES (570,'Sean');
INSERT INTO assignment.SalesRep (SalesRepID, Name)VALUES (571,'Baokang');

/* Insert Data into Shop*/
INSERT INTO assignment.Shop (ShopID, Name)VALUES (100,'Best Books');
INSERT INTO assignment.Shop (ShopID, Name)VALUES (101,'Waterstone');
INSERT INTO assignment.Shop (ShopID, Name)VALUES (103,'WHSmith');

/* Insert Data into Publisher*/
INSERT INTO assignment.Publisher (PublisherID, Name)VALUES (200,'Arena Books');
INSERT INTO assignment.Publisher (PublisherID, Name)VALUES (201,'Janus Publishing');
INSERT INTO assignment.Publisher (PublisherID, Name)VALUES (202,'Pegasus Elliot');
INSERT INTO assignment.Publisher (PublisherID, Name)VALUES (203,'Kevin Maythe Publisher');
INSERT INTO assignment.Publisher (PublisherID, Name)VALUES (204,'Melrose Press Ltd');

/* Insert Data into Book*/
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (300,'Step Into Java','50.99',1,200);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (301,'Step Into C#','30.99',1,201);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (302,'Step Into Python','30.99',1,200);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (303,'Create Java Application','72.99',1,201);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (304,'Create C# Application','53.99',1,201);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (305,'Create Python Application','56.99',1,200);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (306,'Discrete Mathematic','49.99',2,202);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (307,'Algebra','25.99',2,202);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (308,'Linear','50.99',2,203);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (309,'Step Into Biology','50.99',3,202);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (310,'Step Into Chemisty','64.99',4,204);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (311,'How to play guita','50.99',5,202);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (312,'Physics for beginner','54.99',6,201);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (313,'Step into Art','30.99',7,202);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (314,'Naruto','10.99',8,204);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (315,'Adventure Story','20.99',9,203);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (316,'Saw','50.99',10,201);
INSERT INTO assignment.Book (BookID, Title, Price, CategoryID, PublisherID)VALUES (317,'ELTS','30.99',11,202);

/* Insert Data into ShopOrder*/
INSERT INTO assignment.ShopOrder (ShopOrderID, OrderDate, ShopID, SalesRepID)VALUES (400,'2015-12-01',100,567);
INSERT INTO assignment.ShopOrder (ShopOrderID, OrderDate, ShopID, SalesRepID)VALUES (401,'2015-11-15',101,568);
INSERT INTO assignment.ShopOrder (ShopOrderID, OrderDate, ShopID, SalesRepID)VALUES (403,'2015-12-29',103,569);
INSERT INTO assignment.ShopOrder (ShopOrderID, OrderDate, ShopID, SalesRepID)VALUES (404,'2014-12-29',103,569);
INSERT INTO assignment.ShopOrder (ShopOrderID, OrderDate, ShopID, SalesRepID)VALUES (406,'2014-12-30',103,569);

/* Insert Data into OrderLine*/
INSERT INTO assignment.OrderLine (ShopOrderID, BookID, Quantity, UnitSellingPrice)VALUES (400,300,3,'255.00');
INSERT INTO assignment.OrderLine (ShopOrderID, BookID, Quantity, UnitSellingPrice)VALUES (401,302,3,'20.00');
INSERT INTO assignment.OrderLine (ShopOrderID, BookID, Quantity, UnitSellingPrice)VALUES (403,305,3,'20.00');
INSERT INTO assignment.OrderLine (ShopOrderID, BookID, Quantity, UnitSellingPrice)VALUES (404,305,3,'26.00');
INSERT INTO assignment.OrderLine (ShopOrderID, BookID, Quantity, UnitSellingPrice)VALUES (406,305,3,'26.00');