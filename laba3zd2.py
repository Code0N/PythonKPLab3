class Taggable(object):
    def tag(self): 
        raise NotImplementedError( "Не реализован метод tag в Book" )
        
class Book(Taggable) :
  key = 1
  def __init__(self, name, author) :
    assert (len(name)!=0), "Введите название книги!"
    assert (len(author)!=0), "Введите автора книги!"
    self.name = name
    self.author = author
    self.key = self.__class__.key
    self.__class__.key	+=	1	
    
  def tag(self):
      res = self.name.split()
      for x in res:
          if not x.istitle(): res.remove(x)  
      return res
  
  def __str__(self):
        return '[%d] %s "%s"' % (self.key, self.author, self.name)

  
class Library (Book) :
  def __init__(self, number, name):
    assert (len(name)!=0), "Введите название библиотеки!"
    self.number = number
    self.name = name
    self.book = []
    self.itr = -1

  def __iadd__(self, other):
    self.book.append(other)
    return self
  
  def itr(self):
    return self.book

  def __iter__(self):
      return self
  
  def __next__(self):
      self.itr = self.itr  + 1
      if self.itr < len(self.book):
          name = self.book[self.itr].name
          author = self.book[self.itr].author
          key = self.book[self.itr].key
          #print('[' + str(key) + '] ' + author + ' \'' + name + '\'')
          return self.book[self.itr]
      raise StopIteration
    
lib = Library(1, '51 Some str., NY')
lib += Book('War and Peace', 'Leov Tolstoi')
lib += Book('Играть что-бы Жить', 'Дмитрий Рус')

for book in lib:
    print(book)
    print(book.tag())
   

