import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)
  
def getConn():
    #function to retrieve the password, construct
    #the connection string, make a connection and return it.
    pwFile = open("pw.txt", "r")
    pw = pwFile.read();
    pwFile.close()
    connStr = "host='cmpstudb-01.cmp.uea.ac.uk' \
               dbname= 'dxe15gxu' user='dxe15gxu' password = " + pw
    #connStr=("dbname='studentdb' user='dbuser' password= 'dbPassword' " )
    conn=psycopg2.connect(connStr)          
    return  conn
               
@app.route('/')
def home(): 
    return render_template('index.html')
    #back to index page
@app.route('/add_new_category', methods =['POST'])   
def addCategory():
    #Add new category into category table'
    try:
        conn = None
        category_id = request.form['category_id']
        name = request.form['name']
        category_type = request.form['category_type']
        #request data from html form
        conn = getConn()
        cur = conn.cursor()
        cur.execute('SET search_path to assignment')
        #set default search path to schema named 'assignment'

        cur.execute('INSERT INTO Category VALUES (%s, %s, %s)', \
            [category_id, name, category_type])
        #excute insert query to add new data into category table

        conn.commit()
        return render_template('index.html', msg = 'New Category Added')
        #show message if category added else display error message
    except Exception as e:
        return render_template('index.html', msg = 'New Category NOT Added', error=e)
    finally:
        if conn:
            conn.close()

@app.route('/delete_category', methods = ['POST'])
def deleteCategory():
    #delete a record from database
    try:
        conn = None
        category_id = request.form['category_id']
        
        conn = getConn()
        cur = conn.cursor()
        cur.execute('SET search_path to assignment')
        #excute default path query
        cur.execute('DELETE FROM Category WHERE Category.CategoryID = %s', \
                    [category_id])
        #excute delete query
        conn.commit()
        return render_template('index.html', msg = 'Category Deleted')
        #if data deleted, show this message, else display error message
    except Exception as e:
        return render_template('index.html', msg = 'Category Delete Failed', error=e)
    finally:
        if conn:
            conn.close()

@app.route('/show_category', methods = ['GET'])
def displayCategory():
#show all categories
    conn=None
    try:
        conn = getConn()
        cur = conn.cursor()
        cur.execute('SET search_path to assignment')
        #set default path
        cur.execute('SELECT * FROM Category')
        #query to display everything in the category
        CategoryColName = [desc[0] for desc in cur.description]
        #column name variable store column name
        category = cur.fetchall()
        #variable category to store value from category table
        return render_template('show_category.html', category = category, \
                                    CategoryColName = CategoryColName)  
        #
    except Exception as e:
        return render_template('index.html', msg = 'Problem', error = e)
    finally:
        if conn:
            conn.close();

@app.route('/show_available_books', methods = ['GET'])
def show_available_books():
#display available book in stock
    conn=None
    try:
        conn = getConn()
        cur = conn.cursor()
        #use for first query
        cur1 = conn.cursor()
        #use for secon query
        cur.execute('SET search_path to assignment')
        #excute first default path query
        cur1.execute('SET search_path to assignment')
        #excute secon default path query
        cur.execute('SELECT categoryid, COUNT(*) AS "number of book", ROUND (AVG(price),2) AS average,\
                      SUM(price)AS "Total in Each Category"\
                    FROM assignment.book GROUP BY categoryid ORDER BY categoryid;')
        #excute first query to get books and store it in cur
        cur1.execute('SELECT COUNT(Book.BookID) AS "Total Of Books",SUM (price) AS "Total Price" FROM assignment.book;')
        #excute second query to get summary total of books
        availableColName = [desc[0] for desc in cur.description]
        #first query column variable
        available_books = cur.fetchall()
        #first query variable
        totalColName = [desc[0] for desc in cur1.description]
        #second query column varible
        available_books_summary = cur1.fetchall()
        #second query variable
        return render_template('show_available_books.html', available_books = available_books, \
                                    availableColName = availableColName, available_books_summary = available_books_summary, \
                                    totalColName = totalColName) 
        #display in show_available_books.html if successful, else display error message in index.html  
    except Exception as e:
        return render_template('index.html', msg = 'Problem', error = e)
    finally:
        if conn:
            conn.close();

     
@app.route('/publisher_report', methods = ['GET'])
def publisher_report():
#display publisher report
    try:
        conn = None
        publisher_name = request.args['publisher_name']
        #variable to store data from html form
        conn = getConn()
        cur = conn.cursor()
        cur.execute('SET search_path to assignment')
        #excute default search path query
        cur.execute('SELECT Publisher.PublisherID, Publisher.name, Book.BookID, Book.title,\
         OrderLine.Quantity, OrderLine.UnitSellingPrice,  ShopOrder.OrderDate,\
          OrderLine.UnitSellingPrice * OrderLine.Quantity AS "Order Value", \
          Book.Price * OrderLine.Quantity AS "Retail Value" \
          FROM assignment.Publisher,assignment.Book, assignment.OrderLine, assignment.ShopOrder \
          WHERE assignment.Publisher.name = %s \
          AND assignment.Publisher.PublisherID = assignment.Book.PublisherID \
          AND assignment.Book.BookID = assignment.OrderLine.BookID \
          AND assignment.ShopOrder.ShopOrderID = assignment.OrderLine.ShopOrderID \
          ORDER BY ShopOrder.OrderDate',\
          [publisher_name] )
        #excute report query
        publisherColName = [desc[0] for desc in cur.description]
        #variable to store column
        publisher_summary = cur.fetchall()
        #varibale to store report data
        return render_template('show_publisher_summary.html',  publisher_summary = publisher_summary, \
                                    publisherColName = publisherColName)
        #if successful, go to show_publisher_summary.html, else display error in index.html
    except Exception as e:
        return render_template('index.html', msg = 'Problem', error=e)
    finally:
        if conn:
            conn.close()

