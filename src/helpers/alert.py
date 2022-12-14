class Alert():
    # print(config._configuration)

    def push(type, status, message):      
        data = Message(status, message, type)
        result = data.get()
        print(result.message)
        return result

class Message:
    def __init__(self, status, message, title):
         self.message = message
         self.title = title
         self.status = status

    def get(self):
        self.message
        self.title
        self.status
        return self
      
    def set(self, status, message, title):
         self.message = message
         self.title = title
         self.status = status

#     ts = get()
#     print(ts)

# getdata = Message.get()
# print(getdata)

# setdata = Message.set('success', True, 'insert successful...')


# getdata = Message.get()
# print(getdata)

# class Label:
#     def __init__(self, text, font):
#         self._text = text
#         self._font = font

#     def get_text(self):
#         return self._text

#     def set_text(self, value):
#         self._text = value

#     def get_font(self):
#         return self._font

#     def set_font(self, value):
#         self._font = value




# Label("manuk", "data")

# data = Label.get_font("manuk")

# print(data)

