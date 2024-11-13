class Buffer:
    buffer = []
    def add_data(self, data):
        if len(self.buffer) == 5:
            print('буфер переполнен')
            self.buffer=[]
        self.buffer.append(data)
        pass
    def get_data(self):
        if len(self.buffer) > 0:
            temp = self.buffer[len(self.buffer)-1]
            del self.buffer[len(self.buffer)-1]
            return temp
        else:
            print('ошибка, элементов нет')
buf = Buffer()
buf.add_data('1')
buf.add_data('2')
buf.add_data('3')
buf.add_data('4')
buf.add_data('5')
buf.add_data('6')
buf.add_data('7')

print(buf.get_data())
print(buf.get_data())
print(buf.get_data())