@app.route('/order_history', methods = ['GET'])
def order_history():
    #delete a record from database
    try:
        conn = None
        book_id = request.args['book_id']
        #varible to store data from html form
        conn = getConn()
        cur = conn.cursor()
        cur1 = conn.cursor()
        cur.execute('SET search_path to assignment')
        #excute first query
        cur1.execute('SET search_path to assignment')
        #excute second query
        cur.execute('SELECT ShopOrder.OrderDate, Book.title, Book.Price,\
                      OrderLine.UnitSellingPrice, OrderLine.Quantity,\
                      OrderLine.UnitSellingPrice * OrderLine.Quantity AS "Order Value", Shop.name\
                    FROM assignment.ShopOrder,\
                     assignment.Book,\
                     assignment.OrderLine,\
                     assignment.Shop\
                    WHERE Book.BookID = assignment.OrderLine.BookID\
                     AND assignment.OrderLine.ShopOrderID = assignment.ShopOrder.ShopOrderID\
                     AND assignment.Shop.ShopID = assignment.ShopOrder.ShopID\
                     AND assignment.Book.BookID = %s \
                    ORDER BY assignment.ShopOrder.OrderDate',\
                     [book_id] )
        #first query to store report data
        cur1.execute(' SELECT SUM(OrderLine.Quantity) AS "Total Quantity",\
                       SUM(OrderLine.UnitSellingPrice * OrderLine.Quantity) AS "Total Value"\
                      FROM assignment.OrderLine \
                      WHERE OrderLine.BookID = %s',\
                       [book_id] )
        #second query to store summary data for the report
        orderHistoryColName = [desc[0] for desc in cur.description]
        order_history = cur.fetchall()
        #first query varibles
        order_History_Summary_ColName = [desc[0] for desc in cur1.description]
        order_history_summary = cur1.fetchall()
        #second query varibles
        return render_template('show_order_history.html',  order_history = order_history, \
                                    orderHistoryColName = orderHistoryColName, order_history_summary = order_history_summary, \
                                    order_History_Summary_ColName = order_History_Summary_ColName)
        #go to show_order_history.html if successful, else display error in index.html
    except Exception as e:
        return render_template('index.html', msg = 'Problem', error=e)
    finally:
        if conn:
            conn.close()


@app.route('/sells_rep_report', methods = ['GET'])
def sells_rep_report():
#display sales rep report
    try:
        conn = None
        from_date = request.args['from_date']
        end_date = request.args['end_date']
        #get data from form and store them separately.
        #from_date is the begin date
        #end_date is the last date
        conn = getConn()
        cur = conn.cursor()
        cur.execute('SET search_path to assignment')
        #excute default path query
        cur.execute(' SELECT SalesRep.SalesRepID, SalesRep.name, \
                       COUNT(ShopOrder.ShopOrderID)AS "Total Order", \
                       SUM(OrderLine.Quantity)AS "Total Unit", \
                       SUM(OrderLine.UnitSellingPrice * OrderLine.Quantity) AS "Total Selling Price"\
                      FROM assignment.SalesRep\
                      LEFT OUTER JOIN assignment.ShopOrder\
                       ON SalesRep.SalesRepID = ShopOrder.SalesRepID\
                       AND ShopOrder.OrderDate BETWEEN %s AND %s \
                      LEFT OUTER JOIN assignment.OrderLine\
                       ON ShopOrder.ShopOrderID = OrderLine.ShopOrderID\
                       AND ShopOrder.OrderDate BETWEEN %s AND %s \
                      GROUP BY SalesRep.SalesRepID \
                      ORDER BY CASE WHEN SUM(OrderLine.Quantity * OrderLine.UnitSellingPrice) IS NULL THEN 1 ELSE 0 END,\
                      SUM(OrderLine.Quantity * OrderLine.UnitSellingPrice)',\
                       [from_date, end_date, from_date, end_date])
        #main query for sales rep report
        sells_rep_ColName = [desc[0] for desc in cur.description]
        sells_rep_report = cur.fetchall()
        #variable to store data from database
        return render_template('show_sellsrep_report.html',  sells_rep_report = sells_rep_report, \
                                    sells_rep_ColName = sells_rep_ColName)
    except Exception as e:
        return render_template('index.html', msg = 'Problem', error=e)
    finally:
        if conn:
            conn.close()

@app.route('/apply_discount', methods = ['POST'])
def apply_discount():
#apply discount for category by enter category ID
    try:
        conn = None
        category_id = request.form['category_id']
        #store category ID from html form
        discount = request.form['discount']
        #store discount value from html form

        conn = getConn()
        cur = conn.cursor()
        cur.execute('SET search_path to assignment')
        #default path query
        cur.execute('UPDATE assignment.Book\
                     SET Price = Price * %s/100\
                     WHERE Book.CategoryID = %s', \
                    [discount, category_id])
        #update query for apply the discount
        conn.commit()
        return render_template('index.html', msg = 'Discount applied')
    except Exception as e:
        return render_template('index.html', msg = 'Discount Apply Fail', error=e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(debug = True)