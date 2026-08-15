class OrderService:
    def __init__(self):
        self.orders = {
            "1001":{
                "status":"shipped",
                "location":"Islamabad",
                "estimated_delivery":"5 working days"},
            "1002":{
                "status":"processing",
                "location":"peshawar",
                "estimated_delivery":"8 working days"}}
    def get_status(self,ordernumber):
        if ordernumber in self.orders:
            order = self.orders[ordernumber]
            return(self.orders[ordernumber])
        else:
            return None