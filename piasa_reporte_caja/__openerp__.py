# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 
#  
#    
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

{
    'name': 'Cash Report',
    'version': '1.3',
    'category': ' ',
    'description': """ 
      Cash Reports 
    """,
    'author': 'Tantums' ,
    'website': 'www.tantums.com' ,
    'depends': ['base','account'] ,
    'init_xml': [],
    'update_xml': ['report/cash_report_view.xml',
                   'wizard/cash_report_wizard_view.xml',
                  ],
    'demo_xml': [] ,
    'test': [] ,
    'installable': True , 
    'active': False ,
    'certificate': '' ,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
