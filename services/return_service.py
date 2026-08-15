class ReturnService:
    def __init__(self):
        self.orders = {
            "1001" :{
                   "return_eligible":True,
                   "return_status":"Not_requested" },
            "1002" :{
                "return_eligible":False,
                "return_status":"Not_eligible"}}
    def process_return(self,ordernumber):
        if ordernumber not in self.orders:
            return None
        order = self.orders[ordernumber]
        if not order["return_eligible"]:
            return order
        order["return_status"]= "Requested"
        return order