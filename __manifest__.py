# -*- coding: utf-8 -*-
{
    'name': "Botón Crear Factura en Compras (MBA Consultings)",
    'version': "19.0.1.0.0",
    'category': "Purchases",
    'summary': "Restablece el botón directo 'Crear factura' en la orden de compra en Odoo 19",
    'author': "MBA Consultings, Brooks Gonzalez",
    'website': "https://mbaconsultings.com",
    'license': "LGPL-3",
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
