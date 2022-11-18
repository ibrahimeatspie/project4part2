class Jewel:
    def __init__(self, color, row, col, status):
        self.color = color
        self.row = row
        self.col = col
        self.status = status
    def set_row(self, row):
        self.row = row
    def get_row(self):
        return self.row
    def set_col(self, col):
        self.col = col
    def set_color(self, color):
        self.color = color
    
    def get_col(self):
        return self.col
    def get_color(self):
        return self.color
    def get_status(self):
        return self.status