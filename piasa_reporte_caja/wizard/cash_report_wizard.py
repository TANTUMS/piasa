# -*- encoding: utf-8 -*
##############################################################################
#
#    Copyright (c) 2013 SF Soluciones.
#    (http://www.sfsoluciones.com)
#    contacto@sfsoluciones.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields,osv
import pytz
import datetime, time
from openerp import SUPERUSER_ID
from openerp.tools.translate import _

class cash_report_wizard(osv.osv_memory):
    _name = 'cash.report.wizard'
    
    _columns = {
                'start_date': fields.date("Fecha"),
                'sucursal': fields.many2one('account.journal', 'Sucursal')
                }
    _defaults= {
                'start_date' : lambda *a: datetime.date.today().strftime('%Y-%m-%d'),
                'sucursal': 23,

    }



    def view_cash_report(self, cr, uid, ids, context):
        if context is None:
            context = {}
        data = self.read(cr, uid, ids[0], context=context)

         # get user's timezone
        user_pool = self.pool.get('res.users')
        user = user_pool.browse(cr, SUPERUSER_ID, uid)
        tz = pytz.timezone(user.partner_id.tz) or pytz.utc
        # get localized dates
        fecha_final = pytz.utc.localize(datetime.datetime.strptime(str(data['start_date']) + ' 23:59:59', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        fecha = pytz.utc.localize(datetime.datetime.strptime(str(data['start_date'])+ ' 00:00:00', '%Y-%m-%d %H:%M:%S')).astimezone(tz)

        invoice_pool = self.pool.get('account.invoice')
        search_string = [('date_invoice', '>=', fecha),('date_invoice', '<=',fecha_final),('state', '!=','draft'),('journal_id','=',data['sucursal'][0])]
        invoice_ids = invoice_pool.search(cr, uid,search_string,order='number',context=context)
        context['start_date'] = data['start_date']
        # context['end_date'] = data['end_date']
        context['active_ids'] = invoice_ids
        # if data['start_date'] > data['end_date']:
        #     raise osv.except_osv(_('Warning!'), _('Initial date  must be lesser than the Final date'))
        if not  invoice_ids:
            raise osv.except_osv(_('Warning!'), _('No such invoices for corresponding date'))
        
        datas = {
             'ids': invoice_ids,
             'model': 'cash.report.wizard',
             'form': data
                 }
        print datas
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'cash_report_piasa',
            'datas': datas,
            'context': context,
	        'report_type' : 'webkit'
            }
        
    
cash_report_wizard()

class account_invoice(osv.Model):
    _name='account.invoice'
    _inherit='account.invoice'

    _columns = {
        'notas_extra': fields.char('Notas'),
    }

account_invoice()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:-
