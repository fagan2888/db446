-- select command

select CustomerProduct.cust_id, CustomerProduct.prod_id, 
		product.descr, CustomerProduct.qty, 
		CustomerProduct.timestamp
	from CustomerProduct inner join Product
			on CustomerProduct.prod_id = Product.prod_id

select a.cust_id, c.fname + ' ' + c.lname [full name],
		a.prod_id, 
		b.descr, b.price, a.qty, b.price * a.qty total,
		a.timestamp
	from CustomerProduct a inner join Product b
			on a.prod_id = b.prod_id 
			inner join customer c on a.cust_id = c.cust_id