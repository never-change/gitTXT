



import odoorpc

odoo = odoorpc.ODOO('192.168.0.11')

odoo.login('odoo','1174809@qq.com','09090909')

print odoo.env.uid
print odoo.env.user
print 123

U = odoo.env['res.partner']

ids = U.search([('id','<',10)])
#[9, 19, 34, 24, 23, 8, 20, 18, 16, 21, 22, 15, 13, 31, 37, 30, 10, 25, 26, 36, 27, 11, 28, 29, 41, 40, 17, 35, 39, 12, 32, 33, 14, 38, 1, 3, 7, 6, 42, 43]

print U.name_get(ids)


