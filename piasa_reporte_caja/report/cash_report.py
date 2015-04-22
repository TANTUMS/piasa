# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
import pooler
from itertools import chain
from openerp.report import report_sxw

class cash_report_acc(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        
        super(cash_report_acc, self).__init__(cr, uid, name, context=context)
        # u_name = context['user_id']
        invoice_ids = context['active_ids']
        self.localcontext.update({
            'time': time, 
            'start_date': context['start_date'],
            'end_date': context['end_date'],
            # 'user_name': u_name,
            'invoice_ids': context['active_ids'],
            'get_voucher_obj': self.get_voucher_obj,
            'get_total': self.get_total,
            'get_logo': self.get_logo,
            'facturas_contado':self.facturas_contado,
            'facturas_credito':self.facturas_credito,
        })
        
    def get_voucher_obj(self, invoice_ids):
        invoice_object = self.pool.get('account.invoice').browse(self.cr, self.uid,invoice_ids )
        return invoice_object
    
    def get_logo(self):
        cr = self.cr
        uid = self.uid
        company_ids = self.pool.get('res.company').search(cr, uid, [])
        if company_ids:
            company = self.pool.get('res.company').browse(cr, uid, company_ids[0])
            return company.logo
        return True
        
    def get_total(self,invoice_ids):
    
        sum = 0.00
        tax = 0.00
        subtotal = 0.00
        invoice_object = self.pool.get('account.invoice').browse(self.cr, self.uid,invoice_ids )
        for invoice_obj in invoice_object:
               sum += invoice_obj.amount_total
               tax += invoice_obj.amount_tax
               subtotal += invoice_obj.amount_untaxed
        return {'sum_tot': sum, 'sum_tax': tax, 'sum_untaxed': subtotal}


    def facturas_contado(self,invoice_ids):
        sum_contado=0.00
        tax_Contado = 0.00
        total_contado= 0.00
        invoice_object = self.pool.get('account.invoice').browse(self.cr, self.uid,invoice_ids )
        for invoice_obj in invoice_object:
            if invoice_obj.partner_id.property_payment_term.id == 1:
               sum_contado += invoice_obj.amount_untaxed
               tax_Contado += invoice_obj.amount_tax
               total_contado += invoice_obj.amount_total
        return {'contado': sum_contado, 'tax_contado': tax_Contado,'total_contado':total_contado}

    def facturas_credito(self,invoice_ids):
        sum_credito=0.00
        tax_credito = 0.00
        total_credito= 0.00
        invoice_object = self.pool.get('account.invoice').browse(self.cr, self.uid,invoice_ids )
        for invoice_obj in invoice_object:
            if invoice_obj.partner_id.property_payment_term.id != 1:
               sum_credito += invoice_obj.amount_untaxed
               tax_credito += invoice_obj.amount_tax
               total_credito += invoice_obj.amount_total
        return {'credito': sum_credito, 'tax_credito': tax_credito,'total_credito':total_credito}
    

    
report_sxw.report_sxw('report.cash_report_piasa', 'account.voucher', 'piasa_reporte_caja/report/report_cash_piasa.mako', parser=cash_report_acc, header=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

