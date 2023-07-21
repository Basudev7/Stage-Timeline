# Copyright (c) 2023, dev and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import today,now

class Booking(Document):
	# pass
	def validate(self):
		if len(self.stage_timeline):
			if self.lead_stages != self.stage_timeline[-1].lead_stage:
				if self.lead_stages == "Enquiry":
					self.append(
						"stage_timeline",
						{
						"user":frappe.session.user,
						"lead_stage":"Enquiry",
						"datetime": now(),						
						}
					)
				else:
					self.append(
						"stage_timeline",
						{
						"user":frappe.session.user,
						"lead_stage":self.lead_stages,
						"datetime": now(),
						}
					)

		else:
			if self.lead_stages == "Enquiry":
				self.append(
					"stage_timeline",
					{

					"user":frappe.session.user,
					"lead_stage":"Enquiry",
					"datetime": now(),
					# "time":datetime.now().strftime("%H:%M:%S")
					
					}
				)
