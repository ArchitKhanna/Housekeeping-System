#imports
from .models import apartment, block, status, task

#Variables/Values
Blocks = block.objects.all()
Status = status.objects.all()
Tasks = task.objects.all()

#This is where all custom functions go
def getBlocks(id):

    for x in Blocks:
        if Blocks.id == id:
            return Blocks.name
        else:
            return 'Error'
