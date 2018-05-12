#!/usr/bin/python
# -*- coding: UTF-8 -*-

import odoorpc

#连接odoo服务器
odoo = odoorpc.ODOO('192.168.0.107')

#查看可用数据库列表
print odoo.db.list()

#odoo账户登录
odoo.login('odoo','odoo@odoo.com','09090909')

#当前用户id
print odoo.env.uid

#当前用户，用户名,用户的公司名
user = odoo.env.user
print user
print user.name
print user.company_id.name

'''
#原始查询（好像是所有数据）
user_data = odoo.execute('res.users','read',[user.id])
print user_data
'''

#使用模型中的方法
'''
if 'res.partner' in odoo.env:
    Order = odoo.env['res.partner']
    order_ids = Order.search([])
    for order in Order.browse(order_ids):
        print order.name
        products = [line.product_id.name for line in order.order_line]
        print products
'''


U = odoo.env['res.partner']


#print U.search([])

ids = U.search([('id','<',10)])

ids1 = U.search([])
print ids1
print U.name_get(ids1)

#print ids

#print U.name_get([1,3])


print U.partner


