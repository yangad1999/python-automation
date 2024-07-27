class WorkLoad:
    def __init__(self, isHoliday, isWeekEnd) -> None:
        self.isHoliday = isHoliday
        self.isWeekEnd = isWeekEnd
    
    def doWork(self):
        if self.isHoliday is True or self.isWeekEnd is True:
            print("Delete Backlog Files")
        else:
            print("Do Work")
            
if __name__ == "__main__":
    newWorkLoad = WorkLoad(True, False)
    newWorkLoad.doWork()
    
    