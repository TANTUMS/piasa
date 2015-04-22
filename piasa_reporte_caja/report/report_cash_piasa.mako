<html>
<head>
<style type="text/css">
	${css} 
</style>
</head>	
<body>
<div>
				<div>
		%if get_voucher_obj(invoice_ids):
					${helper.embed_image('jpeg',str(get_logo()),220, 90)}

				</div>
				<div align="center">
			<h3 class="title" >
				${_('Corte de Facturas') | entity}
				
			</h3>
			<h5>
			</div>
				<div align="right">
					<p>${_('  FECHA :')}${formatLang(start_date,date=True) | entity}</p>
				</div>
		
			</h5>
		</div>
</div>

<table width="100%" style="font-size:10px; font-weight: bold;">
					<tr width="100%">
						<td colspan="1">${_('Usuario       :')}</td>
						<td colspan="3">Usuario</td>	
						<td colspan="4"></td>
					</tr>
					<tr>
						<td width="10%" align='center'>
							${_('Codigo Cliente') | entity}	
						</td>
						<td width="10%" align='center'>
							${_('Factura') | entity}
						</td>
						<td width="39.96%" align='center'>
							${_(' Nombre') | entity}
						</td>
						<td width="10%" align='center'>
							${_('Subtotal') | entity}
						</td>
						<td width="10%" align='center'>
							${_('Iva') | entity}
						</td> 
						<td width="10" align='center'>
							${_('Total') | entity}
						</td>
						<td width="10%" align='center'>
							${_('Divisas') | entity}
						</td>
					</tr>
			%endif
    		
% for o in 	get_voucher_obj(invoice_ids):
<table  width="100%">	
					<tr>
							<td width="10%" align='center' style="font-size:.5px;">
								<font size="1">
									</div>${o.partner_id.ref}</div>
								</font>
							</td>
							<td width="10%" align='center' style="font-size:.5px;">
								<font size="1">
									${o.number}
								</font>
							</td>
							<td width="39.96%" align='left' style="font-size:.5px;">
								<font size="1">
									${o.partner_id.name}
								</font>
							</td>
							<td  width="10%" align='center' style="font-size:.5px;">
								<font size="1">
									${formatLang(o.amount_untaxed, monetary=True)}
								</font>
							</td>
							<td width="10%" align='center' style="font-size:2px;">
								<font size="1">
									${formatLang(o.amount_tax, monetary=True)}
								</font>
							</td>
							<td width="10%" align='center' style="font-size:.5px;">
								<font size="1">
									${formatLang(o.amount_total, monetary=True)}
								</font>
							</td>
							<td width="10%" align='center' style="font-size:.5px;">
								<font size="1">
									${o.currency_id.name}
								</font>

							</td>
					</tr>
		</table>
%endfor
		<table width="100%"> 
					<tr>
						
							<td width="10%"></td>
							<td width="10%"></td>
							<td width="39.96%"></td>
							<td width="10%" align="center"><font size="1">${formatLang(get_total(invoice_ids)['sum_untaxed'],monetary=True)}</font></td>
							<td width="10%" align="center"><font size="1">${formatLang(get_total(invoice_ids)['sum_tax'],monetary=True)}</font></td>
							<td width="10%" align="center"><font size="1">${formatLang(get_total(invoice_ids)['sum_tot'],monetary=True)}</font></td>
							<td width="10%"></td>
						</font>
					</tr>
		</table>
		
		<table width="100%"> 

				<tr>
						<td rowspan="3">Facturas Contado:</td>
						<td></td>
					</tr>
					<tr>
						<td>
							<tr>${formatLang(facturas_contado(invoice_ids)['contado'],monetary=True)}</tr>
							<tr>${formatLang(facturas_contado(invoice_ids)['tax_contado'],monetary=True)}</tr>
							<tr>${formatLang(facturas_contado(invoice_ids)['total_contado'],monetary=True)}</tr>
						</td>
					</tr>	
		</table>
<p style="page-break-before: always;"></p>
</body>
</html>
