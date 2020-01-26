from .models import state1
class blogView():
   def __init__(self):
       self.a = 0
   def blog_all_query(self, ID):
       query = state1.objects.filter(login_id=ID)
       return query   
